//sending dice click to python
const main_dice_button = document.getElementById('main-click-dice-button');

main_dice_button.addEventListener('click', () => {
    fetch('/get_dice_click_from_js', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ "click": true })
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

const diceCountSpan = document.getElementById('dice-count-span');

async function updateDiceCount() {
  fetch('/get_dice_info_from_py', {cache: "no-cache"})
    .then(res => res.json())
    .then(data => {
      diceCountSpan.textContent = `${data.count} | ${data.username}'s Game`;
    })
    .catch(err => console.error('Error fetching dice count:', err));
}

//setInterval(updateDiceCount, 1000); 
//updateDiceCount(); 

//getting money per second from python

const moneyPerSecSpan = document.getElementById('money-per-sec-span');

async function updateMoneyPerSec() {
  fetch('/get_money_per_sec_info_from_py', {cache: "no-cache"})
    .then(res => res.json())
    .then(data => {
      moneyPerSecSpan.textContent = `Money Per Second: $${data.money_per_sec}`;
    })
    .catch(err => console.error('Error fetching money per second:', err));
}

//setInterval(updateMoneyPerSec, 100);
//updateMoneyPerSec();

//getting money generation from python

const moneyGenerationSpan = document.getElementById('money-generation-span');

async function updateMoneyGeneration() {
  fetch('/get_money_generation_from_py', {cache: "no-cache"})
    .then(res => res.json())
    .then(data => {
      moneyGenerationSpan.textContent = `Money: $${data.money}`;
    })
    .catch(err => console.error('Error fetching money generation:', err));
}

//setInterval(updateMoneyGeneration, 100);
//updateMoneyGeneration();

//sending 39th Street Button to python
const thirtyNinthStreetButton = document.getElementById('39th_street_button');

thirtyNinthStreetButton.addEventListener('click', () => {
    fetch('/get_39th_street_button_click_from_js', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ "buy": true })
    })
    .then(response => response.json())
    .then(data => {
        console.log('39th Street purchase attempt:', data);
    })
    .catch((error) => {
        console.error('Error:', error);
    });
});

//getting 39th Street info from python

const thirtyNinthStreetInfoSpan = document.getElementById('39th_street_info_span');

async function updateThirtyNinthStreetInfo() {
    fetch('/get_39th_street_button_click_from_py', {cache: "no-cache"})
        .then(res => res.json())
        .then(data => {
            thirtyNinthStreetInfoSpan.textContent = `Owned: ${data.owned} | Cost: $${data.cost}`;
        }
    )
    .catch(err => console.error('Error fetching 39th Street info:', err));
}

//setInterval(updateThirtyNinthStreetInfo, 100);
//updateThirtyNinthStreetInfo();

//sending The Paseo Button to python

const thePaseoButton = document.getElementById('the_Paseo_button');

thePaseoButton.addEventListener('click', () => {
    fetch('/get_The_Paseo_button_click_from_js', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ "buy": true })
    })
    .then(response => response.json())
    .then(data => {
        console.log('The Paseo purchase attempt:', data);
    })
    .catch((error) => {
        console.error('Error:', error);
    });
});

//getting The Paseo info from python

const thePaseoInfoSpan = document.getElementById('The_Paseo_info_span');

async function updateThePaseoInfo() {
    fetch('/get_The_Paseo_button_click_from_py', {cache: "no-cache"})
        .then(res => res.json())
        .then(data => {
            thePaseoInfoSpan.textContent = `Owned: ${data.owned} | Cost: $${data.cost}`;
        }
    )
    .catch(err => console.error('Error fetching The Paseo info:', err));
}

//setInterval(updateThePaseoInfo, 100);
//updateThePaseoInfo();

// send data back at one time
// use mod operater if you need different intervals for each

setInterval(() => {
  Promise.all([
    updateDiceCount(),
    updateMoneyPerSec(),
    updateMoneyGeneration(),
    updateThirtyNinthStreetInfo(),
    updateThePaseoInfo()
  ])
  .then(() => {
    console.log('All data updated.');
  })
  .catch((error) => {
    console.error('Error updating all data:', error);
  });
}, 250);

//Saving Data on Window Close
window.addEventListener("beforeunload", () => {
  const payload = JSON.stringify({
    username: "test",
    email: "test@example.com"
  });

  navigator.sendBeacon("/save-on-close", payload);
});