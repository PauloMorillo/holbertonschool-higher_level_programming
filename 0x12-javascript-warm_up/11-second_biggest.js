#!/usr/bin/node
function sortNumber (a, b) {
  return a - b;
}

if (process.argv[2] && process.argv[3]) {
  const sortargu = process.argv.sort(sortNumber);
  const leng = sortargu.length;
  console.log(sortargu[leng - 2]);
} else if (process.argv[2]) {
  console.log('0');
} else {
  console.log('0');
}
