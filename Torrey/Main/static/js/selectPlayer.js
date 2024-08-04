const player1Section = document.getElementById('player1');
const player2Section = document.getElementById('player2');

let toggle1 = false;
let toggle2 = false;

function showStartButton() {
    // Check if the button already exists
    if (document.getElementById('start-game')) return;

    const startButton = document.createElement('button');
    startButton.id = 'start-game';
    startButton.innerText = 'Start Game';
    startButton.classList.add('show'); // Add class for styling
    document.body.appendChild(startButton);

    // Center the button
    startButton.style.left = '50%';
    startButton.style.top = '50%';
    startButton.style.transform = 'translate(-50%, -50%)';
    
    startButton.addEventListener('click', function () {
        window.location.href = 'http://127.0.0.1:5000/localGame'; // Replace with your actual game page URL
    });
}

function selectPlayer(playerNumber) {
    if (playerNumber === 1) {
        if (!toggle1) {
            toggle1 = true;
            player1Section.style.flex = '2';
            player2Section.style.flex = '1';
            document.getElementById('word1').innerHTML = document.getElementById('secret1').innerHTML;
            document.getElementById('word1').style.opacity = 1;
        } else {
            player1Section.style.flex = '1';
            player2Section.style.flex = '1';
            document.getElementById('word1').style.opacity = 0;
            setTimeout(() => {
                document.getElementById('word1').innerHTML = '';
            }, 300);
            player1Section.onclick = null;
        }
    } else {
        if (!toggle2) {
            toggle2 = true;
            player2Section.style.flex = '2';
            player1Section.style.flex = '1';
            document.getElementById('word2').innerHTML = document.getElementById('secret2').innerHTML;
            document.getElementById('word2').style.opacity = 1;
        } else {
            player2Section.style.flex = '1';
            player1Section.style.flex = '1';
            document.getElementById('word2').style.opacity = 0;
            setTimeout(() => {
                document.getElementById('word2').innerHTML = '';
            }, 300);
            player1Section.onclick = null;
            player2Section.onclick = null;
            setTimeout(() => {
                player1Section.style.transition = 'transform 1s';
                player2Section.style.transition = 'transform 1s';
                player1Section.style.transform = 'translateX(-100%)';
                player2Section.style.transform = 'translateX(100%)';
                setTimeout(showStartButton, 1000);
            }, 300);
        }
    }
}
