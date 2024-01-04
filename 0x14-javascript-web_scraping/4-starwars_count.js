#!/usr/bin/node
/**
 * Script that prints the number of movies where the character “Wedge Antilles”
 * is present.
 */

const request = require('request');
const { argv } = require('process');

if (argv.length === 3) {
    request(argv[2], (err, res) => {
        if (err) {
        console.log(err);
        } else {
        console.log(JSON.parse(res.body).results.reduce((count, film) => {
            return count + film.characters.filter((character) => character.includes('18')).length;
        }, 0));
        }
    });
}