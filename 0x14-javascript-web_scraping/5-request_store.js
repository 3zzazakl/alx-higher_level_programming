#!/usr/bin/node

const request = require('request');
const fs = require('fs');

const url = process.argv[2];
const filePath = process.argv[3];

if (!url || !filePath) {
  console.error('Missing arguments');
  process.exit(1);
}

request(url, function (error, response, body) {
  if (error) {
    console.error(error);
  } else if (response.statusCode !== 200) {
    console.error('Invalid status code <' + response.statusCode + '>');
  } else {
    fs.writeFile(filePath, body, function (err) {
      if (err) {
        console.error(err);
      }
    });
  }
});
