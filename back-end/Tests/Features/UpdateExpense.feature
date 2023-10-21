Feature: A user needs to be able to update an expense.

  Scenario Outline: As a user, I incorrectly attempt to update an existing expense.
    Given I am on the home page
    When  I click the manage expenses button
    When  I click the update expense modal on expense <expense_id>
    When  I select <category_id> the update expense category input
    When  I input <date> in the update expense date input
    When  I input <description> in the update expense description input
    When  I input <amount> in the update expense amount input
    When  I click the update expense button
    Then  I should see a toast notification saying <expected_text>

    Examples:
      | expense_id | category_id | date       | description | amount | expected_text                                                           |
      | 1          | -1          | N/A        | test        | 23.89  | The date field cannot be left empty, please try again!                  |
      | 1          | -1          | 2023-10-23 | N/A         | 23.89  | The description field cannot be left empty, please try again!           |
      | 1          | -1          | 2023-10-23 | test        | -23.89 | The amount field must be positive and cannot be 0.00, please try again! |

  Scenario Outline: As a user, I correctly attempt to update an existing expense.
    Given I am on the home page
    When  I click the manage expenses button
    When  I click the update expense modal on expense <expense_id>
    When  I select <category_id> the update expense category input
    When  I input <date> in the update expense date input
    When  I input <description> in the update expense description input
    When  I input <amount> in the update expense amount input
    When  I click the update expense button
    Then  I should see a toast notification saying <expected_text>

    Examples:
      | expense_id | category_id | date       | description | amount | expected_text                 |
      | 1          | -1          | 2023-10-23 | test        | 23.89  | Expense successfully updated! |
