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
      // console.log(data);
      const dictuser = {};
      for (let con = 0; con < data.length; con++) {
        if (data[con].completed === true) {
          if (dictuser[data[con].userId]) {
            dictuser[data[con].userId] = dictuser[data[con].userId] + 1;
          } else {
            dictuser[data[con].userId] = 1;
          }
        }
      // console.log(data.results[con].characters[0]);
      }
      console.log(dictuser);
    }
  });
}
