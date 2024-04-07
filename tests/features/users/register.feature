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
    |username |first_name|last_name|email             |phone_number|password  |confirm_password|title        |
    |''       |''        |''       |''                |''          |''        |''              |'Registering'|
    |'t' * 151|'t' * 101 |'t' * 100|'t@e.com' * 150   |'1' * 21    |'pass1234'|'pass1234'      |'Registering'|
    |'test'   |'test'    |'test'   |'incorrect format'|'1234567890'|'pass1234'|'pass1324'      |'Registering'|
    |'test'   |'test'    |'test'   |'test@email.com'  |'1234567890'|'test'    |'test'          |'Registering'|
    |'test'   |'test'    |'test'   |'test@email.com'  |'1234567890'|'not'     |'matching'      |'Registering'|

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
    |username|first_name|last_name|email           |phone_number|password   |confirm_password|title |
    |'test'  |'test'    |'test'   |'test@email.com'|'1234567890'|'pass12345'|'pass12345'     |'Home'|
