Feature Add new record

  Add new record

 Scenario Outline: Add new record
    Given I access the website
    When I insert <dataT>:<dataH><dataM> <name> <obs>
    And I click add
    Then <name> should be available
   Examples:
   |dataT|dataH|dataM|name|obs|
   |12122021|1111|a|abc|def|