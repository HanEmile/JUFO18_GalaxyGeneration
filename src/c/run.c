#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <math.h>

// Define some constants
int range_max = 1e5;
int range_min = -1e5;

// Define some variables
int sigma = 200;
float f_0 = 0.1;
float R_s = 1e4;

// Define some constants
float G = 4.302e-3;

// Prototype pythagoras function
float pythagoras(float x, float y, float z);
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

  FILE * st = fopen("stars/1.csv", "w+");

  /*
    Generate random coordinates
  */

  printf(">>> Generating %d random coordinates\n", num_of_stars);

  // generate the random coordinates
  for(int i = 0; i < num_of_stars; i++){
    int x = rand() % (range_max - range_min + 1) + range_min;
    int y = rand() % (range_max - range_min + 1) + range_min;
    int z = rand() % (range_max - range_min + 1) + range_min;

    fprintf(st, "%d, ", x);
    fprintf(st, "%d, ", y);
    fprintf(st, "%d, ", z);

    fprintf(st, "%f", pythagoras(x, y, z));
    fprintf(st, "\n");
  }

  fclose(st);

  printf("  -> Done.\n\n");

  /*
    Generate a lookuptable
  */

  printf(">>> Generating a lookuptable\n");

  // If the correct amount (2) of command line arguments are given, continue
  if( argc == 2 ) {

    // Print out how many stars are being generated
    printf("  -> Generating %d Values...\n", num_of_stars);

    char *filename = "testFile.csv";

    printf("  -> Writing data to '%s'\n", filename);

    // Open a file into which the lookuptable wil be written
    FILE * fp = fopen(filename, "w+");

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

    printf("  -> Done.\n\n");

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
float pythagoras(float x, float y, float z){
  return sqrt(pow(x, 2) + pow(y, 2) + pow(z, 2));
}

// Define rho function
float rho(float r){
  float a = (1) / ( sqrt(2 * M_PI) * sigma);
  float b = exp( - (phi(r) / pow(sigma, 2) ));
  return a;
}

// Define phi function
float phi(float x){
  if(x == 0) {
    float a = -4 * M_PI * f_0 * G * pow(R_s, 2);
    return(a);
  }
  else {
    float a = - (4 * M_PI * G * f_0 * pow(R_s, 3) / x);
    float b = log(1 + (x / R_s) );
    return(a * b);
  }
}
