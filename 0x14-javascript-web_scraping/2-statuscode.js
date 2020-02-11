#!/usr/bin/node
if (process.argv[2]) {
  const request = require('request');
  const url = process.argv[2];
  request(url, function (error, response, body) {
    if (error) {
      console.log(error);
    } else {
      console.log('code: ' + response.statusCode);
      // console.log(JSON.parse(body));
    }
  });
}
