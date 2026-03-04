import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'

export default defineConfig({
  plugins: [react()],
  base: '/Health-Flow/', // GitHub Pages: https://mahip-kakan.github.io/Health-Flow/
  server: {
    port: 2302
  }
})
