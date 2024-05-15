<template>
  <div class="flex flex-col items-center justify-start backdrop-blur-lg mx-40 my-10 min-h-60">
    <UTable v-if="rows.length !== 0" :columns="columns" :rows="rows" class="w-2/3 backdrop-blur-md " />
    <!-- show disease and treatment with treatment object -->
    <div v-if="rows.length !== 0" class="flex-col justify-start min-h-32">
      <h1 class="text-2xl font-bold text-gray-800">Treatment</h1>
      <h1 class="text-2xl font-bold text-gray-800"> {{ treatment.name }}</h1>
      <li v-for="item in treatment.treatment" :key="item" class="text-lg font-bold text-gray-800">{{ item }}</li>
    </div>

    <div v-else>
      <div class="flex justify-start min-h-32">
        <h1 class="text-2xl font-bold text-gray-800">No data available</h1>
        <!-- return homepage -->
      </div>
      <div class="flex justify-end">
        <UButton size="xl" to="/" label="Return to homepage" />

      </div>
    </div>
  </div>
</template>

<script lang="ts" setup>
const store = useDataStore()
const fetchStore = useFetchStore()
const columns = [{
  key: 'AK',
  label: 'AK'
}, {
  key: 'BCC',
  label: 'BCC'
}, {
  key: 'BKL',
  label: 'BKL'
}, {
  key: 'DF',
  label: 'DF'
}, {
  key: 'MEL',
  label: 'MEL'
}, {
  key: 'NV',
  label: 'NV'
}, {
  key: 'SCC',
  label: 'SCC'
}, {
  key: 'VASC',
  label: 'VASC'
}, {
  key: 'acne',
  label: 'acne'
}, {
  key: 'eczema',
  label: 'eczema'
}, {
  key: 'not_infected',
  label: 'not_infected'
}]

const result = store.result
const rows = []
const maxKey = store.getMaxKey()
let treatment = fetchStore.data
if (maxKey != null) {
  fetchStore.$reset()
  await fetchStore.fetchData(`/Get-treatment/${maxKey}`, {
    method: 'GET',
  })
  if (fetchStore.statusCode == 200) {
    treatment = fetchStore.data
    console.log('Treatment:', fetchStore.data);

  }
}
console.log('MaxKey:', maxKey);
console.log(result);

if (Object.keys(result).length !== 0) {
  rows.push(result)
}
console.log(rows.length);




</script>

<style></style>