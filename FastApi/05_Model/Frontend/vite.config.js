import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'

// Proxies /api/* to the FastAPI server so you don't need CORS during dev.
export default defineConfig({
  plugins: [react()],
  server: {
    proxy: {
      '/api': {
        target: 'http://127.0.0.1:8000',
        changeOrigin: true,
        rewrite: (path) => path.replace(/^\/api/, ''),
      },
    },
  },
})
