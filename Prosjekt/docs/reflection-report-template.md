# Refleksjonsrapport - Programmering med KI

## 1. Gruppeinformasjon

**Gruppenavn:** SG-Gruppe-2

**Gruppemedlemmer:**
- Soban Rajathurai – 200279 / soban.rajathurai@himolde.no
- Sharan Rajathurai – [250084/ sharan.rajathurai@himolde.no]
- [Gruppemedlem 3] – [Student-ID / E-post]

**Dato:** 16.11.2025

---

## 2. Utviklingsprosessen

### 2.1 Oversikt over prosjektet

Vi implementerte Supabase i prosjektet, men som en helt enkel og minimalistisk lagringsløsning uten autentisering. Integrasjonen bestod av en enkel results tabell hvor backend lagret sammendrag, flashcards og quiz direkte ved bruk av en service key.

---

### 2.2 Arbeidsmetodikk

Arbeidsmetodikken vår utviklet seg i takt med prosjektets kompleksitet og de utfordringene vi støtte på underveis. Vi begynte med en relativt enkel tilnærming der prompt engineering var hovedverktøyet for å samhandle med KI. I stedet for å fordele tradisjonelle roller i gruppen, valgte vi å jobbe tett sammen rundt en felles AI-assistent som skulle støtte oss i alle faser. Dette innebar at vi i fellesskap utarbeidet og finjusterte prompts, og at en person ofte delte skjerm i Teams for at alle skulle kunne følge med og komme med innspill i sanntid.

Denne metoden førte til at vi hele tiden var involvert i både design og utvikling, og at vi kunne lære av hverandres erfaringer med KI og koding. Vi erfarte raskt at det å formulere presise og effektive prompts var en utfordring i seg selv, og at det krevde kontinuerlig tilpasning og eksperimentering. For eksempel måtte vi ofte bryte ned komplekse oppgaver i mindre deler for å sikre at KI forstod og leverte ønsket output.

BMAD-metodikken ble introdusert som et konseptuelt rammeverk for å strukturere samarbeidet vårt. Vi opprettet en mappe i prosjektet med beskrivelser av teamroller som designer, developer, tester, scrummaster og brief, men vi implementerte ikke BMAD som et teknisk orkestreringssystem. I stedet brukte vi rollene som mentale modeller for hvordan vi skulle tenke rundt oppgavene, og for å sikre at alle aspekter av utviklingsprosessen ble ivaretatt. Developer-agenten fungerte som hovedrollen i selve kodeutviklingen, og vi tilpasset promptene våre slik at KI kunne spille denne rollen best mulig. De andre rollene ble brukt som referansepunkter for testing, design og prosjektstyring.

Vi opplevde at denne tilnærmingen ga en god balanse mellom struktur og fleksibilitet. Oppgavene ble fordelt dynamisk etter behov, og alle deltok i diskusjoner, testing og problemløsning. Samtidig var det krevende å holde oversikt over hvem som gjorde hva, særlig når KI genererte store mengder kode som vi måtte evaluere og tilpasse. Dette førte til at vi utviklet interne rutiner for logging og dokumentasjon, blant annet ved å føre en detaljert dev_log.md som dokumenterte beslutninger, feilrettinger og læringspunkter.

Vi erfarte også at KI fungerte som et aktivt verktøy i alle faser av prosjektet: planlegging, utvikling, debugging og dokumentasjon. Det var imidlertid avgjørende at vi som mennesker tok ansvar for kritisk vurdering av alt KI produserte, og at vi ikke stolte blindt på forslagene som ble generert.

Vi beholdt kun hovedpromptene som faktisk fungerte i prosjektet, og disse ble loggført fortløpende i vår dev_log.md. Dette var ikke et sett med planlagte BMAD-prompter, men heller praktiske prompts som utviklet seg organisk gjennom arbeid, testing, feilretting og iterasjoner i ChatGPT Desktop. Dev_log fungerte derfor som vår faktiske dokumentasjon på hva som ble brukt og hvilke endringer som ble gjort i løpet av utviklingen. Mens utvikling skjedde ved hjelp av planning promptsene som hovedsakelig kom fra developer.md. Dette ga en mer reell og transparent oversikt over hvordan KI ble brukt i prosjektet.

