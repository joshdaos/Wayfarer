// $('.owl-carousel').owlCarousel({
//     loop:true,
//     margin:10,
//     nav:true,
//     responsive:{
//         0:{
//             items:1
//         },
//         600:{
//             items:3
//         },
//         1000:{
//             items:5
//         }
//     }
// });

$(document).ready(function(){
    $(".owl-carousel").owlCarousel({
      nav:true,
      slideSpeed : 300,
      paginationSpeed : 400,
      singleItem:true,
      items:1,
      loop:true,
    });
  });

$("#login").on("click", function(){
    console.log("hello modal")
    $(".modal").addClass("is-active")
    $("#close").on("click", function(){
    console.log("bye modal")
    $(".modal").removeClass("is-active")
  })
})
