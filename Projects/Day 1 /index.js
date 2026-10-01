import readline from 'node:readline/promises';

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout,
});
// INPUT: User guess
// OUTPUT: Welcome message and then asks for the guess
// DATA: User guess and random number gen and attempt counter
// ACTIONS: Prompt -> (Loop Guess-> Compare -> Increment if incorrect)

let randomInt = Math.floor(Math.random()* 100) +1
// console.log(randomInt)

console.log("I'm thinking of a number between 1 and 100!\n")



let guessCounter = 0;
while (true ) {

let guess = await rl.question('\nEnter your guess: ');
guessCounter ++
// console.log (`Your guess: ${guess}`)
const numGuess = Number(guess)
if (numGuess === randomInt) {
    console.log(`Correct you got it in ${guessCounter} attempts`)
    break

}else if (numGuess > randomInt) {
    console.log('Too High');
}else {
    console.log('Too low')
}
}
rl.close()
