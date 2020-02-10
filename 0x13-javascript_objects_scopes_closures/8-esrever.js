#!/usr/bin/node
exports.esrever = function (list) {
  if (list.length > 0) {
    const rlist = [];
    const len = list.length;
    for (let con = 0; con < len; con++) {
      rlist[len - con - 1] = list[con];
    }
    return (rlist);
  }
};
