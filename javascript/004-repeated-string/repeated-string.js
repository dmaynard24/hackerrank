function repeatedString(s, n) {
  let aCount = 0;

  const sLength = s.length;
  for (let i = 0; i < sLength; i++) {
    if (s[i] === `a`) {
      aCount++;
    }
  }

  aCount *= Math.floor(n / sLength);

  const remainingLength = n % sLength;
  for (let i = 0; i < remainingLength; i++) {
    if (s[i] === `a`) {
      aCount++;
    }
  }

  return aCount;
}

module.exports = { repeatedString };
