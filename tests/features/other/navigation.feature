Feature: Users need to use the navigation buttons so that they can navigate the site easily

    Scenario Outline: As a user I should be able to navigate to the register page
        Given I am on the login page
        When  I click on the sign up link
        Then  I should be on the a page with the title <title>

        Examples:
        |title      |
        |Registering|

    Scenario Outline: As a user I should be able to navigate to the login page
        Given I am on the login page
        When  I click on the sign up link
        When  I click on the log in link
        Then  I should be on the a page with the title <title>

        Examples:
        |title |
        |Log In|

    Scenario Outline: As a user I should be able to navigate to the mange information page
        Given I am on the login page
        When  I input <username> in the login username input
        When  I input <password> in the login password input
        When  I click the login button
        When  I click the manage information button
        Then  I should be on the a page with the title <title>

        Examples:
        |username|password |title               |
        |test    |pass12345|Updating Information|

    Scenario Outline: As a user I should be able to navigate to the change password page
        Given I am on the login page
        When  I input <username> in the login username input
        When  I input <password> in the login password input
        When  I click the login button
        When  I click the manage information button
        When  I click the change password navigation button
        Then  I should be on the a page with the title <title>

        Examples:
        |username|password |title            |
        |test    |pass12345|Changing Password|

    Scenario Outline: As a user I should be able to navigate to the delete user page
        Given I am on the login page
        When  I input <username> in the login username input
        When  I input <password> in the login password input
        When  I click the login button
        When  I click the manage information button
        When  I click the delete user navigation button
        Then  I should be on the a page with the title <title>

        Examples:
        |username|password |title           |
        |test    |pass12345|Deleting Account|

    Scenario Outline: As a user I should be able to navigate to the track finances page
        Given I am on the login page
        When  I input <username> in the login username input
        When  I input <password> in the login password input
        When  I click the login button
        When  I click the track finances button
        Then  I should be on the a page with the title <title>

        Examples:
        |username|password |title                |
        |test    |pass12345|Finance Tracking Home|

    Scenario Outline: As a user I should be able to navigate to the manage deposits page
        Given I am on the login page
        When  I input <username> in the login username input
        When  I input <password> in the login password input
        When  I click the login button
        When  I click the track finances button
        When  I click the manage deposits button
        Then  I should be on the a page with the title <title>

        Examples:
        |username|password |title            |
        |test    |pass12345|Managing Deposits|

    Scenario Outline: As a user I should be able to navigate to the create deposit page
        Given I am on the login page
        When  I input <username> in the login username input
        When  I input <password> in the login password input
        When  I click the login button
        When  I click the track finances button
        When  I click the manage deposits button
        When  I click the create deposit button
        Then  I should be on the a page with the title <title>

        Examples:
        |username|password |title         |
        |test    |pass12345|Create Deposit|

    Scenario Outline: As a user I should be able to navigate to the deposit detail page
        Given I am on the login page
        When  I input <username> in the login username input
        When  I input <password> in the login password input
        When  I click the login button
        When  I click the track finances button
        When  I click the manage deposits button
        When  I click deposit ID <id>
        Then  I should be on the a page with the title <title>

        Examples:
        |username|password |id|title      |
        |test    |pass12345|1 |Deposit - 1|

    Scenario Outline: As a user I should be able to navigate to the update deposit page
        Given I am on the login page
        When  I input <username> in the login username input
        When  I input <password> in the login password input
        When  I click the login button
        When  I click the track finances button
        When  I click the manage deposits button
        When  I click deposit ID <id>
        When  I click the update deposit button
        Then  I should be on the a page with the title <title>

        Examples:
        |username|password |id|title           |
        |test    |pass12345|1 |Updating Deposit|

    Scenario Outline: As a user I should be able to navigate to the delete deposit page
        Given I am on the login page
        When  I input <username> in the login username input
        When  I input <password> in the login password input
        When  I click the login button
        When  I click the track finances button
        When  I click the manage deposits button
        When  I click deposit ID <id>
        When  I click the delete deposit navigation button
        Then  I should be on the a page with the title <title>

        Examples:
        |username|password |id|title           |
        |test    |pass12345|1 |Deleting Deposit|

    Scenario Outline: As a user I should be able to navigate to the create deposit category page
        Given I am on the login page
        When  I input <username> in the login username input
        When  I input <password> in the login password input
        When  I click the login button
        When  I click the track finances button
        When  I click the manage deposits button
        When  I click the create deposit category button
        Then  I should be on the a page with the title <title>

        Examples:
        |username|password |title          |
        |test    |pass12345|Adding Category|

    Scenario Outline: As a user I should be able to navigate to the update deposit category page
        Given I am on the login page
        When  I input <username> in the login username input
        When  I input <password> in the login password input
        When  I click the login button
        When  I click the track finances button
        When  I click the manage deposits button
        When  I click the update deposit category button
        Then  I should be on the a page with the title <title>

        Examples:
        |username|password |title            |
        |test    |pass12345|Updating Category|

    Scenario Outline: As a user I should be able to navigate to the delete deposit category page
        Given I am on the login page
        When  I input <username> in the login username input
        When  I input <password> in the login password input
        When  I click the login button
        When  I click the track finances button
        When  I click the manage deposits button
        When  I click the delete deposit category button
        Then  I should be on the a page with the title <title>

        Examples:
        |username|password |title            |
        |test    |pass12345|Deleting Category|

    Scenario Outline: As a user I should be able to navigate to the manage expenses page
        Given I am on the login page
        When  I input <username> in the login username input
        When  I input <password> in the login password input
        When  I click the login button
        When  I click the track finances button
        When  I click the manage expenses button
        Then  I should be on the a page with the title <title>

        Examples:
        |username|password |title            |
        |test    |pass12345|Managing Expenses|

    Scenario Outline: As a user I should be able to navigate to the create expense page
        Given I am on the login page
        When  I input <username> in the login username input
        When  I input <password> in the login password input
        When  I click the login button
        When  I click the track finances button
        When  I click the manage expenses button
        When  I click the create expense button
        Then  I should be on the a page with the title <title>

        Examples:
        |username|password |title         |
        |test    |pass12345|Create Expense|

    Scenario Outline: As a user I should be able to navigate to the expense detail page
        Given I am on the login page
        When  I input <username> in the login username input
        When  I input <password> in the login password input
        When  I click the login button
        When  I click the track finances button
        When  I click the manage expenses button
        When  I click expense ID <id>
        Then  I should be on the a page with the title <title>

        Examples:
        |username|password |id|title      |
        |test    |pass12345|1 |Expense - 1|

    Scenario Outline: As a user I should be able to navigate to the update expense page
        Given I am on the login page
        When  I input <username> in the login username input
        When  I input <password> in the login password input
        When  I click the login button
        When  I click the track finances button
        When  I click the manage expenses button
        When  I click expense ID <id>
        When  I click the update expense button
        Then  I should be on the a page with the title <title>

        Examples:
        |username|password |id|title           |
        |test    |pass12345|1 |Updating Expense|

    Scenario Outline: As a user I should be able to navigate to the delete expense page
        Given I am on the login page
        When  I input <username> in the login username input
        When  I input <password> in the login password input
        When  I click the login button
        When  I click the track finances button
        When  I click the manage expenses button
        When  I click expense ID <id>
        When  I click the delete expense navigation button
        Then  I should be on the a page with the title <title>

        Examples:
        |username|password |id|title           |
        |test    |pass12345|1 |Deleting Expense|

    Scenario Outline: As a user I should be able to navigate to the create expense category page
        Given I am on the login page
        When  I input <username> in the login username input
        When  I input <password> in the login password input
        When  I click the login button
        When  I click the track finances button
        When  I click the manage expenses button
        When  I click the create expense category button
        Then  I should be on the a page with the title <title>

        Examples:
        |username|password |title          |
        |test    |pass12345|Adding Category|

    Scenario Outline: As a user I should be able to navigate to the update expense category page
        Given I am on the login page
        When  I input <username> in the login username input
        When  I input <password> in the login password input
        When  I click the login button
        When  I click the track finances button
        When  I click the manage expenses button
        When  I click the update expense category button
        Then  I should be on the a page with the title <title>

        Examples:
        |username|password |title            |
        |test    |pass12345|Updating Category|

    Scenario Outline: As a user I should be able to navigate to the delete expense category page
        Given I am on the login page
        When  I input <username> in the login username input
        When  I input <password> in the login password input
        When  I click the login button
        When  I click the track finances button
        When  I click the manage expenses button
        When  I click the delete expense category button
        Then  I should be on the a page with the title <title>

        Examples:
        |username|password |title            |
        |test    |pass12345|Deleting Category|

    Scenario Outline: As a user I should be able to navigate to the view finances page
        Given I am on the login page
        When  I input <username> in the login username input
        When  I input <password> in the login password input
        When  I click the login button
        When  I click the track finances button
        When  I click the view finances button
        Then  I should be on the a page with the title <title>

        Examples:
        |username|password |title           |
        |test    |pass12345|Viewing Finances|

    Scenario Outline: As a user I should be able to navigate to the analyze finances page
        Given I am on the login page
        When  I input <username> in the login username input
        When  I input <password> in the login password input
        When  I click the login button
        When  I click the track finances button
        When  I click the analyze finances button
        Then  I should be on the a page with the title <title>

        Examples:
        |username|password |title             |
        |test    |pass12345|Analyzing Finances|
