Feature: Users need to edit deposits so that they can keep track of their income accurately

  Scenario Outline: As a user I should not be able to edit a deposit with invalid information
    Given I am on the login page
    When  I input <username> in the login username input
    When  I input <password> in the login password input
    When  I click the login button
    When  I click track finances button
    When  I click the manage deposits buttton
    When  I click deposit ID <id>
    When  I click the update deposit navigation button
    When  I select <category> in the deposit category select
    When  I input <date> in the deposit date input
    When  I enter <description> in the deposit description input
    When  I enter <amount> in the deposit amount input
    When  I enter the update deposit button
    Then  I should be on the a page with the title <title>

    Examples:
    |username|password |id|category|date       |description|amount|title         |
    |test    |pass12345|1 |        |20224-01-05|test       |45.54 |Updating Deposit|
    |test    |pass12345|1 |test    |           |test       |45.54 |Updating Deposit|
    |test    |pass12345|1 |test    |20224-01-05|           |45.54 |Updating Deposit|
    |test    |pass12345|1 |test    |20224-01-05|test       |      |Updating Deposit|
    |test    |pass12345|1 |test    |20224-01-05|'t' * 256  |45.54 |Updating Deposit|
    |test    |pass12345|1 |test    |20224-01-05|test       |-45.54|Updating Deposit|

  Scenario Outline: As a user I should be able to edit a deposit with valid information
    Given I am on the login page
    When  I input <username> in the login username input
    When  I input <password> in the login password input
    When  I click the login button
    When  I click track finances button
    When  I click the manage deposits buttton
    When  I click deposit ID <id>
    When  I click the update deposit navigation button
    When  I select <category> in the deposit category select
    When  I input <date> in the deposit date input
    When  I enter <description> in the deposit description input
    When  I enter <amount> in the deposit amount input
    When  I enter the update deposit button
    Then  I should be on the a page with the title <title>

    Examples:
    |username|password |id|category|date      |description|amount|title            |
    |test    |pass12345|1 |test    |2024-01-08|test       |45.58 |Managing Deposits|
