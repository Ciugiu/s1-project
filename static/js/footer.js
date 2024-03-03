console.log("JavaScript is connected");
// Get the current date
var now = new Date();

// Extract the day, month, and year
var day = now.getDate();
var month = now.getMonth();
var year = now.getFullYear();

// Format the day with the appropriate ordinal suffix
var ordinalSuffix = ["th", "st", "nd", "rd"];
var v = day % 100;
day += ordinalSuffix[(v - 20) % 10] || ordinalSuffix[v] || ordinalSuffix[0];

// Get the month name from the month number
var monthNames = [
  "January",
  "February",
  "March",
  "April",
  "May",
  "June",
  "July",
  "August",
  "September",
  "October",
  "November",
  "December",
];
month = monthNames[month];

// Combine the day, month, and year into a string
var dateString = day + " " + month + " " + year;

// Select the footer element
var footer = document.querySelector("#footer footer");

// Insert the date into the footer
footer.textContent += dateString;
