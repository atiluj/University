console.log(`jesteśmy w pliku modul.js`);
var f;

function g() {
    f = require("./zadanie_03");
    if (typeof f === "function") return f();
    return "f nie jest funkcją!";
}

module.exports = g;
