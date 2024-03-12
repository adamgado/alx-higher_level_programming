#!/usr/bin/node
const dict = require('./101-data.js').dict;
let new_d = {};
for (let a in dict) {
  if (new_d[dict[a]] === undefined) {
    new_d[dict[a]] = [a];
  } else {
    new_d[dict[a]].push(a);
  }
}
console.log(new_d);
