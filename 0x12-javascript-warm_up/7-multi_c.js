#!/usr/bin/node
const myVar = 'C is fun';
if (process.argv[2]) {
  for (let con = 0; con < Math.floor(process.argv[2]); con++) {
    console.log(myVar);
  }
} else {
  console.log('Missing number of occurrences');
}
