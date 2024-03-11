#!/usr/bin/node
const len = process.argv.length;
const x = process.argv.slice(2).map(function (num) {
  return parseInt(num);
});
const topp = Math.max.apply(Math, x);
const bott = Math.min.apply(Math, x);
if (len > 3) {
  let a = 0;
  let n = 0;
  let second = bott;
  for (; a < len; ++a) {
    n = x[a];
    if (n > second && n < topp) {
      second = n;
    }
  }
  console.log(second);
} else {
  console.log(0);
}
