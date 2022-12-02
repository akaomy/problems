// Camel Case is a naming style common in many programming languages. 
// In Java, method and variable names typically start with a lowercase letter, 
// with all subsequent words starting with a capital letter (example: startThread). 
// Names of classes follow the same pattern, except that they start with a capital 
// letter (example: BlueCar).

// Your task is to write a program that creates or splits Camel Case variable, 
// method, and class names.

// link to the problem
// https://www.hackerrank.com/challenges/three-month-preparation-kit-camel-case/problem?h_l=interview&isFullScreen=true&playlist_slugs%5B%5D%5B%5D=preparation-kits&playlist_slugs%5B%5D%5B%5D=three-month-preparation-kit&playlist_slugs%5B%5D%5B%5D=three-month-week-one


// there are probably more efficient ways to do this
// works for just one line of input
// need to add while to handle each input line that Hackerrank system provides when running tests
function processData(input) {
    inputArray = input.split(';') // [0] action, rule type, string to work with
    wordsArray = inputArray[2].split(' ');
    if (inputArray[0] === 'C') { // if we have action create
        if (inputArray[1] === 'C') { // if class
            // words in inputArray[2] into titlecase
            let classCamelCase = '';
            for (let i = 0; i < wordsArray.length; i++) {
              classCamelCase += wordsArray[i][0].toUpperCase() + wordsArray[i].slice(1, wordsArray[i].length)
            }
            // concatenate them into one string without spaces between words
            console.log(classCamelCase)
        } else if (inputArray[1] === 'V') { // if method or variable
          // console.log(wordsArray)
            // words in inputArray[2] into Uppercase after first word (?)
            let methodCamelCase = '';
            for (let i = 1; i < wordsArray.length; i++) {
              methodCamelCase += wordsArray[i][0].toUpperCase() + wordsArray[i].slice(1, wordsArray[i].length)
            }
            // concatenate them into one string without spaces between words
            console.log(wordsArray[0] + methodCamelCase)
        } else {// if method
          let varCamelCase = '';
          for (let i = 1; i < wordsArray.length; i++) {
              varCamelCase += wordsArray[i][0].toUpperCase() + wordsArray[i].slice(1, wordsArray[i].length)
          }
          // add () at the end of the string
          result = wordsArray[0] + varCamelCase + '()';
          console.log(result)
        }
    } else { // if we have action split
        // finds all letters starting from the upper later, splits string by white space, make words starting from lower case letter, replaces () to the white space
        console.log(inputArray[2].replace(/([A-Z])/g, " $1" ).toLowerCase().replace(/\(/g, '').replace(/\)/g, ''))
    }
} 
