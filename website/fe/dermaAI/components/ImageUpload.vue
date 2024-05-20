<template>
  <div class="p-4 max-w-md mx-auto">
    <input type="file" @change="onFileChange" accept="image/*" class="mb-4 block w-full text-sm text-gray-500
             file:mr-4 file:py-2 file:px-4
             file:rounded-full file:border-0
             file:text-sm file:font-semibold
             file:bg-blue-50 file:text-blue-700
             hover:file:bg-blue-100" />
    <div v-if="previewUrl" class="mt-4">
      <img :src="previewUrl" alt="Image Preview" class="max-w-full h-auto rounded-lg shadow-md" />
    </div>
    <UButton :size="xl" :ui="{ rounded: 'rounded-full' }" @click="uploadImage"> Upload Image </UButton>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useRouter } from 'vue-router'
import { useFetchStore } from '~/stores/useFetchStore';

const router = useRouter()
const dataStore = useDataStore()
const fetchStore = useFetchStore()

const previewUrl = ref(null)
const file = ref(null)

const onFileChange = (event) => {
  file.value = event.target.files[0]
  if (file.value) {
    const reader = new FileReader()
    reader.onload = (e) => {
      previewUrl.value = e.target.result
    }
    reader.readAsDataURL(file.value)
  }
}

const uploadImage = async () => {
  if (!file.value) {
    alert('Please select a file first!')
    return
  }

  const formData = new FormData()
  formData.append('file', file.value)

  await fetchStore.fetchData('/Detect', {
    method: 'POST',
    body: formData,
  })
  console.log('Data:', fetchStore.data, 'Error:', fetchStore.error, fetchStore.statusCode);
  if (fetchStore.statusCode == 500) {
    throw createError({
      statusCode: 500,
      statusMessage: 'Internal Server Error',
      fatal: true,
    })
  }
  if (fetchStore.statusCode != 200) {
    console.error('Error uploading image:', fetchStore.error)
    dataStore.error = fetchStore.error
    var message = fetchStore.error.message
    file.value = null
    fetchStore.$reset()
    alert(`Error uploading image: ${message}`, message)

    clearError({ redirect: '/' })
    // router.push({ path: '/error' })
    return
  }
  dataStore.result = fetchStore.data
  router.push({ path: '/result' })
}
</script>

<style scoped>
/* Add any additional scoped styles here if needed */
</style>
