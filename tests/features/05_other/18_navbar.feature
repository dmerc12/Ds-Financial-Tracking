Feature: Users need to use the navigation bar so that they can navigate the site easily

    Scenario Outline: As a user I should not be able to use the home tab in the navbar when not logged in
        Given I am on the login page
        When  I click the home tab in the navbar
        Then  I should be on the a page with the title <title>

        Examples:
        |title |
        |Log In|

    Scenario Outline: As a user I should be able to use the home tab in the navbar
        Given I am on the login page
        When  I input <username> in the login username input
        When  I input <password> in the login password input
        When  I click the login button
        When  I click the home tab in the navbar
        Then  I should be on the a page with the title <title>

        Examples:
        |username|password |title|
        |test3   |pass12345|Home |

    Scenario Outline: As a user I should not be able to use the manage information tab in the navbar when not logged in
        Given I am on the login page
        When  I click the manage information tab in the navbar
        Then  I should be on the a page with the title <title>

        Examples:
        |title |
        |Log In|

    Scenario Outline: As a user I should be able to use the manage information tab in the navbar
        Given I am on the login page
        When  I input <username> in the login username input
        When  I input <password> in the login password input
        When  I click the login button
        When  I click the manage information tab in the navbar
        Then  I should be on the a page with the title <title>

        Examples:
        |username|password |title               |
        |test3   |pass12345|Updating Information|

    Scenario Outline: As a user I should not be able to use the manage deposits tab in the navbar when not logged in
        Given I am on the login page
        When  I click the track finances dropdown in the navbar
        When  I click the manage deposits tab in the navbar
        Then  I should be on the a page with the title <title>

        Examples:
        |title |
        |Log In|

    Scenario Outline: As a user I should be able to use the manage deposits tab in the navbar
        Given I am on the login page
        When  I input <username> in the login username input
        When  I input <password> in the login password input
        When  I click the login button
        When  I click the track finances dropdown in the navbar
        When  I click the manage deposits tab in the navbar
        Then  I should be on the a page with the title <title>

        Examples:
        |username|password |title            |
        |test3   |pass12345|Managing Deposits|

    Scenario Outline: As a user I should not be able to use the manage expenses tab in the navbar when not logged in
        Given I am on the login page
        When  I click the track finances dropdown in the navbar
        When  I click the manage expenses tab in the navbar
        Then  I should be on the a page with the title <title>

        Examples:
        |title |
        |Log In|

    Scenario Outline: As a user I should be able to use the manage expenses tab in the navbar
        Given I am on the login page
        When  I input <username> in the login username input
        When  I input <password> in the login password input
        When  I click the login button
        When  I click the track finances dropdown in the navbar
        When  I click the manage expenses tab in the navbar
        Then  I should be on the a page with the title <title>

        Examples:
        |username|password |title            |
        |test3   |pass12345|Managing Expenses|

    Scenario Outline: As a user I should not be able to use the view finances tab in the navbar when not logged in
        Given I am on the login page
        When  I click the track finances dropdown in the navbar
        When  I click the view finances tab in the navbar
        Then  I should be on the a page with the title <title>

        Examples:
        |title |
        |Log In|

    Scenario Outline: As a user I should be able to use the view finances tab in the navbar
        Given I am on the login page
        When  I input <username> in the login username input
        When  I input <password> in the login password input
        When  I click the login button
        When  I click the track finances dropdown in the navbar
        When  I click the view finances tab in the navbar
        Then  I should be on the a page with the title <title>

        Examples:
        |username|password |title           |
        |test3   |pass12345|Viewing Finances|

    Scenario Outline: As a user I should not be able to use the analyze finances tab in the navbar when not logged in
        Given I am on the login page
        When  I click the track finances dropdown in the navbar
        When  I click the analyze finances tab in the navbar
        Then  I should be on the a page with the title <title>

        Examples:
        |title |
        |Log In|

    Scenario Outline: As a user I should be able to use the analyze finances tab in the navbar
        Given I am on the login page
        When  I input <username> in the login username input
        When  I input <password> in the login password input
        When  I click the login button
        When  I click the track finances dropdown in the navbar
        When  I click the analyze finances tab in the navbar
        Then  I should be on the a page with the title <title>

        Examples:
        |username|password |title             |
        |test3   |pass12345|Analyzing Finances|

    Scenario Outline: As a user I should be able to use the logout in the navbar
        Given I am on the login page
        When  I input <username> in the login username input
        When  I input <password> in the login password input
        When  I click the login button
        When  I click the logout button in the navbar
        Then  I should be on the a page with the title <title>

        Examples:
        |username|password |title |
        |test3   |pass12345|Log In|
