//npm install express
//npm i multer 
//npm install ejs

const express = require("express");
var http = require('http');

const app = express();
app.set("view engine", "ejs");
app.set("views", "./views");

app.get("/", (req, res) => {
  res.render("index.ejs");
});

http.createServer(app).listen(5200);
//http://localhost:5200

