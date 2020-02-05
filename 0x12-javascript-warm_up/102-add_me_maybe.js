#!/usr/bin/node
exports.addMeMaybe = function (number, theFunction) {
  arguments[1](number + 1);
};
