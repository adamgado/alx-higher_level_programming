#!/usr/bin/node
const req = require('request');
req(process.argv[2], function (error, response, body) {
  if (!error) {
    const todolist = JSON.parse(body);
    let tododone = {};
    todolist.forEach((todo) => {
      if (todo.completed && tododone[todo.userId] === undefined) {
        tododone[todo.userId] = 1;
      } else if (todo.completed) {
        tododone[todo.userId] += 1;
      }
    });
    console.log(tododone);
  }
});
