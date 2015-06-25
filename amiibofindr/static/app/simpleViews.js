(function() {
  var SimpleViews = function() {
    this.views = {};
    var self = this;

    window.addEventListener("load", function() {
      self.onLoad();
    });
  };

  SimpleViews.prototype.register = function(identifier, object) {
    if (identifier in this.views) {
      throw "Identifier '" + identifier + "' is already registered.";
    };
    this.views[identifier] = object;
  };

  SimpleViews.prototype.loadView = function(identifier) {
    if (typeof(this.views[identifier]) === 'function') {
      console.log('[SimpleViews] loaded view: ' + identifier);
      this.views[identifier] = new this.views[identifier](window);
    } else {
      console.error('Identifier ' + identifier + ' not registered or already loaded.');
    }
  };

  SimpleViews.prototype.onLoad = function() {
    var body = document.querySelector('body');
    var views = body.getAttribute('data-views').split(',');
    var self = this;
    [].forEach.call(views, function(view) {
      self.loadView(view);
    })
  };

  window.SimpleViews = new SimpleViews();
})(window);
