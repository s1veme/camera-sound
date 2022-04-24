<template>
  <router-link
    :to="{
      path: `/camera/${itemData.id}`,
      params: { id },
    }"
    class="general-card"
  >
    <div class="general-card__top">
      <p class="general-card__title">
        {{ itemData.title }}
        <span class="general-card__id"> №{{ itemData.id }} </span>
      </p>
    </div>
  </router-link>
</template>

<script>
export default {
  name: "GeneralCard",
  props: ["itemData"],
  components: {},
  data() {
    return {};
  },
};
</script>

<style scoped>
.general-card {
  height: 300px;
  width: 450px;
  background: rgb(3, 0, 19);
  border-radius: 16px;
  margin-right: 20px;
  padding: 15px;
}
.general-card__title {
  font-size: 22px;
  line-height: 1.2;
  color: rgb(255, 255, 255);
}
.general-card__id {
  color: rgb(144, 144, 144);
}
.general-card__image {
  width: 100%;
  height: 100%;
}
.general-card__video {
  width: 100px;
  height: 100%;
  object-fit: cover;
}

@media (max-width: 455px) {
  .general-card {
    height: 170px;
  }
  .general-card__title {
    font-size: 18px;
  }
  .general-card__id {
    font-size: 12px;
  }
}
</style>