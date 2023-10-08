let countryData = []; // Global variable to store country data
let exportData = []; // Global variable to store export data
// Function to fetch and store country data
async function fetchCountryData() {
  try {
    const response = await fetch("https://restcountries.com/v3.1/all");
    countryData = await response.json();
  } catch (error) {
    console.error("Error fetching data:", error);
  }
}
// Call the function to fetch and store country data
fetchCountryData();
const searchForm = document.getElementById("search-form");
const searchInput = document.getElementById("search-input");
const searchOption = document.getElementById("search-option");
const countryContainer = document.getElementById("country-container");
const exportButton = document.getElementById("export-json");
searchForm.addEventListener("submit", (e) => {
  e.preventDefault();
  const searchTerm = searchInput.value.trim().toLowerCase();
  const searchType = searchOption.value;
  if (searchTerm === "") {
    return;
  }
  countryContainer.innerHTML = "";
  exportData = []; // Clear previous export data
  let foundCountry = false;
  countryData.forEach((country) => {
    if (
      (searchType === "name" &&
        country.name &&
        country.name.common &&
        country.name.common.toLowerCase().includes(searchTerm)) ||
      (searchType === "currency" &&
        checkCurrency(country.currencies, searchTerm))
    ) {
      displayCountryCard(country);
      // exportData.push({
      //   img: country.flags.png,
      //   name: country.name.common,
      //   capital: country.capital,
      //   population: country.population,

      // });
      foundCountry = true;
    }
  });
  if (!foundCountry) {
    displayErrorMessage("Country not found");
  }
  exportButton.hidden = !foundCountry;
});

exportButton.addEventListener("click", () => {
  downloadJSON(exportData);
});
function checkCurrency(currencies, searchTerm) {
  if (!currencies) {
    return false;
  }
  const currencyKeys = Object.keys(currencies);
  const lastCurrency = currencyKeys[currencyKeys.length - 1];
  return lastCurrency.toLowerCase() === searchTerm;
}
function displayCountryCard(country) {
  const countryCard = document.createElement("div");
  countryCard.classList.add("country-card");
  countryCard.innerHTML = `
<img class="common" src="${country.flags.png}" alt="${country.name.common}">
<h2 class="common">${country.name.common}</h2>
<p class="common">Capital: ${country.capital}</p>
   <p class="common">Population: ${country.population}</p>
   <p class="common">Currency:${Object.keys(country.currencies)[0]}</p>
   
  `;
  countryContainer.appendChild(countryCard);
}

function displayErrorMessage(message) {
  const errorMessage = document.createElement("p");
  errorMessage.classList.add("error-message");
  errorMessage.textContent = message;
  countryContainer.appendChild(errorMessage);
}

function downloadJSON(data) {
  const countryCards = Array.from(
    countryContainer.querySelectorAll(".country-card")
  );

  if (countryCards.length > 0) {
    const jsonData = countryCards.map((countryCard) => {
      return {
        type: countryCard.tagName.toLocaleLowerCase(),
        class: countryCard.className,
        children: Array.from(countryCard.children).map((childElement) => {
          const childData = {
            type: childElement.tagName.toLowerCase(),
            class: childElement.className,
          };
          if (childElement.tagName.toLowerCase() === "img") {
            childData.src = childElement.getAttribute("src");
          } else {
            childData.text = childElement.textContent;
          }
          return childData;
        }),
      };
    });
    const formatjsonData = JSON.stringify([jsonData], null, 2);

    const dataStr =
      "data:text/json;charset=utf-8," + encodeURIComponent(formatjsonData);
    const downloadAnchor = document.createElement("a");
    downloadAnchor.setAttribute("href", dataStr);
    downloadAnchor.setAttribute("download", "country_data.json");
    downloadAnchor.click();
  }
}
