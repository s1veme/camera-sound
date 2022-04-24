<template>
  <div class="load-test-data">
    <load-file class="button load-test-data__input" @load-file="loadFile" />
    <button class="button load-test-data__button" @click="cameraLoadData">Загрузить тестовые данные для камер</button>
    <button class="button load-test-data__button" @click="reportLoadData">
      Загрузить тестовые данные для отчёта
    </button>
  </div>
</template>

<script>
import LoadFile from "../card/LoadFile.vue";

export default {
  name: "LoadTestData",

  components: {
    LoadFile,
  },

  data() {
    const reportData = [
        {
            video: null,
            camera: 1,
            statistics: {'position': 'sitting', 'condition': 'normal'}
        },
        {
            video: null,
            camera: 2,
            statistics: {'position': 'sitting', 'condition': 'normal'}
        },
    ]

    return {
      reportData,
      cameraData: [
        {
          title: "Camera 1",
        },
        {
          title: "Camera 2",
        },
      ],
    };
  },

  methods: {
    async cameraLoadData() {
      for (const item in this.cameraData) {
        await this.$axios.post("/api/v1/cameras/", this.cameraData[item]);
      }
    },

    async reportLoadData() {
      const formData = new FormData();
      
      for (const item in this.reportData) {
        formData.set("camera", this.reportData[item]["camera"]);
        const statisticsBlob = JSON.stringify(this.reportData[item]["statistics"])
        console.log(this.reportData[item]['video']);
        formData.set("video", this.reportData[item]["video"]);
        formData.set("statistics", statisticsBlob);
        this.$axios.post(
          "/api/v1/cameras/create-report/",
          formData
        );
      }
    },

    loadFile(file) {
      for (const item in this.reportData) {
        this.reportData[item].video = file;
        console.log(file);
      }
    },
  },
};
</script>

<style scoped>
.load-test-data__input {
  max-width: 200px;
}
.load-test-data__button {
  font-size: 14px;
}
</style>