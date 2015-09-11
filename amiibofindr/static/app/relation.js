(function() {
  var RelationComponent = function() {
    this.relations = document.querySelectorAll('[data-handle="relation"]');
    this.initialize();
  };

  RelationComponent.prototype.initialize = function() {
    var self = this;

    // Prepare handlers
    var linkHandler = function(event) {
      event.preventDefault();
      self.click(event.target);
    };

    [].forEach.call(this.relations, function(buttons) {
      $(buttons).on('click', 'a', linkHandler);
    });
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

    $.ajax({
      url: href,
      data: { from: from },
      success: function(result) {
        self.handleResult(loader, container, result);
      }
    });
  };

  RelationComponent.prototype.handleResult = function(loader, container, result) {
    container.html(result)
    // loader.removeClass('loading');
  };

  SimpleViews.register('relation', RelationComponent);
})();
