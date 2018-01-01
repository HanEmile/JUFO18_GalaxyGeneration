#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <math.h>

// Define some constants
int range = 100;

// Define some variables
int sigma = 200;
float f_0 = 0.1;
float R_s = 1e4;

// Define some constants
float pi = M_PI;
float e = M_E;
float G = 4.302e-3;

// Prototype pythagoras function
float pythagoras(int x, int y, int z);
// More prototypes
float rho(float r);
float phi(float x);

int main(int argc, char *argv[] ){
  // Seed random
  srand(time(NULL));

  // Define the number of stars that should be generated using command line
  // arguments
  long num_of_stars = atoi(argv[1]);

  // define an array to store the coordinates of the stars in
  int star_arr[num_of_stars][3];

  /*
    Generate random coordinates
  */

  // generate the random coordinates
  for(int i = 0; i < num_of_stars; i++){
    star_arr[i][0] = rand() % range + 1;
    star_arr[i][1] = rand() % range + 1;
    star_arr[i][2] = rand() % range + 1;
  }

  /*
    Print out the coordinates
  */

  // print the content of the array star_arr
  for(int i = 0; i < num_of_stars; i++){
    printf("%d, %d, %d\n", star_arr[i][0], star_arr[i][1], star_arr[i][2]);
    printf("%f\n\n", pythagoras(star_arr[i][0], star_arr[i][1], star_arr[i][2]));

  }

  /*
    Generate a lookuptable
  */

  // If the correct amount (2) of command line arguments are given, continue
  if( argc == 2 ) {

    // Print out how many stars are being generated
    printf("Generating %s Values...\n", num_of_stars);

    // Open a file into which the lookuptable wil be written
    FILE * fp = fopen("testFile.csv", "w+");

    // Abourt if no file is specified
    if(fp == NULL){
      printf("Error opening the file!\n");
      exit(1);
    }

    // generate the lookuptable
    for(int i = 0; i < num_of_stars; i++){
      fprintf(fp, "%d, %f\n", i, phi(i));
    }

    // close the file now containing the lookuptable
    fclose(fp);

  }
  // Exception: to many arguments
  else if( argc > 2 ) {
    printf("Too many arguments supplied.\n");
    return 0;
  }
  // Exception: no argument specified
  else {
    printf("One argument expected.\n");
    return 0;
  }

  // Test if the Star should be generated or not

    // If the star should be generated, write it's coordinates to a file
    // Else do nothing

  return 0;
}

// Define the Pythagorean theorem
float pythagoras(int x, int y, int z){
  float a = pow(x, 2);
  float b = pow(y, 2);
  float c = pow(z, 2);
  float d = a + b + c;
  float e = sqrt(d);
  return e;
}

// Define rho function
float rho(float r){
  float a = (1) / ( sqrt(2 * pi) * sigma);
  float b = exp( - (phi(r) / pow(sigma, 2) ));
  return a;
}

// Define phi function
float phi(float x){
  if(x == 0) {
    float a = -4 * pi * f_0 * G * pow(R_s, 2);
    return(a);
  }
  else {
    float a = - (4 * pi * G * f_0 * pow(R_s, 3) / x);
    float b = log(1 + (x / R_s) );
    return(a * b);
  }
}
