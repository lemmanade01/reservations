'use strict';

const searchBtn = document.querySelector('#search');
searchBtn.addEventListener('click', (evt) => {
    evt.preventDefault();
    console.log('I have been clicked');

    const date = document.querySelector('#date').value;
    const startTime = document.querySelector('#start-time').value;
    const endTime = document.querySelector('#end-time').value;

    const searchInput = {
        date: date,
        start: startTime,
        end: endTime
    }

    fetch('/search-reservations.json', {
        method: 'POST',
        body: JSON.stringify(searchInput),
        headers: {
            'Content-Type': 'application/json'
        },
    })
        .then(response => response.json())
        .then(responseJson => {
            console.log(responseJson);

            if (responseJson['exists'] == 'yes') {
                document.querySelector('.available-times').insertAdjacentHTML('beforeend', '<p id="error">Error: You already have a reservation booked on this date. Please select another date</p>')

                setInterval(myTimer, 6000);

                function myTimer() {
                    document.querySelector('#error').remove();
                }   
            } else {

                const resDate = responseJson['date'];
            
                for (let n=1; n < 49; n++) {
                    const resTime = responseJson['times'][n];
                    console.log(resTime, 'time');
                    
                    let num = n.toString();
                    
                    document.querySelector('.available-times').insertAdjacentHTML('beforeend', 
                    `<div class="col-lg-2 col-md-4 col-sm-6">
                        <span>${resTime}</span><button class="book-btn" id="${num}" value="${num}">Book</button></br>
                    </div>`)    

                    const bookBtns = document.querySelectorAll('.book-btn');

                    for (const bookBtn of bookBtns) {
                        bookBtn.addEventListener('click', (evt) => {

                        if(evt == undefined)return;
                        evt.preventDefault();
                        console.log(`book btn is clicked! time: ${num}`);
                        
                            const btnValue = `${num}`;
                            console.log(btnValue);
                            bookBtn.innerHTML = 'Booked';
                            bookBtn.disabled = true;

                            const bookTime = {
                                time: `${num}`,
                                date: resDate 
                            }
                        
                            fetch('/book-reservations.json', {
                                method: 'POST',
                                body: JSON.stringify(bookTime),
                                headers: {
                                    'Content-Type': 'application/json'
                                },
                            })
                                .then(response => response.json())
                                .then(responseJson => {
                                    console.log('response received');
                                    const bookedTime = responseJson['time'];
                                    console.log(bookedTime); 
                                }
                            )   
                        })
                    }
                }
            }
        });
    })