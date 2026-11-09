<p align="right"><sub><b>Deutsch</b> · <a href="README.en.md">English</a> · <a href="README.it.md">Italiano</a></sub></p>

<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=6,11,20&height=90&section=header" width="100%" alt=""/>

# Mihaela Aghirculesei

### Fullstack-Entwicklerin · Python / FastAPI · Angular · TypeScript

Ich entwickle Web-Anwendungen end-to-end – vom asynchronen FastAPI-Backend bis zum barrierefreien Angular-Frontend, abgesichert durch Tests und CI-Qualitätsgates.

[![Portfolio](https://img.shields.io/badge/Portfolio-aghirculesei.de-FF5722?style=for-the-badge&logo=google-chrome&logoColor=white)](https://aghirculesei.de/)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Profil-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/mihaela-aghirculesei-84147a23b/)
[![E-Mail](https://img.shields.io/badge/E--Mail-Schreiben-D14836?style=for-the-badge&logo=gmail&logoColor=white)](mailto:aghirculesei@gmail.com)

🟢 **Offen für Festanstellung** · Wolfsburg · Remote (EU) · EU-Staatsangehörigkeit, kein Sponsoring nötig

<table>
  <tr>
    <td align="center" width="50%"><a href="https://alina-moments-photography.vercel.app"><b>Kundenprojekt live</b></a><br/><sub>eigenverantwortlich von der Architektur bis zum Deployment</sub></td>
    <td align="center" width="50%"><a href="https://www.npmjs.com/package/bfsg-scanner"><b>npm-Paket</b></a><br/><sub>veröffentlicht mit SLSA-Build-Provenance</sub></td>
  </tr>
  <tr>
    <td align="center" width="50%"><a href="https://github.com/maplibre/maplibre-gl-js/pull/8766"><b>Open Source</b></a><br/><sub>Beitrag zu MapLibre GL JS, gemergt</sub></td>
    <td align="center" width="50%"><a href="https://mihaelaaghirculesei.github.io/bfsg-scanner/"><b>Barrierefreiheit</b></a><br/><sub>WCAG 2.1 AA / BFSG als CI-Gate</sub></td>
  </tr>
</table>

</div>

---

## 👩‍💻 Über mich

Softwareentwicklerin mit Bachelor in Wirtschaftswissenschaften (Wirtschaftsinformatik) und AZAV-zertifizierter Qualifizierung. Ich entwickle Web-Anwendungen end-to-end: **Backends mit Python/FastAPI, PostgreSQL und Redis** und **Frontends mit Angular & TypeScript** (auch Next.js / React und Vue / Nuxt) – inklusive Tests, CI/CD und Monitoring. Mehrere Anwendungen laufen im Live-Betrieb – darunter eine Kundenwebsite, die ich eigenverantwortlich von der Architektur bis zum Deployment umgesetzt habe.

Davor **Projektkoordination** in Automotive- und IT-Entwicklungsprojekten: Anforderungsmanagement, Jira/DMS, Freigabeprozesse und Moderation von Abstimmungsrunden mit bis zu 150 Teilnehmenden. Diese Doppelperspektive – Umsetzung **und** Koordination – bringe ich in jedes Team ein.

- ♿ Schwerpunkt Barrierefreiheit (WCAG 2.1 AA / BFSG) und automatisierte Qualitätssicherung
- 🤝 Open-Source-Beitrag: [MapLibre GL JS](https://github.com/maplibre/maplibre-gl-js) – Doku-Hinweis für Vite-basierte SSR-Frameworks (Nuxt, SvelteKit, Astro), [PR #8766](https://github.com/maplibre/maplibre-gl-js/pull/8766) gemergt

---

## 🎨 Ausgewählte Projekte

### 🍽️ dineos · Echtzeit-Bestellsystem für die Gastronomie
Restaurant-Betriebssystem, allein end-to-end entwickelt – Backend, Frontend, Infrastruktur und Deploy-Pipeline. Gäste bestellen und bezahlen per QR-Code am Tisch, die Küche sieht neue Bestellungen sofort über WebSocket, Manager steuern Tische, Personal und Speisekarte über ein Dashboard.

- **Echtzeit:** WebSocket-Fan-out über Redis Pub/Sub (mehrere Instanzen), Verbindungslimits pro IP, Heartbeat für tote Verbindungen
- **Sicherheit:** JWT mit Refresh-Token und Revocation, 4 Rollen, Rate-Limiting – im eigenen Security-Review ein Cross-Tenant-Datenleck gefunden und mit Regressionstests geschlossen
- **Qualität:** über 380 Backend-Tests (pytest gegen echtes PostgreSQL + Redis in CI) und über 350 Frontend-Tests, `mypy --strict`, Ruff, Coverage-Gate, 7 Architecture Decision Records

**Tech:** Python • FastAPI • SQLAlchemy 2.0 (async) • Alembic • PostgreSQL • Redis • WebSocket • Stripe • Docker • OpenTelemetry • Prometheus • Grafana • Angular 21 • NgRx

🔒 Privates Repository (kommerzielles Produkt) · Code-Walkthrough auf Anfrage

<details>
<summary><b>Architektur, Zahlungen & Betrieb</b></summary>
<br/>

- **Architektur:** asynchrones FastAPI-Backend mit Schichten Router → Service → Repository, SQLAlchemy 2.0 + asyncpg, 11 Alembic-Migrationen, Multi-Tenant-Isolation per `restaurant_id`
- **Zahlungen:** Stripe PaymentIntents mit Idempotency-Keys, Dead-Letter-Queue für fehlgeschlagene Webhooks mit Retry/Backoff (atomar per Lua-Skript), Audit-Log
- **Betrieb:** Docker, zweistufiges CD (Staging automatisch → Produktion per Promotion mit Smoke-Test und Rollback), OpenTelemetry-Traces, Prometheus + Grafana, Sentry, Lasttests mit k6

</details>

<div align="center">
<img src="https://capsule-render.vercel.app/api?type=soft&color=gradient&customColorList=6,11,20&height=10&width=1200" width="100%" alt=""/>
</div>

### 📦 [bfsg-scanner](https://www.npmjs.com/package/bfsg-scanner) · Open-Source npm-Paket
Kommandozeilen-Tool, das eine komplette Website auf WCAG-2.1-AA-Verstöße prüft und jeden Fund der EN-301-549-/BFSG-Klausel zuordnet, gegen die er verstößt – als zitierfähigen Konformitätsbericht in JSON/HTML/PDF. Entwickelt in klein geschnittenen, einzeln reviewten Pull Requests; die zentralen Architekturentscheidungen jeweils mit einem Architecture Decision Record.

🌐 **Live-Beispielbericht:** [mihaelaaghirculesei.github.io/bfsg-scanner](https://mihaelaaghirculesei.github.io/bfsg-scanner/)

- **Supply-Chain:** auf npm veröffentlicht mit SLSA-Build-Provenance; der Release-Workflow publiziert über OIDC Trusted Publishing – keine langlebigen Tokens
- **CI-Gate:** Exit-Code ≠ 0 ab konfigurierbarer Schweregrad-Schwelle – so kann eine Pipeline den Merge auf Barrierefreiheit blockieren
- **Qualität:** 167 Tests, CI auf Linux/Windows/macOS, versioniertes JSON-Schema für die Bericht-Ausgabe, semantische Exit-Codes

**Tech:** TypeScript • Node.js 22+ • Playwright • axe-core • Zod • Vitest • Biome • GitHub Actions

<details>
<summary><b>Screenshot & Engine</b></summary>
<br/>

<img src="imgs/bfsg-scanner.png" width="800" alt="Screenshot: bfsg-scanner"/>

- **Engine:** Sitemap- + robots.txt-bewusster Breadth-First-Crawl, Concurrency-Pool mit Per-Host-Rate-Limit, echtes Chromium via Playwright + axe-core

</details>

<div align="center">
<img src="https://capsule-render.vercel.app/api?type=soft&color=gradient&customColorList=6,11,20&height=10&width=1200" width="100%" alt=""/>
</div>

### 📚 [normeon](https://github.com/MihaelaAghirculesei/normeon-german-technical-rag) · RAG für deutsche technische Dokumentation
RAG-Assistent für deutschsprachige technische Dokumentation (Lastenhefte, UNECE-Regelungen, Handbücher), der mit überprüfbaren Quellenzitaten antwortet – und sich lieber enthält, als zu halluzinieren.

🌐 **Live-Demo:** [normeon.onrender.com](https://normeon.onrender.com) – „Als Gast ansehen“ · Free Tier: der erste Aufruf kann bis zu einer Minute dauern

- **Retrieval:** hybride Suche aus Vektorsuche (pgvector, HNSW-Index), deutscher Volltextsuche und Trigramm-Fallback, fusioniert per Reciprocal Rank Fusion, danach Cross-Encoder-Reranking
- **Generierung:** Zitatvalidierung (erfundene Quellen werden verworfen), Konfidenz-Gate vor dem LLM-Aufruf, Streaming per SSE, Kosten- und Latenz-Logging pro Anfrage
- **Evaluation:** handgeschriebenes deutsches Eval-Set mit 50 Fragen, LLM-as-Judge kalibriert gegen menschliche Bewertung
- **Qualität:** über 700 Tests in CI (Backend mit Testcontainers, eigene Security-Suite, Frontend), austauschbare Adapter für Embeddings, LLM und Reranker; Angular-Frontend mit aus OpenAPI generierten Typen

**Tech:** Python • FastAPI • PostgreSQL + pgvector • Alembic • Docker • Pytest • Testcontainers • Angular 22 • Vitest

<div align="center">
<img src="https://capsule-render.vercel.app/api?type=soft&color=gradient&customColorList=6,11,20&height=10&width=1200" width="100%" alt=""/>
</div>

### Weitere Projekte

| Projekt | Highlights | Stack |
|:--|:--|:--|
| 📸 **[Alina Moments Photography](https://alina-moments-photography.vercel.app)** · Kundenprojekt<br/><sub>Portfolio-Website für eine Fotografin, live</sub> | Eigenverantwortlich von der Architektur bis zum Live-Deployment (über 400 Commits, über 100 gemergte PRs), ≥95 % Testabdeckung, Lighthouse ≥95 (Accessibility), Nonce-basierte CSP, 4 Sprachen | Next.js 16 • React 19 • PostgreSQL |
| ⚡ **[ChargeHub](https://github.com/MihaelaAghirculesei/ChargeHub)** · [Demo](https://charge-hub-one.vercel.app/de)<br/><sub>Dashboard für EV-Ladeinfrastruktur</sub> | Nitro-BFF vor der Open-Charge-Map-API, LLM-Freitextsuche mit Structured Output, Coverage-Gate ~92 %, axe-core als blockierendes CI-Gate | Nuxt 4 • Vue 3 • TypeScript |
| 🎂 **[Birthday Reminder Pro](https://birthday-reminder-aghirculesei.pages.dev/)**<br/><sub>Offline-First-App für Web und Android</sub> | Über 1.200 Commits, über 2.000 Unit- und über 100 E2E-Tests, bidirektionale Google-Calendar-Synchronisierung, native Android-Benachrichtigungen | Angular 22 • NgRx • Capacitor • Firebase |
| 📅 **[Intelligent Family Calendar](https://github.com/MihaelaAghirculesei/intelligent-family-calendar)** · [Demo](https://mihaelaaghirculesei.github.io/intelligent-family-calendar/)<br/><sub>Wochenplaner für Familien</sub> | Angular 17 → 22 mit einem Commit pro Major-Version, Zoneless, 125 Playwright-E2E-Tests auf Chromium, Firefox und WebKit, WCAG 2.2 AA | Angular 22 • Angular CDK • Playwright |
| 🔒 **[SecureNotes Lab](https://github.com/MihaelaAghirculesei/secure-notes-lab)**<br/><sub>Security-Showcase</sub> | Zweimal gebaut: 4 OWASP-Top-10:2025-Schwachstellen plus CSRF eingebaut, dokumentiert und behoben, Fixes mit Regressionstests bewiesen | Python • Flask • Bandit |
| 🐍 **[Todo API](https://github.com/MihaelaAghirculesei/todo-api)** · [Live](https://todo-frontend-aghirculesei.onrender.com)<br/><sub>Teamprojekt (2 Entwickler)</sub> | Mein Beitrag: das komplette Backend – Router → Service → Repository, 25/25 Tests, API so entworfen, dass das React-Frontend unabhängig entstehen konnte | FastAPI • SQLAlchemy 2.1 |

*Ausbildungsprojekte (AZAV-zertifizierte Qualifizierung, Developer Akademie):*

| Projekt | Highlights | Stack |
|:--|:--|:--|
| 💡 **[Pokédex](https://pokedex-aghirculesei.pages.dev/)** | Offline-First-PWA, 242 Unit- und 21 E2E-Tests bei 100 % Coverage, Lighthouse CI | TypeScript • Vite • Vitest |
| 🔥 **[Join Kanban Board](https://join-aghirculesei.pages.dev/)**<br/><sub>Teamprojekt (5 Entwickler)</sub> | Fork eigenständig weitergeführt: Angular 17 → 22, 17 Emulator-Tests für die Firestore-Regeln, CodeQL, npm audit von 97 auf 0 Befunde | Angular 22 • Firebase |
| 🚀 **[El Pollo Loco](https://el-pollo-loco-aghirculesei.pages.dev/)** | 2D-Jump-and-Run ohne Game-Framework: 20 objektorientierte Klassen, pixelgenaue Kollisionserkennung, ~60 FPS | HTML5 Canvas • JavaScript |

<details>
<summary><b>📸 Screenshots ansehen</b></summary>
<br/>

<table>
  <tr>
    <td width="33%" align="center" valign="top"><a href="https://alina-moments-photography.vercel.app"><img src="imgs/thumbs/alina-moments.jpg" alt="Screenshot: Alina Moments Photography"/></a><br/><sub>Alina Moments Photography</sub></td>
    <td width="33%" align="center" valign="top"><a href="https://charge-hub-one.vercel.app/de"><img src="imgs/thumbs/chargehub.jpg" alt="Screenshot: ChargeHub"/></a><br/><sub>ChargeHub</sub></td>
    <td width="33%" align="center" valign="top"><a href="https://birthday-reminder-aghirculesei.pages.dev/"><img src="imgs/thumbs/birthday-memories.jpg" alt="Screenshot: Birthday Reminder Pro"/></a><br/><sub>Birthday Reminder Pro</sub></td>
  </tr>
  <tr>
    <td width="33%" align="center" valign="top"><a href="https://mihaelaaghirculesei.github.io/intelligent-family-calendar/"><img src="imgs/thumbs/intelligent-family-calendar.jpg" alt="Screenshot: Intelligent Family Calendar"/></a><br/><sub>Intelligent Family Calendar</sub></td>
    <td width="33%" align="center" valign="top"><a href="https://github.com/MihaelaAghirculesei/secure-notes-lab"><img src="imgs/thumbs/secure-notes-lab.jpg" alt="Screenshot: SecureNotes Lab"/></a><br/><sub>SecureNotes Lab</sub></td>
    <td width="33%" align="center" valign="top"><a href="https://todo-frontend-aghirculesei.onrender.com"><img src="imgs/thumbs/todo-api.jpg" alt="Screenshot: Todo API"/></a><br/><sub>Todo API</sub></td>
  </tr>
  <tr>
    <td width="33%" align="center" valign="top"><a href="https://pokedex-aghirculesei.pages.dev/"><img src="imgs/thumbs/pokedex.jpg" alt="Screenshot: Pokédex"/></a><br/><sub>Pokédex</sub></td>
    <td width="33%" align="center" valign="top"><a href="https://join-aghirculesei.pages.dev/"><img src="imgs/thumbs/join-board.jpg" alt="Screenshot: Join Kanban Board"/></a><br/><sub>Join Kanban Board</sub></td>
    <td width="33%" align="center" valign="top"><a href="https://el-pollo-loco-aghirculesei.pages.dev/"><img src="imgs/thumbs/el-pollo-loco.jpg" alt="Screenshot: El Pollo Loco"/></a><br/><sub>El Pollo Loco</sub></td>
  </tr>
</table>

</details>

---

## 🛠️ Tech-Stack

**Sprachen**

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

**Backend & Daten**

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

**Testing & Qualität**

![Vitest](https://img.shields.io/badge/Vitest-6E9F18?style=flat-square&logo=vitest&logoColor=white)
![Playwright](https://img.shields.io/badge/Playwright-45ba4b?style=flat-square&logo=playwright&logoColor=white)
![Cypress](https://img.shields.io/badge/Cypress-17202C?style=flat-square&logo=cypress&logoColor=white)
![Jasmine](https://img.shields.io/badge/Jasmine-8A4182?style=flat-square&logo=jasmine&logoColor=white)
![Karma](https://img.shields.io/badge/Karma-56C2E6?style=flat-square)
![Pytest](https://img.shields.io/badge/Pytest-0A9EDC?style=flat-square&logo=pytest&logoColor=white)
![axe-core](https://img.shields.io/badge/axe--core-6633CC?style=flat-square)
![WCAG 2.1 AA](https://img.shields.io/badge/WCAG_2.1_AA-005A9C?style=flat-square)

**Tools & Infrastruktur**

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

## 💼 Werdegang

**Freelance Web- & App-Entwicklung** — Selbstständig · seit 10/2025<br/>
Eigenverantwortliche Entwicklung von Web-Anwendungen – von der Anforderungsaufnahme bis zum Deployment, mit Schwerpunkt auf Terminbuchungssystemen und automatisierten Kommunikationslösungen.

**AZAV-zertifizierte Qualifizierung zur Softwareentwicklerin** — Developer Akademie GmbH · 10/2024 – 10/2025<br/>
18 Module, 12+ Projekte – mehrere davon im Team nach SCRUM/Kanban. Schwerpunkte: Angular, TypeScript, REST-APIs, Firebase, Testautomatisierung, UI/UX (Figma).

**Projektkoordination – Automotive & IT** — Ferchau Automotive, jSERVICE · 2023 – 2024<br/>
Anforderungsmanagement, Arbeitspaket- und Terminsteuerung in Jira/DMS, Koordination internationaler Freigabeprozesse für Fahrerassistenzsysteme, Moderation von Abstimmungsrunden mit bis zu 150 Teilnehmenden.

**Bachelor Wirtschaftswissenschaften (Wirtschaftsinformatik)** — George-Bacovia-Universität, Bacău (RO)<br/>
Originaltitel: Economist licențiat, Fachrichtung Contabilitate și informatică de gestiune (Rechnungswesen und Informatik in Betrieben). Anerkennung durch KMK/ZAB: entspricht einem deutschen Hochschulabschluss auf Bachelor-Ebene.

---

## 📊 GitHub-Aktivität

<picture>
  <source media="(max-width: 600px)" srcset="imgs/year-activity-mobile.png">
  <img src="imgs/year-activity.png" width="100%" alt="Commits pro Monat in den letzten zwölf Monaten"/>
</picture>

<div align="center">

<img src="https://github-readme-stats-iota-gray-47.vercel.app/api/top-langs/?username=MihaelaAghirculesei&layout=compact&theme=radical&hide_border=true&count_private=true&langs_count=7&exclude_repo=github-readme-streak-stats,github-readme-stats&hide=java,php&custom_title=Meistgenutzte%20Sprachen" width="480" alt="Meistgenutzte Sprachen"/>

</div>

---

## 🌍 Verfügbarkeit

- **Rollen:** Fullstack-Entwicklerin (Python/FastAPI + Angular) · Backend-Entwicklerin (Python/FastAPI) · Frontend-Entwicklerin (Angular / TypeScript)
- **Standort:** Wolfsburg · Remote innerhalb der EU
- **Sprachen:** Rumänisch & Italienisch (Muttersprache) · Deutsch fließend (gesamte Berufserfahrung auf Deutsch) · Englisch B1 (Lesen/Schreiben), A2 (Sprechen)
- 🇪🇺 **EU-Staatsangehörigkeit** (Rumänien & Italien) – uneingeschränkte Arbeitserlaubnis in Deutschland und der gesamten EU, kein Visum, kein Sponsoring.

---

## 📫 Kontakt

<div align="center">

[![Portfolio](https://img.shields.io/badge/Portfolio-aghirculesei.de-FF5722?style=for-the-badge&logo=google-chrome&logoColor=white)](https://aghirculesei.de/)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Profil-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/mihaela-aghirculesei-84147a23b/)
[![E-Mail](https://img.shields.io/badge/E--Mail-Schreiben-D14836?style=for-the-badge&logo=gmail&logoColor=white)](mailto:aghirculesei@gmail.com)

<img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=6,11,20&height=100&section=footer" width="100%" alt=""/>

</div>
