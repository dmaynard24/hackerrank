const { cavityMap } = require(`./cavity-map`);

test(`the resulting map from ['1112', '1912', '1892', '1234'] with each cavity replaced with an X looks like ['1112', '1X12', '18X2', '1234']`, () => {
  expect(cavityMap([`1112`, `1912`, `1892`, `1234`])).toStrictEqual([`1112`, `1X12`, `18X2`, `1234`]);
});
