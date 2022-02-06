//npm install express
//npm i multer 
//na podstawie kodu z wykładu 

const express = require("express");
const multer = require("multer");
var http = require('http');
const app = express();
const upload = multer({ dest: "przesłane/" });

app.get("/", (req, res) => {
  res.send(`
  <form method="POST" action="/" enctype="multipart/form-data">
    <input type="file" name="plik">
    <button>WYŚLIJ</button>
  </form>`);
});

app.post("/", upload.single("plik"), (req, res) => {
  res.send(
    `<p>Przesłano plik!</p>`);
});

http.createServer(app).listen(4000);
//http://localhost:4000
