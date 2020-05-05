#!/usr/bin/node
const nbre = process.argv.length;
const n = parseInt(nbre, 10);
const l = process.argv.sort((a, b) => a - b);
const max = l[l.length - 2];
if (n <= 3) {
  console.log('0');
} else {
  console.log(max);
}
