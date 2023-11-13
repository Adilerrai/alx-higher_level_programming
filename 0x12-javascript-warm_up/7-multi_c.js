#!/usr/bin/node
const process = require('process');
const args = process.argv;
const NewList = args.slice(2);
if (isNaN(Number(NewList[0]))) {
  console.log('Missing number of occurrences');
} else {
  if (Number(NewList[0]) > 0) {
    for (let i = 0; i < Number(NewList[0]); i++) {
      console.log('C is fun');
    }
  }
}