---

### 2.3 Teknologi og verktøy

Valget av teknologi og verktøy var basert på ønsket om å bygge en moderne, skalerbar applikasjon med fokus på AI-generert studieinnhold. Frontend ble utviklet med en enkel, men funksjonell arkitektur basert på HTML, CSS og JavaScript, for å sikre rask prototyping og enkel integrasjon med backend.

Backend ble implementert i Python med FastAPI og Uvicorn som ASGI-server. FastAPI ble valgt for sin gode dokumentasjon, hastighet og støtte for asynkrone operasjoner, noe som var viktig for å håndtere API-kall til Gemini og Supabase.

Supabase ble brukt som en svært enkel lagringsløsning. Vi implementerte kun en minimal integrasjon uten autentisering, der backend lagret resultater direkte i en results tabell ved hjelp av en service key. Denne løsningen gav oss fungerende datalagring uten behov for brukerpålogging eller avansert konfigurasjon.

For AI-funksjonaliteten brukte vi Google Gemini 2.5 Flash som språkmodell. Denne modellen ga oss gode resultater, men vi opplevde også flere begrensninger, spesielt når det gjaldt konsistens i språkvalg og format på generert JSON.

PyMuPDF ble brukt som PDF-parser for å hente ut tekst fra opplastede dokumenter. Vi erfarte at kvaliteten på parsing var avgjørende for videre behandling, og at vi måtte implementere flere lag med tekstsanitering for å sikre at dataene som ble sendt til Gemini var rene og konsistente.

I tillegg til disse teknologiene brukte vi verktøy som VS Code for kodeditor, ChatGPT Desktop for sanntids interaksjon med KI, Git og GitHub for versjonskontroll, og Teams for kommunikasjon og skjermdeling.

---

### 2.4 Utviklingsfaser

#### Fase 1: Planlegging

Planleggingsfasen var preget av omfattende diskusjoner om prosjektets omfang, teknologivalg og arkitektur. Vi brukte KI til å lage oversikter over nødvendige API-endepunkter og dataflyt, og til å generere forslag til datamodeller og filstruktur. Dette bidro til å skape en felles forståelse i gruppen, men vi erfarte også at KI sine forslag ofte måtte tilpasses for å passe vår konkrete kontekst og krav.

En av de største utfordringene i denne fasen var å definere klare grenser mellom kjernefunksjonalitet og optional features, spesielt knyttet til Supabase-integrasjon og backend-automatisering. Vi diskuterte også hvordan BMAD-metodikken kunne brukes som et rammeverk for samarbeid, men det var uklart hvordan vi skulle implementere dette teknisk. Vi valgte derfor å bruke BMAD som en mental modell og ikke som en teknisk plattform, noe som senere viste seg både som en styrke og en svakhet.

#### Fase 2: Utvikling

Utviklingsfasen startet med backend, der vi først implementerte /upload-endepunktet for å håndtere PDF-opplasting og tekstutvinning. Her støtte vi på flere tekniske utfordringer knyttet til filhåndtering, asynkron behandling og feilkontroll. Parsing av PDF viste seg å være vanskeligere enn forventet, spesielt med hensyn til å håndtere forskjellige PDF-formater og sikre korrekt tekstutvinning.

Deretter implementerte vi integrasjonen med Gemini, som skulle generere sammendrag, flashcards og quiz basert på teksten. Her støtte vi på betydelige utfordringer knyttet til formatet på svarene fra Gemini. Spesielt quiz-generering ga ofte ufullstendig eller feilformatert JSON, noe som førte til at applikasjonen brøt. Vi måtte derfor utvikle en robust saniteringsfunksjon som fjernet kodeblokker, identifiserte JSON via regex og forsøkte parsing med fallback-strategi. Denne prosessen var tidkrevende og krevde flere iterasjoner med KI for å forbedre promptene og parsing-logikken.

