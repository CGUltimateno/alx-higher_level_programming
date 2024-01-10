#!/usr/bin/node
/**
 * Script that computes the number of tasks completed by user id.
 */
const request = require('request');
const { argv } = require('process');

if (argv.length === 3) {
    request(argv[2], (err, res) => {
        if (err) {
        console.log(err);
        } else {
            const todos = JSON.parse(res.body);
            const completed = {};
            for (const todo of todos) {
                if (todo.completed) {
                    if (completed[todo.userId]) {
                        completed[todo.userId]++;
                    } else {
                        completed[todo.userId] = 1;
                    }
                }
            }
            console.log(completed);
        }
    });
}