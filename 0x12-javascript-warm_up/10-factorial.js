#!/usr/bin/node
function factorial (num) {
  if (num === 0 || isNaN(num)) {
    return 1;
  }
  return num * factorial(num - 1);
}
const a = parseInt(process.argv[2]);
console.log(factorial(a));
