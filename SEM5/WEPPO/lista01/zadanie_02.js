function divideByEach(i){
    const x = i;
    var num =  0;
    while(i != 0){
        num = i%10;
        i = Math.floor(i / 10);

        if(x%num != 0){
            return false;
        }
    }
    return true;
}

function divideBySum(i){
    var sum =  0;
    const x = i;
    while(i != 0){
        sum = sum + i%10;
        i = Math.floor(i / 10);
    }
    
    if(x%sum === 0){
        return true;
    }
    return false;
}

const result = [];

for (let i = 1; i <= 100000; i++) {

    if (divideBySum(i) && divideByEach(i)){
        result.push(i);
    }
}

console.info(result.join(" "));
