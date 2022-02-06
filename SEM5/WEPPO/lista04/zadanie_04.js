let finished = false;
let nick = "";

function printNickAndExit() {
    console.log(`Witaj ${nick}`);
    process.exit(0);
}

const stream = process.stdin;

stream.setEncoding("utf8");

stream.on("data", (chunk) => {
    const parts = chunk.split("\n");
    nick += parts[0];
    printNickAndExit();
});

stream.on("end", () => {
    printNickAndExit();
});

process.stdout.write("Podaj swój nick: ");
process.stdin.resume();