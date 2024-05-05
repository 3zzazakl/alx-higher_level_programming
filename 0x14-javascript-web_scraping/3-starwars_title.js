#!/usr/bin/node

const MovieId = process.argv[2];
const request = require('request');
const url = `https://swapi-api.alx-tools.com/api/films/${MovieId}`;

request(url, function (error, response, body) {
    if (error) {
        console.log(error);
    }
    else {
        const movie = JSON.parse(body);
        console.log(movie.title);
    }  
});
