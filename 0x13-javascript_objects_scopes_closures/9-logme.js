#!/usr/bin/node
let a = 0;
const makeCounter = function (b) {
  a = a + b;
  return (a);
};

exports.logMe = function (item) {
  const coun = makeCounter(1);
  console.log(coun, item);
};
