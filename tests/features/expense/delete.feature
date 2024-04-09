Feature: Users need to delete expenses so that they can keep track of their expenses accurately

  Scenario Outline: As a user I should be able to delete an expense
    Given I am on the login page
    When  I input <username> in the login username input
    When  I input <password> in the login password input
    When  I click the login button
    When  I click track finances button
    When  I click the manage expenses buttton
    When  I click expense ID <id>
    When  I click the delete expense navigation button
    When  I enter the delete expense button
    Then  I should be on the a page with the title <title>

    Examples:
    |username|password |id|title            |
    |test    |pass12345|1 |Managing Expenses|
