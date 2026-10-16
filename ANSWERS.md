# Teorifrågor
### Dessutom ska du svara kortfattat på följande frågor i ANSWERS.md för att demonstrera dina kunskaper.
1. Vad är skillnaden mellan enhetstest, integrationstest, regressionstest och prestandatest?
- Svar: ``Enhetstest`` är en form av testning som fokuserar på funktioner i en isolerad miljö där den ej påverkas eller påverkar andra funktioner. Förlitar sig funktionen på en annan tex klass eller dylik använder man sig oftast av mocking för att härma den klassen / funktionen som den förlitar sig på.
``integrationstest`` då rör vi oss från att testa isolerade klasser och funktioner till att testa deras samspel. Nu testar man istället att klassen / funktionen faktiskt fungerar i samspel med andra redan implementerade klasser och funktioner.
``Regressionstest`` är ett testscenario som oftast gör kontinuerligt under projektets gång men målet med testningen är att testa så att tidigare funktioner fortfarande fungerar som det ska, eventuellt så gör man till och med tester som fokuserar på tidigare fel och då testar man så att felet ej återkommit med ny kodimplementering.
``Prestandatest`` här är målet med att testa prestandan på produkten. Här fokuserar testarna på att se till att produkten klarar av att driva sina funktioner utan att svarstiden är för lång, man simulerar olika typer av scenarios som skulle kunna ske i verkligeheten så som massivtflöde av användare, men det är också en naturlig del för att testa att saker och ting generellt fungerar utan noterbara förseningar under förväntade men även oväntade situationer.

1. Beskriv hur det går till när man arbetar med TDD.
- Svar: Med test driven development så använder man sig av red green refactor metoden. Man utgår från user stories och acceptanskriterier när man börjar utforma tester som skall testa de funktioner produkten skall ha, dessa kallar man för testscenarios. Alla testscenarios kommer först att bli röda alltså "Faila" och det är därefter man måste skriva kod till dessa funktioner, detta gör man tills att testen blir gröna. När testen blivit gröna kan man omfaktorisera koden för att optimera den.

1. Beskriv hur BDD skiljer sig från TDD.
- Svar: BDD använder verktyget Behave, som använder språket Gherkin för att beskriva hur en funktion förväntas fungera när en användare använder den. Gherkin är ett mer vardagligt språk som gör testerna enklare att förstå för både testare och utvecklare. BDD fokuserar på att beskriva systemets förväntade beteende ur användarens perspektiv, medan TDD fokuserar på att skriva tester före koden för att styra utvecklingen av funktionaliteten.

1. Tänk dig att du skulle göra en webbsida som liknar Läslistan, både frontend och backend. Om du fick välja förutsättningslöst, vilka sorters tester skulle du vilja använda? Motivera ditt val.
- Svar: Jag skulle använda mig av fler olika typer av tester för att säkerställa att både frontend och backend funger som de ska.
- ``Enhetstester`` skulle jag använda för att säkerställa att individuella funktioner på hemsidan fungerar som de ska tex, att lägga till eller ta bort böcker från läslistan.
- ``Integrationstester`` skulle jag använda för att testa så att backend funktioner samspelar som förväntat tex, att en bok kan sparas och sedan hämtas från databasen.
- ``BDD / E2E`` tester skulle jag använda för att hela användarflödet tex, att användaren lägger till en bok och att den visas korrekt på sidan.
- ``Regressionstester`` skulle användas för att kontrollera att befintlig funtkionalitet fungerar som de ska efter att ny kod implementerats. 
- ``Prestandstester`` Skulle jag använda för att testa sidans svarstid, hur många användare den kan klara av men även hur den klarar av samt hur sidan påverkas av att få större mängder böcker tillagda.

