@katalog
Feature: katalog
som användare vill jag kunna se en lista med alla tillgängliga böcker så att jag vet vad jag kan läsa
  Background:
    Given att jag har öppnat läslistan

    @story1
    Scenario: Katalogen visar alla böcker med titel och författare
      When jag trycker på katalog
      Then ska en lista med böcker visas

    @story2
    Scenario: favoritmarkera en bok
      When jag trycker på hjärtat vid en bok
      Then ska boken vara favoritmarkerad

    @story3
    Scenario: Ta bort favoritmarkering
      Given att jag favoritmarkerat en bok
      When Jag trycker på hjärtat igen
      Then ska boken inte längre vara favoritmarkerad