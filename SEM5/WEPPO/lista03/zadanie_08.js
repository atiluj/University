// zwykły iterator
function fibI() {
    let a = 0, b = 1;
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

function* take(it, max){
    for(let i=0; i<max; i++){
        const res = it.next();
        if(res.done) 
            return;
        yield res.value;
    }
}

for(let num of take(fibG(), 10)){
    console.log(num);
}