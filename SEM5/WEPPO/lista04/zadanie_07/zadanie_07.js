const fs = require("fs");
const file = "z7.txt";

fs.readFile(file, function (err, data) {
  if (err) {
    console.error(err);
  } else {
    console.log(data.toString());
  }
});

// za pomocą ”ręcznie” napisanej funkcji przyjmującej te same argumenty co fs::readFile
// ale zwracającej Promise
function readFile01(path) {
  return new Promise(function (resolve, reject) {
    fs.readFile(path, function (err, data) {
      if (err) {
        reject(err);
      } else {
        resolve(data);
      }
    });
  });
}

//readFile01(file).then((data) => {console.log(data.toString())});
readFile01(file).then(() => {});

//  za pomocą util.promisify z biblioteki standardowej
const util = require("util");
const readFile02 = util.promisify(fs.readFile);
readFile02(file).then(() => {});

// za pomocą fs.promises z biblioteki standardowej
const readFile03 = fs.promises.readFile;
readFile03(file).then(() => {});

//obsługA funkcji zwracającej Promise

// ”po staremu” - wywołanie z kontynuacją (Promise::then)
readFile03(file)
  .then((data) => { console.log(data.toString()); })
  .catch((error) => { console.error(error); });

//  ”po nowemu” - wywołanie przez async/await
(async function () {
  try {
    const data = await readFile03(file);
    console.log(data.toString());
  } catch (error) {
    console.error(error);
  }
})();