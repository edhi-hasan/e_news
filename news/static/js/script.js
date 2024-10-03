const now = new Date();

// Extract date and time information
const day = now.getDate();
const month = now.toLocaleString('default', { month: 'long' });
const year = now.getFullYear();
const date = `${day} ${month} ${year}`;  // Format the date as Day MonthName Year
const time = now.toLocaleTimeString();  // Format the time (HH:MM:SS AM/PM)

// Display the date and time in the HTML element with id="datetime"
document.getElementById("datetime").innerHTML = `${date} <br> ${time}`;
