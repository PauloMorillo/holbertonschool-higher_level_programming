#!/usr/bin/node
if (process.argv[2]) {
  const request = require('request');
  const url = process.argv[2];
  const file = process.argv[3];
  const fs = require('fs');
  request(url, function (error, response, body) {
    if (error) {
      console.log(error);
    } else {
      const data = body;
      fs.writeFile(file, data, err => {
        if (err) {
          console.error(err);
        }
      });
    }
  });
}
