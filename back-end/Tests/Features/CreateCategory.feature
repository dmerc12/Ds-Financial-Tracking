Feature: A user needs to be able to add a category.

  Scenario Outline: As a user, I incorrectly attempt to create a new category.
    Given I am on the home page
    When  I click the manage categories button
    When  I click the create category modal
    When  I input <category_name> in the create category name input
    When  I click the create category button
    Then  I should see a toast notification saying <expected_text>

    Examples:
      | category_name | expected_text                                                   |
      | N/A           | The category name field cannot be left empty, please try again! |
      | test category | A category with this name already exists, please try again!     |

  Scenario Outline: As a user, I correctly attempt to create a new category.
    Given I am on the home page
    When  I click the manage categories button
    When  I click the create category modal
    When  I input <category_name> in the create category name input
    When  I click the create category button
    Then  I should see a toast notification saying <expected_text>

    Examples:
      | category_name | expected_text                  |
      | new           | Category successfully created! |
