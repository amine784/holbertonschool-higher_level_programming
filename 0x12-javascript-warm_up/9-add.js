#!/usr/bin/node
const arg1 = process.argv[2];
const a = parseInt(arg1, 10);
const arg2 = process.argv[3];
const b = parseInt(arg2, 10);
function add (a, b) {
  return (a + b);
}
console.log(add(a, b));
