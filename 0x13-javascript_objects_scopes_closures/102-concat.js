#!/usr/bin/node
const filesystem = require('fs').promises;

filesystem.readFile(process.argv[2])
  .then(contents => filesystem.writeFile(process.argv[4], contents))
  .catch(error => console.log(error));

filesystem.readFile(process.argv[3])
  .then(contents => filesystem.writeFile(process.argv[4],
    contents, { flag: 'a' }))
  .catch(error => console.log(error));
