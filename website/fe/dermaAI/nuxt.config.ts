// https://nuxt.com/docs/api/configuration/nuxt-config
export default defineNuxtConfig({
  devtools: { enabled: true },
  modules: ['@nuxt/ui', '@nuxt/eslint', 'nuxt-icon', '@pinia/nuxt'],
  eslint: {
    config: {
      stylistic: {
        semi: true,
        indent: 'tab',
        quotes: 'double',
      }, // <---
    },
  },
  colorMode: {
    preference: 'light',
  },
  pinia: {
    storesDirs: ['./stores/**', './custom-folder/stores/**'],
  },
  runtimeConfig: {
    public: {
      apiBase: 'http://localhost:5000/api',
    },
  },
});
