#!/usr/bin/node
const liste = require('./100-data').list;
console.log(liste);
const map1 = liste.map((x, i) => { return (x * i); });
console.log(map1);
