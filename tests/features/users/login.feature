Feature: Users need to log into the site so that they can access the main portion of the site

  Scenario Outline: As a user I should not be able to login with invalid information
    Given I am on the login page
    When  I input <username> in the login username input
    When  I input <password> in the login password input
    When  I click the login button
    Then  I should be on the a page with the title <title>

    Examples:
    |username |password |title |
    |         |pass12345|Log In|
    |test     |         |Log In|
    |'t' * 150|pass12345|Log In|
    |incorrect|creds    |Log In|

  Scenario Outline: As a user I should be able to login with valid information
    Given I am on the login page
    When  I input <username> in the login username input
    When  I input <password> in the login password input
    When  I click the login button
    Then  I should be on the a page with the title <title>

    Examples:
    |username|password |title|
    |test    |pass12345|Home |
