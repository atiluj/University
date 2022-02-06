console.log(`\njesteśmy w pliku zadanie_03.js`);
console.log('spróbujmy włączyć moduł do kodu')
const g = require("./modul");
console.log(`wrocilismy do pliku zadanie_03.js`);

function f() 
{ 
    return "Udało się!"; 
}

module.exports = f;

console.log(g());