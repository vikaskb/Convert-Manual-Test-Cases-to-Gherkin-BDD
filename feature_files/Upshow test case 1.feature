Feature: Upshow test case 1

Scenario : Display and access the Upshow pipeline
Given I am logged into the ADF pipeline
When I search for the pipeline "pl_Upshow_export_DnB"
Then the pipeline should be searchable
When I open the pipeline
Then I should be able to open and view the pipeline
