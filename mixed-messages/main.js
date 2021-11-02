//store pieces of text
const planets = [
  "Mercury",
  "Venus",
  "Earth",
  "Mars",
  "Jupiter",
  "Saturn",
  "Uranus",
  "Neptune",
];
const months = [
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
const prophecies = [
  "It is certain.",
  "It is decidedly so.",
  "Without a doubt.",
  "Yes definitely.",
  "You may rely on it.",
  "As I see it, yes.",
  "Most likely.",
  "Outlook good.",
  "Yes.",
  "Signs point to yes.",
  "Reply hazy, try again.",
  "Ask again later.",
  "Better not tell you now.",
  "Cannot predict now.",
  "Concentrate and ask again.",
  "Don't count on it.",
  "My reply is no.",
  "My sources say no.",
  "Outlook not so good.",
  "Very doubtful.",
];

//select a random piece of text
const randomPart = (set) => {
  return set[Math.floor(Math.random() * set.length)];
};

//combine random pieces of text
const mixedProphecy = () => {
  let planet = randomPart(planets);
  let month = randomPart(months);
  let prophecy = randomPart(prophecies);
  let direction =
    Math.floor(Math.random() * 2) === 0 ? "ascension" : "retrograde";

  return `With ${planet} in ${direction} for the month of ${month}, Magic 8-ball says "${prophecy}"`;
};
//ouput the message
console.log(mixedProphecy());
