(function() {
  var RelationComponent = function() {
    this.relationsQuerySelector = '[data-handle="relation"]';
    this.initialize();
  };

  RelationComponent.prototype.initialize = function() {
    var self = this;

    // Prepare handlers
    var linkHandler = function(event) {
      event.preventDefault();
      event.stopPropagation();

      var target = event.target;

      // Handles clicking in the icon
      if (event.target.href === undefined)
        target = event.target.parentNode

      self.click(target);
    };

    $(document).on('click', this.relationsQuerySelector + ' a', linkHandler);
  };

  RelationComponent.prototype.click = function(element) {
    var $link = element;
    var href = $link.href;
    var $buttons = $(element).closest('[data-amiibo]');
    var from = $buttons.attr('data-from');
    var amiiboId = $buttons.attr('data-amiibo');
    var loader = $buttons.closest('[data-loader="' + amiiboId + '"]');
    this.doGet(href, from, loader, $buttons);
  };

  RelationComponent.prototype.doGet = function(href, from, loader, container) {
    var self = this;
    // loader.addClass('loading');

    // If list, the entire card is the container
    if (from === "list") container = loader;

    $.ajax({
      url: href,
      data: { from: from },
      success: function(result) {
        self.handleResult(loader, from, container, result);
      }
    });
  };

  RelationComponent.prototype.handleResult = function(loader, from, container, result) {
    if (from === 'list') {
      container.replaceWith(result);
    } else {
      container.html(result)
    }
    // loader.removeClass('loading');
  };

  SimpleViews.register('relation', RelationComponent);
})();
