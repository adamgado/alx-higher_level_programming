#!/usr/bin/node
const dict = require('./101-data.js').dict;
const newD = {};
for (const a in dict) {
  if (newD[dict[a]] === undefined) {
    newD[dict[a]] = [a];
  } else {
    newD[dict[a]].push(a);
  }
}
console.log(newD);
