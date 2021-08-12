

//search bar
$(document).ready(function () {

  
  $("#search_btn").click(function () {
    if (window.matchMedia("(max-width: 600px)").matches) {
      $("#search_bar_sm").fadeToggle(300);
    } else {
      $("#search_bar").fadeToggle(300);
    }
  });


  //fade effect

  $(window).scroll(function () {
    $('.my_fade1').each(function (i) {

      var bottom_of_object = $(this).position().top + $(this).outerHeight();
      var bottom_of_window = $(window).scrollTop() + $(window).height();
      var topp = $(this).position().top;
      if (bottom_of_window > bottom_of_object) {
        $(this).animate({ 'opacity': '1', 'left': '0px', }, 1200);

      }
    });
    $('.my_fade2').each(function (i) {

      var bottom_of_object = $(this).position().top + $(this).outerHeight();
      var bottom_of_window = $(window).scrollTop() + $(window).height();

      if (bottom_of_window > bottom_of_object) {

        $(this).animate({ 'opacity': '1', 'right': '0px', }, 1200);
      }

    });

  });




  


  


  $("#publish_problem_btn").click(function () {
    $("#post_form").fadeToggle(300);
  });

  $("#dark_mode").click(function () {
    $("#post_section").toggleClass("bg-dark text-light");
  });



  $("#id_tag").css({
    "height": "75px",
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
      if ($(this).prop('checked') == true) {
        var value = $(this).parent().text();
        $('#myInput_tag').before('<h6 class="d-inline-block mx-1"><span class="badge badge-secondary">' + value + '</span></h6>');
      }
      else {
        var value = $(this).parent().text();
        // console.log(value);
        $('#id_tag').siblings('h6').each(function () {
          // console.log($(this).text());
          if ($(this).text() == value) {
            $(this).remove();
          }
        })
      }
    });

  // var tags = $("#id_tag li label").find("input[type=checkbox]")
  // console.log(tags)

  $('#id_tag').prevAll().eq(1).addClass('d-block').text('Tag (Selecet One or More):');
  $('#cmt_btn').click(function () {
    $('#cmt_form_p').show().trigger('reset');
    $('#cmt_btn_cls').show();
    $('.submit_cmt_p').show();
    $('.edit_cmt_p').hide();
  })

  //edit cmt
  $('#cmt_p_list').on('click', '#cmt_edit_open', function (e) {
    e.preventDefault();
    var cmt_id = $(this).attr('data-sid');
    $('#cmt_form_p').show();
    $('#cmt_btn_cls').show();
    $('.edit_cmt_p').show();
    $('.submit_cmt_p').hide();
    var val = $(this).closest('#cmt_content').find('#cmt_body').text();
    $('#cmt_form_p #cmt_id').val(cmt_id);
    $('#cmt_form_p textarea').val(val);
  })

  $('#cmt_btn_cls').click(function () {
    $('#cmt_btn_cls').hide();
    $('#cmt_form_p').hide();
  })
});
