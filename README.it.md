<div align="center">

# Mihaela Aghirculesei

### 🌐 Language / Sprache
[![Deutsch](https://img.shields.io/badge/Sprache-Deutsch-red?style=for-the-badge)](README.md)
[![English](https://img.shields.io/badge/language-English-blue?style=for-the-badge)](README.en.md)
[![Italiano](https://img.shields.io/badge/lingua-Italiano-green?style=for-the-badge)](README.it.md)

**Sviluppatrice Fullstack** — Python / FastAPI · PostgreSQL · Angular · Vue/Nuxt · TypeScript

[![Disponibile per nuovi progetti](https://img.shields.io/badge/Disponibile_per_nuovi_progetti-1a7f37?style=for-the-badge)](mailto:aghirculesei@gmail.com)
[![Sede](https://img.shields.io/badge/Wolfsburg_·_Remote_(UE)-30363d?style=for-the-badge)](#-disponibilità)

[![Typing SVG](https://readme-typing-svg.demolab.com?font=Fira+Code&size=24&duration=3000&pause=1000&color=2196F3&center=true&vCenter=true&width=650&lines=Sviluppatrice+Fullstack;Backend+con+FastAPI+e+PostgreSQL;Frontend+con+Angular%2C+Vue+e+Nuxt;Accessibilit%C3%A0+e+quality+gate+CI)](https://github.com/MihaelaAghirculesei)

<img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=6,11,20&height=100&section=header"/>

[![Portfolio](https://img.shields.io/badge/Portfolio-FF5722?style=flat-square&logo=google-chrome&logoColor=white)](https://aghirculesei.de/)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=flat-square&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/mihaela-aghirculesei-84147a23b/)
[![E-mail](https://img.shields.io/badge/E--mail-D14836?style=flat-square&logo=gmail&logoColor=white)](mailto:aghirculesei@gmail.com)
![Visitatori](https://visitor-badge.laobi.icu/badge?page_id=MihaelaAghirculesei)

</div>

---

## 👩‍💻 Chi sono

Sviluppatrice software con laurea triennale in Scienze economiche (Informatica per l'economia) e una qualifica certificata AZAV. Realizzo applicazioni web end-to-end: **backend con Python/FastAPI, PostgreSQL e Redis** e **frontend con Angular & TypeScript** (anche Next.js / React e Vue / Nuxt) – inclusi test, CI/CD e monitoring. Diverse applicazioni sono in produzione – tra cui un sito per un cliente che ho realizzato dall'architettura al deployment, in autonomia.

In precedenza, diversi anni di **coordinamento di progetto** in ambito automotive e IT: gestione dei requisiti, Jira/DMS, processi di rilascio e moderazione di riunioni di allineamento con fino a 150 partecipanti. Porto in ogni team questa doppia prospettiva – realizzazione **e** coordinamento.

- 🌍 Wolfsburg, Germania · disponibile al lavoro da remoto nell'UE
- 🇪🇺 Cittadinanza UE (Romania & Italia) – nessun permesso di lavoro o sponsorizzazione necessari
- 🗣️ Rumeno & Italiano (madrelingua) · Tedesco fluente · Inglese B1 (lettura/scrittura)
- ♿ Focus su accessibilità (WCAG 2.1 AA / BFSG) e controllo qualità automatizzato
- 🤝 Contributo open source: [MapLibre GL JS](https://github.com/maplibre/maplibre-gl-js) – nota nella documentazione per i framework SSR basati su Vite (Nuxt, SvelteKit, Astro), [PR #8766](https://github.com/maplibre/maplibre-gl-js/pull/8766) mergiata

```typescript
const mihaela = {
  role: "Sviluppatrice Fullstack",
  location: "Wolfsburg, DE · Remote (UE)",
  languages: ["TypeScript", "JavaScript", "Python", "HTML", "CSS"],
  backend:  ["FastAPI", "SQLAlchemy 2.0 (async)", "Alembic", "Pydantic", "PostgreSQL / pgvector", "Redis", "WebSocket", "Stripe", "Firebase / Firestore"],
  frontend: ["Angular 17–22", "RxJS", "NgRx", "Signals", "React 18/19", "Next.js", "Vue 3 / Nuxt", "Tailwind CSS", "PWA"],
  quality:  ["Vitest", "Playwright", "Cypress", "Pytest", "axe-core"],
  ops:      ["Docker", "GitHub Actions CI/CD", "OpenTelemetry", "Prometheus / Grafana", "Sentry"],
  focus:    "Backend FastAPI robusti, frontend Angular e Nuxt manutenibili, accessibilità",
};
```

---

## 📊 Statistiche GitHub

<div align="center">

<img src="https://github-readme-stats-iota-gray-47.vercel.app/api?username=MihaelaAghirculesei&show_icons=true&theme=radical&hide_border=true&count_private=true&card_width=250" width="500"/>

<img src="https://github-readme-streak-stats-blush-zeta.vercel.app/?user=MihaelaAghirculesei&theme=radical&hide_border=true" width="500"/>

### Grafico di attività

<picture>
  <source media="(max-width: 600px)" srcset="imgs/year-activity-mobile.png">
  <img src="imgs/year-activity.png" width="100%"/>
</picture>

### Linguaggi più utilizzati

<img src="https://github-readme-stats-iota-gray-47.vercel.app/api/top-langs/?username=MihaelaAghirculesei&layout=compact&theme=radical&hide_border=true&count_private=true&langs_count=8" width="500"/>

</div>

---

## 🎨 Progetti in Evidenza

### 📸 [Alina Moments Photography](https://alina-moments-photography.vercel.app) · Progetto cliente
Sito portfolio pronto per la produzione per una fotografa – realizzato in autonomia dall'architettura al deployment live (oltre 400 commit, oltre 100 pull request mergiate).

- **Qualità:** copertura test ≥95% (Codecov), Lighthouse ≥95 (Accessibility), ≥90 (SEO), CLS ≤ 0,1 – garantita da gate CI bloccanti su ogni pull request
- **Sicurezza:** CSP basata su nonce per ogni richiesta, rate limiting atomico, autenticazione HMAC stateless per la moderazione delle recensioni, HSTS
- **Accessibilità:** WCAG 2.1 AA – navigazione da tastiera completa, focus trap, audit axe-core automatizzati

**Tech:** Next.js 16 (App Router, RSC) • React 19 • TypeScript • Tailwind CSS 4 • PostgreSQL (Neon) • Drizzle ORM • Vercel

<details>
<summary><b>Screenshot, CI/CD e internazionalizzazione</b></summary>
<br/>

<img src="imgs/alina-moments.png" width="800" alt="Screenshot: Alina Moments Photography"/>

- **CI/CD:** pipeline GitHub Actions completa con lint, type-check, test unit/E2E, gate di coverage, budget dimensione bundle (≤500 KB) e audit Lighthouse automatizzato
- **Internazionalizzazione:** 4 lingue (DE/EN/RO/IT) con next-intl, routing localizzato, SEO multilingua

</details>

<div align="center">
<img src="https://capsule-render.vercel.app/api?type=soft&color=gradient&customColorList=6,11,20&height=10&width=1200" width="100%"/>
</div>

### 🍽️ dineos · Sistema di ordinazione in tempo reale per la ristorazione ![In Sviluppo](https://img.shields.io/badge/🚧_In_Sviluppo-FFC107?style=flat-square)
Un sistema operativo per ristoranti realizzato in autonomia end-to-end – backend, frontend, infrastruttura e pipeline di deploy. Gli ospiti ordinano e pagano da un QR code al tavolo, la cucina vede i nuovi ordini all'istante via WebSocket, i manager gestiscono tavoli, personale e menu da una dashboard.

- **Tempo reale:** fan-out WebSocket tramite Redis Pub/Sub (multi-istanza), limiti di connessione per IP, heartbeat per chiudere le connessioni morte
- **Sicurezza:** JWT con refresh token e revoca, 4 ruoli, rate limiting – in una security review interna ho trovato una fuga di dati tra tenant, corretta e blindata con test di regressione
- **Qualità:** 376 test backend (pytest su PostgreSQL + Redis reali in CI), `mypy --strict`, Ruff, gate di coverage, 6 architecture decision record

**Tech:** Python • FastAPI • SQLAlchemy 2.0 (async) • Alembic • PostgreSQL • Redis • WebSocket • Stripe • Docker • OpenTelemetry • Prometheus • Grafana • Angular 21 • NgRx

🔒 Repository privato (prodotto commerciale) · Walkthrough del codice su richiesta

<details>
<summary><b>Architettura, pagamenti e operatività</b></summary>
<br/>

- **Architettura:** backend FastAPI asincrono a strati Router → Service → Repository, SQLAlchemy 2.0 + asyncpg, 11 migrazioni Alembic, isolamento multi-tenant per `restaurant_id`
- **Pagamenti:** Stripe PaymentIntents con chiavi di idempotenza, dead-letter queue per i webhook falliti con retry/backoff (atomica via script Lua), audit log
- **Operatività:** Docker, CD in due fasi (deploy automatico su staging → promozione in produzione con smoke test e rollback), tracce OpenTelemetry, Prometheus + Grafana, Sentry, load test con k6

</details>

<div align="center">
<img src="https://capsule-render.vercel.app/api?type=soft&color=gradient&customColorList=6,11,20&height=10&width=1200" width="100%"/>
</div>

### 📦 [bfsg-scanner](https://www.npmjs.com/package/bfsg-scanner) · Pacchetto npm open-source
CLI che analizza un intero sito web per violazioni WCAG 2.1 AA e mappa ogni riscontro alla clausola EN 301 549 / BFSG che infrange – producendo un report di conformità citabile in JSON/HTML/PDF. Costruito con una serie di pull request piccole, revisionate singolarmente; le decisioni architetturali chiave documentate ciascuna in un architecture decision record.

🌐 **Report di esempio live:** [mihaelaaghirculesei.github.io/bfsg-scanner](https://mihaelaaghirculesei.github.io/bfsg-scanner/)

- **Supply chain:** pubblicato su npm con SLSA build provenance; il workflow di release pubblica tramite OIDC trusted publishing – nessun token a lunga durata
- **CI gate:** esce con codice ≠ 0 oltre una soglia di severità configurabile, così una pipeline può bloccare il merge sull'accessibilità
- **Qualità:** 167 test, CI su Linux/Windows/macOS, JSON Schema versionato per l'output del report, exit code semantici

**Tech:** TypeScript • Node.js 22+ • Playwright • axe-core • Zod • Vitest • Biome • GitHub Actions

<details>
<summary><b>Screenshot ed engine</b></summary>
<br/>

<img src="imgs/bfsg-scanner.png" width="800" alt="Screenshot: bfsg-scanner"/>

- **Engine:** crawl breadth-first che rispetta sitemap e robots.txt, pool di concorrenza con rate limit per host, Chromium reale via Playwright + axe-core

</details>

<div align="center">
<img src="https://capsule-render.vercel.app/api?type=soft&color=gradient&customColorList=6,11,20&height=10&width=1200" width="100%"/>
</div>

### Altri progetti

| Progetto | In evidenza | Stack |
|:--|:--|:--|
| 📚 **[normeon](https://github.com/MihaelaAghirculesei/normeon-german-technical-rag)** 🚧<br/><sub>RAG per documentazione tecnica tedesca</sub> | Ricerca ibrida (pgvector + full-text search tedesca, Reciprocal Rank Fusion) con reranking cross-encoder, validazione delle citazioni invece di allucinazioni, eval set di 50 domande, 356 test | Python • FastAPI • pgvector |
| ⚡ **[ChargeHub](https://github.com/MihaelaAghirculesei/ChargeHub)** · [Demo](https://charge-hub-one.vercel.app/de)<br/><sub>Dashboard per infrastruttura di ricarica EV</sub> | BFF Nitro davanti all'API di Open Charge Map, ricerca a testo libero via LLM con structured output, gate di coverage ~92%, axe-core come gate CI bloccante | Nuxt 4 • Vue 3 • TypeScript |
| 🎂 **[Birthday Reminder Pro](https://birthday-reminder-aghirculesei.pages.dev/)**<br/><sub>App offline-first per web e Android</sub> | Oltre 1.200 commit, oltre 2.000 unit test e oltre 100 test E2E, sincronizzazione bidirezionale con Google Calendar, notifiche native Android | Angular 22 • NgRx • Capacitor • Firebase |
| 📅 **[Intelligent Family Calendar](https://github.com/MihaelaAghirculesei/intelligent-family-calendar)** · [Demo](https://mihaelaaghirculesei.github.io/intelligent-family-calendar/)<br/><sub>Planner settimanale per famiglie</sub> | Angular 17 → 22 con un commit per ogni versione major, zoneless, 125 test E2E Playwright su Chromium, Firefox e WebKit, WCAG 2.2 AA | Angular 22 • Angular CDK • Playwright |
| 🔒 **[SecureNotes Lab](https://github.com/MihaelaAghirculesei/secure-notes-lab)**<br/><sub>Vetrina di sicurezza</sub> | Costruita due volte: 4 vulnerabilità OWASP Top 10:2025 più CSRF introdotte, documentate e corrette, fix dimostrati da test di regressione | Python • Flask • Bandit |
| 🐍 **[Todo API](https://github.com/MihaelaAghirculesei/todo-api)** · [Live](https://todo-frontend-aghirculesei.onrender.com)<br/><sub>Progetto in team (2 sviluppatori)</sub> | Il mio contributo: l'intero backend – Router → Service → Repository, 25/25 test, API progettata perché il frontend React potesse nascere in autonomia | FastAPI • SQLAlchemy 2.1 |

*Progetti formativi (qualificazione certificata AZAV, Developer Akademie):*

| Progetto | In evidenza | Stack |
|:--|:--|:--|
| 💡 **[Pokédex](https://pokedex-aghirculesei.pages.dev/)** | PWA offline-first, 242 unit test e 21 test E2E al 100% di coverage, Lighthouse CI | TypeScript • Vite • Vitest |
| 🔥 **[Join Kanban Board](https://join-aghirculesei.pages.dev/)**<br/><sub>Progetto in team (5 sviluppatori)</sub> | Fork portato avanti da sola: Angular 17 → 22, 17 test sull'emulatore per le regole Firestore, CodeQL, npm audit da 97 a 0 segnalazioni | Angular 22 • Firebase |
| 🚀 **[El Pollo Loco](https://el-pollo-loco-aghirculesei.pages.dev/)** | Jump-and-run 2D senza framework di gioco: 20 classi orientate agli oggetti, rilevamento collisioni pixel-perfect, ~60 FPS | HTML5 Canvas • JavaScript |

<details>
<summary><b>📸 Guarda gli screenshot</b></summary>
<br/>

<table>
  <tr>
    <td width="50%" align="center"><a href="https://charge-hub-one.vercel.app/de"><img src="imgs/chargehub.png" alt="Screenshot: ChargeHub"/></a><br/><sub>ChargeHub</sub></td>
    <td width="50%" align="center"><a href="https://birthday-reminder-aghirculesei.pages.dev/"><img src="imgs/birthday-memories.png" alt="Screenshot: Birthday Reminder Pro"/></a><br/><sub>Birthday Reminder Pro</sub></td>
  </tr>
  <tr>
    <td width="50%" align="center"><a href="https://mihaelaaghirculesei.github.io/intelligent-family-calendar/"><img src="imgs/intelligent-family-calendar.png" alt="Screenshot: Intelligent Family Calendar"/></a><br/><sub>Intelligent Family Calendar</sub></td>
    <td width="50%" align="center"><a href="https://github.com/MihaelaAghirculesei/secure-notes-lab"><img src="imgs/secure-notes-lab.png" alt="Screenshot: SecureNotes Lab"/></a><br/><sub>SecureNotes Lab</sub></td>
  </tr>
  <tr>
    <td width="50%" align="center"><a href="https://todo-frontend-aghirculesei.onrender.com"><img src="imgs/todo-api.png" alt="Screenshot: Todo API"/></a><br/><sub>Todo API</sub></td>
    <td width="50%" align="center"><a href="https://pokedex-aghirculesei.pages.dev/"><img src="imgs/pokedex.png" alt="Screenshot: Pokédex"/></a><br/><sub>Pokédex</sub></td>
  </tr>
  <tr>
    <td width="50%" align="center"><a href="https://join-aghirculesei.pages.dev/"><img src="imgs/join-board.png" alt="Screenshot: Join Kanban Board"/></a><br/><sub>Join Kanban Board</sub></td>
    <td width="50%" align="center"><a href="https://el-pollo-loco-aghirculesei.pages.dev/"><img src="imgs/el-pollo-loco.png" alt="Screenshot: El Pollo Loco"/></a><br/><sub>El Pollo Loco</sub></td>
  </tr>
</table>

</details>

---

## 🛠️ Stack tecnologico

**Linguaggi**

![TypeScript](https://img.shields.io/badge/TypeScript-007ACC?style=flat-square&logo=typescript&logoColor=white)
![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=flat-square&logo=javascript&logoColor=black)
![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white)
![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=flat-square&logo=html5&logoColor=white)
![CSS3](https://img.shields.io/badge/CSS3-1572B6?style=flat-square&logo=css3&logoColor=white)
![SASS](https://img.shields.io/badge/SASS-CC6699?style=flat-square&logo=sass&logoColor=white)

**Frontend**

![Angular](https://img.shields.io/badge/Angular-DD0031?style=flat-square&logo=angular&logoColor=white)
![Angular SSR](https://img.shields.io/badge/Angular_SSR-DD0031?style=flat-square&logo=angular&logoColor=white)
![RxJS](https://img.shields.io/badge/RxJS-B7178C?style=flat-square&logo=reactivex&logoColor=white)
![NgRx](https://img.shields.io/badge/NgRx-BA2BD2?style=flat-square&logo=reactivex&logoColor=white)
![React](https://img.shields.io/badge/React-61DAFB?style=flat-square&logo=react&logoColor=black)
![Next.js](https://img.shields.io/badge/Next.js-000000?style=flat-square&logo=nextdotjs&logoColor=white)
![Vue.js](https://img.shields.io/badge/Vue.js-4FC08D?style=flat-square&logo=vuedotjs&logoColor=white)
![Nuxt](https://img.shields.io/badge/Nuxt-00DC82?style=flat-square&logo=nuxtdotjs&logoColor=white)
![Tailwind CSS](https://img.shields.io/badge/Tailwind_CSS-06B6D4?style=flat-square&logo=tailwindcss&logoColor=white)
![Material Design](https://img.shields.io/badge/Material_Design-757575?style=flat-square&logo=material-design&logoColor=white)

**Mobile & PWA**

![Capacitor](https://img.shields.io/badge/Capacitor-119EFF?style=flat-square&logo=capacitor&logoColor=white)
![PWA](https://img.shields.io/badge/PWA-5A0FC8?style=flat-square&logo=pwa&logoColor=white)
![Workbox](https://img.shields.io/badge/Workbox-FF6D00?style=flat-square)

**Backend & Dati**

![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=flat-square&logo=fastapi&logoColor=white)
![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-D71F00?style=flat-square&logo=sqlalchemy&logoColor=white)
![Pydantic](https://img.shields.io/badge/Pydantic_2-E92063?style=flat-square&logo=pydantic&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-4169E1?style=flat-square&logo=postgresql&logoColor=white)
![SQLite](https://img.shields.io/badge/SQLite-003B57?style=flat-square&logo=sqlite&logoColor=white)
![Firebase](https://img.shields.io/badge/Firebase-FFCA28?style=flat-square&logo=firebase&logoColor=black)
![Drizzle ORM](https://img.shields.io/badge/Drizzle_ORM-C5F74F?style=flat-square&logo=drizzle&logoColor=black)
![IndexedDB](https://img.shields.io/badge/IndexedDB-003B57?style=flat-square)
![REST API](https://img.shields.io/badge/REST_API-0052CC?style=flat-square)
![WebSocket](https://img.shields.io/badge/WebSocket-010101?style=flat-square)
![Redis](https://img.shields.io/badge/Redis-DC382D?style=flat-square&logo=redis&logoColor=white)

**Testing & Qualità**

![Vitest](https://img.shields.io/badge/Vitest-6E9F18?style=flat-square&logo=vitest&logoColor=white)
![Playwright](https://img.shields.io/badge/Playwright-45ba4b?style=flat-square&logo=playwright&logoColor=white)
![Cypress](https://img.shields.io/badge/Cypress-17202C?style=flat-square&logo=cypress&logoColor=white)
![Jasmine](https://img.shields.io/badge/Jasmine-8A4182?style=flat-square&logo=jasmine&logoColor=white)
![Karma](https://img.shields.io/badge/Karma-56C2E6?style=flat-square)
![Pytest](https://img.shields.io/badge/Pytest-0A9EDC?style=flat-square&logo=pytest&logoColor=white)
![axe-core](https://img.shields.io/badge/axe--core-6633CC?style=flat-square)
![WCAG 2.1 AA](https://img.shields.io/badge/WCAG_2.1_AA-005A9C?style=flat-square)

**Strumenti & Infrastruttura**

![Git](https://img.shields.io/badge/Git-F05032?style=flat-square&logo=git&logoColor=white)
![GitHub Actions](https://img.shields.io/badge/GitHub_Actions-2088FF?style=flat-square&logo=githubactions&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-2496ED?style=flat-square&logo=docker&logoColor=white)
![OpenTelemetry](https://img.shields.io/badge/OpenTelemetry-000000?style=flat-square&logo=opentelemetry&logoColor=white)
![Prometheus](https://img.shields.io/badge/Prometheus-E6522C?style=flat-square&logo=prometheus&logoColor=white)
![Grafana](https://img.shields.io/badge/Grafana-F46800?style=flat-square&logo=grafana&logoColor=white)
![Vercel](https://img.shields.io/badge/Vercel-000000?style=flat-square&logo=vercel&logoColor=white)
![npm](https://img.shields.io/badge/npm-CB3837?style=flat-square&logo=npm&logoColor=white)
![VS Code](https://img.shields.io/badge/VS_Code-007ACC?style=flat-square&logo=visual-studio-code&logoColor=white)
![Figma](https://img.shields.io/badge/Figma-F24E1E?style=flat-square&logo=figma&logoColor=white)
![Jira](https://img.shields.io/badge/Jira-0052CC?style=flat-square&logo=jira&logoColor=white)
![Scrum](https://img.shields.io/badge/Scrum-6DB33F?style=flat-square)
![Google Calendar API](https://img.shields.io/badge/Google_Calendar_API-4285F4?style=flat-square&logo=google-calendar&logoColor=white)
![Sentry](https://img.shields.io/badge/Sentry-362D59?style=flat-square&logo=sentry&logoColor=white)
![Zod](https://img.shields.io/badge/Zod-3E67B1?style=flat-square&logo=zod&logoColor=white)

---

## 💼 Percorso

**Sviluppo web & app freelance** — Libera professionista · da 10/2025
Sviluppo end-to-end di applicazioni web – dalla raccolta dei requisiti al deployment, con focus su sistemi di prenotazione appuntamenti e soluzioni di comunicazione automatizzate.

**Qualifica certificata AZAV come sviluppatrice software** — Developer Akademie GmbH · 10/2024 – 10/2025
18 moduli, oltre 12 progetti – diversi in team secondo SCRUM/Kanban. Focus: Angular, TypeScript, API REST, Firebase, automazione dei test, UI/UX (Figma).

**Coordinamento di progetto – Automotive & IT** — Ferchau Automotive, jSERVICE · 2023 – 2024
Gestione dei requisiti, controllo dei work package e delle scadenze in Jira/DMS, coordinamento dei processi di rilascio internazionali per i sistemi di assistenza alla guida, moderazione di riunioni di allineamento con fino a 150 partecipanti.

**Laurea triennale in Scienze economiche (Informatica per l'economia)** — Università George Bacovia, Bacău (RO)
Titolo originale: Economist licențiat, specializzazione Contabilitate și informatică de gestiune (Contabilità e informatica gestionale). Riconosciuto da KMK/ZAB come equivalente a una laurea triennale tedesca.

---

## 🌍 Disponibilità

- **Ruoli:** Sviluppatrice Fullstack (Python/FastAPI + Angular) · Sviluppatrice Backend (Python/FastAPI) · Sviluppatrice Frontend (Angular / TypeScript)
- **Sede:** Wolfsburg · da remoto nell'UE
- **Lingue:** Rumeno & Italiano (madrelingua) · Tedesco fluente (tutta l'esperienza professionale in tedesco) · Inglese B1 (lettura/scrittura), A2 (parlato)
- 🇪🇺 **Cittadinanza UE** (Romania & Italia) – pieno diritto di lavorare in Germania e in tutta l'UE, nessun visto, nessuna sponsorizzazione.

---

## 📫 Contatti

<div align="center">

[![Portfolio](https://img.shields.io/badge/🌐_Portfolio-aghirculesei.de-FF5722?style=for-the-badge)](https://aghirculesei.de/)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connettiti-0077B5?style=for-the-badge&logo=linkedin)](https://www.linkedin.com/in/mihaela-aghirculesei-84147a23b/)
[![E-mail](https://img.shields.io/badge/E--mail-Scrivimi-D14836?style=for-the-badge&logo=gmail)](mailto:aghirculesei@gmail.com)

<img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=6,11,20&height=100&section=footer"/>

</div>
