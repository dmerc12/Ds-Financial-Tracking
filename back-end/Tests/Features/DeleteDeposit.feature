Feature: A user needs to be able to delete a deposit.

  Scenario Outline: As a user, I correctly attempt to delete an existing deposit.
    Given I am on the home page
    When  I click the manage deposits button
    When  I click the delete deposit modal on deposit <deposit_id>
    When  I click the delete deposit button
    Then  I should see a toast notification saying <expected_text>

    Examples:
      | deposit_id | expected_text                 |
      | 1          | Deposit successfully deleted! |
