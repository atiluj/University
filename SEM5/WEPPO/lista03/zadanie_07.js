
// zwykły iterator
function fibI() {
    let a = 1, b = 1;
    return {
      next: function () {
        const value = a;
        a = b;
        b += value;
  
        return {
          value,
          done: false,
        };
      },
    };
}

// generator (yield)
function* fibG(){
    let a = 1, b = 1;
    yield a;
    yield b;
    while(true){
        let p = a;
        a = b;
        b = p + b;
        yield b;
    }
}

// wypisanie
function showResult(result, max){ //max - ile wypisać
    let i = 0;
    for(const x of result){
        i++;
        if(i > max){
            break;
        }
        console.log(x);
    }
    console.log("koniec");
}

const ans1 = {
    [Symbol.iterator]: fibI
};
showResult(ans1, 15);

const ans2 = {
    [Symbol.iterator]: fibG
};
showResult(ans2, 10);

// const ans3 = fibI(); //dla fibI nie można tak
// showResult(ans3);

const ans4 = fibG();
showResult(ans4,20);