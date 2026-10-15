@mina_böcker
Feature: Mina böcker
  som användare vill jag kunna trycka på mina böcker så att jag ser de böcker jag favoritmarkerat

  Background:
  Given att jag har öppnat läslistan

  @story1
  Scenario: Favoritmarkerad bok visas i Mina böcker
    Given att jag favoritmarkerat en bok
    When jag öppnar mina böcker
    Then ska boken finnas i Mina böcker

  @story2
  Scenario: Tom lista när inga favoritmarkerkade böcker valts
    When jag öppnar mina böcker
    Then ska information om att listan är tom visas