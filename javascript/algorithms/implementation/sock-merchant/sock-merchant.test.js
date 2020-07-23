const { sockMerchant } = require(`./sock-merchant`);

test(`the number of pairs that can be made from 7 socks with colors represented by the array [1, 2, 1, 2, 1, 3, 2] is 2`, () => {
  expect(sockMerchant(7, [1, 2, 1, 2, 1, 3, 2])).toBe(2);
});

test(`the number of pairs that can be made from 9 socks with colors represented by the array [10, 20, 20, 10, 10, 30, 50, 10, 20] is 3`, () => {
  expect(sockMerchant(9, [10, 20, 20, 10, 10, 30, 50, 10, 20])).toBe(3);
});
