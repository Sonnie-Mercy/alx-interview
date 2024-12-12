#!/usr/bin/node

const request = require('request');

// Get the movie ID from the command-line arguments
const movieId = process.argv[2];
if (!movieId) {
  console.error('Usage: ./0-starwars_characters.js <Movie_ID>');
  process.exit(1);
}

// URL for the Star Wars API with the movie ID
const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}/`;

// Fetch the movie data from the API
request(apiUrl, (err, response, body) => {
  if (err) {
    console.error(err);
    return;
  }

  if (response.statusCode !== 200) {
    console.error(`Failed to fetch movie data: ${response.statusCode}`);
    return;
  }

  const movieData = JSON.parse(body);
  const characters = movieData.characters;

  // Fetch and print each character in order
  const fetchCharacter = (index) => {
    if (index >= characters.length) {
      return;
    }

    request(characters[index], (err, response, body) => {
      if (err) {
        console.error(err);
        return;
      }

      if (response.statusCode === 200) {
        const characterData = JSON.parse(body);
        console.log(characterData.name);
        fetchCharacter(index + 1); // Fetch the next character
      } else {
        console.error(`Failed to fetch character: ${response.statusCode}`);
      }
    });
  };

  fetchCharacter(0);
});
