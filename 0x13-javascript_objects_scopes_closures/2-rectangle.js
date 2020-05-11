#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if (w > 0 && Number.isInteger(w) !== false &&
      h > 0 && Number.isInteger(h) !== false) {
      this.width = w;
      this.height = h;
    }
  }
}
module.exports = Rectangle;
