#!/usr/bin/node
const process = require('process');
const args = process.argv;
const arglist = args.slice(2);
if (arglist.length > 2) {
  console.log('NaN');
} else {
  const result = add(Number(arglist[0]), Number(arglist[1]));
  console.log(result);
}

function add (a, b) {
  return a + b;
}
