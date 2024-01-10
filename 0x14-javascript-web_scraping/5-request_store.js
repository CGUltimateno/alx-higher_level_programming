#!/usr/bin/node
/**
 * Script that writes the contents of a webpage to a file.
 */

const request = require('request');
const fs = require('fs');

if (process.argv.length === 4) {
    request(process.argv[2], (err, res) => {
        if (err) {
        console.log(err);
        } else {
        fs.writeFile(process.argv[3], res.body, 'utf-8', (err) => {
            if (err) {
            console.log(err);
            }
        });
        }
    });
}