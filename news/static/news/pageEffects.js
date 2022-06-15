// -----------SCROLL-BARS----------
document.addEventListener(
    "scroll",
    function() {
      var scrollTop =
        document.documentElement["scrollTop"] || document.body["scrollTop"];
      var scrollBottom =
        (document.documentElement["scrollHeight"] ||
          document.body["scrollHeight"]) - document.documentElement.clientHeight;
      scrollPercent = scrollTop / scrollBottom * 100 + "%";
      document
        .getElementById("bar")
        .style.setProperty("--scroll", scrollPercent);
    },
    { passive: true }
  );
  
  document.addEventListener(
    "scroll",
    function() {
      var scrollTop =
        document.documentElement["scrollTop"] || document.body["scrollTop"];
      var scrollBottom =
        (document.documentElement["scrollHeight"] ||
          document.body["scrollHeight"]) - document.documentElement.clientHeight;
      scrollPercent = scrollTop / scrollBottom * 100 + "%";
      document
        .getElementById("bar1")
        .style.setProperty("--scroll", scrollPercent);
    },
    { passive: true }
  ); 



// -----------TRANSFORM-HEADER-COLOR----------

function navScroll() {
    let navElement = document.querySelector(".header");
    let navHeight = navElement.clientHeight;
    let refElement = document.querySelector(".headerRef");
  
    function checkPosition() {
      let posicionY = refElement.getBoundingClientRect().bottom;
      if (posicionY - navHeight < 0) {
        navElement.classList.add("scroll");
      } else {
        navElement.classList.remove("scroll");
      }
    }
  
    window.addEventListener("scroll", checkPosition);
}
navScroll();
  