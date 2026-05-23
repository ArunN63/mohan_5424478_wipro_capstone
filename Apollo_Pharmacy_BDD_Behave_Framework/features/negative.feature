Feature: Negative Test Scenarios

  Scenario: Invalid health condition index

    Given user launches Apollo Pharmacy website
    When user clicks Buy Medicines
    And user opens invalid category "50"
    Then exception should be handled

  Scenario: Invalid page navigation

    Given user launches Apollo Pharmacy website
    When user clicks Buy Medicines
    And user opens category "3"
    Then product page should load
    When user navigates to invalid page
    Then invalid page should be validated