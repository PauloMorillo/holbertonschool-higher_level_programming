#!/usr/bin/node
let charac = 'X';
if (Math.floor(process.argv[2])) {
  const sizes = Math.floor(process.argv[2]);
  for (let con = 0; con < sizes; con++) {
    for (let con2 = 1; con2 < sizes; con2++) {
      charac = charac + 'X';
    }
    console.log(charac);
    charac = 'X';
  }
} else {
  console.log('Missing size');
}
