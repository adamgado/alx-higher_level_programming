#!/usr/bin/node
const Square1 = require('./5-square');
module.exports = class Square extends Square1 {
  constructor (size) {
    super(size, size);
  }
  charPrint (c = 'X') {
    super.print(c);
  }
};
