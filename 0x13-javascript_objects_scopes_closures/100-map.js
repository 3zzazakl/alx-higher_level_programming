#!/usr/bin/node

const { list } = require('./100-data');

const newlst = list.map((value, index) => value * index);

console.log(list);
console.log(newlst);
