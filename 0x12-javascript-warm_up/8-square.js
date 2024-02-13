#!/usr/bin/node

const size = parseInt(process.argv[2]);

if (isNaN(size) || size < 1) {
  console.log('Missing size');
} else {
  for (let i = 0; i < size; i++) {
    const row = '';
    for (let ii = 0; ii < size; ii++) {
      line += 'X';
    }
    console.log(row);
  }
}
