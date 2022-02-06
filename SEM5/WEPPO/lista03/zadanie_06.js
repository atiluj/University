function createGenerator(max) {
    return function(){
        var _state = 0;
        return {
            next : function() {
                return {
                    value : _state,
                    done : _state++ >= max
                }
            }
        }   
    }
}

var foo1 = {
    [Symbol.iterator] : createGenerator(5)
};

var foo2 = {
    [Symbol.iterator] : createGenerator(12)
};

var foo3 = {
    [Symbol.iterator] : createGenerator(21)
};


for ( var f of foo1 )
    console.log(f);

console.log("---------");

for ( var f of foo2 )
    console.log(f);

console.log("---------");

for ( var f of foo3 )
    console.log(f);

console.log("---------");