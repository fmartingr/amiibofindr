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

    $('.right.menu.open').on("click",function(e){
        e.preventDefault();
        $('.ui.vertical.menu').toggle();
    });
});
