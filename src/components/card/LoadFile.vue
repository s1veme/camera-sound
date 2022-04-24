<template>
  <div>
    <input ref="file" @change="handleFileUpload()" type="file" />
  </div>
</template>
<script>
import { ref } from "vue";

export default {
  name: "LoadFile",

  setup(_, { emit }) {
    const file = ref(null);

    const handleFileUpload = () => {
      emit("loadFile", file.value.files[0]);
    };

    return {
      handleFileUpload,
      file,
    };
  },
};
</script>
<style scoped>
input[type="file"] {
  color: transparent;
}
</style>