#!/usr/bin/node
/*
 * print a simple message using a const variable
 * to the console log
 */

function printNumber (arg) {
  // Check if the argument is a number
  const parsedNumber = parseInt(arg);

  if (isNaN(parsedNumber)) {
    console.log('Not a number');
  } else {
    console.log(`My number: ${arg}`);
  }
}

const number = parseInt(process.argv[2]);
printNumber(number);
