const { jumpingOnClouds } = require(`./jumping-on-clouds`);

test(`the minimum number of jumps needed to win a game where c = [0, 0, 1, 0, 0, 1, 0] is 4`, () => {
  expect(jumpingOnClouds([0, 0, 1, 0, 0, 1, 0])).toBe(4);
});

test(`the minimum number of jumps needed to win a game where c = [0, 0, 0, 0, 1, 0] is 3`, () => {
  expect(jumpingOnClouds([0, 0, 0, 0, 1, 0])).toBe(3);
});
