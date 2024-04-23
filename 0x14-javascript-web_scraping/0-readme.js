#!/usr/bin/node
const file_s = require('fs');
file_s.readFile(process.argv[2], 'utf8', function (error, content) {
  console.log(error || content);
});
