const { equalizeArray } = require(`./equalize-array`);

test(`the minimum number of elements that can be removed from the array [37, 32, 97, 35, 76, 62] in order to equalize all remaining elements is 5`, () => {
  expect(equalizeArray([37, 32, 97, 35, 76, 62])).toBe(5);
});

test(`the minimum number of elements that can be removed from the array [3, 3, 2, 1, 3] in order to equalize all remaining elements is 2`, () => {
  expect(equalizeArray([3, 3, 2, 1, 3])).toBe(2);
});
