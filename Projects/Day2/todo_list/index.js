// INPUT:
// - Menu choice
// - New task text
// - Which task to remove

// OUTPUT:
// - Menu
// - Current tasks
// - Success/error messages
// - Questions/prompts

// DATA:
// - Array containing the tasks
// - Current menu choice

// ACTIONS:
// - Display menu
// - Ask for choice
// - Add task
// - View tasks
// - Remove task
// - Exit
// - Repeat menu until exit


import readline from 'node:readline/promises'

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
})




let option = 0;
let numberOption = 0;
const tasks = [];

while (numberOption !== 4) {

    console.log('\n=== TO-DO LIST ===\n')

    console.log('1. Add tasks')
    console.log('2. View tasks')
    console.log('3. Remove task')
    console.log('4. Exit')

    option = await rl.question('\nChoose an option: ')
    numberOption = Number(option)

    if (numberOption === 1) {
        let newTask = await rl.question('Enter task: ')
        tasks.push(newTask)
        console.log(tasks)
    }
    if (numberOption === 2) {
        console.log('YOUR TASKS:\n')
        for (let i = 0; i < tasks.length; i++ ) {
            console.log('Task ' + (i+1), tasks[i] )

        }
    }
    if (numberOption === 3) {
        let removeTask = await rl.question('Which task would you like to remove? ')
        let numRTask = Number(removeTask) - 1
        if (numRTask >= 0 && numRTask < tasks.length) {
        tasks.splice(numRTask,1)
        } else {
            console.log("\nInvalid Task\n")
        }
        for (let i = 0; i < tasks.length; i++ ) {
            console.log('Task ' + (i+1), tasks[i] )

        }
    }


}

rl.close()
