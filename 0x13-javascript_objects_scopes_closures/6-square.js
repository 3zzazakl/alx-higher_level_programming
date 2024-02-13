#!/usr/bin/node

const Rect = require('./5-square');

class Square extends Rect {
  charPoint (c) {
    if (c === undefined) {
      c = 'X';
    }

    for (let i = 0; i < this.height; i++) {
      let row = '';
      for (let ii = 0; ii < this.width; ii++) {
        row += c;
      }
      console.log(row);
    }
  }
}

module.exports = Square;
