#!/usr/bin/node

const i = parseInt(process.argv[2]);

if (!isNaN(i)) {
  for (let ii = 0; ii < i; ii++) {
    console.log('C is fun');
  }
} else {
  console.log('Missing number of occurrences');
}
