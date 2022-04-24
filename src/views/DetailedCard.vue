<template>
  <div class="detailed-card">
    <div class="container">
      <div class="detailed-card__wrapper">
        <router-link to="/" class="detailed-card__arrow">
          <span>Назад</span>
        </router-link>
        <div class="detailed-card-filters">
          <button @click="handleCardFilter" data-name="today">Today</button>
          <button @click="handleCardFilter" data-name="clear">Clear</button>
        </div>
        <div class="detailed-card__top">
          <p class="detailed-card__title">
            {{ data?.title }}
            <span class="detailed-card__id"> №{{ data?.id }} </span>
          </p>
        </div>
        <div class="detailed-card__body">
          <div v-if="!jobReports?.length">
            <p>No video at the moment</p>
          </div>
          <div
            class="detailed-card__item"
            v-for="job in jobReports"
            :key="job['created_at']"
          >
            <div class="detailed-card__item-video">
              <video :src="job.video" width="350" height="250" controls>
                <source :src="job.video" type="video/mp4" />
              </video>
            </div>
            <router-link
              class="detailed-card__item-info"
              :to="{
                name: 'JobReport',
                params: { id: job.id, parentId: id },
              }"
            >
              <p class="detailed-card__item-number">
                Camera №{{ job.camera }} |
                <span class="detailed-card__item-id">ID №{{ job.id }}</span>
              </p>
              <p class="detailed-card__item-created">{{ job["created_at"] }}</p>
              <p class="detailed-card__item-statistics">
                {{ job.statistics.slice(0, 50) }}...
              </p>
            </router-link>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "DetailedCard",
  props: ["id"],
  components: {},
  data() {
    const data = null;
    const jobReports = null;
    const hiddenData = null;
    return {
      data,
      hiddenData,
      jobReports,
    };
  },
  methods: {
    async getData() {
      const detailedData = await this.$axios.get(`/api/v1/cameras/${this.id}`);
      this.data = detailedData.data;
      this.jobReports = detailedData.data.job_reports;
    },
    async handleCardFilter(event) {
      switch (event.target.dataset.name) {
        case "today": {
          const detailedData = await this.$axios.get(
            `/api/v1/job-report?camera=${this.id}&created_at=${this.getToday()}`
          );
          this.jobReports = detailedData.data;
          break;
        }
        case "clear": {
          const detailedData = await this.$axios.get(
            `/api/v1/cameras/${this.id}`
          );
          this.jobReports = detailedData.data.job_reports;
          break;
        }
      }
    },
    getToday() {
      return new Date().toISOString().slice(0, 10);
    },
  },
  async mounted() {
    await this.getData();
  },
};
</script>

<style scoped>
.detailed-card__title {
  font-size: 26px;
  line-height: 1.2;
  color: rgb(255, 255, 255);
  margin-bottom: 1rem;
}
.detailed-card__id {
  font-size: 22px;
  color: rgb(144, 144, 144);
}
.detailed-card__item {
  display: flex;
  justify-content: space-between;
  margin-bottom: 30px;
}
.detailed-card__item-info {
  width: 80%;
  text-decoration: none;
  color: #fff;
}
.detailed-card__item-video {
  width: 300px;
  margin-right: 90px;
}
.detailed-card__item-number {
  font-size: 24px;
  margin-bottom: 8px;
}
.detailed-card__item-id {
  font-size: 22px;
  color: rgb(188, 188, 188);
}
.detailed-card__item-created {
  margin-bottom: 8px;
}
.detailed-card__item-statistics {
  line-height: 1.2;
}
.detailed-card__arrow {
  position: relative;
  height: 2px;
  width: 36px;
  display: block;
  background-color: #fff;
  margin: 1rem 0 3rem;
}
.detailed-card__arrow::after {
  content: "";
  position: absolute;
  left: -2px;
  top: 6px;
  height: 2px;
  width: 18px;
  background-color: #fff;
  transform: rotate(45deg);
}
.detailed-card__arrow::before {
  content: "";
  position: absolute;
  left: -2px;
  top: -6px;
  height: 2px;
  width: 18px;
  background-color: #fff;
  transform: rotate(-45deg);
}
.detailed-card__arrow span {
  color: #fff;
  font-size: 22px;
  position: relative;
  top: -15px;
  left: 45px;
}
.detailed-card-filters {
  width: 100%;
  padding: 12px;
  margin-bottom: 30px;
  background-color: #08092a;
  border-radius: 4px;
  display: flex;
}
.detailed-card-filters button {
  padding: 5px 10px;
  margin: 0 10px;
  color: #fff;
  background-color: #1a1d88;
  border: none;
  border-radius: 4px;
  font-family: inherit;
  font-size: 16px;
}

@media (max-width: 700px) {
  .detailed-card__item {
    flex-direction: column;
    justify-content: center;
    align-items: center;
  }
  .detailed-card__item-video {
    margin-bottom: 1rem;
  }
}
</style>