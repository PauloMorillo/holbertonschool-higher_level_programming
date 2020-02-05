#!/usr/bin/node
exports.callMeMoby = function (x, theFunction) {
  for (let con = 0; con < x; con++) {
    arguments[1]();
    // callMeMoby()
  }
};
