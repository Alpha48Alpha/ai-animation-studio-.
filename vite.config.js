import { defineConfig } from "vite";

export default defineConfig({
  // index.html at repo root is the Vite entry point.
  // Static assets (images, audio) live in public/ and are served at /.
  root: ".",
  // public/ is served as-is at /; public/assets/* → /assets/*
  publicDir: "public",
  build: {
    outDir: "dist",
    emptyOutDir: true,
  },
  server: {
    open: true,
  },
});
