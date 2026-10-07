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

import readline from "node:readline/promises";

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

let option = 0;
let numberOption = 0;
const tasks = [];

function viewTasks() {
  console.log("YOUR TASKS:\n");
  for (let i = 0; i < tasks.length; i++) {
    let result = "[ ]";
    if (tasks[i].completed == true) {
      result = "[X]";
    }
    console.log(`${i + 1}. ${result} ${tasks[i].name}`);
  }
}

async function markComplete() {
  let completionState = await rl.question("Which task# completed: ");
  let numState = Number(completionState) - 1;

  if (numState >= 0 && numState < tasks.length) {
    tasks[numState].completed = true;
  } else {
    console.log("\nInvalid Task\n");
  }
}
async function addTasks() {
  let taskObj = {
    name: "None",
    completed: false,
  };
  let newTask = await rl.question("Enter task: ");

  taskObj.name = newTask;
  tasks.push(taskObj);
  console.log("Task added!");
}

function viewIncompleteTasks() {
    console.log("INCOMPLETE TASKS")
    for (let i = 0; i< tasks.length; i ++) {
        if (tasks[i].completed == false) {
            console.log(`${i+1}. ${tasks[i].name}`)
        }
    }
}
function taskStats() {
    console.log("TASK STATS")
    console.log(`Total: ${tasks.length}`);
    let falseCounter = 0;
    let trueCounter = 0;
    for(let i = 0; i< tasks.length; i++) {
        if(tasks[i].completed == true) {
            trueCounter += 1
        } else {
            falseCounter += 1
        }
    }
    console.log(`Completed: ${trueCounter}`)
    console.log(`Incomplete: ${falseCounter}`)
}
async function editTask() {
    let editTask = await rl.question("Which task would you like to edit? ")
    let numTask = Number(editTask) - 1
    let newName = ""

    if (numTask >= 0 && numTask < tasks.length) {
        newName = await rl.question("Enter the new task name: ")
        tasks[numTask].name = newName
        console.log("Task updated!")
    }else {
        console.log("\nInvalid Task\n")
    }

}
async function removeTasks() {
  let removeTask = await rl.question("Which task would you like to remove? ");
  let numRTask = Number(removeTask) - 1;
  if (numRTask >= 0 && numRTask < tasks.length) {
    tasks.splice(numRTask, 1);
  } else {
    console.log("\nInvalid Task\n");
  }
}

while (numberOption !== 6) {
  console.log("\n=== TO-DO LIST ===\n");

  console.log("1. Add tasks");
  console.log("2. View tasks");
  console.log("3. Remove task");
  console.log("4. Mark as Completed");
  console.log("5. Edit task")
  console.log("6. Exit")

  option = await rl.question("\nChoose an option: ");
  numberOption = Number(option);

  if (numberOption === 1) {
    await addTasks();
  }
  if (numberOption === 2) {
    viewTasks();
  }
  if (numberOption === 3) {
    await removeTasks();
    viewTasks();
  }
  if(numberOption === 4) {
    await markComplete()
    viewTasks()
  }
  if (numberOption === 5) {
    await editTask()
    viewTasks()
  }
}

rl.close();
