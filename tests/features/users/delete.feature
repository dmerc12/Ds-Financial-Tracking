Feature: Users need to delete their account so that they can remove their information from the site

  Scenario Outline: As a user I should be able to delete my account
    Given I am on the login page
    When  I input <username> in the login username input
    When  I input <password> in the login password input
    When  I click the login button
    When  I click the manage information button
    When  I click the delete user navigation button
    When  I click the delete user button
    Then  I should be on the a page with the title <title>

    Examples:
    |username|password |title |
    |test3   |pass12345|Log In|
