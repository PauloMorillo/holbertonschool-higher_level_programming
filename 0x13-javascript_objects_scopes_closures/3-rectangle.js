#!/usr/bin/node
// This script create an empty class
class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let con = 0; con < this.height; con++) {
      let charac = 'X';
      for (let con2 = 1; con2 < this.width; con2++) {
        charac = charac + 'X';
      }
      console.log(charac);
    }
  }
}
module.exports = Rectangle;
