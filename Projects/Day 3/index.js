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
  console.log(tasks);
  console.log("Task added!");
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

while (numberOption !== 5) {
  console.log("\n=== TO-DO LIST ===\n");

  console.log("1. Add tasks");
  console.log("2. View tasks");
  console.log("3. Remove task");
  console.log("4. Mark as Completed");
  console.log("5. Exit")

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
}

rl.close();
