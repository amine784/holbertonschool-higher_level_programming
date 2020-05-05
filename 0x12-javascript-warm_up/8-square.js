#!/usr/bin/node
const y = process.argv[2];
let i = 0;
if (isNaN(y)) {
  console.log('Missing size');
} else {
  for (; i < y; i++) {
    console.log('X'.repeat(y));
  }
}
