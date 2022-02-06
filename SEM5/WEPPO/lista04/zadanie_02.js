function Foo() {
    console.log("Hello world! I greet you from Foo.");

    Foo.prototype.Bar = function() {
        var Qux = function () {
            console.log("Hello world! I greet you from Qux.");
        };
        Qux();
    }
};

var x = new Foo();
x.Bar();