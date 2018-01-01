#include <stdio.h>
#include <math.h>
#include <stdlib.h>

// Define some variables
int sigma = 200;
float f_0 = 0.1;
float R_s = 1e4;

// Define some constants
float pi = M_PI;
float e = M_E;
float G = 4.302e-3;

// Define the directory where the data shall be stored

// Prototype
float rho(float r);
float phi(float x);

int main(int argc, char *argv[] ){
  if( argc == 2 ) {
    printf("Generating %s Values...\n", argv[1]);

    FILE * fp = fopen("testFile.csv", "w+");
    if(fp == NULL){
      printf("Error opening the file!\n");
      exit(1);
    }

    int x = atoi(argv[1]);

    for(int i = 0; i < x; i++){
      printf("%d, %f\n", i, phi(i));
    }

    // for(int i = 0; i < 1e7; i = i + 1e4){
    //   printf("%s, %f\n", i, phi(i));
    // }

    fclose(fp);

  }
  else if( argc > 2 ) {
    printf("Too many arguments supplied.\n");
    return 0;
  }
  else {
    printf("One argument expected.\n");
    return 0;
  }

  return 0;
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
