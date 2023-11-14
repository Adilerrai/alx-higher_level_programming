#!/usr/bin/node
function swap (arr, firstIndex, secondIndex) {
  const temp = arr[firstIndex];
  arr[firstIndex] = arr[secondIndex];
  arr[secondIndex] = temp;
}
function bubbleSortAlgo (arraaytest) {
  const len = arraaytest.length;
  let i; let j; let stop;
  for (i = 0; i < len; i++) {
    for (j = 0, stop = len - i; j < stop; j++) {
      if (Number(arraaytest[j]) > Number(arraaytest[j + 1])) {
        swap(arraaytest, j, j + 1);
      }
    }
  } return arraaytest;
}
const process = require('process');
const args = process.argv;
const array = args.slice(2);

const sortedArray = bubbleSortAlgo(array);

// Using negative indexing to get the item before the last
const itemBeforeLast = sortedArray[sortedArray.length - 2];
console.log(itemBeforeLast);
