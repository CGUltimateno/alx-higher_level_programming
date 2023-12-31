#!/usr/bin/node
/**
 * Script that reads and prints the content of a file.
 */

const fs = require('fs');
const { argv } = require('process');

if (argv.length === 3) {
  fs.readFile(argv[2], 'utf-8', (err, data) => {
    if (err) {
      console.log(err);
    } else {
      console.log(data.toString());
    }
  });
}