Frontend ble utviklet parallelt, med fokus på enkelhet og brukervennlighet. Vi bygde en arkitektur som kommuniserte med backend via fetch-kall, og implementerte funksjoner for å vise sammendrag, flashcards og quiz. Underveis oppsto det mange feil, blant annet knyttet til språkvalg, JSON-parsing og kommunikasjon med Supabase. Disse feilene krevde mye debugging, og vi benyttet KI aktivt for å identifisere og løse problemene. Vi erfarte at språkvalget ofte ble ignorert av modellen, som svarte på engelsk selv om norsk var valgt. Dette løste vi ved å innføre strengere prompts og eksplisitte parametere for språk både i API-kall og backend.

Supabase-integrasjonen var en av de mest krevende delene av prosjektet. Vi støtte på problemer knyttet til feil nøkler, DNS-feil i frontend og feil bruk av service keys. For å løse dette måtte vi teste miljøvariabler nøye, bruke REPL for å teste tilkoblinger og lage enkle datalagringsfunksjoner for å verifisere at alt fungerte. KI var nyttig i denne prosessen ved å gi oss korrekt pakke og kodeeksempler for Supabase i Python, men mye av feilsøkingen måtte vi gjøre manuelt.

Gjennom hele utviklingsfasen var det tydelig at prompt engineering var en kontinuerlig læringsprosess. Vi måtte stadig forbedre og tilpasse promptene for å få KI til å levere ønsket output. Vi erfarte også at det var krevende å holde oversikt over hva som var KI-generert kode og hva som var håndskrevet, noe som førte til behov for strengere dokumentasjon og testing.

---

## 3. Utfordringer og løsninger

### 3.1 Tekniske utfordringer


#### Utfordring 1: Quiz-generering brøt applikasjonen
En av de mest kritiske tekniske utfordringene vi møtte var knyttet til quiz-generering. Gemini-modellen returnerte ofte ufullstendig eller feilformatert JSON som applikasjonen ikke klarte å tolke riktig. Selve quiz-spørsmålene ble generert, og alternativer som A, B, C og D ble vist i frontend, men svarene ble aldri korrekte. Frontend viste ofte A A på alternativer og selve fasiten kom ut som undefined. Dette skapte store problemer for brukeropplevelsen fordi quizene så riktige ut, men fasiten manglet eller var feil.

Vi erfarte at modellen ofte inkluderte kodeblokker, ekstra tekst eller feilaktige tegn som gjorde parsing umulig. For å løse dette utviklet vi en saniteringsfunksjon som fjernet alle kodeblokker og annen irrelevant tekst. Vi brukte regex for å identifisere JSON-strukturen i svaret, og implementerte flere parsingforsøk med fallback-strategier dersom første parsing feilet.

Denne løsningen krevde flere iterasjoner med testing og forbedring, og vi brukte KI til å foreslå regex-mønstre og robust parsinglogikk. Til tross for dette var det krevende å sikre at alle mulige feilformaterte svar ble håndtert, og vi måtte legge inn omfattende feilhåndtering i frontend for å unngå krasj.

#### Utfordring 2: Språkvalg ble ignorert

Vi at Gemini ofte svarte på engelsk selv om norsk var valgt som språk i promptene og API-kallene. Dette skapte forvirring for brukerne og gjorde det vanskelig å bruke quiz og flashcards i norsk kontekst.

Problemstillingen viste seg å være todelt: dels at promptene ikke var tydelige nok på språkpreferanse, og dels at modellen til tider ignorerte instruksjoner om språk.

For å løse dette innførte vi strengere og mer eksplisitte prompts hvor vi gjentok språkvalget flere ganger. Vi la også inn eksplisitte parametere for språk i API-kallene og backend-logikken for å sikre at modellen fikk korrekt kontekst.

KI hjalp oss med å forstå hvorfor modellen kunne ignorere språkvalg, og foreslo bedre prompt-strukturer som inkluderte eksempler på ønsket språkbruk. Selv med dette var det fortsatt utfordringer med inkonsistens, noe som krevde manuell oppfølging i flere tilfeller.

#### Utfordring 3: Supabase lagret ikke data

Supabase-integrasjonen skapte flere utfordringer i starten fordi vi brukte feil nøkler og opplevde problemer med miljøvariabler. Etter testing løste vi dette ved å bruke en minimal integrasjon uten autentisering hvor backend kun brukte en service key. Vi opprettet en enkel results tabell i Supabase og backend lagret sammendrag, flashcards og quiz direkte. Denne modellen fungerte stabilt og gav oss en fungerende lagringsflyt uten kompleksitet.

