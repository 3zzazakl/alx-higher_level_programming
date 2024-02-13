#!/usr/bin/node

const files = require('fs');

const filea = files.readFileSync(process.argv[2], 'utf8');
const fileb = files.readFileSync(process.argv[3], 'utf8');

files.writeFileSync(process.argv[4], filea + fileb);
