Feature: Upshow test case 2

Scenario : Verify the new table is created for the locations
Given I am logged in to Databricks
When I open the SQL editor
Then the login should be successful
When I run the SQL query "select * from gold_pos.Upshow_locations"
Then the table should be accessible
When I verify the data in the table
Then the table should be loaded with all DnB stores location data that are required to be sent to Upshow
When I compare the location data in "gold_pos.Upshow_locations" with the original location table "sandbox_pos.dim_location"
Then the location IDs and names should match from the original table
