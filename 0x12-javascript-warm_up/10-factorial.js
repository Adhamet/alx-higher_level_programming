#!/usr/bin/node
function factorial (n) {
  if (n === 0 || n === 1) {
    return 1;
  } else {
    return factorial(n - 1) * n;
  }
}
const numArg = process.argv[2];
if (numArg === undefined) {
  console.log(1);
} else {
  console.log(factorial(numArg));
}
