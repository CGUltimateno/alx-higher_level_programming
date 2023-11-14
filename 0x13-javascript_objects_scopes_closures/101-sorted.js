#!/usr/bin/node
const dict = require('./101-data').dict;
const users = Object.values(dict);
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
