#!/usr/bin/node
// Script to find the second biggest number

function sortNumber (a, b) {
  return a - b;
}

const argslen = process.argv.length;
if (argslen === 2 || argslen === 3) {
  console.log('0');
} else {
  const arr = [];
  for (let i = 2; i < argslen; i++) {
    arr.push(process.argv[i]);
  }
  arr.sort(sortNumber);
  console.log(arr[arr.length - 2]);
}
