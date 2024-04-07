Feature: Users need to update categories so that they can categorize their deposits and expenses better

  Scenario Outline: As a user I should not be able to update a deposit category with invalid information
    Given I am on the login page
    When  I input <username> in the login username input
    When  I input <password> in the login password input
    When  I click the login button
    When  I click track finances button
    When  I click the manage deposits buttton
    When  I click the update deposit category button
    When  I enter <name> in the category name input
    When  I enter the update category button
    Then  I should be on the a page with the title <title>

    Examples:
    |username|password   |name    |title            |
    |'test'  |'pass12345'|''      |'Adding Category'|
    |'test'  |'pass12345'|'t' * 61|'Adding Category'|

  Scenario Outline: As a user I should not be able to update a deposit category with invalid information
    Given I am on the login page
    When  I input <username> in the login username input
    When  I input <password> in the login password input
    When  I click the login button
    When  I click track finances button
    When  I click the manage expenses buttton
    When  I click the update deposit category button
    When  I enter <name> in the category name input
    When  I enter the create category button
    Then  I should be on the a page with the title <title>

    Examples:
    |username|password   |name    |title            |
    |'test'  |'pass12345'|''      |'Adding Category'|
    |'test'  |'pass12345'|'t' * 61|'Adding Category'|

  Scenario Outline: As a user I should be able to update a deposit category with valid information
    Given I am on the login page
    When  I input <username> in the login username input
    When  I input <password> in the login password input
    When  I click the login button
    When  I click track finances button
    When  I click the manage deposits buttton
    When  I click the update deposit category button
    When  I enter <name> in the category name input
    When  I enter the update category button
    Then  I should be on the a page with the title <title>

    Examples:
    |username|password   |name     |title              |
    |'test'  |'pass12345'|'updated'|'Managing Deposits'|

  Scenario Outline: As a user I should be able to update a deposit category with valid information
    Given I am on the login page
    When  I input <username> in the login username input
    When  I input <password> in the login password input
    When  I click the login button
    When  I click track finances button
    When  I click the manage expenses buttton
    When  I click the update deposit category button
    When  I enter <name> in the category name input
    When  I enter the update category button
    Then  I should be on the a page with the title <title>

    Examples:
    |username|password   |name     |title              |
    |'test'  |'pass12345'|'updated'|'Managing Expenses'|
