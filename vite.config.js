import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'

// Local dev: base '/' so http://localhost:2302/ works.
// Production: base must match the GitHub repo name in the Pages URL (case-sensitive path).
// CI sets GITHUB_PAGES_BASE (see .github/workflows/deploy.yml). Local build default below.
const pagesBase =
  process.env.GITHUB_PAGES_BASE ||
  process.env.VITE_PAGES_BASE ||
  '/Health-Flow/'

export default defineConfig(({ command }) => ({
  plugins: [react()],
  base: command === 'serve' ? '/' : pagesBase.endsWith('/') ? pagesBase : `${pagesBase}/`,
  server: {
    port: 2302
  }
}))
