#!/usr/bin/node
/*
 * print a simple message using a const variable
 * to the console log
 */

const text1 = process.argv[2];
const text2 = process.argv[3];

const result = text1.concat(' is ', text2);

console.log(result);
