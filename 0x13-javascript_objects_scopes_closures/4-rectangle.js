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

  double () {
    this.height = this.height * 2;
    this.width = this.width * 2;
  }

  rotate () {
    const tem = this.height;
    this.height = this.width;
    this.width = tem;
    // this.width = this.height;
  }
}

module.exports = Rectangle;
