function createFs(n){ // tworzy tablicę n funkcji
    var fs = []; // i-ta funkcja z tablicy ma zwrócić i
    for(var i=0; i<n; i++){
        fs[i] = function(){ return i; };
    };
    return fs;
}

function createFs2(n){ // tworzy tablicę n funkcji
    var fs = []; // i-ta funkcja z tablicy ma zwrócić i
    for(let i=0; i<n; i++){
        fs[i] = function(){ return i; };
    };
    return fs;
}
    
console.log("funkcja bez zmian");
var myfs = createFs(10);
//console.log(myfs);
console.log(myfs[0]()); // zerowa funkcja miała zwrócić 0
console.log(myfs[2]()); // druga miała zwrócić 2
console.log(myfs[7]());
// 10 10 10


console.log("zamiana var na let");
var myfs2 = createFs2(10);
//console.log(myfs2);
console.log(myfs2[0]()); // zerowa funkcja miała zwrócić 0
console.log(myfs2[2]()); // druga miała zwrócić 2
console.log(myfs2[7]());

// DLACZEGO ZASTĄPNIE VAR NA LET PRZY i W PĘTLI for POMOŻE
// let pozwala deklarować zmienne, których zakres jest 
// ograniczony do bloku, instrukcji lub wyrażenia, w którym jest używany. 
// W przeciwieństwie do słowa kluczowego var, które definiuje zmienną 
// globalnie lub lokalnie dla całej funkcji, niezależnie od zakresu bloku.
// W przypadku użycia let i otrzymuje nowe wiązanie dla każdej iteracji pętli. 
 
function pomFunc(i){
    return function(){
        return i;
    };
}

//NAPRAWA FUNKCJI BEZ ZASTĘPYWANIA VAR NA LET
function createFs3(n){ // tworzy tablicę n funkcji
    var fs = []; // i-ta funkcja z tablicy ma zwrócić i
    for(var i=0; i<n; i++){
        fs[i] = pomFunc(i)
    };
    return fs;
}

console.log("nowa funkcja");
var myfs3 = createFs3(10);
//console.log(myfs3);
console.log(myfs3[0]()); // zerowa funkcja miała zwrócić 0
console.log(myfs3[2]()); // druga miała zwrócić 2
console.log(myfs3[7]());

// CO ZORBI BABEL?
// Babel konwertuje let, var, const na var, ale zachowuje znaczenie zakresu.
// Babel konwertuje składnię ES6 na składnie ES5, co często powoduje utratę
// niekórych niuansów w kodzie.
