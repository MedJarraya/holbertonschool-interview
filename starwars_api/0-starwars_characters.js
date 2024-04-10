#!/usr/bin/node
/* This script prints characters
    of Star Wars movie */
    const request = require('request');
    const process = require('process');
    
    const Id = process.argv[2];
    const url = `https://swapi.dev/api/films/${Id}/`;
    
    request.get(url, async (error, response, body) => {
        if (error) {
            console.error(error);
            return;
        }
    
        const characters = JSON.parse(body).characters;
        for (const character of characters) {
            try {
                const people = await new Promise((resolve, reject) => {
                    request(character, (error, response, body) => {
                        if (error) {
                            reject(error);
                        } else {
                            resolve(JSON.parse(body).name);
                        }
                    });
                });
                console.log(people);
            } catch (error) {
                console.error(error);
            }
        }
    });
    