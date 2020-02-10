#!/usr/bin/node
const Square1 = require('./5-square');

class Square extends Square1 {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    if (c === undefined) {
      super.print();
    } else {
      for (let con = 0; con < this.height; con++) {
        let charac = c;
        for (let con2 = 1; con2 < this.width; con2++) {
          charac = charac + c;
        }
        console.log(charac);
      }
    }
  }
}
module.exports = Square;
