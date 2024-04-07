Feature: Users need to change their password so that they can enhance the security of their account

  Scenario Outline: As a user I should not be able to change my password with invalid information
    Given I am on the login page
    When  I input <username> in the login username input
    When  I input <password> in the login password input
    When  I click the login button
    When  I click the manage information button
    When  I click the change password navigation button
    When  I enter <new_password1> in the new password 1 input
    When  I enter <new_password2> in the new password 2 input
    When  I click the change password button
    Then  I should be on the a page with the title <title>

    Examples:
    |username|password |new_password1|new_password2|title            |
    |test2   |pass12345|             |new_pass12345|Changing Password|
    |test2   |pass12345|new_pass12345|             |Changing Password|
    |test2   |pass12345|test2        |test2        |Changing Password|
    |test2   |pass12345|not          |matching     |Changing Password|

  Scenario Outline: As a user I should be able to change my password with valid information
    Given I am on the login page
    When  I input <username> in the login username input
    When  I input <password> in the login password input
    When  I click the login button
    When  I click the manage information button
    When  I click the change password navigation button
    When  I enter <new_password1> in the new password 1 input
    When  I enter <new_password2> in the new password 2 input
    When  I click the change password button
    Then  I should be on the a page with the title <title>

    Examples:
    |username|password |new_password1|new_password2|title|
    |test2   |pass12345|new_pass1234 |new_pass1234 |Home |
