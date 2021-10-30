#include <stdio.h>
#include <stdlib.h>
#include <limits.h>
#include <float.h>

// Thanks to https://www.tutorialspoint.com/cprogramming/index.htm for the tutorial

// These are constants/literals. Note the syntax carefully
#define LENGTH 8
#define WIDTH 10

// This is also constants/literals
const int DEPTH = 100;

// Prints out hello world
int hello_world() {
    printf("Hello, World!\n");
    return 0;
}

int print_integer_types() {
    printf("CHAR_BIT    :   %d\n", CHAR_BIT);
    printf("CHAR_MAX    :   %d\n", CHAR_MAX);
    printf("CHAR_MIN    :   %d\n", CHAR_MIN);
    printf("INT_MAX     :   %d\n", INT_MAX);
    printf("INT_MIN     :   %d\n", INT_MIN);
    printf("LONG_MAX    :   %ld\n", (long) LONG_MAX);
    printf("LONG_MIN    :   %ld\n", (long) LONG_MIN);
    printf("SCHAR_MAX   :   %d\n", SCHAR_MAX);
    printf("SCHAR_MIN   :   %d\n", SCHAR_MIN);
    printf("SHRT_MAX    :   %d\n", SHRT_MAX);
    printf("SHRT_MIN    :   %d\n", SHRT_MIN);
    printf("UCHAR_MAX   :   %d\n", UCHAR_MAX);
    printf("UINT_MAX    :   %u\n", (unsigned int) UINT_MAX);
    printf("ULONG_MAX   :   %lu\n", (unsigned long) ULONG_MAX);
    printf("USHRT_MAX   :   %d\n", (unsigned short) USHRT_MAX);

    return 0;
}

int print_float_types() {
    printf("Storage size for float : %d \n", sizeof(float));
    printf("FLT_MAX     :   %g\n", (float) FLT_MAX);
    printf("FLT_MIN     :   %g\n", (float) FLT_MIN);
    printf("-FLT_MAX    :   %g\n", (float) -FLT_MAX);
    printf("-FLT_MIN    :   %g\n", (float) -FLT_MIN);
    printf("DBL_MAX     :   %g\n", (double) DBL_MAX);
    printf("DBL_MIN     :   %g\n", (double) DBL_MIN);
    printf("-DBL_MAX     :  %g\n", (double) -DBL_MAX);
    printf("Precision value: %d\n", FLT_DIG );

    return 0;
}

int print_data_types() {
    printf("There are four data types: Integers, Floats, Void, and Derived");
    printf("There are many subtypes of integers");
    print_integer_types();
    printf("There are several types of floats");
    print_float_types();
    printf("Voids are used to return a void from a function, pass in nothing, or pointers to nothing");
    printf("Derived types are more complex types");
    return 0;
}

int crazy_value = 99;

void declare_variables() {
    int i = 0;
    char c = 'd';
    float f = 27.9;
    double d = 27.99999999999;
    printf("value of i : %d \n", i);
    printf("value of crazyvalue : %d \n", crazy_value);
}


void constants_literals() {
    int x;
    x = LENGTH * WIDTH * DEPTH;
    #define WHAT "What?"
    printf("Volume : %d \n", x);
    printf(WHAT);
}

void describe_storage_classes(){
    auto int month = 12; //This is the default for local variables. Only exists within the function
    register int miles = 100; //Stored in register instead of RAM. This is faster but has limitations. Can only be used locally
    static int crazy = 5; //Causes even a local variable to not be destroyed at end of program. Can be used on a global to be only visible in the current file.
    extern void constant_literals(); //Used to access a global variable or function in another class
}

void operators() {
    printf("Adding, Equality operators are as they are in Python");
    printf("&& = and, || = or, ! = not");
    printf("There are also bitwise operators");
    printf("Assignment operators very similar =, +=, -=, ...");
    int x = 10;
    sizeof(x); // gets size of x
    &x; // returns the address of x
    char y[3] = "123";
    *y; //pointer to a variable
    printf("More on precedence: https://www.tutorialspoint.com/cprogramming/c_operators.htm");
    
}

void conditionals() {
    // Ifs, elses, etc...
    int x = 10;
    int y = 100;
    int z = 1000;
    if (x == 10){
        if (y == 100){
            if (z==1000){
                printf("if-if-if");
            }
            else{
                printf("if-if-else");
            }
        }
        else {
            printf("if-else");
        }
    }
    else if (x == 100){
        printf("elseif");
    }
    else {
        printf("else");
    }
    // Switch statements
    x = 100;
    switch(x){
        case 10:
            printf("case 1");
            break; //note the use of the break
        case 100:
            printf("case 2");
            break;
        default:
            printf("case default");
    }
}

