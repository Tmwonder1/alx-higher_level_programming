#!/usr/bin/node
const fs = require('fs');

// Extract command line arguments for file path and string to write
const filePath = process.argv[2];
const contentToWrite = process.argv[3];

// Function to write the string to the specified file
function writeStringToFile(path, content) {
  fs.writeFile(path, content, 'utf8', (err) => {
    if (err) {
      // If there's an error, print the error object
      console.error(err);
    }
  });
}

// Call the function with the provided arguments
writeStringToFile(filePath, contentToWrite);
