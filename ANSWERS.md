# Testprojekt – Inlämningsuppgift

## Checklista

### 1. Projekt och GitHub
- [x] Skapa projektet enligt kursens instruktioner
- [x] Initiera Git
- [x] Ladda upp projektet till ett publikt GitHub-repository
- [x] Skapa `README.md`, `STORIES.md` och `ANSWERS.md` i projektets rotmapp

### 2. Backend och testning
- [ ] Implementera backend-kod med TDD
- [ ] Skriva enhetstester
- [ ] Skriva integrationstester
- [ ] Verifiera att testerna fungerar

### 3. User stories och BDD
- [ ] Dokumentera user stories för befintlig funktionalitet i `STORIES.md`
- [ ] Skapa feature-filer utifrån user stories
- [ ] Skapa step-filer för samtliga features
- [ ] Skapa page-filer vid behov

### 4. CI – GitHub Actions
- [ ] Konfigurera CI för projektet
- [ ] Köra samtliga tester automatiskt vid push till `main`
- [ ] Köra webbläsartester i headless-läge
- [ ] Kontrollera att GitHub Actions-workflowen fungerar

### 5. Dokumentation
- [x] Besvara teorifrågorna i `ANSWERS.md`
- [ ] Dokumentera vad som har testats i `README.md`
- [ ] Dokumentera hur projektet installeras och startas i `README.md`

### 6. Slutkontroll
- [ ] Alla filer finns i projektets rotmapp
- [ ] Alla tester körs utan fel
- [ ] Alla ändringar är committade och pushade till GitHub
- [ ] Repository är publikt
- [ ] Projektet är redo för inlämning

---

## Vad har testats?

**Enhetstester:**

Beskriv vilka enskilda funktioner eller klasser som testas.

**Integrationstester:**

Beskriv vilka delar av backend som testas tillsammans.

**BDD/E2E-tester:**

Beskriv vilka funktioner och användarflöden på webbsidan som testas.

**CI:**

Beskriv hur testerna körs automatiskt via GitHub Actions.

---

## Installera och starta projektet

Beskriv hur projektet installeras och startas, inklusive eventuella beroenden och konfiguration
# Teorifrågor
### Dessutom ska du svara kortfattat på följande frågor i ANSWERS.md för att demonstrera dina kunskaper.
1. Vad är skillnaden mellan enhetstest, integrationstest, regressionstest och prestandatest?
- Svar: ``Enhetstest`` är en form av testning som fokuserar på funktioner i en isolerad miljö där den ej påverkas eller påverkar andra funktioner. Förlitar sig funktionen på en annan tex klass eller dylik använder man sig oftast av mocking för att härma den klassen / funktionen som den förlitar sig på.
``integrationstest`` då rör vi oss från att testa isolerade klasser och funktioner till att testa deras samspel. Nu testar man istället att klassen / funktionen faktiskt fungerar i samspel med andra redan implementerade klasser och funktioner.
``Regressionstest`` är ett testscenario som oftast gör kontinuerligt under projektets gång men målet med testningen är att testa så att tidigare funktioner fortfarande fungerar som det ska, eventuellt så gör man till och med tester som fokuserar på tidigare fel och då testar man så att felet ej återkommit med ny kodimplementering.
``Prestandatest`` här är målet med att testa prestandan på produkten. Här fokuserar testarna på att se till att produkten klarar av att driva sina funktioner utan att svarstiden är för lång, man simulerar olika typer av scenarios som skulle kunna ske i verkligeheten så som massivtflöde av användare, men det är också en naturlig del för att testa att saker och ting generellt fungerar utan noterbara förseningar under förväntade men även oväntade situationer.

1. Beskriv hur det går till när man arbetar med TDD.
- Svar:

1. Beskriv hur BDD skiljer sig från TDD.
- Svar:

1. Tänk dig att du skulle göra en webbsida som liknar Läslistan, både frontend och backend. Om du fick välja förutsättningslöst, vilka sorters tester skulle du vilja använda? Motivera ditt val.
- Svar:

