@lägg_till_bok
Feature: Lägg till bok
  Som användare vill jag kunna fylla i titel och författare och lägga till en ny bok så att den dyker upp i katalogen

  Background:
    Given att jag har öppnat läslistan
    And att jag har öppnat lägg till bok

    @story1
    Scenario: Lägga till en ny bok
      When jag fyller i titeln "Gäster" och författaren "Edward Blom"
      And jag trycker på lägg till en ny bok
      Then ska boken "Gäster" finnas i katalogen

    @story2
    Scenario: Knapp är inaktiv när fälten är tomma
      Then ska knappen lägg till ny bok vara inaktiv

    @story2
    Scenario: Knappen är aktiv när både titel och författare är ifyllda
      When jag fyller i titeln "Gäster" och författaren "Edward Blom"
      Then ska knappen lägg till ny bok vara aktiv

