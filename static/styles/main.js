// MY ACCOUNT DROPDOWN

const myAccount = document.getElementById("my-account");
const dropDown = document.getElementById("dropdown");

myAccount.addEventListener("click", function () {
  dropDown.classList.toggle("hidden");
});

// CATEGORY DROPDOWN

const category = document.getElementById("category");
const categoryDropDown = document.getElementById("category-dropdown");

category.addEventListener("click", function () {
  categoryDropDown.classList.toggle("hidden");
});

// BASKET DROPDOWN

const shoppingBasket = document.getElementById("basket");
const basketDropdown = document.getElementById("basket-dropdown");

shoppingBasket.addEventListener("click", function () {
  basketDropdown.classList.toggle("hidden");
});

/////////////////////////////
// ADD TO BASKET //
/////////////////////////////

// this keyword refers to objects. Similar to self in python.

// const addToBasketBtn = document.getElementById("add-btn");

// addToBasketBtn.addEventListener("click", function (e) {
//   e.preventDefault();
//   let productId = this.dataset.product;
//   let action = this.dataset.action;
//   console.log("productID", productId, "Action:", action);
//   console.log("USER", user);

//   if (user == "AnonymousUser") {
//     addCookieItem(productID, action);
//   } else {
//     updateUserOrder(productId, action);
//   }
// });

// function updateUserOrder(productId, action) {
//   console.log("User is authenticated, sending data...");

//   const url = "/basket/update-item/";

//   fetch(url, {
//     method: "POST",
//     headers: {
//       "Content-Type": "application/json",
//       "X-CSRFToken": csrftoken,
//     },
//     body: JSON.stringify({ 'productId': productId, 'action': action }),
//   })
//     .then((response) => {
//       return response.json();
//     })
//     .then((data) => {
//       console.log('data:', data);
//       // location.reload();
//     });
// }
