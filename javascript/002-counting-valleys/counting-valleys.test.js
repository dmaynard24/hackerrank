const { countingValleys } = require(`./counting-valleys`);

test(`the number of valleys entered and left when the length of the string describing the path is 8 and the string is 'UDDDUDUU' is 1`, () => {
  expect(countingValleys(8, `UDDDUDUU`)).toBe(1);
});
