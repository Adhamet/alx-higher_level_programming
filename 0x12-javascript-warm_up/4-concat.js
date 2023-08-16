#!/usr/bin/node
const myArgs = process.argv.slice(2);
if (myArgs[0] && myArgs[1]) {
  console.log(`${myArgs[0]}` + ' is ' + `${myArgs[1]}`);
} else if (myArgs[0] && !myArgs[1]) {
  console.log(`${myArgs[0]}` + ' is ' + 'undefined');
} else {
  console.log('undefined is undefined');
}
