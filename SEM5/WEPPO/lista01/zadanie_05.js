function fibonacciRec(n){
    if(n === 0)
        return 0;
    if(n === 1)
        return 1;
    return fibonacciRec(n - 1) + fibonacciRec(n - 2);
}

function fibonacciIter(n){
    if(n === 0)
        return 0;
    var result = 0;
    for(let i = 1; i <= n; i++){
        result = result + i;
    }
    return result;
}

//console.info(fibonacciIter(5));

for(let i = 10; i <= 43; i++){
    console.log(`Zmierzenie czasu dla liczby ${i}`);

    console.time("Fibonacci iteracyjnie");
    fibonacciIter(i);
    console.timeEnd("Fibonacci iteracyjnie");

    console.time("Fibonacci rekurencyjnie");
    fibonacciRec(i);
    console.timeEnd("Fibonacci rekurencyjnie");

    console.log("---------------------------------------------");
}

//Występują różnice w pomiarach w zaleźności od środowiska
//Najlepiej wypada node.js, następnie Chrom i Opera

//NODE.JS
//Dla i = 40 znacznie zwalnia
// ---------------------------------------------
// Zmierzenie czasu dla liczby 40
// Fibonacci iteracyjnie: 0.201ms
// Fibonacci rekurencyjnie: 1.650s
// ---------------------------------------------
// Zmierzenie czasu dla liczby 41
// Fibonacci iteracyjnie: 0.158ms
// Fibonacci rekurencyjnie: 2.594s
// ---------------------------------------------
// Zmierzenie czasu dla liczby 42
// Fibonacci iteracyjnie: 0.136ms
// Fibonacci rekurencyjnie: 4.205s
// ---------------------------------------------
// Zmierzenie czasu dla liczby 43
// Fibonacci iteracyjnie: 0.136ms
// Fibonacci rekurencyjnie: 6.759s
// ---------------------------------------------
// Zmierzenie czasu dla liczby 44
// Fibonacci iteracyjnie: 0.164ms
// Fibonacci rekurencyjnie: 11.567s
// ---------------------------------------------

//CHROME
// ---------------------------------------------
// VM65:22 Zmierzenie czasu dla liczby 40
// VM65:26 Fibonacci iteracyjnie: 0.00390625 ms
// VM65:30 Fibonacci rekurencyjnie: 1883.58203125 ms
// VM65:32 ---------------------------------------------
// VM65:22 Zmierzenie czasu dla liczby 41
// VM65:26 Fibonacci iteracyjnie: 0.003173828125 ms
// VM65:30 Fibonacci rekurencyjnie: 2957.06103515625 ms
// VM65:32 ---------------------------------------------
// VM65:22 Zmierzenie czasu dla liczby 42
// VM65:26 Fibonacci iteracyjnie: 0.005859375 ms
// VM65:30 Fibonacci rekurencyjnie: 5246.39501953125 ms
// VM65:32 ---------------------------------------------
// VM65:22 Zmierzenie czasu dla liczby 43
// VM65:26 Fibonacci iteracyjnie: 0.005126953125 ms
// VM65:30 Fibonacci rekurencyjnie: 8115.865966796875 ms
// VM65:32 ---------------------------------------------
// VM65:22 Zmierzenie czasu dla liczby 44
// VM65:26 Fibonacci iteracyjnie: 0.004638671875 ms
// Fibonacci rekurencyjnie: 13079.572021484375 ms
// VM65:32 ---------------------------------------------


// OPERA
// ---------------------------------------------
// VM40:22 Zmierzenie czasu dla liczby 41
// VM40:26 Fibonacci iteracyjnie: 0.005859375 ms
// VM40:30 Fibonacci rekurencyjnie: 3410.926025390625 ms
// VM40:32 ---------------------------------------------
// VM40:22 Zmierzenie czasu dla liczby 42
// VM40:26 Fibonacci iteracyjnie: 0.005126953125 ms
// VM40:30 Fibonacci rekurencyjnie: 5358.09912109375 ms
// VM40:32 ---------------------------------------------
// VM40:22 Zmierzenie czasu dla liczby 43
// VM40:26 Fibonacci iteracyjnie: 0.006103515625 ms
// VM40:30 Fibonacci rekurencyjnie: 8286.326171875 ms
// VM40:32 ---------------------------------------------
// VM40:22 Zmierzenie czasu dla liczby 44
// VM40:26 Fibonacci iteracyjnie: 0.00390625 ms
// VM40:30 Fibonacci rekurencyjnie: 13218.06201171875 ms
// VM40:32 ---------------------------------------------