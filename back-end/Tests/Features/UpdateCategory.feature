Feature: A user needs to be able to update a category.

  Scenario Outline: As a user, correctly attempt to update an existing category.
    Given I am on the home page
    When  I click on the manage categories button
    When  I click the update category modal on category <category_id>
    When  I input <category_name> in the update category name input
    When  I click the update category button
    Then  I should see a toast notification saying <expected_text>

    Examples:
      | category_id | category_name    | expected_text                                                   |
      | 1           | updated category | Category successfully updated!                                  |
      | 1           | N/A              | The category name field cannot be left empty, please try again! |
      | 1           | test category    | A category with this name already exists, please try again!     |

  Scenario Outline: As a user, correctly attempt to update an existing category.
    Given I am on the home page
    When  I click on the manage categories button
    When  I click the update category modal on category <category_id>
    When  I input <category_name> in the update category name input
    When  I click the update category button
    Then  I should see a toast notification saying <expected_text>

    Examples:
      | category_id | category_name    | expected_text                  |
      | 1           | updated category | Category successfully updated! |
