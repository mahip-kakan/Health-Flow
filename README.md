# Gravity Flow Studio

A low-code studio to build, deploy, and automate healthcare workflows — part of the Gravity AI Studio experience.

## Run locally

```bash
npm install
npm run dev
```

Open [http://localhost:2302](http://localhost:2302).

## Build

```bash
npm run build
```

Output is in `dist/`.

## Deploy to GitHub Pages

1. **Push this repo** to your GitHub account. Set `origin` to your repo if needed:
   ```bash
   git remote set-url origin https://github.com/mahip-kakan/Health-Flow.git
   git add .
   git commit -m "Add GitHub Pages deploy"
   git push -u origin main
   ```

2. **Enable GitHub Pages** in the repo:
   - Go to **Settings** → **Pages**
   - Under **Source**, choose **Deploy from a branch**
   - Branch: **gh-pages** (or select it after the first workflow run)
   - Folder: **/ (root)**
   - Save

3. **Trigger the workflow**: On every push to `main`, the **Deploy to GitHub Pages** workflow runs, builds the app, and deploys to the `gh-pages` branch. The first run will create that branch.

4. **Live URL**: After deployment, the app will be at:
   **https://mahip-kakan.github.io/Health-Flow/**
   (Use this exact URL — not the repo URL `github.com/mahip-kakan/Health-Flow`.)

**If you see a 404:**
- Use the **Pages URL** above (with `username.github.io`), not the repo address.
- In **Settings → Pages**, set source to the **gh-pages** branch, folder **/ (root)**.
- Check the **Actions** tab: the "Deploy to GitHub Pages" workflow must have run and succeeded (green check).
- Try both capital and lowercase in the path if your repo name differs: `.../Health-Flow/` and `.../health-flow/`. If lowercase works, set `base: '/health-flow/'` in `vite.config.js` and redeploy.

If you rename the repo, update `base` in `vite.config.js` to match (e.g. `base: '/your-repo-name/'`).

## Tech

- React 18
- Vite 5
- Lucide React icons
