// exercises from easiest to hardest to practice string manipulation

// problem 1
// v1
const reverseString = givenString => {
    if (givenString.length == 0) return;

    let newString = "";
    for (let i = givenString.length-1; i >= 0; i--) {
        newString += givenString[i];
    }
    console.log(newString);
}

// v2
'abcde'.split().reverse().join()

// v3
const reverseStringRec = givenString => {
    return reverseString(givenString.substr(1) + givenString[0])
}