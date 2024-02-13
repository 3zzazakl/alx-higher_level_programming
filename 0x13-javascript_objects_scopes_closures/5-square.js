#!/usr/bin/node

const Rect = require('./4-rectangle');

class Square extends Rect {
  constructor (size) {
    super(size, size);
  }
}

module.exports = Square;
