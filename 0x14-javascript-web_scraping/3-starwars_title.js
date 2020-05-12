#!/usr/bin/node
const req = require('request');
req('https://swapi-api.hbtn.io/api/' + process.argv[2], (err, response, body) => { if (err) { console.log(err); } else { console.log(JSON.parse(response.body).title); } });
