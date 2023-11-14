#!/usr/bin/node
const Rectangle = require('./4-rectangle');

class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }

  // Overriding the print method
  print () {
    for (let i = 0; i < this.height; i++) {
      console.log('X'.repeat(this.width));
    }
  }

  // New method to double the size of the square
  double () {
    this.width *= 2;
    this.height *= 2;
  }
}

module.exports = Square;
