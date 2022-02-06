
//lista 1 zad 5 - REKURENCJA
function fibonacciRec(n){
    if(n === 0)
        return 0;
    if(n === 1)
        return 1;
    return fibonacciRec(n - 1) + fibonacciRec(n - 2);
}

//lista 1 zad 5 - ITERACJA
function fibonacciIter(n){
    if(n === 0)
        return 0;
    var result = 1, p1 = 0;
    for(let i = 1; i <= n; i++){
        const p2 = result;
        result = result + p1;
        p1 = p2;
    }
    return result;
}

// MEMOIZACJA

function memoization(fun){
    const memo = {};
    return function(x){
        if(memo[x] === undefined){
            memo[x] = fun(x);
            return memo[x];
        }
        return memo[x];
    };
}

const fibonacciMemo = memoization((n) => {
    if(n == 0)
        return 0;
    if(n == 1)
        return 1;
    return fibonacciMemo(n - 1) + fibonacciMemo(n - 2);
});


for(let i = 10; i <= 43; i++){
    console.log(`Zmierzenie czasu dla liczby ${i}`);

    console.time("Fibonacci iteracyjnie");
    fibonacciIter(i);
    console.timeEnd("Fibonacci iteracyjnie");

    console.time("Fibonacci rekurencyjnie");
    fibonacciRec(i);
    console.timeEnd("Fibonacci rekurencyjnie");

    console.time("Fibonacci memoizacja");
    fibonacciMemo(i);
    console.timeEnd("Fibonacci memoizacja");

    console.log("---------------------------------------------");
}

