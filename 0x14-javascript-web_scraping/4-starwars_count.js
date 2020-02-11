#!/usr/bin/node
if (process.argv[2]) {
  const request = require('request');
  const url = process.argv[2];
  request(url, function (error, response, body) {
    if (error) {
      console.log(error);
    } else {
      // console.log('code: ' + response.statusCode);
      const data = JSON.parse(body);

      let numf = 0;
      for (let con = 0; con < data.results.length; con++) {
        for (let con2 = 0; con2 < data.results[con].characters.length; con2++) {
          if (data.results[con].characters[con2].indexOf('18') !== -1) {
            numf = numf + 1;
          }
        }
      // console.log(data.results[con].characters[0]);
      }
      console.log(numf);
    }
  });
}
