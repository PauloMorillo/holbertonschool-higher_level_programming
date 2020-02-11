#!/usr/bin/node
const fs = require('fs');

if (process.argv[2] && process.argv[3]) {
  fs.writeFile(process.argv[2], process.argv[3], err => {
    if (err) {
      console.error(err);
    }
  // file written successfully
  });
}
