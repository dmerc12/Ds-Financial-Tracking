Feature: Users need to register with the site so that they have an account

  Scenario Outline: As a user I should not be able to register with invalid information
    Given I am on the login page
    When  I click on the sign up link
    When  I input <username> in the register username input
    When  I input <first_name> in the register first name input
    When  I input <last_name> in the register last name input
    When  I input <email> in the register email input
    When  I input <phone_number> in the register phone number input
    When  I input <password> in the register password input
    When  I input <confirm_password> in the register password confirmation input
    When  I click the registser button
    Then  I should be on the a page with the title <title>

    Examples:
    |username |first_name|last_name|email           |phone_number|password |confirm_password|title      |
    |         |test      |test     |t@e.com         |123-456-7890|pass12345|pass12345       |Registering|
    |test     |          |test     |t@e.com         |123-456-7890|pass12345|pass12345       |Registering|
    |test     |test      |         |t@e.com         |123-456-7890|pass12345|pass12345       |Registering|
    |test     |test      |test     |                |123-456-7890|pass12345|pass12345       |Registering|
    |test     |test      |test     |t@e.com         |            |pass12345|pass12345       |Registering|
    |test     |test      |test     |t@e.com         |123-456-7890|         |pass12345       |Registering|
    |test     |test      |test     |t@e.com         |123-456-7890|pass12345|                |Registering|
    |'t' * 151|test      |test     |t@e.com         |123-456-7890|pass12345|pass12345       |Registering|
    |test     |'t' * 101 |test     |t@e.com         |123-456-7890|pass12345|pass12345       |Registering|
    |test     |test      |'t' * 101|t@e.com         |123-456-7890|pass12345|pass12345       |Registering|
    |test     |test      |test     |'t@e.com' * 150 |123-456-7890|pass12345|pass12345       |Registering|
    |test     |test      |test     |t@e.com         |'1' * 21    |pass12345|pass12345       |Registering|
    |test     |test      |test     |incorrect format|123-456-7890|pass1234 |pass1324        |Registering|
    |test     |test      |test     |test@email.com  |123-456-7890|test     |test            |Registering|
    |test     |test      |test     |test@email.com  |123-456-7890|not      |matching        |Registering|

  Scenario Outline: As a user I should be able to register with valid information
    Given I am on the login page
    When  I click on the sign up navigation link
    When  I input <username> in the register username input
    When  I input <first_name> in the register first name input
    When  I input <last_name> in the register last name input
    When  I input <email> in the register email input
    When  I input <phone_number> in the register phone number input
    When  I input <password> in the register password input
    When  I input <confirm_password> in the register password confirmation input
    When  I click the registser button
    Then  I should be on the a page with the title <title>

    Examples:
    |username|first_name|last_name|email         |phone_number|password |confirm_password|title|
    |test    |test      |test     |test@email.com|123-456-7890|pass12345|pass12345       |Home |
