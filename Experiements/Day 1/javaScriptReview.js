// 1. Create an array containing:
// 3, 7, 2, 9, 4
const array = [3,7,2,9,4]
// Loop through the array and print every number greater than 4.
for (let i = 0;  i < array.length ; i++) {
    if (array[i] > 4) {
        console.log(array[i])
    }
}

// 2. Find the largest number WITHOUT using Math.max().
// It must also work if every number is negative.

let largestNum = array[0]
for (let i = 0; i < array.length ; i++) {

    if (largestNum < array[i]) {
        largestNum = array[i]
    }
}


// 3. Write a function:
// double(number)
function double(number) {
    return number * 2
}
// It should RETURN twice the number.
console.log(largestNum)
console.log(double(4))
