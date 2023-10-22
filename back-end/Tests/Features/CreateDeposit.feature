Feature: A user needs to be able to add a deposit.

  Scenario Outline: As a user, I correctly attempt to create a new deposit.
    Given I am on the home page
    When  I click the manage deposits button
    When  I click the create deposit modal
    When  I select <category_id> the create deposit category input
    When  I input <date> in the create deposit date input
    When  I input <description> in the create deposit description input
    When  I input <amount> in the create deposit amount input
    When  I click the create deposit button
    Then  I should see a toast notification saying <expected_text>

    Examples:
      | category_id | date       | description | amount | expected_text                                                           |
      | -1          | N/A        | test        | 23.89  | The date field cannot be left empty, please try again!                  |
      | -1          | 2023-10-23 | N/A         | 23.89  | The description field cannot be left empty, please try again!           |
      | -1          | 2023-10-23 | test        | -23.89 | The amount field must be positive and cannot be 0.00, please try again! |

  Scenario Outline: As a user, I correctly attempt to create a new deposit.
    Given I am on the home page
    When  I click the manage deposits button
    When  I click the create deposit modal
    When  I select <category_id> the create deposit category input
    When  I input <date> in the create deposit date input
    When  I input <description> in the create deposit description input
    When  I input <amount> in the create deposit amount input
    When  I click the create deposit button
    Then  I should see a toast notification saying <expected_text>

    Examples:
      | category_id | date       | description | amount | expected_text                 |
      | -1          | 2023-10-23 | test        | 23.89  | Deposit successfully created! |
