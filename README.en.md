<p align="right"><sub><a href="README.md">Deutsch</a> · <b>English</b> · <a href="README.it.md">Italiano</a></sub></p>

<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=6,11,20&height=90&section=header" width="100%" alt=""/>

# Mihaela Aghirculesei

### Fullstack Developer · Python / FastAPI · Angular · TypeScript

I build web applications end-to-end – from async FastAPI back ends to accessible Angular front ends, backed by tests and CI quality gates.

[![Portfolio](https://img.shields.io/badge/Portfolio-aghirculesei.de-FF5722?style=for-the-badge&logo=google-chrome&logoColor=white)](https://aghirculesei.de/)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Profile-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/mihaela-aghirculesei-84147a23b/)
[![Email](https://img.shields.io/badge/Email-Get_in_touch-D14836?style=for-the-badge&logo=gmail&logoColor=white)](mailto:aghirculesei@gmail.com)

🟢 **Open to full-time roles** · Wolfsburg · Remote (EU) · EU citizen, no sponsorship needed

<table>
  <tr>
    <td align="center" width="50%"><a href="https://alina-moments-photography.vercel.app"><b>Client project live</b></a><br/><sub>built on my own, from architecture to deployment</sub></td>
    <td align="center" width="50%"><a href="https://www.npmjs.com/package/bfsg-scanner"><b>npm package</b></a><br/><sub>published with SLSA build provenance</sub></td>
  </tr>
  <tr>
    <td align="center" width="50%"><a href="https://github.com/maplibre/maplibre-gl-js/pull/8766"><b>Open source</b></a><br/><sub>contribution to MapLibre GL JS, merged</sub></td>
    <td align="center" width="50%"><a href="https://mihaelaaghirculesei.github.io/bfsg-scanner/"><b>Accessibility</b></a><br/><sub>WCAG 2.1 AA / BFSG as a CI gate</sub></td>
  </tr>
</table>

</div>

---

## 👩‍💻 About Me

Software developer with a bachelor's degree in economics (business informatics) and an AZAV-certified qualification. I build web applications end-to-end: **back ends with Python/FastAPI, PostgreSQL and Redis** and **front ends with Angular & TypeScript** (also Next.js / React and Vue / Nuxt) – including tests, CI/CD and monitoring. Several applications are live in production – including a client website I built end-to-end, from architecture to deployment, on my own.

Before that, several years in **project coordination** on automotive and IT development projects: requirements management, Jira/DMS, release processes, and facilitating alignment meetings with up to 150 participants. I bring that dual perspective – delivery **and** coordination – to every team.

- 🗣️ Romanian & Italian (native) · German (fluent) · English B1 (reading/writing)
- ♿ Focus on accessibility (WCAG 2.1 AA / BFSG) and automated quality assurance
- 🤝 Open-source contribution: [MapLibre GL JS](https://github.com/maplibre/maplibre-gl-js) – docs note for Vite-based SSR frameworks (Nuxt, SvelteKit, Astro), [PR #8766](https://github.com/maplibre/maplibre-gl-js/pull/8766) merged

---

## 🎨 Featured Projects

### 🍽️ dineos · Real-time ordering system for restaurants ![In Development](https://img.shields.io/badge/🚧_In_Development-FFC107?style=flat-square)
A restaurant operating system built end-to-end on my own – back end, front end, infrastructure and deploy pipeline. Guests order and pay from a QR code at the table, the kitchen sees new orders instantly over WebSocket, and managers run tables, staff and the menu from a dashboard.

- **Real time:** WebSocket fan-out via Redis Pub/Sub (multi-instance), per-IP connection caps, heartbeat to reclaim dead sockets
- **Security:** JWT with refresh tokens and revocation, 4 roles, rate limiting – my own security review found a cross-tenant data leak, fixed and locked down with regression tests
- **Quality:** 376 back-end tests (pytest against real PostgreSQL + Redis in CI), `mypy --strict`, Ruff, coverage gate, 6 architecture decision records

**Tech:** Python • FastAPI • SQLAlchemy 2.0 (async) • Alembic • PostgreSQL • Redis • WebSocket • Stripe • Docker • OpenTelemetry • Prometheus • Grafana • Angular 21 • NgRx

🔒 Private repository (commercial product) · Code walkthrough on request

<details>
<summary><b>Architecture, payments & operations</b></summary>
<br/>

- **Architecture:** async FastAPI back end layered Router → Service → Repository, SQLAlchemy 2.0 + asyncpg, 11 Alembic migrations, multi-tenant isolation by `restaurant_id`
- **Payments:** Stripe PaymentIntents with idempotency keys, a dead-letter queue for failed webhooks with retry/backoff (atomic via Lua script), audit log
- **Operations:** Docker, two-stage CD (auto-deploy to staging → promotion to production with smoke test and rollback), OpenTelemetry traces, Prometheus + Grafana, Sentry, k6 load tests

</details>

<div align="center">
<img src="https://capsule-render.vercel.app/api?type=soft&color=gradient&customColorList=6,11,20&height=10&width=1200" width="100%"/>
</div>

### 📦 [bfsg-scanner](https://www.npmjs.com/package/bfsg-scanner) · Open-source npm package
A CLI that scans an entire website for WCAG 2.1 AA violations and maps every finding to the EN 301 549 / BFSG clause it breaches – producing a citeable conformance report in JSON/HTML/PDF. Built as a series of small, individually reviewed pull requests; the key architecture decisions each captured in an architecture decision record.

🌐 **Live sample report:** [mihaelaaghirculesei.github.io/bfsg-scanner](https://mihaelaaghirculesei.github.io/bfsg-scanner/)

- **Supply chain:** published to npm with SLSA build provenance; the release workflow publishes via OIDC trusted publishing – no long-lived tokens
- **CI gate:** exits non-zero at a configurable severity threshold, so a pipeline can block a merge on accessibility
- **Quality:** 167 tests, CI on Linux/Windows/macOS, a versioned JSON Schema for the report output, semantic exit codes

**Tech:** TypeScript • Node.js 22+ • Playwright • axe-core • Zod • Vitest • Biome • GitHub Actions

<details>
<summary><b>Screenshot & engine</b></summary>
<br/>

<img src="imgs/bfsg-scanner.png" width="800" alt="Screenshot: bfsg-scanner"/>

- **Engine:** sitemap + robots.txt-aware breadth-first crawl, concurrency pool with per-host rate limiting, real Chromium via Playwright + axe-core

</details>

<div align="center">
<img src="https://capsule-render.vercel.app/api?type=soft&color=gradient&customColorList=6,11,20&height=10&width=1200" width="100%"/>
</div>

### 📚 [normeon](https://github.com/MihaelaAghirculesei/normeon-german-technical-rag) · RAG for German technical documentation ![In Development](https://img.shields.io/badge/🚧_In_Development-FFC107?style=flat-square)
A RAG assistant for German-language technical documentation (requirement specs, UNECE regulations, manuals) that answers with verifiable source citations – and abstains rather than hallucinates.

- **Retrieval:** hybrid search combining vector search (pgvector, HNSW index), German full-text search and a trigram fallback, fused with Reciprocal Rank Fusion, then cross-encoder reranking
- **Generation:** citation validation (invented sources are dropped), a confidence gate before the LLM call, SSE streaming, per-request cost and latency logging
- **Evaluation:** a hand-written 50-question German eval set, LLM-as-judge calibrated against human scoring
- **Quality:** 356 tests (integration tests with Testcontainers), CI, swappable adapters for embeddings, LLM and reranker

**Tech:** Python • FastAPI • PostgreSQL + pgvector • Alembic • Docker • Pytest • Testcontainers

<div align="center">
<img src="https://capsule-render.vercel.app/api?type=soft&color=gradient&customColorList=6,11,20&height=10&width=1200" width="100%"/>
</div>

### More projects

| Project | Highlights | Stack |
|:--|:--|:--|
| 📸 **[Alina Moments Photography](https://alina-moments-photography.vercel.app)** · Client project<br/><sub>Portfolio website for a photographer, live</sub> | Built on my own from architecture to live deployment (over 400 commits, over 100 merged PRs), ≥95% test coverage, Lighthouse ≥95 (Accessibility), nonce-based CSP, 4 languages | Next.js 16 • React 19 • PostgreSQL |
| ⚡ **[ChargeHub](https://github.com/MihaelaAghirculesei/ChargeHub)** · [Demo](https://charge-hub-one.vercel.app/de)<br/><sub>EV charging infrastructure dashboard</sub> | Nitro BFF in front of the Open Charge Map API, LLM free-text search with structured output, ~92% coverage gate, axe-core as a blocking CI gate | Nuxt 4 • Vue 3 • TypeScript |
| 🎂 **[Birthday Reminder Pro](https://birthday-reminder-aghirculesei.pages.dev/)**<br/><sub>Offline-first app for web and Android</sub> | Over 1,200 commits, over 2,000 unit and over 100 E2E tests, two-way Google Calendar sync, native Android notifications | Angular 22 • NgRx • Capacitor • Firebase |
| 📅 **[Intelligent Family Calendar](https://github.com/MihaelaAghirculesei/intelligent-family-calendar)** · [Demo](https://mihaelaaghirculesei.github.io/intelligent-family-calendar/)<br/><sub>Weekly planner for families</sub> | Angular 17 → 22 with one commit per major version, zoneless, 125 Playwright E2E tests on Chromium, Firefox and WebKit, WCAG 2.2 AA | Angular 22 • Angular CDK • Playwright |
| 🔒 **[SecureNotes Lab](https://github.com/MihaelaAghirculesei/secure-notes-lab)**<br/><sub>Security showcase</sub> | Built twice: 4 OWASP Top 10:2025 vulnerabilities plus CSRF introduced, documented and fixed, fixes proven with regression tests | Python • Flask • Bandit |
| 🐍 **[Todo API](https://github.com/MihaelaAghirculesei/todo-api)** · [Live](https://todo-frontend-aghirculesei.onrender.com)<br/><sub>Team project (2 developers)</sub> | My contribution: the complete back end – Router → Service → Repository, 25/25 tests, API designed so the React front end could be built independently | FastAPI • SQLAlchemy 2.1 |

*Training projects (AZAV-certified qualification, Developer Akademie):*

| Project | Highlights | Stack |
|:--|:--|:--|
| 💡 **[Pokédex](https://pokedex-aghirculesei.pages.dev/)** | Offline-first PWA, 242 unit and 21 E2E tests at 100% coverage, Lighthouse CI | TypeScript • Vite • Vitest |
| 🔥 **[Join Kanban Board](https://join-aghirculesei.pages.dev/)**<br/><sub>Team project (5 developers)</sub> | Continued my fork on my own: Angular 17 → 22, 17 emulator tests for the Firestore rules, CodeQL, npm audit from 97 findings to 0 | Angular 22 • Firebase |
| 🚀 **[El Pollo Loco](https://el-pollo-loco-aghirculesei.pages.dev/)** | 2D jump-and-run with no game framework: 20 object-oriented classes, pixel-perfect collision detection, ~60 FPS | HTML5 Canvas • JavaScript |

<details>
<summary><b>📸 View screenshots</b></summary>
<br/>

<table>
  <tr>
    <td width="33%" align="center"><a href="https://alina-moments-photography.vercel.app"><img src="imgs/alina-moments.png" alt="Screenshot: Alina Moments Photography"/></a><br/><sub>Alina Moments Photography</sub></td>
    <td width="33%" align="center"><a href="https://charge-hub-one.vercel.app/de"><img src="imgs/chargehub.png" alt="Screenshot: ChargeHub"/></a><br/><sub>ChargeHub</sub></td>
    <td width="33%" align="center"><a href="https://birthday-reminder-aghirculesei.pages.dev/"><img src="imgs/birthday-memories.png" alt="Screenshot: Birthday Reminder Pro"/></a><br/><sub>Birthday Reminder Pro</sub></td>
  </tr>
  <tr>
    <td width="33%" align="center"><a href="https://mihaelaaghirculesei.github.io/intelligent-family-calendar/"><img src="imgs/intelligent-family-calendar.png" alt="Screenshot: Intelligent Family Calendar"/></a><br/><sub>Intelligent Family Calendar</sub></td>
    <td width="33%" align="center"><a href="https://github.com/MihaelaAghirculesei/secure-notes-lab"><img src="imgs/secure-notes-lab.png" alt="Screenshot: SecureNotes Lab"/></a><br/><sub>SecureNotes Lab</sub></td>
    <td width="33%" align="center"><a href="https://todo-frontend-aghirculesei.onrender.com"><img src="imgs/todo-api.png" alt="Screenshot: Todo API"/></a><br/><sub>Todo API</sub></td>
  </tr>
  <tr>
    <td width="33%" align="center"><a href="https://pokedex-aghirculesei.pages.dev/"><img src="imgs/pokedex.png" alt="Screenshot: Pokédex"/></a><br/><sub>Pokédex</sub></td>
    <td width="33%" align="center"><a href="https://join-aghirculesei.pages.dev/"><img src="imgs/join-board.png" alt="Screenshot: Join Kanban Board"/></a><br/><sub>Join Kanban Board</sub></td>
    <td width="33%" align="center"><a href="https://el-pollo-loco-aghirculesei.pages.dev/"><img src="imgs/el-pollo-loco.png" alt="Screenshot: El Pollo Loco"/></a><br/><sub>El Pollo Loco</sub></td>
  </tr>
</table>

</details>

---

## 🛠️ Tech Stack

**Languages**

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

**Back end & Data**

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

**Testing & Quality**

![Vitest](https://img.shields.io/badge/Vitest-6E9F18?style=flat-square&logo=vitest&logoColor=white)
![Playwright](https://img.shields.io/badge/Playwright-45ba4b?style=flat-square&logo=playwright&logoColor=white)
![Cypress](https://img.shields.io/badge/Cypress-17202C?style=flat-square&logo=cypress&logoColor=white)
![Jasmine](https://img.shields.io/badge/Jasmine-8A4182?style=flat-square&logo=jasmine&logoColor=white)
![Karma](https://img.shields.io/badge/Karma-56C2E6?style=flat-square)
![Pytest](https://img.shields.io/badge/Pytest-0A9EDC?style=flat-square&logo=pytest&logoColor=white)
![axe-core](https://img.shields.io/badge/axe--core-6633CC?style=flat-square)
![WCAG 2.1 AA](https://img.shields.io/badge/WCAG_2.1_AA-005A9C?style=flat-square)

**Tools & Infrastructure**

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

## 💼 Background

**Freelance Web & App Development** — Self-employed · since 10/2025
End-to-end development of web applications – from requirements gathering to deployment, focusing on appointment-booking systems and automated communication solutions.

**AZAV-certified Software Developer Qualification** — Developer Akademie GmbH · 10/2024 – 10/2025
18 modules, 12+ projects – several as part of SCRUM/Kanban teams. Focus: Angular, TypeScript, REST APIs, Firebase, test automation, UI/UX (Figma).

**Project Coordination – Automotive & IT** — Ferchau Automotive, jSERVICE · 2023 – 2024
Requirements management, work-package and schedule control in Jira/DMS, coordination of international release processes for driver-assistance systems, facilitation of alignment meetings with up to 150 participants.

**Bachelor's in Economics (Business Informatics)** — George Bacovia University, Bacău (RO)
Original title: Economist licențiat, specialization Contabilitate și informatică de gestiune (Accounting and Management Information Systems). Recognized by KMK/ZAB as equivalent to a German bachelor's degree.

---

## 📊 GitHub Activity

<picture>
  <source media="(max-width: 600px)" srcset="imgs/year-activity-mobile.png">
  <img src="imgs/year-activity.png" width="100%" alt="Commits per month over the last twelve months"/>
</picture>

<div align="center">

<img src="https://github-readme-stats-iota-gray-47.vercel.app/api/top-langs/?username=MihaelaAghirculesei&layout=compact&theme=radical&hide_border=true&count_private=true&langs_count=7&exclude_repo=github-readme-streak-stats,github-readme-stats&hide=java,php" width="480" alt="Most used languages"/>

</div>

---

## 🌍 Availability

- **Roles:** Fullstack Developer (Python/FastAPI + Angular) · Backend Developer (Python/FastAPI) · Frontend Developer (Angular / TypeScript)
- **Location:** Wolfsburg · remote within the EU
- **Languages:** Romanian & Italian (native) · Fluent German (all professional experience in German) · English B1 (reading/writing), A2 (speaking)
- 🇪🇺 **EU citizenship** (Romania & Italy) – full right to work in Germany and the entire EU, no visa, no sponsorship.

---

## 📫 Let's Connect

<div align="center">

[![Portfolio](https://img.shields.io/badge/🌐_Portfolio-aghirculesei.de-FF5722?style=for-the-badge)](https://aghirculesei.de/)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-0077B5?style=for-the-badge&logo=linkedin)](https://www.linkedin.com/in/mihaela-aghirculesei-84147a23b/)
[![Email](https://img.shields.io/badge/Email-Get_in_touch-D14836?style=for-the-badge&logo=gmail)](mailto:aghirculesei@gmail.com)

<img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=6,11,20&height=100&section=footer"/>

</div>
