function forEach(a, f){
    for(const x of a){
        f(x);
    }
}

//alternatywa do funkcji typu console.log
// function forEach2(a, f){
//     const pom = [];
//     for(const x of a){
//         pom.push(f(x));
//     }
//     return pom;
// }

// var ans2 = forEach2( a, _ => _ );
// console.log(ans2);
// [1,2,3,4]

function map(a, f){
    const pom = [];
    for(const x of a){
        pom.push(f(x));
    }
    return pom;
}

function filter(a, f){
    const pom = [];
    for(const x of a){
        if(f(x))
            pom.push(x);
    }
    return pom;
}

var a = [1,2,3,4];

forEach( a, _ => { console.log( _ ); } );
// [1,2,3,4]

var ans = map(a , _ => _ * 2 );
console.log(ans);
// [2,4,6,8]

var ans2 = filter( a, _ => _ < 3 );
console.log(ans2);
// // [1,2]

