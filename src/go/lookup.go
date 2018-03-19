// ./lookup.py <number_of_stars> <save_name>

package main

import (
  "fmt"         // printing
  // "os"          // system arguments
  "math"
)

const sigma = 200
const f_0 = 0.1
const R_s = 1e4
const pi = 3.141592
// e = math.e
const G = 4.302e-3

func rho(r int) float64 {
  var a float64 = (1000) / (math.Sqrt( 2 * pi ) * sigma )
  var b float64 = r / sigma * sigma
  var c float64 = math.Exp(float64(b))
  var d float64 = float64(a) * float64(c)
  return d
}

// # rho function
// def rho(r):
//     a = (1) / (math.sqrt( 2 * pi ) * sigma )
//     b = math.exp( - (phi(r) / sigma ** 2 ) )
//     return a * b

// func phi(x int) float64 {
//   // if x == 0{
//   //   return -4 * pi * f_0 * G * (R_s * R_s)
//   // } else {
//   //   a := - ( 4 * pi * G * f_0 * (R_s * R_s * R_s) ) / x
//   //   b := 1 + (x / R_s)
//   //   c := math.Log(b)
//   //   d := a * b
//   //   return d
//   // }
// }

func main(){
  // nos := os.Args[1]
  // save := "/data/" + string(os.Args[2]) + ".csv"

  fmt.Println(float64(rho(1e6)))
  fmt.Println(float64(rho(3e6)))
  fmt.Println(float64(rho(5e6)))
  fmt.Println(float64(rho(7e6)))
  fmt.Println(float64(rho(9e6)))

}
