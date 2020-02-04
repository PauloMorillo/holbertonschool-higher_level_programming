#!/usr/bin/node
const factorial = function (a) {
  if (a === 1) {
    return 1;
  }
  return (factorial(a - 1) * a);
};
if (Math.floor(process.argv[2])) {
  console.log(factorial(Math.floor(process.argv[2])));
} else {
  console.log('1');
}
