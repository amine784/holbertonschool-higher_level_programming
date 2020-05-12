#!/usr/bin/node
require('request')(process.argv[2], (err, res, body) => {
  if (err) console.log(err);
  else {
    let m = 0;
    let c, h;
    const data = JSON.parse(body).results;
    for (c of data) {
      for (h of c.characters) {
        if (h.includes('18')) { m++; }
      }
    }
    console.log(m);
  }
});
