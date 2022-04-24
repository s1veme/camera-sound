<template>
  <div class="list-cards">
    <div class="container">
      <div class="list-cards__wrapper">
        <general-card
          v-for="itemData in cardsData"
          :key="itemData.id"
          :itemData="itemData"
        />
      </div>
      <load-test-data v-if="!isLoaded" />
      <button class="load-test-data__button button" @click="getData" v-if="!isLoaded">
        Получить тестовые данные (После того, как загрузили)
      </button>
    </div>
  </div>
</template>

<script>
import GeneralCard from "@/components/card/GeneralCard.vue";
import LoadTestData from "@/components/test-data/LoadTestData.vue";

export default {
  name: "ListCards",

  components: {
    GeneralCard,
    LoadTestData,
  },

  data() {
    let cardsData = null;
    const isLoaded = false
    return {
      cardsData,
      isLoaded
    };
  },

  methods: {
    async getData() {
      const response = await this.$axios.get("/api/v1/cameras/");
      this.cardsData = response.data;
      this.isLoaded = true
    },
  },
  mounted() {
    if (!this.cardsData) {
      this.getData();
    }
  },
};
</script>

<style scoped>
.list-cards__wrapper {
  display: flex;
}
.load-test-data__button {
  font-size: 14px;
}
</style>