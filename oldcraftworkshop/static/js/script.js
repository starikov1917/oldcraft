$(document).ready(function () {
  $("input[type=tel]").mask("+0 000 000 00 00");
  
  if($("div").is(".index-slider")) {  

    var mySwiper = new Swiper('.index-slider', {
      loop: true,
      navigation: {
        nextEl: '.swiper-button-next',
        prevEl: '.swiper-button-prev',
      },
      pagination: {
        el: '.swiper-pagination',
        type: 'bullets',
        clickable: true
      },
      slidesPerView: 1,
      spaceBetween: 0
    });
  }
  var swiperCard = new Swiper(".swiper-card-slider", {
    spaceBetween: 30,
    slidesPerView: 3,
    freeMode: true,
    watchSlidesVisibility: true,
    watchSlidesProgress: true,
    breakpoints: {
      1024: {
        direction: "vertical",
        spaceBetween: 40 ,
        slidesPerView: 5            
      },
      992: {
        direction: "vertical",
        spaceBetween: 30 ,
        slidesPerView: 4
      },
      768: {
        direction: "vertical",
        spaceBetween: 20 ,
        slidesPerView: 4
      }
    }
  });
  var swiperCardThumbs = new Swiper(".swiper-card-thumbs-slider", {
    slidesPerView: 1,
    autoHeight: true,
    thumbs: {
      swiper: swiperCard,
    }
  });
  
  $("[data-toggle=modal]").on("click" , function() {
    setTimeout(function() {
      var swiperCardModal = new Swiper(".swiper-card-modals", {
        spaceBetween: 30,
        slidesPerView: 3,
        
        freeMode: true,
        watchSlidesVisibility: true,
        watchSlidesProgress: true,
        breakpoints: {
          1024: {
            direction: "vertical",
            spaceBetween: 40 ,
            slidesPerView: 5            
          },
          992: {
            direction: "vertical",
            spaceBetween: 30 ,
            slidesPerView: 4
          },
          768: {
            direction: "vertical",
            spaceBetween: 20 ,
            slidesPerView: 4
          }
        }
      });
      var swiperCardThumbsModal = new Swiper(".swiper-card-thumbs-modals", {
        slidesPerView: 1,
        autoHeight: true,
        thumbs: {
          swiper: swiperCardModal,
        }
      });
    },300);
  });



$("form[name=oformlenie]").submit(function(event) {
  event.preventDefault();  
  var curform = $(this);
  var goodform =  true;
  var focus = false;
  var pattern = /^([a-z0-9_\.-])+@[a-z0-9-]+\.([a-z]{2,4}\.)?[a-z]{2,4}$/i;
  curform.find(".required").each(function() {

      if($(this).attr("name") == "name") {

          if( $(this).val().length > 5) {
              $(this).closest(".input").removeClass("input--error");
              goodform = true;

          }
          else {
              $(this).closest(".input").addClass("input--error");
              if(!focus) {
                  $(this).focus();
                  focus = true;
              }
              goodform = false;
          }
      }

      if ($(this).attr("name") == "email")  {
          if (pattern.test($(this).val())) {
              $(this).closest(".input").removeClass("input--error");
              goodform = true;
          }
          else {
              $(this).closest(".input").addClass("input--error");
              if(!focus) {
                  $(this).focus();
                  focus = true;
              }
              goodform = false;
          }
      }


      if($(this).attr("name") == "phone") {

        if( $(this).val().length > 15) {
            $(this).closest(".input").removeClass("input--error");
            goodform = true;

        }
        else {
            $(this).closest(".input").addClass("input--error");
            if(!focus) {
                $(this).focus();
                focus = true;
            }
            goodform = false;
        }
    }
  });

  if (goodform) {
    console.log('Ajax')
  }
  return false;
});

});

$(document).on("click" , ".open-menu" , function(event) {
  $("body").toggleClass("menu-active")
});

$(document).on("click" , ".filter-catalog__item" , function(event) {
  $(".filter-catalog__item").addClass("button--plain");
  $(this).removeClass("button--plain")
});

$(document).on("click" , ".tabs-item" , function(event) {
  let id = $(this).attr("data-tab")
  $(".tabs-item").addClass("button--plain");
  $(this).removeClass("button--plain");

  $(".tabs-body").removeClass("tabs-body--active")
  $(".tabs-body#"+id).addClass("tabs-body--active")
});





$(document).on("click", ".btn-number",function(e) {
  var type = $(this).attr('data-type');
  var input = $(this).closest('.count-current').find('input');
  var min = input.attr('data-min');
  var max = input.attr('data-max');
  min = parseInt(min);
  max = parseInt(max);

  var value = parseInt(input.val());

  var new_val = 0

  if (type == 'plus'){
        new_val = Math.min(parseInt(max), value + 1)
        input.val(new_val)
  }
  if (type == 'minus'){
        new_val = Math.max(1, value - 1)
        input.val(new_val)
  }
    var sub_total = $("#sub-total")

    sub_total[0].textContent = (parseFloat(sub_total[0].getAttribute("data-price")) * new_val).toFixed(2)


});





$(document).on("blur" , ".count-current__value" , function(event) {
  if($(this).val() === "") {
    $(this).val(1)
  }
})

$(document).on("click" , ".site-lang__head" , function(){

  if(!$(this).closest(".site-lang").hasClass("site-lang--active")) {
    $(this).closest(".site-lang").addClass("site-lang--active")
  }

  else {
    $(this).closest(".site-lang").removeClass ("site-lang--active")
  }
});

$(document).on("click" , ".site-lang__item:not(.site-lang__item--active)" , function() {
  $(this).closest(".site-lang").find(".site-lang__item").removeClass("site-lang__item--active");
  $(this).addClass("site-lang__item--active")
  $(this).closest(".site-lang").find(".site-lang__head").text($(this).text());
  $(this).closest(".site-lang").removeClass("site-lang--active")
})



function validate(evt) {
  var theEvent = evt || window.event;
  var key = theEvent.keyCode || theEvent.which;
  key = String.fromCharCode( key );
  var regex = /[0-9]|\./;
  if( !regex.test(key) ) {
    theEvent.returnValue = false;
    if(theEvent.preventDefault) theEvent.preventDefault();
  }
}



$(document).mouseup(function(e) {

  if ($(".site-lang").has(e.target).length === 0) {
      $(".site-lang").removeClass("site-lang--active")
  }
});

$(document).on("click", ".modal-added-item", function(element){
    $(this).addClass("hiden")
})




