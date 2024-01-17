Feature: A user needs to be able to delete an expense.

  Scenario Outline: As a user, I correctly attempt to delete an existing expense.
    Given I am on the home page
    When  I click the manage expenses button
    When  I click the delete expense modal on expense <expense_id>
    When  I click the delete expense button
    Then  I should see a toast notification saying <expected_text>

    Examples:
      | expense_id | expected_text                 |
      | 1          | Expense successfully deleted! |