---

### 3.2 Samarbeidsutfordringer

Samarbeidet i gruppen var i utgangspunktet godt, men vi støtte på flere utfordringer som påvirket arbeidsflyten.

En stor utfordring var å jobbe synkront når KI genererte store mengder kode. Det var vanskelig å følge med på hva som ble generert, hva som var riktig, og hva som måtte tilpasses. Dette førte til at vi ofte måtte stoppe opp og diskutere i detalj for å unngå misforståelser.

Det var også utfordrende å holde styr på hva som var KI-generert og hva som var håndskrevet. Vi utviklet en praksis med å kommentere kode og dokumentere endringer i dev_log.md, men det var tidkrevende og krevde disiplin.

Vi erfarte også at vi måtte lære oss å forklare problemer presist for å få nyttige svar fra KI. Dette krevde øvelse i prompt engineering, og det var lett å gjøre feil som førte til unødvendig tid brukt på å rette opp i misforståelser.

Kommunikasjon via Teams fungerte bra for skjermdeling og diskusjon, men det var tidkrevende å koordinere når flere jobbet på samme tid. Vi erfarte at mer strukturert bruk av BMAD kunne ha hjulpet oss å organisere samarbeidet bedre.

---

### 3.3 KI-spesifikke utfordringer

KI-modellen var ikke uten sine begrensninger. Vi opplevde at modellen var inkonsistent, og at svarene ofte var på feil språk eller blandet gamle og nye instruksjoner.

Promptene måtte stadig forbedres for å få bedre resultater, noe som krevde mye eksperimentering og testing. Noen ganger ga modellen direkte feil eller utdatert kode som ikke fungerte i vårt miljø.

Vi erfarte også at KI kunne gi forslag som så gode ut, men som ikke passet vår tekniske stack, for eksempel kode som krevde nyere Python-versjoner eller biblioteker som ikke var kompatible med vårt system.

Det var derfor avgjørende at vi tok ansvar for å kvalitetssikre alt KI produserte, og at vi ikke stolte blindt på forslagene. Dette krevde en kombinasjon av teknisk kunnskap, kritisk tenkning og tålmodighet.

---

## 4. Kritisk vurdering av KI sin påvirkning

### 4.0 Bruken av BMAD i prosjektet

BMAD-metodikken ble introdusert som en måte å strukturere samarbeidet på, men vi erfarte at det var krevende å implementere BMAD som et teknisk orkestreringssystem innenfor prosjektets tidsramme. Vi valgte derfor å bruke BMAD som et konseptuelt rammeverk, der rollene designer, developer, tester, scrummaster og brief fungerte som mentale modeller for hvordan vi skulle tenke rundt oppgaver og arbeidsflyt.

Denne tilnærmingen hadde både fordeler og ulemper. På den positive siden hjalp BMAD oss med å sikre at vi tok hensyn til alle aspekter av utviklingsprosessen, fra analyse og design til testing og styring. Rollen developer ble brukt aktivt til å styre promptene og kodeutviklingen, mens de andre rollene fungerte som referansepunkter for kvalitetssikring og prosjektledelse.

På den negative siden førte mangelen på teknisk implementering til at vi ikke fikk utnyttet BMADs fulle potensial som et orkestreringssystem. Dette resulterte i at samarbeidet noen ganger føltes ustrukturert, og at vi brukte mye tid på å koordinere manuelt. Vi erfarte at en mer teknisk implementering av BMAD kunne ha gitt bedre oversikt og kontroll, men dette var utenfor prosjektets omfang.

Vi lærte at BMAD som konsept er nyttig for å tenke helhetlig rundt utviklingsprosessen, men at det krever tid og ressurser å implementere det fullt ut i praksis.

### 4.1 Fordeler med KI-assistanse

Bruken av KI i prosjektet hadde flere klare fordeler. KI genererte store deler av koden raskere enn vi kunne gjort manuelt, noe som betydelig økte effektiviteten. Feilsøking gikk også raskere når vi fikk hjelp til å isolere problemer og foreslå løsninger.

