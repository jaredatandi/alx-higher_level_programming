#!/usr/bin/node
let n = 0;
exports.legMe = function (item) {
  console.log(n + ': ' + item);
  n++;
};
