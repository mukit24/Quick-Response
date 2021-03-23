// side nav bar
function openNav() {
  document.getElementById("mySidenav").style.width = "220px";
  document.getElementById("main_content").style.marginLeft = "220px";
}

function closeNav() {
  document.getElementById("mySidenav").style.width = "0";
  document.getElementById("main_content").style.marginLeft = "0";
}

//search bar
$(document).ready(function () {
  $("#search_btn").click(function () {
    if (window.matchMedia("(max-width: 600px)").matches) {
      $("#search_bar_sm").fadeToggle(300);
    } else {
      $("#search_bar").fadeToggle(300);
    }
  });
});

//fade effect
$(document).ready(function () {
    $(window).scroll(function () {
        $('.my_fade1').each(function (i) {

            var bottom_of_object = $(this).position().top + $(this).outerHeight();
            var bottom_of_window = $(window).scrollTop() + $(window).height();
            var topp = $(this).position().top;
            if (bottom_of_window > bottom_of_object) {
                $(this).animate({ 'opacity': '1','left':'0px', }, 1200);
    
            }
        });
        $('.my_fade2').each(function (i) {

            var bottom_of_object = $(this).position().top + $(this).outerHeight();
            var bottom_of_window = $(window).scrollTop() + $(window).height();

            if (bottom_of_window > bottom_of_object) {

                $(this).animate({ 'opacity': '1','right':'0px', }, 1200);
            }

        });

    });

});
            
