#!/usr/bin/node
/**
 * Script that prints the title of a Star Wars movie where the episode number
 */

const request = require('request');
const { argv } = require('process');

if (argv.length === 3) {
    request(`https://swapi-api.hbtn.io/api/films/${argv[2]}`, (err, res) => {
        if (err) {
        console.log(err);
        } else {
        console.log(JSON.parse(res.body).title);
        }
    });
}