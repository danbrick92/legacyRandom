package main

/*
	One time, I had to run this:
		- cd %USERPROFILE%\Go\bin\
		- go install github.com/aws/aws-lambda-go/cmd/build-lambda-zip@latest

	To get this working in Lambda, I performed the following steps:
		- go get -u github.com/aws/aws-lambda-go
		- $Env:GOOS = "linux"
		- $Env:GOARCH = "amd64"
		- $Env:CGO_ENABLED = "0"
		- go build -tags lambda.norpc -o bootstrap main.go
		- ~\Go\bin\build-lambda-zip.exe -o myFunction.zip bootstrap
		- Go into AWS Lambda in your function, and upload the zip
			- Make sure using custom runtime al2
			- Upload the zip
			- Set the handler to bootstrap
		- Now test it, passing in whatever you want to the Events struct

	To get the dynamo stuff working:
		- go get -u github.com/aws/aws-sdk-go/...
		- Add dynamo permissions to the lambda's IAM role

	Notes:
		- you have to create a session, then the client
		- then you have to create an input configuration instance
		- make the call, check, and then perform your work
*/

/*
	DynamoDB lesson:
		I need to fetch data:
			Do I need 1 item or a collection?
				Yes
					Do you know the item's partition or sort key?
						Yes -> Use GetItem
						No -> Use Scan with FilterExpressions
				No
					Do you know the item's partition or sort key?
						Yes
							Are they using the same partition key?
								Yes -> Use Query
								No -> Use BatchGetItem
						No
							Use Scan with FilterExpressions
*/

import (
	"context"
	"fmt"
	"log"
	"strconv"

	"github.com/aws/aws-lambda-go/lambda"
	"github.com/aws/aws-sdk-go/aws"
	"github.com/aws/aws-sdk-go/aws/session"
	"github.com/aws/aws-sdk-go/service/dynamodb"
	"github.com/aws/aws-sdk-go/service/dynamodb/dynamodbattribute"
)

type MyEvent struct {
	Name string `json:"name"`
}

func getDynamoClient() *dynamodb.DynamoDB {
	sess := session.Must(session.NewSessionWithOptions(session.Options{
		SharedConfigState: session.SharedConfigEnable,
	}))
	svc := dynamodb.New(sess)
	return svc
}

func dynamoList(svc *dynamodb.DynamoDB) {
	// create the input configuration instance
	input := &dynamodb.ListTablesInput{}
	log.Println("Tables:")

	result, err := svc.ListTables(input)
	if err != nil {
		log.Println("Could not get back result", err)
		return
	}

	// Get table names
	for _, n := range result.TableNames {
		fmt.Println(*n)
	}
}

type Item struct { // Model an item in the Dynamo table
	Name          string
	UnixTimestamp int
	Alias         string
}

var item Item = Item{
	"dan", 900, "the brick",
}
var tableName string = "test"

func dynamoAddItem(svc *dynamodb.DynamoDB) {
	// Convert struct to dynamo types
	av, err := dynamodbattribute.MarshalMap(item)
	if err != nil {
		log.Fatalf("Got error marshalling new movie item: %s", err)
	}

	// Set the input
	input := &dynamodb.PutItemInput{
		Item:      av,
		TableName: aws.String(tableName),
	}

	// Add to table
	_, err = svc.PutItem(input)
	if err != nil {
		log.Fatalf("Got error calling PutItem: %s", err)
	}
	fmt.Println("Successfully added '" + item.Name + " to table " + tableName)
}

func dynamoReadItem(svc *dynamodb.DynamoDB) {
	// Get Item
	result, err := svc.GetItem(&dynamodb.GetItemInput{
		TableName: aws.String(tableName),
		Key: map[string]*dynamodb.AttributeValue{
			"Name": {
				S: aws.String(item.Name),
			},
			"UnixTimestamp": {
				N: aws.String(strconv.Itoa(item.UnixTimestamp)),
			},
		},
	})

	// Check for errors
	if err != nil {
		log.Fatalf("Got error calling GetItem: %s", err)
	}
	if result.Item == nil {
		log.Fatalln("Item was empty")
	}

	// Unmarshall data to Item struct
	item := Item{}
	err = dynamodbattribute.UnmarshalMap(result.Item, &item)
	if err != nil {
		panic(fmt.Sprintf("Failed to unmarshal Record, %v", err))
	}
	fmt.Println("GetItem returned the following data:", item)

}

func dynamoUpdateItem(svc *dynamodb.DynamoDB) {
	newAlias := "bubba"

	// Update the input
	input := &dynamodb.UpdateItemInput{
		ExpressionAttributeValues: map[string]*dynamodb.AttributeValue{ // Set update expression values
			":a": {
				S: aws.String(newAlias),
			},
		},
		TableName: aws.String(tableName), // Set table and keys
		Key: map[string]*dynamodb.AttributeValue{
			"Name": {
				S: aws.String(item.Name),
			},
			"UnixTimestamp": {
				N: aws.String(strconv.Itoa(item.UnixTimestamp)),
			},
		},
		ReturnValues:     aws.String("UPDATED_NEW"),
		UpdateExpression: aws.String("set Alias = :a"), // Here is the update expression that will be evaled
	}

	// Make call and check for errors
	_, err := svc.UpdateItem(input)
	if err != nil {
		log.Fatalf("Got error calling UpdateItem: %s", err)
	}

	fmt.Println("Successfully updated '" + item.Name + "' Alias = " + newAlias)
}

func dynamoDelete(svc *dynamodb.DynamoDB) {
	// Call delete input
	input := &dynamodb.DeleteItemInput{
		Key: map[string]*dynamodb.AttributeValue{
			"Name": {
				S: aws.String(item.Name),
			},
			"UnixTimestamp": {
				N: aws.String(strconv.Itoa(item.UnixTimestamp)),
			},
		},
		TableName: aws.String(tableName),
	}

	_, err := svc.DeleteItem(input)
	if err != nil {
		log.Fatalf("Got error calling DeleteItem: %s", err)
	}

	fmt.Println("Deleted '" + item.Name + "' from table " + tableName)
}

func HandleRequest(ctx context.Context, name MyEvent) (string, error) {
	log.Println("Hello", name.Name)

	// Create dynamo client
	svc := getDynamoClient()

	// Print out dynamo tables
	dynamoList(svc)
	dynamoAddItem(svc)
	dynamoReadItem(svc)
	dynamoUpdateItem(svc)
	dynamoDelete(svc)

	return fmt.Sprintf("Hello %s!", name.Name), nil
}

func main() {
	lambda.Start(HandleRequest)
}
