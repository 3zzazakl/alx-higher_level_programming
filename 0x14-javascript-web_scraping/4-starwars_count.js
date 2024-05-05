#!/usr/bin/node

const request = require('request');
const apiUrl = process.argv[2];

request(apiUrl, function (error, response, body) {
  if (error) {
    console.error(error);
  } else if (response.statusCode !== 200) {
    console.error('Invalid status code <' + response.statusCode + '>');
  } else {
    const films = JSON.parse(body).results;
    const characterID = 18;
    let count = 0;

    films.forEach(film => {
      film.characters.forEach(character => {
        if (character.includes('/' + characterID + '/')) {
          count++;
        }
      });
    });
    console.log(count);
  }
});
