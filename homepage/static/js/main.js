$('#toggle').click(function() {
  $(this).toggleClass('active');
  $('#overlay').toggleClass('open');
});
$('.overlay-menu a').click(function() {
  $('.button_container').toggleClass('active');
  $('#overlay').toggleClass('open');
  return false;
});
