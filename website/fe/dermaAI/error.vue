<template>

  <NuxtLayout>
    <div class="mt-7 max-w-sm mx-auto text-center backdrop-blur-md card roboto-bold">
      <h1 class="mt-7 text-7xl font-bold">{{ error.statusCode }}</h1>
      <p class="mt-5 text-3xl">{{ error.message }}</p>
      <UButton label="Return home page" size="xl" class="mt-5" @click="handleClearError" />
    </div>
  </NuxtLayout>
</template>

<script lang="ts" setup>
const error = useError()
// defineProps(['error'])

const handleClearError = () => clearError({ redirect: "/" })

</script>

<style>
@import url('https://fonts.googleapis.com/css2?family=Montserrat:ital,wght@0,100..900;1,100..900&display=swap');
</style>