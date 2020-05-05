#!/usr/bin/node
const nbre = process.argv[2];
const n = parseInt(nbre, 10);
function factorial (n) {
  if (n <= 0) {
    return (1);
  } else {
    return (n * factorial(n - 1));
  }
}
console.log(factorial(n));
