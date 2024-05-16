<template>
  <div class="flex flex-col items-center justify-start backdrop-blur-xl lg:mx-40 my-10 min-h-60 sm:m-0 text-black">
    <strong class="text-6xl">RESULT</strong>
    <UTable v-if="rows.length !== 0" :columns="columns" :rows="rows" class="w-2/3 " />
    <!-- show disease and treatment with treatment object -->
    <div v-if="rows.length !== 0" class="flex-col justify-start min-h-32 r">
      <h1 class="text-2xl ">Predict: <strong>{{ treatment.name }}</strong></h1>
      <h1 class="text-2xl "> Treatment:</h1>
      <ul class="list-disc">
        <li v-for="item in treatment.treatment" :key="item" class="text-lg  mx-5">{{ item }}</li>
      </ul>
      <i class="mt-4">Disclaimer: This information is provided for educational purposes only and should not be used as a
        substitute
        for medical advice. Please consult a healthcare professional for an accurate diagnosis and treatment plan.</i>
    </div>

    <div v-else>
      <div class="flex justify-start min-h-32">
        <h1 class="text-2xl font-bold ">No data available</h1>
        <!-- return homepage -->
      </div>
      <div class="flex justify-center">
        <UButton size="xl" to="/" label="Return to homepage" class="my-5" />

      </div>

    </div>

  </div>
</template>

<script lang="ts" setup>
const store = useDataStore()
const fetchStore = useFetchStore()
const colorMode = useColorMode()
colorMode.value = 'Light'
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

console.log(result);

console.log(rows.length);




</script>

<style>
@import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@100..900&family=Roboto:ital,wght@0,100;0,300;0,400;0,500;0,700;0,900;1,100;1,300;1,400;1,500;1,700;1,900&display=swap');
</style>