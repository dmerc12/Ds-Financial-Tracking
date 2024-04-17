Feature: Users need to search finances so that they can better understand their finances in a date range

    Scenario Outline: As a user I should be able to search for an finances with a range of dates from the analyze finances page
        Given I am on the login page
        When  I input <username> in the login username input
        When  I input <password> in the login password input
        When  I click the login button
        When  I click track finances button
        When  I click the analyze finances buttton
        When  I input <start_date> in the start input
        When  I input <end_date> in the end date input
        When  I click the search button
        Then  I should be on the a page with the title <title>

        Examples:
        |username|password |start_date|end_date  |title             |
        |test3   |pass12345|2024-01-01|2024-02-01|Analyzing Finances|
