#!/usr/bin/node
const process = require('process');
const args = process.argv;
const NewList = args.slice(2);
if (isNaN(Number(NewList[0])) || Number(NewList[0]) < 0) {
  console.log('Missing size');
} else if (Number(NewList[0]) > 0) {
  let output = '';
  for (let i = 0; i < Number(NewList[0]); i++) {
    output += 'X';
  }
  console.log(output.trim());
}
