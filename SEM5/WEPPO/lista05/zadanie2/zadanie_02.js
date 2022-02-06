const https = require("https");
const fs = require("fs");

https.createServer(
      {
        pfx: fs.readFileSync("cert.pfx"),
      },
      function(req, res){
        res.writeHead(200, { 'Content-Type': 'text/html' });
        res.end('Hello World!\n');
      }
).listen(3000);