const fs = require("fs");

const text = fs.readFileSync("z5-text.txt");
process.stdout.write(text);