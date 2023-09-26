#!/usr/bin/node
const request = require('request');
const endpoint = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];
request({ url: endpoint, methods: 'GET' }, function (err, response, body) {
  if (err) {
    console.log(err);
  } else {
    console.log(body && JSON.parse(body).title);
  }
});