KI bidro til læring ved å gi oss innsikt i FastAPI og JSON-validering på en praktisk måte. Vi forstod bedre hvordan prompts fungerer, og hvorfor tydelighet og presisjon er avgjørende for gode resultater.

Kvaliteten på løsningene ble forbedret gjennom KI, som foreslo strukturerte og velorganiserte løsninger som vi kanskje ikke ville kommet på selv. KI hjalp også med å forbedre sikkerhet, dataflyt og universell utforming, ved å foreslå beste praksis og standarder.

KI fungerte som en samarbeidspartner som kunne gi raske svar og forslag, noe som gjorde utviklingsprosessen mer fleksibel og dynamisk.

### 4.2 Begrensninger og ulemper

Samtidig hadde KI-assistanse sine begrensninger. Mange forslag fra KI fungerte ikke i praksis, og modellen ga ofte kode som ikke passet vårt miljø, for eksempel på grunn av forskjeller i Python-versjoner eller biblioteker.

Vi merket også at vi ble for avhengige av KI når noe ikke fungerte, og at vi noen ganger aksepterte løsninger uten å forstå dem fullt ut. Dette kunne føre til problemer senere i utviklingsprosessen.

KI løste problemer raskt, men gjorde oss mindre tilbøyelige til å eksperimentere selv. Det var en risiko for at vi mistet noe av kreativiteten og læringspotensialet ved å stole for mye på KI.

### 4.3 Sammenligning: Med og uten KI

Uten KI ville prosjektet tatt mye lengre tid, og flere oppgaver, som parsing av PDF og quiz-generering, ville vært svært krevende. Vi måtte sannsynligvis skrevet backend helt fra scratch, og løsningsdesignet ville vært annerledes og kanskje mindre effektivt.

Med KI fikk vi en komplett applikasjon, en dypere forståelse av FastAPI, bedre arkitektur og mer effektive prompts. KI ga oss også verdifull kunnskap om hvordan man kan bruke AI i utviklingsprosesser.

### 4.4 Samlet vurdering

KI var en klart positiv faktor i prosjektet, men krevde mye kontroll og kritisk tenkning. Den viktigste lærdommen var at KI er et verktøy, ikke en erstatning for menneskelig forståelse. Vi måtte kvalitetssikre alt som ble generert, og vi lærte hvordan vi kan bruke KI på en mer reflektert og ansvarlig måte.

---

## 5. Etiske implikasjoner

### 5.1 Ansvar og eierskap
Selv om KI genererte deler av koden, er det vi som står ansvarlige for kvaliteten. Vi lærte at man må validere alt KI produserer.

### 5.2 Transparens
Det er viktig å være åpen om hvor KI ble brukt, noe denne rapporten beskriver i detalj.

### 5.3 Påvirkning på læring
KI gjør utvikling lettere, men kan svekke læringen hvis man ikke forstår det KI genererer.

### 5.4 Arbeidsmarkedet
KI vil endre hvordan utviklere jobber, men menneskelig vurdering og validering vil være essensielt.

### 5.5 Datasikkerhet og personvern
Vi sendte ikke sensitiv informasjon til KI-tjenester. Vi diskuterte risikoene ved å bruke eksterne API-er.

---

## 6. Teknologiske implikasjoner

### 6.1 Kodekvalitet
KI-kode kan være vanskelig å vedlikeholde. Vi lærte viktigheten av å rydde opp i generert kode.

### 6.2 Standarder
KI følger ikke alltid beste praksis, så vi måtte validere alt som ble foreslått.

### 6.3 Fremtidig utvikling
KI vil være en integrert del av utviklingsprosessen i fremtiden. De som kan bruke KI effektivt, ligger et steg foran.

---

## 7. Konklusjon og læring

### 7.1 Viktigste lærdommer

Prosjektet ga oss mange viktige lærdommer og innsikter. For det første erfarte vi at prompt engineering er en ferdighet som må trenes kontinuerlig. Det er ikke nok å bare skrive en prompt; man må forstå hvordan KI tolker instruksjoner, og hvordan man kan strukturere spørsmål for å få best mulig respons.

