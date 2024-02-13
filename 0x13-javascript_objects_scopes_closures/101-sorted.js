#!/usr/bin/node

const dict = require('./101-data.js').dict;

const newDct = {};

for (const key in dict) {
  if (newDct[dict[key]] === undefined) {
    newDct[dict[key]] = [key];
  } else {
    newDct[dict[key]].push(key);
  }
}

console.log(newDct);
