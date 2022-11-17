const myAccount = document.getElementById("my-account");
const dropDown = document.getElementById("dropdown");

myAccount.addEventListener("click", function () {
  dropDown.classList.toggle("hidden");
});
