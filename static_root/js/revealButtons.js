function burger(id) {
  var navBurger = document.getElementById(id);
  if (navBurger.style.display === "none") {
    navBurger.style.display = "flex";
  } else {
    navBurger.style.display = "none";
  }
}
