#!/usr/bin/node
let num = process.argv.slice(2);
if (num.length === 0 || num.length === 1) {
  console.log(0);
} else {
  num = num.map(Number);
  num.sort(function (a, b) { return b - a; });
  console.log(num[1]);
}
