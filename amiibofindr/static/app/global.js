// Handle data-href
$('[data-href]').on('click', function(event) {
  location.href = $(this).attr('data-href');
});

// Enable dropdowns
$('.dropdown').dropdown({transition: 'drop', on: 'hover'});

$('.toggle-menu').on('click', function() {
  $('.responsive-menu').toggle(200);
})

$(function(){
  $('[data-component="silbingPopup"]').popup({
    inline: true,
    position: 'left center'
  });

  // Tabs
  $('.tabular.menu .item').tab();

  $(document).on('click', '[data-toggle]', function(event) {
    var $el = event.target;
    var $target = $($el.getAttribute('data-toggle'));
    $target.slideToggle(200);
  });

  $('.right.menu.open').on("click",function(e){
    e.preventDefault();
    $('.ui.vertical.menu').toggle();
  });

  moment.locale(document.querySelector('html').getAttribute('lang'));
});
