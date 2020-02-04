#!/usr/bin/node
if (process.argv[2] && process.argv[3]) {
  let secon = Math.floor(process.argv[3]);
  let last = Math.floor(process.argv[2]);
  for (let con = 0; con < process.argv.length; con++) {
    if (last < process.argv[con]) {
      secon = last;
      last = process.argv[con];
    }
  }
  console.log(secon);
} else if (process.argv[2]) {
  console.log('0');
} else {
  console.log('0');
}
