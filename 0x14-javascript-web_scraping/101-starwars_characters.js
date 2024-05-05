#!/usr/bin/node

const request = require('request');
const movieID = process.argv[2];

if (!movieID) {
  console.error('Missing argument');
  process.exit(1);
}

const apiURL = `https://swapi-api.hbtn.io/api/films/${movieID}/`;

function getCharacter (url, callback) {
  request(url, function (error, response, body) {
    if (error) {
      console.error(error);
      return;
    }

    if (response.statusCode !== 200) {
      console.error('Invalid status code <' + response.statusCode + '>');
      return;
    }
    callback(JSON.parse(body).name);
  });
}

request(apiURL, function (error, response, body) {
  if (error) {
    console.error(error);
    process.exit(1);
  }
  if (response.statusCode !== 200) {
    console.error('Invalid status code <' + response.statusCode + '>');
    process.exit(1);
  }

  const movieData = JSON.parse(body);
  const characterUrls = movieData.characters;

  function fetchCharacter (urls) {
    let completedRequests = 0;
    const characterNames = new Array(urls.length);

    urls.forEach((url, index) => {
      getCharacter(url, function (name) {
        characterNames[index] = name;
        completedRequests++;
        if (completedRequests === urls.length) {
          characterNames.forEach(name => console.log(name));
        }
      });
    });
  }
  fetchCharacter(characterUrls);
});
