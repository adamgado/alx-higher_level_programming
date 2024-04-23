#!/usr/bin/node
const file = require('fs');
const req = require('request');
req(process.argv[2]).pipe(file.createWriteStream(process.argv[3]));
