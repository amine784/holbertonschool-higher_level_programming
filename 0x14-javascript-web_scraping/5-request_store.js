#!/usr/bin/node
require('request')(process.argv[2], (err, res, body) => {
  if (err) console.log(err);
  else {
    const fil = require('fs');
    fil.writeFile(process.argv[3], body, 'utf-8', (error) => {
      if (error) console.log(error);
    });
  }
});
