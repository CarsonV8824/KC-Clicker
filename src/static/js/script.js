//sending dice click to python
const main_dice_button = document.getElementById('main-click-dice-button');

main_dice_button.addEventListener('click', () => {
    fetch('/get_dice_click_from_js', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ click: true })
    })
    .then(response => response.json())
    .then(data => {
        console.log('Dice click registered:', data);
    })
    .catch((error) => {
        console.error('Error:', error);
    });
});

//getting dice count from python
function updateDiceCount() {

    fetch('/get_dice_info_from_py')
    .then(response => response.json())
    .then(data => {
        const diceCountElement = document.getElementById('dice-count');
        diceCountElement.textContent = `Dice: ${data.count} (User: ${data.username})`;
    })
    .catch((error) => {
        console.error('Error fetching dice count:', error);
    });
}

setInterval(updateDiceCount, 5000); // Update every 5 seconds
updateDiceCount(); // Initial call to set the count immediately