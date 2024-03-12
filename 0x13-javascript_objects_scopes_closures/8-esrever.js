#!/usr/bin/node
exports.esrever = function (list) {
  let end = list.length - 1;
  let start = 0;
  while ((end - start) > 0) {
    const temp = list[end];
    list[end] = list[start];
    list[start] = temp;
    start++;
    end--;
  }
  return list;
};
