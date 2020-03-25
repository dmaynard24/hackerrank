const { repeatedString } = require(`./repeated-string`);

test(`gets the total count of the letter 'a' in the string 'aba' when it is repeated until its length is 10 to be 7`, () => {
  expect(repeatedString(`aba`, 10)).toBe(7);
});

test(`gets the total count of the letter 'a' in the string 'a' when it is repeated until its length is 1000000000000 to be 1000000000000`, () => {
  expect(repeatedString(`a`, 1000000000000)).toBe(1000000000000);
});
