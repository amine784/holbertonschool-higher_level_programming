#!/usr/bin/node
const request = require('request');
request(process.argv[2], function (err, response, body) { if (err) { console.log(err); }
  let m = 0;
  let c, h;
  const data = JSON.parse(body).results;
  for (c of data) {
    for (h of c.characters) {
      if (h.includes('18')) { m++; }
    }
  }
  console.log(m);
});
