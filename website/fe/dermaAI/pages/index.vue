<template>
  <div>
    <div
      class="bg-[url('assets/poster.jpg')] bg-cover bg-no-repeat flex flex-col items-center justify-center min-h-60 ">
      <div class="flex flex-col items-center justify-start mx-40 my-28 min-h-60">
        <strong class="text-5xl text-white m-4">SKINCARE ONLINE</strong>
        <p class="text-xl text-white font-semibold">DON'T WAIT TO BE SKINCHECK</p>

        <ImageUpload />
      </div>
    </div>
    <div class="flex items-center justify-center  text-3xl font-bold text-black">How to use Derma AI </div>
    <UCarousel v-slot="{ item }" :items="items" :ui="{ item: 'basis-full md:basis-1/2 lg:basis-1/3' }" indicators
      class="rounded-lg overflow-hidden lg:mx-52 sm:m-0">
      <img :src="item" class="w-full" draggable="false">
    </UCarousel>
  </div>


</template>

<script setup>

const items = [
  'step1.png',
  'step2.png',
  'step3.png',
]
</script>
