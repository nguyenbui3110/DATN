// composables/useApiFetch.ts
export async function useApiFetch(endpoint: string, options = {}) {
  const config = useRuntimeConfig();
  const url = `${config.public.apiBase}${endpoint}`;
  const { data, error, status } = await useFetch(url, options);

  return { data, error, status };
}
