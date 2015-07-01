(function() {
  var MoneyComponent = function() {
    this.DEBUG = DEBUG;
    this.currency = 'EUR';
    this.currencies = CURRENCIES;
    this.ratesSet = false;
    this.initialize();
  };

  MoneyComponent.prototype.initialize = function() {
    this.loadRatesFromBrowser();
    if (!this.ratesSet) this.refreshRates();
    this.handlers();
    var userCurrency = window.localStorage.getItem('currency');
    if (userCurrency && this.currencies.indexOf(userCurrency) !== -1) {
      this.currency = userCurrency;
    }
    this.setCurrency(this.currency);
  };

  /*
   * Rates
   */
  MoneyComponent.prototype.loadRatesFromBrowser = function() {
    // Try to load and set the stored rates if the object is not older than 7 days
    try {
      var rates = JSON.parse(window.localStorage.getItem('rates'));
      var storedDate = new Date(rates.time).getTime();
      var weekDate = new Date().getTime() - (1000*60*60*24*7);
      if (storedDate >= weekDate) this.setRates(rates);
      if (this.DEBUG) console.log('[money] Using localStorage rates');
    } catch(err) {
      console.error(err)
    }
  };

  MoneyComponent.prototype.setRates = function(data) {
    if (!this.ratesSet) {
      if (typeof fx !== "undefined" && fx.rates) {
        fx.rates = data.rates;
        fx.base = data.base;
      }
      this.ratesSet = true;
    }
  };

  MoneyComponent.prototype.refreshRates = function() {
    var self = this;
    if (this.DEBUG) console.log('[money] Refreshing rates from server');
    $.getJSON(
      MEDIA_URL + '/rates.json',
      function(data) {
        data['time'] = new Date();
        window.localStorage.setItem('rates', JSON.stringify(data));
        self.setRates(data);
      }
    );
  };

  MoneyComponent.prototype.setCurrency = function(currency) {
    var self = this;
    if (this.currencies.indexOf(currency) !== -1) {
      if (this.DEBUG) console.log('[money] set user currency: ' + currency)
      $('[data-currency-change]').removeClass('underlined');
      $('[data-currency-change="' + currency + '"]').addClass('underlined');
      window.localStorage.setItem('currency', currency);
      this.currency = currency;
      this.convertPrices();
    }
  };

  MoneyComponent.prototype.convertPrices = function() {
    var self = this;
    if (!this.ratesSet) {
      if (this.DEBUG) console.log('[money] wait 300ms to convert prices...');
      setTimeout(function() {
        self.convertPrices()
      }, 300);
      return false;
    }
    [].forEach.call(document.querySelectorAll('[data-money]'), function(item) {
      var price = item.getAttribute('data-price');
      var currency = item.getAttribute('data-currency');
      if ((price && currency)) {
        if (currency != self.currency) {
          var conversion = fx(parseFloat(price)).from(currency).to(self.currency);
          if (self.DEBUG) console.log('[money] converting ' + price + ' from ' + currency + ' to ' + self.currency + ': ' + conversion);
          if (conversion) item.innerHTML = '<span class="price-converted">' + conversion.toFixed(2) + ' ' + self.currency + '</span>';
        } else {
          item.innerHTML = price + ' ' + currency;
        }
      }
    });
  };

  MoneyComponent.prototype.handlers = function() {
    var self = this;
    [].forEach.call(document.querySelectorAll('[data-currency-change]'), function(item) {
      var currency = item.getAttribute('data-currency-change');
      item.addEventListener('click', function(event) {
        event.preventDefault();
        self.setCurrency(currency);
      })
    });
  };

  SimpleViews.register('money', MoneyComponent);
})();
