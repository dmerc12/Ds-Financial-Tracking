Feature: Users need to use the back buttons so that they can navigate the site easily

    Scenario Outline: As a user I should be able to use the back button on the change password page
        Given I am on the login page
        When  I input <username> in the login username input
        When  I input <password> in the login password input
        When  I click the login button
        When  I click the manage information button
        When  I click the change password navigation button
        When  I click the back button
        Then  I should be on the a page with the title <title>

        Examples:
        |username|password |title               |
        |test3   |pass12345|Updating Information|

    Scenario Outline: As a user I should be able to use the back button on the delete user page
        Given I am on the login page
        When  I input <username> in the login username input
        When  I input <password> in the login password input
        When  I click the login button
        When  I click the manage information button
        When  I click the delete user navigation button
        When  I click the back button
        Then  I should be on the a page with the title <title>

        Examples:
        |username|password |title               |
        |test3   |pass12345|Updating Information|

    Scenario Outline: As a user I should be able to use the back button on the create deposit category page when coming from the manage deposits page
        Given I am on the login page
        When  I input <username> in the login username input
        When  I input <password> in the login password input
        When  I click the login button
        When  I click the track finances button
        When  I click the manage deposits button
        When  I click the create deposit category button
        When  I click the back button
        Then  I should be on the a page with the title <title>

        Examples:
        |username|password |title            |
        |test3   |pass12345|Managing Deposits|

    Scenario Outline: As a user I should be able to use the back button on the update deposit category page when coming from the manage deposits page
        Given I am on the login page
        When  I input <username> in the login username input
        When  I input <password> in the login password input
        When  I click the login button
        When  I click the track finances button
        When  I click the manage deposits button
        When  I click the update deposit category button
        When  I click the back button
        Then  I should be on the a page with the title <title>

        Examples:
        |username|password |title            |
        |test3   |pass12345|Managing Deposits|

    Scenario Outline: As a user I should be able to use the back button on the delete deposit category page when coming from the manage deposits page
        Given I am on the login page
        When  I input <username> in the login username input
        When  I input <password> in the login password input
        When  I click the login button
        When  I click the track finances button
        When  I click the manage deposits button
        When  I click the delete deposit category button
        When  I click the back button
        Then  I should be on the a page with the title <title>

        Examples:
        |username|password |title            |
        |test3   |pass12345|Managing Deposits|

    Scenario Outline: As a user I should be able to use the back button the create deposit page
        Given I am on the login page
        When  I input <username> in the login username input
        When  I input <password> in the login password input
        When  I click the login button
        When  I click the track finances button
        When  I click the manage deposits button
        When  I click the create deposit button
        When  I click the back button
        Then  I should be on the a page with the title <title>

        Examples:
        |username|password |title         |
        |test3   |pass12345|Managing Deposits|

    Scenario Outline: As a user I should be able to use the back button the deposit detail page
        Given I am on the login page
        When  I input <username> in the login username input
        When  I input <password> in the login password input
        When  I click the login button
        When  I click the track finances button
        When  I click the manage deposits button
        When  I click deposit ID <id>
        When  I click the back button
        Then  I should be on the a page with the title <title>

        Examples:
        |username|password |id|title      |
        |test3   |pass12345|1 |Managing Deposits|

    Scenario Outline: As a user I should be able to use the back button the update deposit page
        Given I am on the login page
        When  I input <username> in the login username input
        When  I input <password> in the login password input
        When  I click the login button
        When  I click the track finances button
        When  I click the manage deposits button
        When  I click deposit ID <id>
        When  I click the update deposit button
        When  I click the back button
        Then  I should be on the a page with the title <title>

        Examples:
        |username|password |id|title      |
        |test3   |pass12345|1 |Deposit - 1|

    Scenario Outline: As a user I should be able to use the back button the delete deposit page
        Given I am on the login page
        When  I input <username> in the login username input
        When  I input <password> in the login password input
        When  I click the login button
        When  I click the track finances button
        When  I click the manage deposits button
        When  I click deposit ID <id>
        When  I click the delete deposit navigation button
        When  I click the back button
        Then  I should be on the a page with the title <title>

        Examples:
        |username|password |id|title      |
        |test3   |pass12345|1 |Deposit - 1|

    Scenario Outline: As a user I should be able to use the back button on the create expense category page when coming from the manage expenses page
        Given I am on the login page
        When  I input <username> in the login username input
        When  I input <password> in the login password input
        When  I click the login button
        When  I click the track finances button
        When  I click the manage expenses button
        When  I click the create expense category button
        When  I click the back button
        Then  I should be on the a page with the title <title>

        Examples:
        |username|password |title            |
        |test3   |pass12345|Managing Expenses|

    Scenario Outline: As a user I should be able to use the back button on the update expense category page when coming from the manage expenses page
        Given I am on the login page
        When  I input <username> in the login username input
        When  I input <password> in the login password input
        When  I click the login button
        When  I click the track finances button
        When  I click the manage expenses button
        When  I click the update expense category button
        When  I click the back button
        Then  I should be on the a page with the title <title>

        Examples:
        |username|password |title            |
        |test3   |pass12345|Managing Expenses|

    Scenario Outline: As a user I should be able to use the back button on the delete expense category page when coming from the manage expenses page
        Given I am on the login page
        When  I input <username> in the login username input
        When  I input <password> in the login password input
        When  I click the login button
        When  I click the track finances button
        When  I click the manage expenses button
        When  I click the delete expense category button
        When  I click the back button
        Then  I should be on the a page with the title <title>

        Examples:
        |username|password |title            |
        |test3   |pass12345|Managing Expenses|

    Scenario Outline: As a user I should be able to use the back button the create expense page
        Given I am on the login page
        When  I input <username> in the login username input
        When  I input <password> in the login password input
        When  I click the login button
        When  I click the track finances button
        When  I click the manage expenses button
        When  I click the create expense button
        When  I click the back button
        Then  I should be on the a page with the title <title>

        Examples:
        |username|password |title            |
        |test3   |pass12345|Managing Expenses|

    Scenario Outline: As a user I should be able to use the back button the expense detail page
        Given I am on the login page
        When  I input <username> in the login username input
        When  I input <password> in the login password input
        When  I click the login button
        When  I click the track finances button
        When  I click the manage expenses button
        When  I click expense ID <id>
        When  I click the back button
        Then  I should be on the a page with the title <title>

        Examples:
        |username|password |id|title            |
        |test3   |pass12345|1 |Managing Expenses|

    Scenario Outline: As a user I should be able to use the back button the update expense page
        Given I am on the login page
        When  I input <username> in the login username input
        When  I input <password> in the login password input
        When  I click the login button
        When  I click the track finances button
        When  I click the manage expenses button
        When  I click expense ID <id>
        When  I click the update expense button
        When  I click the back button
        Then  I should be on the a page with the title <title>

        Examples:
        |username|password |id|title      |
        |test3   |pass12345|1 |Expense - 1|

    Scenario Outline: As a user I should be able to use the back button the delete deposit page
        Given I am on the login page
        When  I input <username> in the login username input
        When  I input <password> in the login password input
        When  I click the login button
        When  I click the track finances button
        When  I click the manage deposits button
        When  I click deposit ID <id>
        When  I click the delete deposit navigation button
        When  I click the back button
        Then  I should be on the a page with the title <title>

        Examples:
        |username|password |id|title      |
        |test3   |pass12345|1 |Expense - 1|