void loops() {
    // While loops
    int i = 0;
    while (i < 10) {
        i+= 1;
        printf("value of i : %d \n", i);
    }
    // For loops
    for (i = 1; i < 11; i+=1) {
        printf("value of i : %d \n", i);
    }
    // Do while loops
    i = 0;
    do {
        i+=1;
        printf("value of i : %d \n", i);
    } while( i < 10 );
    // break and continue used as normal
    // goto exists, but this is garbage
}

int max(int x, int y){
    // Sample function call
    // Call by value is default, meaning we edit the copy of the variable
    // Can use call by reference by adding the * pointer which edits the actual variable
    int retval = 0;
    if (y>x){
        retval = 1;
    }
    else if (y==x){
        retval = -1;
    }
    return retval;
}

int * array_passing_returning(int *a, int b[3], int c[]){
    // The arrays passed in are pointers to the arrays, not copies
    static int retval[] = {1,2,3}; // retval will be a pointer. Needs to be static to be available once outside this function.
    return retval;
    // How to get the size of the array, you can't easily. Better to keep track of it.
}

void arrays(){
    //int array1 [3] = {1.0, 2.0, 3.0};
    double array2[] = {1.0, 2.0, 3.0};
    array2[1] = 2.1;
    int size_array2 = sizeof(array2) / sizeof(double);
    // C does not check out of bounds errors, so you can screw things up bad!
    for (int i = 0; i < size_array2; i+=1) {
        double value = array2[i];
        printf("value of value : %f \n", value);
    }
    // Multidimensional arrays
    int a[5][2] = { {0,0}, {1,2}, {2,4}, {3,6},{4,8}};
    int i, j;
    for ( i = 0; i < 5; i++ ) {
        for ( j = 0; j < 2; j++ ) {
            printf("a[%d][%d] = %d\n", i,j, a[i][j] );
        }
    }
    // Passing and returning to array
    int x[] = {1, 2, 3};
    int y[] = {4, 5, 6};
    int z[] = {7, 8, 9};
    int *combined = array_passing_returning(x, y, z);
    printf("c1 = %d\n", combined[0] );
}

void pointers(){
    int  var = 20;   /* actual variable declaration */
    int  *ip = NULL;        /* pointer variable declaration */

    ip = &var;  /* store address of var in pointer variable*/
    printf("Greeting message: %d\n", *ip ); // this prints the int
    printf("Greeting message: %p\n", ip ); // this prints the pointer address
    
    //You can change the location of a pointer with ++, --, +, -
    //You can create an array of pointers
    //You can have a pointer to a pointer
    
}

void strings(){
    char greeting[6] = {'H', 'e', 'l', 'l', 'o', '\0'};
    char greeting1[] = "Hello"; // automatically \0 is placed at end
    printf("Greeting message: %s\n", greeting1 );
    // string functions:
    //strcpy(s1, s2) - copy s2 into s1
    //strcat(s1, s2) - s2 concat onto s1
    //strlen(s1) - get length of s1
    //strcmp(s1, s2) - Returns 0 if s1 and s2 are the same; less than 0 if s1<s2; greater than 0 if s1>s2.
    // strchr(s1, ch) - Returns a pointer to the first occurrence of character ch in string s1.
    // strstr(s1, s2) - Returns a pointer to the first occurrence of string s2 in string s1.
}

struct Books {
   char  title[50];
   char  author[50];
   char  subject[100];
   int   book_id;
};

void printBook( struct Books book ) { //struct passed in by copying
    printf( "Book 1 title : %s\n", book.title);
    printf( "Book 1 author : %s\n", book.author);
    printf( "Book 1 subject : %s\n", book.subject);
    printf( "Book 1 book_id : %d\n", book.book_id);
};

void printBookPt( struct Books *book ) { //struct passed in by copying
    printf( "Book 1 title : %s\n", book->title);
    printf( "Book 1 author : %s\n", book->author);
    printf( "Book 1 subject : %s\n", book->subject);
    printf( "Book 1 book_id : %d\n", book->book_id); // access elements using ->
};

void structures() {
    // Allow for the combining of objects of different types
    struct Books Book1;
    strcpy( Book1.title, "Sample Title");
    strcpy( Book1.author, "Sample Author");
    strcpy( Book1.subject, "Sample Subject");
    Book1.book_id = 1000;
    
    /* print Book1 info */
    //printBook(Book1);
    
    // pointer to structs
    struct Books *struct_pointer;
    struct_pointer = &Book1;
    printBookPt(struct_pointer);
    
    //you can pack a struct to make it smaller in memory or disk space: https://www.tutorialspoint.com/cprogramming/c_structures.htm
    
}

void unions(){
    // Unions allow to store different data types at the same location
    union Data {
       int i;
       float f;
       char str[20];
    } data;
    
    // The above object has a size of 20, since the char[] is the largest object
    // We can use any of the above fields to store data at that memory location
    // You can only use one of the fields to store data at a time
    data.i = 10;
    data.f = 10.0;
    printf( "Data i : %f\n", data.i);
    // If I would try to print data.i, it would not print out what I assigned above.
    // You can pass a union by copy or by reference
}

