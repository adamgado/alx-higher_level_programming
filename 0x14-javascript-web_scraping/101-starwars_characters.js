#!/usr/bin/node
const req = require('request');
const endPoint = 'http://swapi-api.hbtn.io/api/films/' + process.argv[2];
req.get(endPoint, function (err, response, body) {
  if (err) {
    throw err;
  } else if (response.statusCode === 200) {
    const characters = JSON.parse(body).characters;
    const charlist = [];
    characters.forEach(character => {
      charlist.push(new Promise((resolve, reject) => {
        req.get(character, function (err, response, body) {
          if (err) {
            reject(err);
          } else if (response.statusCode === 200) {
            resolve(JSON.parse(body).name);
          }
        });
      }));
    });
    Promise.all(charlist).then(names => {
      names.forEach(name => console.log(name));
    });
  }
});
