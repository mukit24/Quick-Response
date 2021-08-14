$(document).ready(function () {
  // menu button
  $("#menu_btn").click(function (e) {
    console.log("yoo");
    e.preventDefault();
    if ($("#my_side_nav").hasClass("open_nav")) {
      $("#my_side_nav").css({ width: "0" }).removeClass("open_nav");
      $("#menu_icon").removeClass("fa fa-remove").addClass("fa fa-reorder");
      $("#main_content").css({ filter: "blur(0px)" });
    } else {
      console.log("yooside");
      if ($("#slide_noti").hasClass("expand")) {
        // $("#main_content").css({ filter: 'blur(0px)' });
        $("#slide_noti").css({ width: "0px" }).removeClass("expand");
      }
      $("#my_side_nav").css({ width: "180px" }).addClass("open_nav");
      $("#menu_icon").removeClass("fa fa-reorder").addClass("fa fa-remove");
      $("#main_content").css({ filter: "blur(2px)" });
    }
  });

  // notification button
  $("#noti").click(function (e) {
    e.preventDefault();
    if ($("#slide_noti").hasClass("expand")) {
      $("#main_content").css({ filter: "blur(0px)" });
      $("#slide_noti").css({ width: "0px" }).removeClass("expand");
    } else {
      if ($("#my_side_nav").hasClass("open_nav")) {
        $("#my_side_nav").css({ width: "0" }).removeClass("open_nav");
        $("#menu_icon").removeClass("fa fa-remove").addClass("fa fa-reorder");
      }
      if ($(window).width() < 425) {
        $("#slide_noti").css({ width: "220px" }).addClass("expand");
        $("#main_content").css({ filter: "blur(2px)" });
      } else {
        $("#slide_noti").css({ width: "280px" }).addClass("expand");
        $("#main_content").css({ filter: "blur(2px)" });
      }
    }
  });

  //fade effect
  $(window).scroll(function () {
    $(".my_fade1").each(function (i) {
      var bottom_of_object = $(this).position().top + $(this).outerHeight();
      var bottom_of_window = $(window).scrollTop() + $(window).height();
      var topp = $(this).position().top;
      if (bottom_of_window > bottom_of_object) {
        $(this).animate({ opacity: "1", left: "0px" }, 1200);
      }
    });
    $(".my_fade2").each(function (i) {
      var bottom_of_object = $(this).position().top + $(this).outerHeight();
      var bottom_of_window = $(window).scrollTop() + $(window).height();

      if (bottom_of_window > bottom_of_object) {
        $(this).animate({ opacity: "1", right: "0px" }, 1200);
      }
    });

    $(".my_fade_main").each(function (i) {
      var bottom_of_object = $(this).position().top + $(this).outerHeight();
      var bottom_of_window = $(window).scrollTop() + $(window).height();
      var topp = $(this).position().top;
      if (bottom_of_window > bottom_of_object) {
        $(this).animate({ opacity: "1", bottom: "0px" }, 2000);
      }
    });
  });

  // post index //

  // open post form
  $("#publish_problem_btn").click(function () {
    $("#post_form").fadeToggle(300);
  });

  //tag selection in post form
  $("#id_tag").css({
    height: "75px",
    "overflow-y": "scroll",
    "list-style-type": "none",
    "padding-left": "5px",
  });

  $("#id_tag").before(
    '<input class="form-control" id="myInput_tag" type="text" placeholder="Search..">'
  );

  $("#myInput_tag").on("keyup", function () {
    var value = $(this).val().toLowerCase();
    $("#id_tag li").filter(function () {
      $(this).toggle($(this).text().toLowerCase().indexOf(value) > -1);
    });
  });

  $("#id_tag li label")
    .find("input[type=checkbox]")
    .click(function () {
      if ($(this).prop("checked") == true) {
        var value = $(this).parent().text();
        $("#myInput_tag").before(
          '<h6 class="d-inline-block mx-1" id="tag_h6"><span class="badge badge-secondary">' +
            value +
            "</span></h6>"
        );
      } else {
        var value = $(this).parent().text();
        // console.log(value);
        $("#id_tag")
          .siblings("h6")
          .each(function () {
            // console.log($(this).text());
            if ($(this).text() == value) {
              $(this).remove();
            }
          });
      }
    });

  $("#id_tag")
    .prevAll()
    .eq(1)
    .addClass("d-block")
    .text("Tag (Selecet One or More):");

  // tag select in sort by section
  $(document).ready(function () {
    $("#id_title").removeAttr("required");
    $("#search_tag_input").on("keyup", function () {
      var value = $(this).val().toLowerCase();
      $("#tag_list_modal label").filter(function () {
        $(this).toggle($(this).text().toLowerCase().indexOf(value) > -1);
      });
    });

    $("#tag_list_modal label")
      .find("input[type=checkbox]")
      .click(function () {
        if ($(this).prop("checked") == true) {
          var value = $(this).parent().text();
          $("#search_tag_input").before(
            '<h6 class="d-inline-block mx-1"><span class="badge badge-info">' +
              value +
              "</span></h6>"
          );
        } else {
          console.log("test");
          var value = $(this).parent().text();
          console.log(value);
          $("#tag_list_form")
            .siblings("h6")
            .each(function () {
              console.log($(this).text());
              if ($(this).text() == value) {
                $(this).remove();
              }
            });
        }
      });
  });

  //post details
  // for edit post
  $("#id_tag input[type=checkbox]").each(function () {
    if (this.checked) {
      var value = $(this).parent().text();
      console.log(value);
      $("#myInput_tag").before(
        '<h6 class="d-inline-block mx-1"><span class="badge badge-secondary">' +
          value +
          "</span></h6>"
      );
    }
  });
  // open comment form
  $("#cmt_btn").click(function () {
    $("#cmt_form_p").show().trigger("reset");
    $("#cmt_btn_cls").show();
    $(".submit_cmt_p").show();
    $(".edit_cmt_p").hide();
  });

  //edit cmt
  $("#cmt_p_list").on("click", "#cmt_edit_open", function (e) {
    e.preventDefault();
    var cmt_id = $(this).attr("data-sid");
    $("#cmt_form_p").show();
    $("#cmt_btn_cls").show();
    $(".edit_cmt_p").show();
    $(".submit_cmt_p").hide();
    var val = $(this).closest("#cmt_content").find("#cmt_body").text();
    $("#cmt_form_p #cmt_id").val(cmt_id);
    $("#cmt_form_p textarea").val(val);
  });

  //close comment form
  $("#cmt_btn_cls").click(function () {
    $("#cmt_btn_cls").hide();
    $("#cmt_form_p").hide();
  });

  // owl carousel
  //did not use later
  $(".feature-carousel").owlCarousel({
    loop: true,
    autoplay: true,
    margin: 0,
    nav: true,
    navText: [
      "<i class='fa fa-caret-left' aria-hidden='true'></i>",
      "<i class='fa fa-caret-right' aria-hidden='true'></i>",
    ],
    responsiveClass: true,
    responsive: {
      0: {
        items: 1,
      },
      500: {
        items: 2,
      },
      1000: {
        items: 4,
      },
    },
  });
});
