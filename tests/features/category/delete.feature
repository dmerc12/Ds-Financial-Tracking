Feature: Users need to delete categories so that they can remove unused categories

  Scenario Outline: As a user I should be able to delete a deposit category with valid information
    Given I am on the login page
    When  I input <username> in the login username input
    When  I input <password> in the login password input
    When  I click the login button
    When  I click track finances button
    When  I click the manage deposits buttton
    When  I select <category> in the manage deposit category dropdown
    When  I click the delete deposit category button
    When  I click the delete category button
    Then  I should be on the a page with the title <title>

    Examples:
    |username|password |category|title            |
    |test3   |pass12345|test    |Managing Deposits|

  Scenario Outline: As a user I should be able to delete a expense category with valid information
    Given I am on the login page
    When  I input <username> in the login username input
    When  I input <password> in the login password input
    When  I click the login button
    When  I click track finances button
    When  I click the manage expenses buttton
    When  I select <category> in the manage expense category dropdown
    When  I click the delete expense category button
    When  I click the delete category button
    Then  I should be on the a page with the title <title>

    Examples:
    |username|password |category|title            |
    |test3   |pass12345|test    |Managing Expenses|
