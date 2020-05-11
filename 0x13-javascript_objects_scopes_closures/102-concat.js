#!/usr/bin/node
const fileA = require('fs').readFileSync(process.argv[2]);
const fileB = require('fs').readFileSync(process.argv[3]);
require('fs').writeFileSync(process.argv[4], fileA + fileB);
