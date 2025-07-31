Feature: Test Case 1

Scenario : Verify user login functionality with valid credentials
Given the user is on the login page
When the user enters valid credentials
And the user clicks the login button
Then the user should be redirected to the dashboard
And the user should see a welcome message
