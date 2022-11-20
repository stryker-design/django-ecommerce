const myAccount = document.getElementById("my-account");
const dropDown = document.getElementById("dropdown");

myAccount.addEventListener("click", function () {
  dropDown.classList.toggle("hidden");
});

const category = document.getElementById("category");
const categoryDropDown = document.getElementById("category-dropdown");

category.addEventListener("click", function () {
  categoryDropDown.classList.toggle("hidden");
});
