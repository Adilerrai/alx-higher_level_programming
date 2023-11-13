#!/usr/bin/node
const process = require('process');
const args = process.argv;
const newList = args.slice(2,);
const intayger = Math.trunc(Number(newList[0]));
if(isNaN(intayger)) {
	console.log('Not a number');
}else{
	console.log('My number:' + intayger);
}
