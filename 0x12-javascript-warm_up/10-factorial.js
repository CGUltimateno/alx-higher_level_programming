#!/usr/bin/node
function factorial (n) {
  if (isNaN(n) || n === 1) {
    return 1;
  }
  return n * factorial(n - 1);


}
const inputArgument = process.argv[2];
const inputNumber = parseInt(inputArgument);
console.log(`Factorial of ${inputNumber} is: ${calculateFactorial(inputNumber)}`);
