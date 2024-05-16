<template>
  <header class="sticky top-0">
    <div class="backdrop-blur-2xl">
      <div class="lg:mx-52 flex justify-between items-center p-4 bg-inherit shadow-md backdrop-blur-2xl sm:m-0">
        <div class="flex items-start space-x-4">
          <router-link to="/" class="text-2xl font-bold text-gray-800">
            <span class="text-blue-500">Derma</span>AI
          </router-link>
        </div>

        <div class="flex items-center space-x-4">
          <router-link to="/" class="text-gray-500">home</router-link>
          <UButton :ui="{ rounded: 'rounded-full' }">Contact us</UButton>
          <Icon name="mdi:gmail" />

        </div>
      </div>
    </div>

  </header>
</template>

<script lang="ts" setup>
const colorMode = useColorMode()
colorMode.value = 'Dark'
</script>

<style></style>