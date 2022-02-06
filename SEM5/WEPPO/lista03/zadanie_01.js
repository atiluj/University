// zdefiniowanie nowego obiektu
const obj = {
    // obiekt zawierający pole
    field1: "pole1",

    // obiekt zawierający metode
    metoda1: () => {console.log("wypisanie w metodzie1");},

    // właściwość z get
    get attr1(){
        return 1;
    },

    // właściwość z set
    set attr1(value){
        console.log(`attr1 <- ${value}`);
    }
};

// --testy--
obj.field1 = 1;
console.log(obj.field1);
obj.metoda1();
console.log(obj.attr1);
obj.attr1 = 2;

//Object.defineProperty
// nowe pole
obj.field2 = 2;

// nowa metoda
obj.metoda2 = () => {console.log("wypisanie w metodzie2");};

// nowa własność
Object.defineProperty(obj, "attr2", {
    get: () => 1,
    set: (value) => console.log(`attr2 <- ${value}`),
});

// --testy-- dla Object.defineProperty
obj.field2 = 1;
console.log(obj.field2);
obj.metoda2();
console.log(obj.attr2);
obj.attr2 = 2;
