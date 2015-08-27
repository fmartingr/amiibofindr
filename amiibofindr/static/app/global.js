// Handle data-href
$('[data-href]').on('click', function(event) {
    location.href = $(this).attr('data-href');
});

// Enable dropdowns
$('.dropdown').dropdown({transition: 'drop', on: 'hover'});

$(function(){
    $('[data-component="silbingPopup"]').popup({
        inline: true,
        position: 'left center'
    });
});
