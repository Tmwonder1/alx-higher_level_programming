#!/usr/bin/node
const fs = require('fs');

// Get the file path from command line arguments
const filePath = process.argv[2];

// Function to read and print the file content
function readFileAndPrint(path) {
  fs.readFile(path, 'utf8', (err, data) => {
    if (err) {
      // Print the error in the desired format
      console.error(`{ Error: ${err.code}: no such file or directory, open '${err.path}'\n    at Error (native)\n  errno: ${err.errno},\n  code: '${err.code}',\n  syscall: '${err.syscall}',\n  path: '${err.path}' }`);
    } else {
      // Print the data if no error
      console.log(data);
    }
  });
}

// Call the function with the file path
readFileAndPrint(filePath);
