Feature: Users need to delete deposits so that they can keep track of their income accurately

  Scenario Outline: As a user I should be able to delete a deposit
    Given I am on the login page
    When  I input <username> in the login username input
    When  I input <password> in the login password input
    When  I click the login button
    When  I click track finances button
    When  I click the manage deposits buttton
    When  I click deposit ID <id>
    When  I click the delete deposit navigation button
    When  I click the delete deposit button
    Then  I should be on the a page with the title <title>

    Examples:
    |username|password |id|title            |
    |test    |pass12345|1 |Managing Deposits|
