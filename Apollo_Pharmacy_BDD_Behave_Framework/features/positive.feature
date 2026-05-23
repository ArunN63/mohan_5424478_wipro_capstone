

  Feature: Positive Test Scenarios


  Scenario: Add product and open cart

    Given user launches Apollo Pharmacy website
    When user clicks Buy Medicines
    And user opens category "1"
    Then product page should load
    When user adds product to cart
    Then cart should open successfully


  Scenario: Apply filters and add product

    Given user launches Apollo Pharmacy website
    When user clicks Buy Medicines
    And user opens category "3"
    Then product page should load
    When user applies filters
    Then filters should apply successfully
    When user adds product to cart
    Then cart should open successfully


  Scenario: Navigate to another category page and add product

    Given user launches Apollo Pharmacy website
    When user clicks Buy Medicines
    And user opens category "4"
    Then product page should load
    When user navigates to another page
    When user adds product to cart
    Then cart should open successfully


  Scenario: Cart quantity validation

    Given user launches Apollo Pharmacy website
    When user clicks Buy Medicines
    And user opens category "3"
    Then product page should load
    When user adds product to cart
    And user increases quantity
    And user decreases quantity
    Then cart quantity should update