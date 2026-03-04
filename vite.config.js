import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'

export default defineConfig({
  plugins: [react()],
  base: '/Impact-Flow/', // Must match repo name exactly. Live: https://mahipkumar-dotcom.github.io/Impact-Flow/
  server: {
    port: 2302
  }
})
