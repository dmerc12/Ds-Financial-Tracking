Feature: A user needs to be able to use the navigation bar.

  Scenario: As a user, I use the manage categories button in the navigation bar.
    Given I am on the home page
    When  I click the manage categories button in the navigation bar
    Then  I am on a page with the tite Managing Categories

  Scenario: As a user, I use the manage deposits button in the navigation bar.
    Given I am on the home page
    When  I click the manage deposits button in the navigation bar
    Then  I am on a page with the tite Managing Deposits

  Scenario: As a user, I use the manage expenses button in the navigation bar.
    Given I am on the home page
    When  I click the manage expenses button in the navigation bar
    Then  I am on a page with the tite Managing Expenses

  Scenario: As a user, I use the home button in the navigation bar.
    Given I am on the home page
    When  I click the manage categories button in the navigation bar
    When  I click the home button in the navigation bar
    Then  I am on a page with the tite Managing Finances
