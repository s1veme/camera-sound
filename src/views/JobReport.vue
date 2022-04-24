<template>
  <div class="job-report">
    <div class="container">
      <div class="job-report__wrapper">
        <router-link
          :to="{
            name: 'DetailedCard',
            params: { id: reportParendId },
          }"
          class="job-report__arrow"
        >
          <span>Назад</span>
        </router-link>
        <div class="breadcrumbs">
          <span
            >Cameras / {{ data?.data?.camera_title }} / Reports /
            {{ reportId }}</span
          >
        </div>
        <div class="job-report-content">
          <p class="job-report-number">
            Report | <span class="job-report-id">ID №{{ data?.data?.id }}</span>
          </p>
          <div class="job-report__wrap">
            <p class="job-report__statistics">
              {{ data?.data?.statistics }}
            </p>
            <div class="job-report__wrap-rigth">
              <div class="job-report-video">
                <video
                  :src="data?.data?.video"
                  width="700"
                  height="400"
                  controls
                >
                  <source :src="data?.data?.video" type="video/mp4" />
                </video>
              </div>
              <div class="download-file">
                <a :href="data?.data?.report_xlsx" download
                  >Download report (XLSX)</a
                >
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "JobReport",
  props: ["id", "parentId"],
  data() {
    const data = null;
    const reportId = null;
    const reportParendId = 0;
    return {
      data,
      reportId,
      reportParendId,
    };
  },
  methods: {
    async getJobReport() {
      console.log(this.id);
      if (this.id) {
        this.reportId = this.id;
      } else {
        this.reportId = this.$route.params.id;
      }
      this.data = await this.$axios.get(`/api/v1/job-report/${this.reportId}`);
      if (this.parentId) {
        this.reportParendId = this.parentId;
      } else {
        this.reportParendId = this.data?.data?.camera;
      }
    },
  },
  async mounted() {
    await this.getJobReport();
  },
};
</script>

<style scoped>
.job-report__arrow {
  position: relative;
  height: 2px;
  width: 36px;
  display: block;
  background-color: #fff;
  margin: 1rem 0 3rem;
}
.job-report__arrow::after {
  content: "";
  position: absolute;
  left: -2px;
  top: 6px;
  height: 2px;
  width: 18px;
  background-color: #fff;
  transform: rotate(45deg);
}
.job-report__arrow::before {
  content: "";
  position: absolute;
  left: -2px;
  top: -6px;
  height: 2px;
  width: 18px;
  background-color: #fff;
  transform: rotate(-45deg);
}
.job-report__arrow span {
  color: #fff;
  font-size: 22px;
  position: relative;
  top: -15px;
  left: 45px;
}
.job-report__statistics {
  white-space: pre-line;
}
.breadcrumbs {
  margin-bottom: 30px;
}
.job-report-number {
  font-size: 24px;
  margin-bottom: 8px;
}
.job-report-id {
  font-size: 22px;
  color: rgb(188, 188, 188);
}
.job-report__wrap {
  display: flex;
  justify-content: space-between;
  margin-top: 20px;
}

.download-file {
  margin-top: 20px;
}
.download-file a {
  text-decoration: none;
  cursor: pointer;
  background-color: #1a1d88;
  color: #fff;
  padding: 5px 10px;
  border-radius: 2px;
}

@media (max-width: 1050px) {
  .job-report-video video {
    width: 400px;
    height: 300px;
    margin-bottom: 1rem;
  }
}
@media (max-width: 700px) {
  .job-report__wrap {
    flex-direction: column-reverse;
    justify-content: center;
    align-items: center;
  }
   .download-file {
    margin-bottom: 1rem;
  }
}
@media (max-width: 455px) {
  .job-report-video video {
    width: 300px;
    height: 200px;
  }
}
</style>