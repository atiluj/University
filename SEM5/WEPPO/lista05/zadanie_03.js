const http = require("http");
const fs = require("fs");

http.createServer((req, res) => {
    res.setHeader("Content-Disposition", 'attachment; filename="zadanie.js"');
    res.setHeader("Content-Type", "application/javascript");

    res.write(fs.readFileSync("zadanie_03.js"));
    res.end();
  }).listen(3000);
