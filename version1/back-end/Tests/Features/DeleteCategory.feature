Feature: A user needs to be able to delete a category.

  Scenario Outline: As a user, I correctly attempt to delete an existing category.
    Given I am on the home page
    When  I click the manage categories button
    When  I click the delete category modal on category <category_id>
    When  I click the delete category button
    Then  I should see a toast notification saying <expected_text>

    Examples:
      | category_id | expected_text                  |
      | 1           | Category successfully deleted! |
