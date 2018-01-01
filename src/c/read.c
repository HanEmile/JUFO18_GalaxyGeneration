#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <math.h>

// Define some constants
int range = 100;

// Prototype pythagoras function
float pythagoras(int x, int y, int z);

int main(int argc, char *argv[] ){
  // Seed random
  srand(time(NULL));

  // Define the number of stars that should be generated using command line
  // arguments
  long num_of_stars = atoi(argv[1]);

  // define an array to store the coordinates of the stars in
  int star_arr[num_of_stars][3];

  // generate the random coordinates
  for(int i = 0; i < num_of_stars; i++){
    star_arr[i][0] = rand() % range + 1;
    star_arr[i][1] = rand() % range + 1;
    star_arr[i][2] = rand() % range + 1;
  }

  // print the content of the array star_arr
  for(int i = 0; i < num_of_stars; i++){
    printf("%d, %d, %d\n", star_arr[i][0], star_arr[i][1], star_arr[i][2]);
    printf("%f\n\n", pythagoras(star_arr[i][0], star_arr[i][1], star_arr[i][2]));

  }

  // Test if the Star should be generated or not

    // If the star should be generated, write it's coordinates to a file
    // Else do nothing

  return 0;
}

float pythagoras(int x, int y, int z){
  float a = pow(x, 2);
  float b = pow(y, 2);
  float c = pow(z, 2);
  float d = a + b + c;
  float e = sqrt(d);
  return e;
}
