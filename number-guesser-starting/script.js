let humanScore = 0;
let computerScore = 0;
let currentRoundNumber = 1;

// Write your code below:

const generateTarget = () => Math.floor(Math.random() * 10);

const getAbsoluteDistance = (num1,num2) => Math.abs(num1,num2);

const compareGuesses = (userGuess,computerGuess,secretNumber) =>{
    const userDistance = getAbsoluteDistance(userGuess - secretNumber)
    const computerDistance = getAbsoluteDistance(computerGuess - secretNumber)
    
    return (computerDistance < userDistance) ?  false : true;
}

const updateScore = winner =>{

    if(winner === 'human'){
        humanScore++
    }
    if(winner === 'computer'){
        computerScore++
    }
}

const advanceRound = () => currentRoundNumber++;
