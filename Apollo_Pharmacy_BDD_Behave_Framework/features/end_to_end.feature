Feature: End To End Workflow

  Scenario: Complete Apollo workflow

    Given user launches Apollo Pharmacy website

    When user clicks Buy Medicines

    And user opens category dynamically

    Then product page should load

    When user applies filters

    Then filters should apply successfully

    When user adds product to cart

    Then cart should open successfully

    When user proceeds to checkout

    And user enters mobile number dynamically

    And user selects location dynamically

    Then address should save successfully