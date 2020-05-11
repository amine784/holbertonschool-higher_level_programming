#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if (w > 0 && Number.isInteger(w) !== false &&
      h > 0 && Number.isInteger(h) !== false) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let i = 0; i < this.height; i++) {
      console.log('X'.repeat(this.width));
    }
  }

  rotate () {
    const tmp = this.width;
    this.width = this.height;
    this.height = tmp;
  }

  double () {
    this.width *= 2;
    this.height *= 2;
  }
}
module.exports = Rectangle;
