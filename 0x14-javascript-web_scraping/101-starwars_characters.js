#!/usr/bin/node

const request = require('request');
const movieID = process.argv[2];

if (!movieID) {
  console.error('Missing argument');
  process.exit(1);
}

const apiURL = 'https://swapi-api.hbtn.io/api/films/' + movieID;

request(apiURL, function (error, response, body) {
  if (error) {
    console.error(error);
  } else {
    const characters = JSON.parse(body).characters;
    for (const character of characters) {
      request(character, function (error, response, body) {
        if (error) {
          console.error(error);
        } else {
          console.log(JSON.parse(body).name);
        }
      });
    }
  }
});
