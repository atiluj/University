function Tree(val, left, right) {
    this.left = left;
    this.right = right;
    this.val = val;
  }
  
// W TREŚCI ZADANIA - enumerowanie zawartości drzewa w głąb
// Tree.prototype[Symbol.iterator] = function*() {
//     yield this.val;
//     if ( this.left ) yield* this.left;
//     if ( this.right ) yield* this.right;
// }

// var root = new Tree( 1, 
//                     new Tree( 2, new Tree(3)), 
//                     new Tree(4));

// for (var e of root) {
//     console.log( e );
// }
// 1 2 3 4

//ROZWIĄZANIE - enumerowanie zawratości drzewa wszerz
Tree.prototype[Symbol.iterator] = function* () {
    const queue = [this];

    while (queue.length > 0) {
        const node = queue.shift(); //usunięcie pierwszego elementu z tablicy
  
        // plan działania:
        // jeśli istnieje prawe dziecko to wrzucamy je do kolejki
        // jeśli istnieje lewe dziecko to wrzucamy je do kolejki
        // wypisujemy obecnie pierwszy element kolejki (czyli znajudujący sie obecnie najwyżej i najbardziej na prawo wierzchołek)
        if (node.right) 
            queue.push(node.right);
        if (node.left) 
            queue.push(node.left);
        yield node.val;
    }
};
  
const root = new Tree(1, new Tree(2, new Tree(3)), new Tree(4));

//     1
//   2   4
// 3  - -  -
//- -- - -- -
//step1: kolejka: 142 -- wypisane: 1 kolejka: 42
//step2: kolejka: 42 -- wypisane: 1, 4 kolejka: 2
//step3: kolejka: 23 -- wypisane: 1, 4, 2 kolejka: 3
//step4: kolejka: x -- wypisane: 1, 4, 2, 3 kolejka: x

for (var e of root) {
    console.log(e);
}