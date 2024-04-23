#!/usr/bin/node
const req = require('request');
const link = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2] + '/';
req(link, function (error, response, body) {
  console.log(error || JSON.parse(body).title);
});
