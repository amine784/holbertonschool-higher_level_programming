#!/usr/bin/node
const y = process.argv[2];
let i = 0;
if (isNaN(y)) {
  console.log('Missing number of occurrences');
} else {
  for (; i < y; i++) {
    console.log('C is fun');
  }
}
