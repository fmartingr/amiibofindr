(function() {
  var TimeComponent = function() {
    this.initialize();
  };

  TimeComponent.prototype.initialize = function() {
    [].forEach.call(document.querySelectorAll('[data-relative]'), function(item) {
      var isoTime = item.getAttribute('data-relative');
      item.textContent = moment(isoTime).fromNow();
    })
  };

  SimpleViews.register('time', TimeComponent);
})();
