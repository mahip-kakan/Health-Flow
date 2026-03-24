# Gravity Flow Studio (Health Flow)

A low-code studio to build, deploy, and automate healthcare workflows — part of the **Gravity AI Studio** experience. This repo powers the public demo at **[mahip-kakan.github.io/Health-Flow](https://mahip-kakan.github.io/Health-Flow/)**.

## What’s in the app

- **Flow editor** — Triggers, actions, templates (e.g. post-discharge follow-up, readmission risk, appointment reminders).
- **Discover & product flows** — Browse pre-built automation ideas across Gravity healthcare domains.
- **AI assistant & Healthcare glossary** — In-app help for US healthcare terms and Gravity concepts, including **HMCP** (Healthcare Model Context Protocol) and **MCP** (Model Context Protocol).
- **Action configuration** — Each step opens a contextual settings panel (care plans, Tasks, Microsoft Teams, email, models/agents, reminders, and more).
- **Roles** — Switch between Developer, Product Manager, and Admin (affects sidebar and access to the testing dashboard).

## Run locally

```bash
npm install
npm run dev
```

Open **[http://localhost:2302/](http://localhost:2302/)**.  
Local dev uses Vite with `base: '/'`. Production builds use `base: '/Health-Flow/'` for GitHub Pages (see [`vite.config.js`](vite.config.js)).

## Testing dashboard (PM / Admin)

1. In the studio, open the **user menu** (top right) → **View as** → **Product Manager** or **Admin**.
2. Use the **Testing** (beaker) item in the left sidebar.

The UI lives under [`src/testing-dashboard/`](src/testing-dashboard/). For a **standalone** dev server on port **2303**, see **[testing/README.md](testing/README.md)**.

## Architecture diagram

An Excalidraw diagram of the Gravity / HMCP / DAP-style stack is in:

[`docs/architecture/gravity-hmcp-architecture.excalidraw`](docs/architecture/gravity-hmcp-architecture.excalidraw)

Open it in [Excalidraw](https://excalidraw.com) or with the Excalidraw extension in VS Code / Cursor.

## Build & preview

```bash
npm run build    # output in dist/
npm run preview  # local preview of production build
```

## Deploy to GitHub Pages

This repo is **[github.com/mahip-kakan/Health-Flow](https://github.com/mahip-kakan/Health-Flow)**.

1. **Push to `main`** — the **Deploy to GitHub Pages** workflow ([`.github/workflows/deploy.yml`](.github/workflows/deploy.yml)) runs `npm run build` and pushes the contents of **`dist/`** to the **`gh-pages`** branch.
2. **Repo settings (required)** — **Settings** → **Pages** → **Build and deployment** → **Source**: **Deploy from a branch** → choose branch **`gh-pages`**, folder **`/ (root)`**.  
   **Do not** set the source to **`main`** with **`/ (root)`**. If you do, GitHub serves the raw repo `index.html` (with `/src/main.jsx`), which only works with `vite dev` — the site will look blank or broken in production.
3. **Live site** — **[https://mahip-kakan.github.io/Health-Flow/](https://mahip-kakan.github.io/Health-Flow/)**  
   Use this `*.github.io` URL, not the raw `github.com/.../Health-Flow` code URL.

**Site not loading / blank page**

- **Wrong Pages source** — Most common: Pages is on **`main`** instead of **`gh-pages`**. Switch to **`gh-pages`** as above, wait a minute, hard-refresh.
- **Actions** — In the **Actions** tab, open **Deploy to GitHub Pages** and confirm the latest run on `main` is green.
- **First deploy** — Until the workflow runs once, the `gh-pages` branch may not exist; run the workflow (push to `main` or **Run workflow**), then select `gh-pages` in Pages settings.
- **Path casing** — If only a lowercase URL works, set `base` in `vite.config.js` to match (e.g. `'/health-flow/'`) and redeploy.

## Tech

- React 18  
- Vite 5  
- Lucide React  
