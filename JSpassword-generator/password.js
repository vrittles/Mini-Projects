const ouput = document.querySelector(".output");
const gen = document.querySelector("#gen");
const copy = document.querySelector("#copy");
const length = document.querySelector("#len");
const numb = document.getElementById("num");
const upper = document.getElementById("upper");
const lower = document.getElementById("lower");
const symb = document.getElementById("symb");

//symbols

const lowercaseChars = "abcdefghijklmnopqrstuvwxyz";
const uppercaseChars = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
const numberChars = "0123456789";
const symbolChars = "!@#$%^&*()_-+=<>?";

function getPassword(len, incLower, incUpper, incNum, incSymb) {
  let allchar = "";
  incLower ? (allchar += lowercaseChars) : (allchar += "");
  incUpper ? (allchar += uppercaseChars) : (allchar += "");
  incSymb ? (allchar += symbolChars) : (allchar += "");
  incNum ? (allchar += numberChars) : (allchar += "");
  if (allchar.length == 0) {
    alert("Include at least a character!");
    return;
  }
  let password = "";
  for (i = 0; i < len; i++) {
    const random = Math.floor(Math.random() * allchar.length);
    password += allchar[random];
  }

  ouput.textContent = password;
}

gen.addEventListener("click", () => {
  const lengthVal = Number(length.value);
  const includeLowercase = lower.checked;
  const includeUppercase = upper.checked;
  const includeNumbers = numb.checked;
  const includeSymbols = symb.checked;

  getPassword(
    lengthVal,
    includeLowercase,
    includeUppercase,
    includeNumbers,
    includeSymbols
  );
});

copy.onclick = function () {
  const clip = ouput.textContent;
  if (clip == "") {
    alert("Nothing to copy!");
    return;
  }
  navigator.clipboard.writeText(clip);
  alert("Copied!");
};
