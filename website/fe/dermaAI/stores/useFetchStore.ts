// stores/useFetchStore.ts
import { defineStore } from 'pinia';
import { useApiFetch } from '~/composables/useApiFetch';

export const useFetchStore = defineStore({
  id: 'fetchStore',
  state: () => ({
    data: Object.create(null),
    loading: false,
    error: Object.create(null),
    statusCode: 200,
  }),
  actions: {
    async fetchData(endpoint: string, options: RequestInit = {}) {
      this.loading = true;
      try {
        const { data: fetchData, error: fetchError } = await useApiFetch(endpoint, options);

        if (fetchError.value) {
          this.statusCode = fetchError.value.statusCode ?? 0;
          console.log(fetchError);

          throw fetchError.value.data;
        }
        this.data = fetchData.value;
      } catch (err) {
        this.data = Object.create(null);
        this.error = err;
      } finally {
        this.loading = false;
      }
    },
  },
});
