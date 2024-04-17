Feature: Users need to search expenses so that they can find the expense they are looking for

  Scenario Outline: As a user I should be able to search for an expense with the expense ID
    Given I am on the login page
    When  I input <username> in the login username input
    When  I input <password> in the login password input
    When  I click the login button
    When  I click track finances button
    When  I click the manage expenses buttton
    When  I click the search tab
    When  I input <id> in the expense ID input
    When  I click the search button
    Then  I should be on the a page with the title <title>

    Examples:
    |username|password |id|title            |
    |test    |pass12345|1 |Managing Expenses|

  Scenario Outline: As a user I should be able to search for an expense with a range of dates
    Given I am on the login page
    When  I input <username> in the login username input
    When  I input <password> in the login password input
    When  I click the login button
    When  I click track finances button
    When  I click the manage expenses buttton
    When  I click the search tab
    When  I input <start_date> in the start input
    When  I input <end_date> in the end date input
    When  I click the search button
    Then  I should be on the a page with the title <title>

    Examples:
    |username|password |start_date|end_date  |title            |
    |test    |pass12345|2024-01-01|2024-02-01|Managing Expenses|
