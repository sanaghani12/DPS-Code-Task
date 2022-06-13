const hotpTotpGenerator = require("hotp-totp-generator");

const password = hotpTotpGenerator.totp({
  // Key ==> name@example.comDPSCHALLENGE
  key: "sanaghani94@gmail.comDPSCHALLENGE",
  // Time Step X ==> 120 seconds
  X: 120,
  // T0 ==> 0
  T0: 0,
  // algorithm => HMAC-SHA-512
  algorithm: "sha512",
  // password =>  10-digit
  digits: 10,
});

console.log(password);
