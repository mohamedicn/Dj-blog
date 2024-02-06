let anglesup = document.querySelector(".anglesup");
window.addEventListener("scroll", function () {
  if (window.scrollY > 600) {
   anglesup.classList.add("active");
  } else {
    anglesup.classList.remove("active");
  }
});
anglesup.addEventListener("click", function () {
  window.scrollTo({
    top: 0,
    behavior: "smooth",
  });
});