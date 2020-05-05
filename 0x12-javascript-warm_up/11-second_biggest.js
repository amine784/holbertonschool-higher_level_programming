#!/usr/bin/node
const nbre = process.argv.length;
const n = parseInt(nbre, 10);
const l = process.argv.sort();
const max = l[l.length - 1];
if (n <= 3) {
  console.log('0');
} else {
  console.log(max - 1);
}
