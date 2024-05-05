#!/usr/bin/node

const request = require('request');
const apiURL = process.argv[2];

if (!apiURL) {
  console.error('Missing argument');
  process.exit(1);
}

request(apiURL, function (error, response, body) {
  if (error) {
    console.error(error);
  } else {
    const completedTasks = {};
    const tasks = JSON.parse(body);
    for (const task of tasks) {
      if (task.completed) {
        if (!completedTasks[task.userId]) {
          completedTasks[task.userId] = 0;
        }
        completedTasks[task.userId] += 1;
      }
    }
    console.log(completedTasks);
  }
});
