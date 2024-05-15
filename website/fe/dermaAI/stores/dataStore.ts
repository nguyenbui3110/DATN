// stores/dataStore.ts
import { defineStore } from 'pinia';

export const useDataStore = defineStore('data', {
  state: () => ({
    result: Object.create(null),
    error: Object.create(null),
  }),
  actions: {
    setResult(data: object) {
      this.result = data;
    },
    setError(error: object) {
      this.error = error;
    },
    getMaxKey() {
      if (Object.keys(this.result).length !== 0)
        return Object.keys(this.result).reduce((a, b) => (this.result[a] > this.result[b] ? a : b));
      return null;
    },
  },
});
