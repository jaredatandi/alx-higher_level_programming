#!/usr/bin/node
/*
 * print a simple message using a const variable
 * to the console log
 */

function printMessage (x) {
  // Check if x is a number
  if (isNaN(x)) {
    // If it is not a number, print "Missing number of occurrences"
    console.log('Missing number of occurrences');
  } else {
    // If it is a number, convert it to an integer and use a loop to print the message x times
    x = parseInt(x, 10);
    for (let i = 0; i < x; i++) {
      console.log('C is fun');
    }
  }
}

const number = process.argv[2];
printMessage(number);
