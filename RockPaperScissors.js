// console.log('ciao');
//caching the dom: storing for future use. document.get/document.querySelector
let playerScore = 0;
let computerScore = 0;
const playerScore_span = document.getElementById('player-score');
const computerScore_span = document.getElementById('computer-score');
const scoreBoard_div = document.querySelector('.score-board');
const result_p = document.querySelector('.result > p');
const rock_div = document.getElementById('r');
const paper_div = document.getElementById('p');
const scissors_div = document.getElementById('s');

function getComputerChoice() {
    const choices = ['r', 'p', 's'];
    const randomNumber = (Math.floor(Math.random() * 3));
    return choices[randomNumber];
}
function convertToWord(letter) {
    if (letter === 'r') return 'Rock';
    if (letter === 'p') return 'Paper'; 
    return 'Scissors'
}
function win(playerChoice, computerChoice) {
    playerScore++;
    playerScore_span.innerHTML = playerScore;
    computerScore_span.innerHTML = computerScore;
    const smallPlayerWord = 'player'.fontsize(3).sup();
    const smallCompWord = 'computer'.fontsize(3).sup();
    result_p.innerHTML = `${smallPlayerWord} ${convertToWord(playerChoice)} smashes  ${smallCompWord} ${convertToWord(computerChoice)}  YOU WIN! ` ;
}
function lose(playerChoice, computerChoice) {
    computerScore++;
    playerScore_span.innerHTML = playerScore;
    computerScore_span.innerHTML = computerScore;
    const smallPlayerWord = 'player'.fontsize(3).sup();
    const smallCompWord = 'computer'.fontsize(3).sup();
    result_p.innerHTML = `${smallPlayerWord} ${convertToWord(playerChoice)} loses to  ${smallCompWord} ${convertToWord(computerChoice)}  YOU LOSE... ` ;
}
function tie(playerChoice, computerChoice) {
    const smallPlayerWord = 'player'.fontsize(3).sup();
    const smallCompWord = 'computer'.fontsize(3).sup();
    result_p.innerHTML = `${smallPlayerWord} ${convertToWord(playerChoice)} ties with  ${smallCompWord} ${convertToWord(computerChoice)}  TIE: TRY AGAIN ` ;
}

function getPlayerChoice(playerChoice) {
    const computerChoice = getComputerChoice();
    switch (playerChoice + computerChoice) {
        case 'rs':
        case 'pr':
        case 'sp':
            win(playerChoice, computerChoice);
            break;
        case 'rp':
        case 'ps':
        case 'sr':
            lose(playerChoice, computerChoice);
            break;
        case 'rr':
        case 'pp':
        case 'ss':
            tie(playerChoice, computerChoice);
            break;
    }
}







function main () {
    rock_div.addEventListener('click', function() {
        getPlayerChoice('r');
    })

    paper_div.addEventListener('click', function() {
        getPlayerChoice('p');
    })

    scissors_div.addEventListener('click', function() {
        getPlayerChoice('s');
    })
}
main();