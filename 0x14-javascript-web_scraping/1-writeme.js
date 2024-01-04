#!/usr/bin/node
/**
 * Script that writes a string to a file.
 *
 */

const fs = require('fs');
const { argv } = require('process');

if (argv.length === 4) {
    fs.writeFile(argv[2], argv[3], 'utf-8', (err, data) => {
        if (err) {
        console.log(err);
        }
    });
}