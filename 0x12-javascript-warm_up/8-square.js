#!/usr/bin/node
const x = parseInt(process.argv[2]);
if (x) {
  for (let a = 0; a < x; ++a) {
    let b = 0;
    for (; b < x; ++b) {
      process.stdout.write('X');
    }
    if (b === x) {
      console.log('');
    }
  }
} else {
  console.log('Missing size');
}
