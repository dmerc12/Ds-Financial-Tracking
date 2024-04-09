Feature: Users need to create expenses so that they can keep track of their expenses

  Scenario Outline: As a user I should not be able to create an expense with invalid information
    Given I am on the login page
    When  I input <username> in the login username input
    When  I input <password> in the login password input
    When  I click the login button
    When  I click track finances button
    When  I click the manage expenses buttton
    When  I click the create expense button
    When  I select <category> in the expense category select
    When  I input <date> in the expense date input
    When  I enter <description> in the expense description input
    When  I enter <amount> in the expense amount input
    When  I click the create expense button
    Then  I should be on the a page with the title <title>

    Examples:
    |username|password |category|date       |description|amount|title         |
    |test    |pass12345|        |20224-01-05|test       |45.54 |Create Expenses|
    |test    |pass12345|test    |           |test       |45.54 |Create Expenses|
    |test    |pass12345|test    |20224-01-05|           |45.54 |Create Expenses|
    |test    |pass12345|test    |20224-01-05|test       |      |Create Expenses|
    |test    |pass12345|test    |20224-01-05|'t' * 256  |45.54 |Create Expenses|
    |test    |pass12345|test    |20224-01-05|test       |-45.54|Create Expenses|

  Scenario Outline: As a user I should be able to create an expense with valid information
    Given I am on the login page
    When  I input <username> in the login username input
    When  I input <password> in the login password input
    When  I click the login button
    When  I click track finances button
    When  I click the manage expenses buttton
    When  I click the create expense button
    When  I select <category> in the expense category select
    When  I input <date> in the expense date input
    When  I enter <description> in the expense description input
    When  I enter <amount> in the expense amount input
    When  I click the create expense button
    Then  I should be on the a page with the title <title>

    Examples:
    |username|password |category|date      |description|amount|title            |
    |test    |pass12345|test    |2024-01-08|test       |45.58 |Managing Expensess|
