#!/usr/bin/node
const { list } = require('./101-data').list;
const users = Object.values(list);
const set = new Set(users);
const setaslist = Array.from(set);
const entries = Object.entries(dict);
const newDict = {};
let i = [];

setaslist.forEach((element) => {
    i = [];
    entries.forEach((entry) => {
        if (entry[1] === element) {
        i.push(entry[0]);
        }
    });
    newDict[element] = i;
});
console.log(newDict);