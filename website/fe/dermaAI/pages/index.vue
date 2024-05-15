<template>
  <form @submit.prevent="uploadImage">
    <input type="file" @change="onFileChange" />
    <button type="submit">Upload</button>
  </form>
</template>

<script setup>
import { ref } from 'vue'
import { useRouter } from 'vue-router'
import { useFetchStore } from '~/stores/useFetchStore';


const selectedFile = ref(null)
const router = useRouter()
const dataStore = useDataStore()
const fetchStore = useFetchStore()

const onFileChange = (event) => {
  selectedFile.value = event.target.files[0]
}

const uploadImage = async () => {
  if (!selectedFile.value) {
    alert('Please select a file first!')
    return
  }

  const formData = new FormData()
  formData.append('file', selectedFile.value)

  await fetchStore.fetchData('/Detect', {
    method: 'POST',
    body: formData,
  })
  console.log('Data:', fetchStore.data, 'Error:', fetchStore.error, fetchStore.statusCode);
  if (fetchStore.statusCode != 200) {
    console.error('Error uploading image:', fetchStore.error)
    dataStore.error = fetchStore.error
    alert(`Error uploading image: ${fetchStore.error.message}`, fetchStore.error.message)
    // router.push({ path: '/error' })
    return
  }
  dataStore.result = fetchStore.data
  router.push({ path: '/result' })
}
</script>
