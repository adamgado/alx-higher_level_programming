#!/usr/bin/node
const req = require('request');
const endPoint = 'http://swapi-api.hbtn.io/api/films/' + process.argv[2];
req.get(endPoint, function (err, response, body) {
  if (err) {
    throw err;
  } else if (response.statusCode === 200) {
    const characters = JSON.parse(body).characters;
    characters.forEach(character => {
      req.get(character, function (err, response, body) {
        if (err) {
          throw err;
        } else if (response.statusCode === 200) {
          console.log(JSON.parse(body).name);
        }
      });
    });
  }
});