void bit_fields() {
    struct {
       unsigned int widthValidated;
       unsigned int heightValidated;
    } status;
    // The above requires 8 bytes, but we are only storing T/F values
    // The above can be re-written to the following:
    struct {
       unsigned int widthValidated : 1;
       unsigned int heightValidated : 1;
    } status1;
    // Now this will only use 2 bits to store the values
}

void typedefs() {
    // Typedefs are used to give a type a new name
    typedef unsigned char BYTE;
    // we can use BYTE as an abbreviation of unsigned char
    BYTE b1, b2;
}

void io() {
    // This will only get the first character entered
    printf( "Enter a value :");
    char c = getchar( ); // reads the input and returns an int
    printf( "\nYou entered: ");
    putchar( c ); // puts the passed character on the screen and returns the same character
    // This will get the first 100 characters
    char str[100];
    printf( "Enter a value :");
    fgets( str, sizeof(str), stdin); // reads a line from stdin into the buffer pointed to by s until either a terminating newline or EOF
    printf( "\nYou entered: ");
    puts( str ); // writes the string 's' and 'a' trailing newline to stdout
    // This
    char fart[100];
    int i;
    printf( "Enter a value :");
    scanf("%s %d", fart, &i); // reads the input from the standard input stream stdin and scans that input according to the format provided
    printf( "\nYou entered: %s %d ", str, i);
}

void file_io(){
    // https://www.tutorialspoint.com/cprogramming/c_file_io.htm
}

void preprocessors(){
    // Not part of compiler. Instructs compiler to do pre-processing before actual compilation
    // Called CPP
    // All CPP commands start with #
    // https://www.tutorialspoint.com/cprogramming/c_preprocessors.htm
}

void headers() {
    // a file with extension .h
    // contains C function declarations and macro definitions to be shared between several source files
    // use #include
    // we've been including stdio.h
    // A simple practice in C or C++ programs is that we keep all the constants, macros, system wide global variables, and function prototypes in the header files and include that header file wherever it is required
    // To prevent a header being imported twice, dependent includes, etc... go here: https://www.tutorialspoint.com/cprogramming/c_header_files.htm
}

void type_casting() {
    int i = 10;
    double s = 6;
    double sum = (double) i / s;
    printf("\nSum:%f ", sum);
}

void error_handling() {
    // https://www.tutorialspoint.com/cprogramming/c_error_handling.htm
}

double average(int num,...) { // the ellipses allows passing of variable # of arguments
    // notice how fin
   va_list valist;
   double sum = 0.0;
   int i;

   /* initialize valist for num number of arguments */
   //va_start(valist, num);

   /* access all the arguments assigned to valist */
   //for (i = 0; i < num; i++) {
   //   sum += va_arg(valist, i);
   //}
    
   /* clean memory reserved for valist */
   //va_end(valist);

   return sum/num;
}

void memory_management() {
    // M emory allocation and management. Found in the <stdlib.h> header file.
    // If you are aware size of array, then you can easily define char name[100];
    
    //Dynamically allocating memory
    char name[100];
    char *description;
    
    strcpy(name, "Zara Ali");
    
    description = malloc( 200 * sizeof(char) ); // alocates the memory dynamically
    if( description == NULL ) {
       fprintf(stderr, "Error - unable to allocate required memory\n");
    } else {
       strcpy( description, "Zara ali a DPS student in class 10th");
    }
    
    printf("Name = %s\n", name );
    printf("Description: %s\n", description );
    // could have also used calloc
    // calloc - This function allocates an array of num elements each of which size in bytes will be size.
    //malloc - This function allocates an array of num bytes and leave them uninitialized.
    // realloc - Reallocates memory, preserving what is in place already (not a free and malloc)
    
    // Releasing memory - it is good practice to release memory when done with it
    free(description);
}

int main(int argc, const char * argv[]) {
    //hello_world();
    //print_data_types();
    //declare_variables();
    //constants_literals();
    //describe_storage_classes();
    //operators();
    //conditionals();
    //loops();
    
    //int x = 10;
    //int y = 100;
    //int mx = max(x,y);
    //printf("value of mx : %d \n", mx);
    // scope rule - formal parameters are local ones that override the value of the global ones
    
    //arrays();
    //pointers();
    //strings();
    //structures();
    //unions();
    //bit_fields();
    //typedefs();
    //io();
    //file_io();
    //preprocessors();
    //headers();
    //type_casting();
    //error_handling();
    // supports recursion
    //double fin = average(3, 5,10,15);
    //memory_management();
    
    // Command line arguments
    //argc is how many arguments were passed in
    //argv[0] is the name of the program
    //arggv[1] is a pointer to the command line argument specified
    // all other argv[] are ones passed in
}

