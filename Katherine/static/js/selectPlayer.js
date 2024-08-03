const player1Section = document.getElementById('player1');
const player2Section = document.getElementById('player2');

var toggle1=false
var toggle2=false

// Function to create and show the start button
function showStartButton() {
    // Check if the button already exists
    if (document.getElementById('start-game')) return;

    const startButton = document.createElement('button');
    startButton.id = 'start-game';
    startButton.innerText = 'Start Game';
    startButton.style.display = 'block'; // Show the button
    document.body.appendChild(startButton);

    // Fade in the start game button
    setTimeout(() => {
        startButton.style.opacity = '1';
    }, 100);

    startButton.addEventListener('click', function () {
        window.location.href = 'http://127.0.0.1:5000/localGame'; // Replace with your actual game page URL
    });
}

function selectPlayer(playerNumber) {
    if (playerNumber === 1) {
        if (toggle1 == false) {
            toggle1=true
            player1Section.style.flex = '2';
            player2Section.style.flex = '1';
            document.getElementById('word1').innerHTML = document.getElementById('secret1').innerHTML;
            document.getElementById('word1').style.opacity = 1;
        } else{
            player1Section.style.flex = '1';
            player2Section.style.flex = '1';
            document.getElementById('word1').style.opacity = 0;
            setTimeout(function(){
                document.getElementById('word1').innerHTML = '';
            }, 300)
            player1Section.onclick = null;
        }
        
    } else {
        if (toggle2 == false) {
            toggle2=true
            player2Section.style.flex = '2';
            player1Section.style.flex = '1';
            document.getElementById('word2').innerHTML = document.getElementById('secret2').innerHTML;;
            document.getElementById('word2').style.opacity = 1;
        } else{
            player2Section.style.flex = '1';
            player1Section.style.flex = '1';
            document.getElementById('word2').style.opacity = 0;
            setTimeout(function(){
                document.getElementById('word2').innerHTML = '';
            }, 300)
            player1Section.onclick = null;
            showStartButton();
        }
    }
}
