var memoriesSection = document.querySelector(".memories-section");
var memoriesLightText = document.querySelector(".light-text");
var memoriesBoldText = document.querySelector(".bold-text");
var memoriesImages = document.querySelectorAll(".memories-section img");
var skills = document.querySelectorAll(".skill");

document.addEventListener("scroll", function () {
  var clientHeight = document.documentElement.clientHeight;
  var memoriesSectionY = memoriesSection.getBoundingClientRect().y;
  var memoriesSectionHeight = memoriesSection.getBoundingClientRect().height;

  if (clientHeight > memoriesSectionY + (memoriesSectionHeight * 2) / 3) {
    memoriesLightText.style.animation =
      "slideUp 1s forwards cubic-bezier(0.87, 0, 0.13, 1)";
    memoriesBoldText.style.animation =
      "slideUp 1s 0.2s forwards cubic-bezier(0.87, 0, 0.13, 1)";
    memoriesImages[0].style.animation =
      "slideFirstImage 1.4s forwards cubic-bezier(0.22, 1, 0.36, 1)";
    memoriesImages[1].style.animation =
      "slideSecondImage 1.4s forwards cubic-bezier(0.22, 1, 0.36, 1)";
    memoriesImages[2].style.animation =
      "slideThirdImage 1.4s forwards cubic-bezier(0.22, 1, 0.36, 1)";
  }
  var skillsY = skills[1].getBoundingClientRect().y;

  if (clientHeight > skillsY) {
    skills[0].style.animation =
      "fadeInUp 1s forwards cubic-bezier(0.87, 0, 0.13, 1)";
    skills[1].style.animation =
      "fadeInUp 1s 0.2s forwards cubic-bezier(0.87, 0, 0.13, 1)";
    skills[2].style.animation =
      "fadeInUp 1s 0.4s forwards cubic-bezier(0.87, 0, 0.13, 1)";
    skills[3].style.animation =
      "fadeInUp 1s 0.6s forwards cubic-bezier(0.87, 0, 0.13, 1)";
    skills[4].style.animation =
      "fadeInUp 1s 0.6s forwards cubic-bezier(0.87, 0, 0.13, 1)";
    skills[5].style.animation =
      "fadeInUp 1s 0.6s forwards cubic-bezier(0.87, 0, 0.13, 1)";
  }

});
