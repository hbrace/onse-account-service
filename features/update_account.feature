Feature: Update account
  As a customer
  I want to update an account

  Scenario: An account is updated successfully
#        Given Account with ID "1" exists
    Given there an "active" account with customer id "1"
    When I update the status of an account with id "1" to "closed"
    Then Account with id "1" should be "closed"

