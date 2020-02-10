#!/usr/bin/node
let a = -1;
const makeCounter = function (b) {
  a = a + b;
  return (a);
};

exports.logMe = function (item) {
  const coun = makeCounter(1);
  let pr = coun + ": " + item;
  console.log(pr);
};
