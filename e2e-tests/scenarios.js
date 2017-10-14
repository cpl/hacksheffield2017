'use strict';

/* https://github.com/angular/protractor/blob/master/docs/toc.md */

describe('my app', function() {


  it('should automatically redirect to /organisationSearch when location hash/fragment is empty', function() {
    browser.get('index.html');
    expect(browser.getLocationAbsUrl()).toMatch("/organisationSearch");
  });


  describe('organisationSearch', function() {

    beforeEach(function() {
      browser.get('index.html#!/organisationSearch');
    });


    it('should render organisationSearch when user navigates to /organisationSearch', function() {
      expect(element.all(by.css('[ng-view] p')).first().getText()).
        toMatch(/partial for view 1/);
    });

  });


  describe('peopleSearch', function() {

    beforeEach(function() {
      browser.get('index.html#!/peopleSearch');
    });


    it('should render peopleSearch when user navigates to /peopleSearch', function() {
      expect(element.all(by.css('[ng-view] p')).first().getText()).
        toMatch(/partial for view 2/);
    });

  });
});
