const int green = 9;
const int blue = 10;
const int red  = 11;

const int redSensor = A0;
const int greenSensor = A1;
const int blueSensor = A2;

float redVal = 0;
float greenVal = 0;
float blueVal = 0;

int redSensorVal = 0;
int greenSensorVal = 0;
int blueSensorVal = 0;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  pinMode(green, OUTPUT);
  pinMode(red, OUTPUT);
  pinMode(blue, OUTPUT);
}

void loop() {
  // put your main code here, to run repeatedly:
  redSensorVal = analogRead(redSensor);
  delay(5);
  greenSensorVal = analogRead(greenSensor);
  delay(5);
  blueSensorVal = analogRead(blueSensor);
  delay(1000);
  // convert
  redVal = redSensorVal/4.0;
  greenVal = greenSensorVal/4.0;
  blueVal = blueSensorVal/4.0;
  Serial.print("red");
  Serial.print(redVal);
  Serial.print("green");
  Serial.print(greenVal);
  Serial.print("blue");
  Serial.print(blueVal);
  // write
  analogWrite(red, redVal);
  analogWrite(blue, blueVal);
  analogWrite(green, greenVal);
}
