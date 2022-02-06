const fs = require("fs");
const readline = require("readline");

const fileStream = fs.createReadStream("./file.txt");
const rl = readline.createInterface({
  input: fileStream
});

const usage = {};

rl.on("line", function (line) {
  const ip = line.split(' ')[1];
  if (usage[ip]) usage[ip]++;
  else usage[ip] = 1;
});

rl.on("close", function () {
  const pairs = Object.entries(usage).sort((a, b) => b[1] - a[1]);
  let i = 0;
  for (const pair of pairs) {
    console.log(pair[0]);
    i++;
    if(i == 3) break;
  }
});
