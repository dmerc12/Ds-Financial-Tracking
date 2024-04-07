Feature: Users need to update their information so that their information stays relevant

  Scenario Outline: As a user I should not be able to update my information with invalid information
    Given I am on the login page
    When  I input <username> in the login username input
    When  I input <password> in the login password input
    When  I click the login button
    When  I click the manage information button
    When  I enter <new_username> in the update username input
    When  I enter <first_name> in the update first name input
    When  I enter <last_name> in the update last name input
    When  I enter <email> in the update email input
    When  I enter <phone_number> in the update phone number input
    When  I click the update information button
    Then  I should be on the a page with the title <title>

    Examples:
    |username|password   |new_username|first_name|last_name|email             |phone_number|title                 |
    |'test'  |'pass12345'|''          |''        |''       |''                |''          |'Updating Information'|
    |'test'  |'pass12345'|'t' * 151   |'t' * 101 |'t' * 101|'t@e.com' * 150   |'1' * 21    |'Updating Information'|
    |'test'  |'pass12345'|'updated'   |'updated' |'updated'|'incorrect format'|'1234567890'|'Updating Information'|

  Scenario Outline: As a user I should be able to update my information with valid information
    Given I am on the login page
    When  I input <username> in the login username input
    When  I input <password> in the login password input
    When  I click the login button
    When  I click the manage information button
    When  I enter <new_username> in the update username input
    When  I enter <first_name> in the update first name input
    When  I enter <last_name> in the update last name input
    When  I enter <email> in the update email input
    When  I enter <phone_number> in the update phone number input
    When  I click the update information button
    Then  I should be on the a page with the title <title>

    Examples:
    |username|password   |new_username|first_name|last_name|email              |phone_number|title |
    |'test'  |'pass12345'|'updated'   |'updated' |'updated'|'updated@email.com'|'1234567890'|'Home'|