// Zmierzenie czasu dla liczby 10
// Fibonacci iteracyjnie: 2.268ms
// Fibonacci rekurencyjnie: 0.209ms
// Fibonacci memoizacja: 0.353ms
// ---------------------------------------------
// Zmierzenie czasu dla liczby 11
// Fibonacci iteracyjnie: 0.168ms
// Fibonacci rekurencyjnie: 0.195ms
// Fibonacci memoizacja: 0.178ms
// ---------------------------------------------
// Zmierzenie czasu dla liczby 12
// Fibonacci iteracyjnie: 0.147ms
// Fibonacci rekurencyjnie: 0.185ms
// Fibonacci memoizacja: 0.206ms
// ---------------------------------------------
// Zmierzenie czasu dla liczby 13
// Fibonacci iteracyjnie: 0.194ms
// Fibonacci rekurencyjnie: 0.227ms
// Fibonacci memoizacja: 0.144ms
// ---------------------------------------------
// Zmierzenie czasu dla liczby 14
// Fibonacci iteracyjnie: 0.152ms
// Fibonacci rekurencyjnie: 0.27ms
// Fibonacci memoizacja: 0.184ms
// ---------------------------------------------
// Zmierzenie czasu dla liczby 15
// Fibonacci iteracyjnie: 0.132ms
// Fibonacci rekurencyjnie: 0.315ms
// Fibonacci memoizacja: 0.158ms
// ---------------------------------------------
// Zmierzenie czasu dla liczby 16
// Fibonacci iteracyjnie: 0.142ms
// Fibonacci rekurencyjnie: 0.417ms
// Fibonacci memoizacja: 0.17ms
// ---------------------------------------------
// Zmierzenie czasu dla liczby 17
// Fibonacci iteracyjnie: 0.159ms
// Fibonacci rekurencyjnie: 0.566ms
// Fibonacci memoizacja: 0.165ms
// ---------------------------------------------
// Zmierzenie czasu dla liczby 18
// Fibonacci iteracyjnie: 0.138ms
// Fibonacci rekurencyjnie: 2.125ms
// Fibonacci memoizacja: 0.142ms
// ---------------------------------------------
// Zmierzenie czasu dla liczby 19
// Fibonacci iteracyjnie: 0.137ms
// Fibonacci rekurencyjnie: 0.328ms
// Fibonacci memoizacja: 0.171ms
// ---------------------------------------------
// Zmierzenie czasu dla liczby 20
// Fibonacci iteracyjnie: 0.15ms
// Fibonacci rekurencyjnie: 1.839ms
// Fibonacci memoizacja: 0.177ms
// ---------------------------------------------
// Zmierzenie czasu dla liczby 21
// Fibonacci iteracyjnie: 0.187ms
// Fibonacci rekurencyjnie: 0.56ms
// Fibonacci memoizacja: 0.187ms
// ---------------------------------------------
// Zmierzenie czasu dla liczby 22
// Fibonacci iteracyjnie: 0.505ms
// Fibonacci rekurencyjnie: 0.844ms
// Fibonacci memoizacja: 0.136ms
// ---------------------------------------------
// Zmierzenie czasu dla liczby 23
// Fibonacci iteracyjnie: 0.138ms
// Fibonacci rekurencyjnie: 1.338ms
// Fibonacci memoizacja: 0.189ms
// ---------------------------------------------
// Zmierzenie czasu dla liczby 24
// Fibonacci iteracyjnie: 0.158ms
// Fibonacci rekurencyjnie: 1.609ms
// Fibonacci memoizacja: 0.162ms
// ---------------------------------------------
// Zmierzenie czasu dla liczby 25
// Fibonacci iteracyjnie: 0.135ms
// Fibonacci rekurencyjnie: 2.642ms
// Fibonacci memoizacja: 4.83ms
// ---------------------------------------------
// Zmierzenie czasu dla liczby 26
// Fibonacci iteracyjnie: 0.14ms
// Fibonacci rekurencyjnie: 3.774ms
// Fibonacci memoizacja: 0.135ms
// ---------------------------------------------
// Zmierzenie czasu dla liczby 27
// Fibonacci iteracyjnie: 0.144ms
// Fibonacci rekurencyjnie: 6.218ms
// Fibonacci memoizacja: 0.21ms
// ---------------------------------------------
// Zmierzenie czasu dla liczby 28
// Fibonacci iteracyjnie: 0.166ms
// Fibonacci rekurencyjnie: 9.231ms
// Fibonacci memoizacja: 0.149ms
// ---------------------------------------------
// Zmierzenie czasu dla liczby 29
// Fibonacci iteracyjnie: 0.17ms
// Fibonacci rekurencyjnie: 15.252ms
// Fibonacci memoizacja: 0.145ms
// ---------------------------------------------
// Zmierzenie czasu dla liczby 30
// Fibonacci iteracyjnie: 0.16ms
// Fibonacci rekurencyjnie: 23.807ms
// Fibonacci memoizacja: 0.194ms
// ---------------------------------------------
// Zmierzenie czasu dla liczby 31
// Fibonacci iteracyjnie: 0.162ms
// Fibonacci rekurencyjnie: 39.616ms
// Fibonacci memoizacja: 0.151ms
// ---------------------------------------------
// Zmierzenie czasu dla liczby 32
// Fibonacci iteracyjnie: 0.147ms
// Fibonacci rekurencyjnie: 54.844ms
// Fibonacci memoizacja: 0.579ms
// ---------------------------------------------
// Zmierzenie czasu dla liczby 33
// Fibonacci iteracyjnie: 0.19ms
// Fibonacci rekurencyjnie: 72.811ms
// Fibonacci memoizacja: 0.116ms
// ---------------------------------------------
// Zmierzenie czasu dla liczby 34
// Fibonacci iteracyjnie: 0.094ms
// Fibonacci rekurencyjnie: 105.796ms
// Fibonacci memoizacja: 0.14ms
// ---------------------------------------------
// Zmierzenie czasu dla liczby 35
// Fibonacci iteracyjnie: 0.138ms
// Fibonacci rekurencyjnie: 167.51ms
// Fibonacci memoizacja: 0.161ms
// ---------------------------------------------
// Zmierzenie czasu dla liczby 36
// Fibonacci iteracyjnie: 0.154ms
// Fibonacci rekurencyjnie: 282.797ms
// Fibonacci memoizacja: 0.155ms
// ---------------------------------------------
// Zmierzenie czasu dla liczby 37
// Fibonacci iteracyjnie: 0.146ms
// Fibonacci rekurencyjnie: 511.167ms
// Fibonacci memoizacja: 0.123ms
// ---------------------------------------------
// Zmierzenie czasu dla liczby 38
// Fibonacci iteracyjnie: 0.327ms
// Fibonacci rekurencyjnie: 754.602ms
// Fibonacci memoizacja: 0.156ms
// ---------------------------------------------
// Zmierzenie czasu dla liczby 39
// Fibonacci iteracyjnie: 0.151ms
// Fibonacci rekurencyjnie: 1.123s
// Fibonacci memoizacja: 0.323ms
// ---------------------------------------------
// Zmierzenie czasu dla liczby 40
// Fibonacci iteracyjnie: 0.174ms
// Fibonacci rekurencyjnie: 2.254s
// Fibonacci memoizacja: 0.107ms
// ---------------------------------------------
// Zmierzenie czasu dla liczby 41
// Fibonacci iteracyjnie: 0.09ms
// Fibonacci rekurencyjnie: 3.603s
// Fibonacci memoizacja: 0.11ms
// ---------------------------------------------
// Zmierzenie czasu dla liczby 42
// Fibonacci iteracyjnie: 0.1ms
// Fibonacci rekurencyjnie: 5.343s
// Fibonacci memoizacja: 0.094ms
// ---------------------------------------------
// Zmierzenie czasu dla liczby 43
// Fibonacci iteracyjnie: 0.15ms
// Fibonacci rekurencyjnie: 7.913s
// Fibonacci memoizacja: 0.271ms
// ---------------------------------------------