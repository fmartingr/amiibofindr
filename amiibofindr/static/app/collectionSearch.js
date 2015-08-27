(function() {
    var CollectionSearchComponent = function() {
       this.initialize();
    };

    CollectionSearchComponent.prototype.initialize = function() {
        var self = this;

        // Required DOM
        this.$searchInput = document.querySelector('[data-component="collectionSearchInput"]');
        this.$collectionList = document.querySelector('[data-component="collectionList"]').children;

        // Add event handlers
        this.$searchInput.addEventListener('keyup', function(event) {
            self.search(self.$searchInput.value);
        });

        // Focus search input
        this.$searchInput.focus();
    };

    CollectionSearchComponent.prototype.showItem = function(item) {
        item.style.display = 'block';
    };

    CollectionSearchComponent.prototype.hideItem = function(item) {
        item.style.display = 'none';
    };

    CollectionSearchComponent.prototype.reset = function() {
        for (var index = 0; index < this.$collectionList.length; index++) {
            var item = this.$collectionList[index];
            this.showItem(item);
        }
    };

    CollectionSearchComponent.prototype.search = function(searchQuery) {
        if (!searchQuery || searchQuery === null || searchQuery === '') {
            this.reset();
            return false;
        }

        for (var index = 0; index < this.$collectionList.length; index++) {
            var item = this.$collectionList[index];
            var names = item.getAttribute('data-amiibo-names');
            if (names.indexOf(searchQuery.toLowerCase()) === -1) {
                this.hideItem(item);
            } else {
                this.showItem(item);
            }
        }
    };

    SimpleViews.register('collection-search', CollectionSearchComponent);
})();
