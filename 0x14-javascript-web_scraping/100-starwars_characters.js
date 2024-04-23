#!/usr/bin/node
const req = require('request');
const movieId = process.argv[2];
const link = 'https://swapi.co/api/films/' + movieId;
req(link, function (err, res, body) {
  if (err) {
    console.log(err);
  }
  const movie = JSON.parse(body);
  for (const characterId of movie.characters) {
    req(characterId, function (err, res, body) {
      if (err) {
        console.log(err);
      }
      const chara = JSON.parse(body);
      console.log(chara.name);
    });
  }
});
