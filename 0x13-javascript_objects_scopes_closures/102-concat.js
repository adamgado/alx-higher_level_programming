#!/usr/bin/node
const fs = require('fs');
let result = '';
result = result.concat(fs.readFileSync(process.argv[2]));
result = result.concat(fs.readFileSync(process.argv[3]));
fs.writeFileSync(process.argv[4], result);
