Feature: Test Case 2

Scenario : Check user logout functionality after successful login
Given the user is on the login page
When the user enters valid credentials
And the user clicks the login button
Then the user should be logged in successfully
When the user clicks the logout button
Then the user should be logged out successfully
And the user should be redirected to the login page
