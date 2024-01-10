#!/usr/bin/node
/**
 * Script that display the status code of a GET request.
 */

const request = require('request');
const { argv } = require('process');

if (argv.length === 3) {
    request(argv[2], (err, res) => {
        if (err) {
        console.log(err);
        } else {
        console.log('code:', res.statusCode);
        }
    });
}