Vi lærte også at KI er et kraftig verktøy, men at det må brukes kritisk og med forståelse for begrensningene. Parsing av KI-generert JSON viste seg å være en stor utfordring, og krevde både teknisk innsikt og kreativ problemløsning for å håndtere feilformatert eller ufullstendig data.

Utviklingsprosessen ble raskere og mer fleksibel med KI, spesielt når det gjaldt generering av kode og feilsøking. Samtidig måtte vi være nøye med å sikre at alt fungerte i vårt miljø, og at vi ikke tok snarveier som kunne føre til tekniske problemer senere.

Vi erfarte også at Supabase og FastAPI er gode teknologier, men at de krever forståelse for miljøvariabler, sikkerhet og autentisering. Feil i disse områdene kan føre til store problemer, som vi erfarte i prosjektet.

### 7.2 Hva vi ville gjort annerledes

Hvis vi skulle gjort prosjektet på nytt, ville vi startet med Supabase tidligere for å unngå tidkrevende problemer med nøkler og tilkobling. Vi ville også laget strengere og mer presise prompts fra starten av, for å redusere tid brukt på debugging og feilretting.

Vi ville dokumentert testene og feilene mer systematisk, for å lettere kunne spore hva som fungerte og hva som ikke gjorde det. Dette ville også gjort det enklere å lære av feilene.

Videre ville vi forsøkt å implementere BMAD mer teknisk for å få bedre struktur og kontroll på samarbeidet. Dette kunne ha redusert friksjon og forbedret arbeidsflyten.

### 7.3 Anbefalinger til andre studenter

Vi anbefaler andre studenter å ikke stole blindt på KI, men alltid teste og kvalitetssikre alt som genereres. Det er viktig å lage små og presise prompts, og å bruke KI som en samarbeidspartner og ikke som fasit.

Videre anbefaler vi å sette av tid til å forstå teknologiene man bruker, og å dokumentere prosessen grundig. Dette gjør det lettere å feilsøke og forbedre løsninger underveis.

### 7.4 Personlig refleksjon

**Soban Rajathurai:**  
Dette prosjektet lærte meg hvor mye KI kan bidra i en utviklingsprosess. Samtidig innså jeg at forståelse av systemer, API-er og datastrukturer fortsatt er helt nødvendig. Jeg lærte mer om FastAPI, Supabase, prompt engineering og debugging av KI-feil enn jeg forventet. Jeg ser nå hvordan KI kan brukes på en produktiv måte uten at det svekker læringen.

**Sharan Rajathurai:**  
Dette prosjektet ga meg en bedre forståelse av hvordan KI kan brukes som støtte i programmering, men også hvilke begrensninger som finnes. Jeg lærte hvor viktig det er å teste og validere alt som KI genererer, og at ting som ser riktig ut ikke alltid fungerer i praksis. Arbeidet med parsing av data, språkvalg og feilsøking viste at man må ha god struktur og tålmodighet. Jeg fikk også mer innsikt i hvordan backend og frontend samarbeider, og hvordan gode prompts kan forbedre både kodekvalitet og output fra modellen. Prosjektet gjorde meg tryggere på å bruke KI-verktøy på en kritisk og bevisst måte.

---

## 8. Vedlegg
- Skjermbilder av applikasjonen  
- Lenke til GitHub repository  
- Logger og prompts brukt i prosjektet  

---

**Ordantall:** Ca. 4400 ord
# Refleksjonsrapport – Programmering med KI

## 1. Gruppeinformasjon

**Gruppenavn:** AI Study Buddy Group  

**Gruppemedlemmer:**  
- Soban Rajathurai – 200279 / soban.rajathurai@himolde.no  
- [Gruppemedlem 2] – [Student-ID / E-post]  
- [Gruppemedlem 3] – [Student-ID / E-post]  

**Dato:** 16.11.2025  

---

## 2. Utviklingsprosessen

### 2.1 Oversikt over prosjektet

Prosjektet gikk ut på å utvikle en fungerende prototype for en studieassistent som kan generere sammendrag, flashcards og quiz fra opplastede dokumenter. Vi bygde løsningen med FastAPI som backend og HTML, CSS og JavaScript som frontend. Gemini var kjernen i KI-funksjonaliteten og produserte tekstlig innhold basert på opplastede PDF-filer.

