#!/usr/bin/node
if (Math.floor(process.argv[2])) {
  console.log('My number: ' + Math.floor(process.argv[2]));
} else {
  console.log('Not a number');
}
