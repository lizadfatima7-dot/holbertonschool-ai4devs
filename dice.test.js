const { roll } = require('./dice');
for (let i = 1; i <= 5; i++) {
  console.log('Roll ' + i + ': ' + roll(6));
}