Vi prioriterte kjernefunksjonene. Målet var å levere et stabilt produkt med:

- Sammendrag i flere språk  
- Flashcards  
- Quiz  
- Valg av språk  
- Valg av sammendragslengde  
- Markdown til HTML  
- Stabil kommunikasjon mellom backend og frontend

Supabase-integrasjon ble definert som valgfritt i revidert prosjektforslag, siden omfanget ble for stort. Vi valgte å fokusere på kjernen som faktisk kunne leveres innen tidsrammen.

---

### 2.2 Arbeidsmetodikk

Vi jobbet i fellesskap og brukte ChatGPT Desktop aktivt som en del av samarbeidet. Én person delte skjerm i Teams, og alle ga innspill på prompts og kode i sanntid. Dette gjorde prompt engineering til en sentral del av arbeidsflyten vår.

Vi brukte BMAD rollene kun som konseptuell struktur, ikke som et teknisk system. Det betyr at vi tenkte i roller som designer, developer, tester og scrummaster, men uten å bruke teknisk orkestrering. Rollen developer var den mest brukte og styrte mye av kodegenereringen.

Prompt engineering krevde mye testing. Vi måtte formulere presise prompts, og justere dem for å få riktig output. Vi erfarte fort at små endringer kunne gi helt andre resultater fra modellen.

Vi dokumenterte alle viktige funksjoner og problemer i dev_log.md. Vi beholdt kun hovedpromptene som faktisk fungerte i prosjektet. Loggen ble derfor et ekte historisk dokument over utviklingen og alle endringer som ble gjort.

Developer-rollen, slik vi hadde definert den i developer.md, ble en viktig rettesnor for hvordan vi samarbeidet med KI i praksis. Dokumentet beskrev hvordan backend skulle bygges opp, hvilke endepunkter som måtte utvikles, hvordan PDF parsing skulle fungere, og hvordan KI skulle integreres for å generere sammendrag, flashcards og quiz. Disse føringene ble ikke bare teoretiske; de ble brukt aktivt i prosjektet og styrte hvilke prompts vi utviklet og brukte videre. Promptene som er loggført i dev_log.md oppstod direkte fra behovene som developer.md beskrev. Det var derfor kun disse hovedpromptene som ble tatt med videre. De representerer de faktiske stegene vi brukte sammen med KI for å løse problemer og bygge funksjoner. Dette gjorde developer.md til et operativt veikart og et bindeledd mellom planlegging og praktisk utvikling.

---

### 2.3 Teknologi og verktøy

Backend ble laget med FastAPI og Uvicorn. FastAPI gav oss rask utvikling av endepunkter, god dokumentasjon og enkel testing via Swagger.

Frontend ble laget i ren HTML, CSS og JavaScript for å få rask og stabil prototyping uten kompleksitet.

PDF parsing ble gjort med PyMuPDF. Dette gav oss ren tekst som kunne sendes videre til KI.

Markdown til HTML ble gjort med python-biblioteket “markdown” slik at strukturerte sammendrag ble vist pent i nettleseren.

Gemini 2.5 Flash ble brukt som språkmodell via google genai klienten. Vi måtte migrere bort fra den gamle klienten etter at den ble avviklet.

Verktøy:
- VS Code som editor  
- Teams for møter og skjermdeling  
- Git og GitHub for versjonskontroll  
- ChatGPT Desktop for prompts og kode  

---

### 2.4 Utviklingsfaser

#### Fase 1 Planlegging

Vi startet med å kartlegge API-endepunkter, datamodeller og flyt. KI hjalp oss med struktur og forslag. Vi bestemte oss tidlig for å skille mellom kjernefunksjoner og valgfri funksjonalitet.

#### Fase 2 Backend og frontend integrasjon

Vi implementerte upload-endepunktet som tok imot PDF, hentet tekst og sendte det videre. Vi lagde flashcards-endepunktet. Vi testet alt i Swagger og fikk en fungerende grunnstruktur.

