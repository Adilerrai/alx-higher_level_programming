#!/usr/bin/node
const process = require('process');
const args = process.argv.slice();
const list = args.slice(2);
if (list.length === 0) {
  console.log('undefined is undefined');
} else if (list.length === 1) {
  console.log(list[0] + ' is undefined');
} else if (list.length === 2) {
  console.log(list[0] + ' is ' + list[1]);
}
