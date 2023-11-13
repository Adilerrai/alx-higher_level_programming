#!/usr/bin/node
const process = require('process');
const args = process.argv;
const newList = args.slice(2);
if (newList[0] === undefined) {
  console.log('No argument');
} else {
  console.log(newList[0]);
}