Under denne fasen brukte vi hovedpromptene som ble dokumentert i dev_log.md. Disse inkluderte blant annet backend-struktur, flashcard-generator, markdown til HTML, quiz-generator og multilingual prompts. Promptene ble ikke utviklet som en del av en forhåndsdefinert BMAD-prosess, men vokste naturlig ut av behov som oppstod i utviklingen. Developer.md fungerte som grunnlaget for dette arbeidet, og promptene ble utviklet etter hvert som nye problemer måtte løses. Dette ga oss en dynamisk og behovsdrevet arbeidsprosess som ble godt dokumentert i loggene våre.

Frontend ble laget parallelt, med seksjonene Upload, Results og Settings. Vi brukte fetch-kall for kommunikasjon.

Markdown ble konvertert til HTML for bedre brukeropplevelse.

#### Fase 3 KI-funksjonalitet og quiz

Dette var den vanskeligste fasen. Quiz-generering gav ofte feil JSON. Vi løste dette ved å lage en robust parser som:

- Fjernet kodeblokker  
- Fant JSON med regex  
- Prøvde parsing flere ganger  
- Håndterte feil uten at appen krasjet  

Språkvalg måtte forbedres. Gemini svarte på engelsk selv når norsk var valgt. Vi forbedret prompts og sendte språk eksplisitt som parameter.

Sammendragslengde ble gjort dynamisk. Vi laget logikk som endret prompten basert på valget kort, medium eller lang.

---

## 3. Utfordringer og løsninger

### 3.1 Tekniske utfordringer

**Quiz JSON feilet**  
Gemini returnerte ufullstendig og rotete JSON. Vi lagde en parser som fant og renset JSON uansett hvordan svaret kom.

**Språk ble ignorert**  
Modellen svarte ofte på engelsk. Vi løste dette gjennom sterkere prompts og tydelig parameterbruk.

**Markdown ble vist som ren tekst**  
Vi løste dette ved å konvertere til HTML i backend.

**Frontend og backend var ute av synk**  
Vi lagret brukerinnstillinger i localStorage og sendte dem med alle kall.

### 3.2 Samarbeidsutfordringer

KI genererte store mengder kode raskt. Det var krevende å følge med. Vi måtte stoppe ofte og diskutere. Det krevde god kommunikasjon og struktur.

Vi opplevde også at det var lett å miste oversikt over endringer. Derfor ble dev_log.md viktig.

### 3.3 KI-spesifikke utfordringer

KI leverte noen ganger kode som ikke var kompatibel. Den blandet sammen gamle og nye prompts. Den gav løsninger som så riktige ut, men som ikke fungerte. Dette lærte oss viktigheten av manuell kontroll.

---

## 4. Kritisk vurdering av KI sin innvirkning

### 4.1 Fordeler

- Hurtigere utvikling  
- Effektiv feilsøking  
- God læring i praksis  
- Bedre struktur på løsninger  
- Rask generering av kodeeksempler  

### 4.2 Begrensninger

- Ikke alltid korrekt kode  
- Inkonsekvent språk  
- Feil JSON  
- Må alltid dobbeltsjekkes  

### 4.3 Med og uten KI

Uten KI ville prosjektet tatt mye lenger tid. Parsing og quiz-logikk hadde vært krevende. Med KI fikk vi en fungerende prototype innen tidsrammen.

---

## 5. Etiske implikasjoner

- Vi må alltid kvalitetssikre KI-kode  
- Transparens om KI-bruk er viktig  
- Data må håndteres sikkert  
- KI må ikke redusere læringen  

---

## 6. Teknologiske implikasjoner

Ki påvirket kodekvaliteten. Koden krevde rydding. Vi lærte viktigheten av kontroll og testing. KI følger ikke alltid standarder, derfor må utviklere ha kompetanse til å evaluere alt KI produserer.

---

## 7. Konklusjon og læring

Vi lærte mye om FastAPI, JSON parsing, quiz-design, prompt engineering og frontend backend integrasjon. Vi erfarte at KI er et kraftig verktøy, men at det krever kritisk bruk.

Hvis vi skulle startet på nytt ville vi:

- Strukturert prompts tidligere  
- Testet full flyt tidligere  
- Dokumentert feil mer systematisk  

Vi er fornøyde med resultatet og hva vi lærte.

---

Ordantall ca 3300