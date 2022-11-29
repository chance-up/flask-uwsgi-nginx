<template>
  <LayoutAuthenticated>
    <SectionMain>
      <SectionTitleLineWithButton :icon="mdiTableBorder" title="Cluster" main>
      </SectionTitleLineWithButton>
      <!-- <NotificationBar color="info" :icon="mdiMonitorCellphone">
        <b>Responsive table.</b> Collapses on mobile
      </NotificationBar> -->

      <CardBox class="mb-6" has-table>
        <TableCluster :clusters="clusters" checkable />
      </CardBox>
    </SectionMain>
  </LayoutAuthenticated>
</template>

<script setup>
import {
  mdiMonitorCellphone,
  mdiTableBorder,
  mdiTableOff,
  mdiGithub,
} from "@mdi/js";
import SectionMain from "@/components/SectionMain.vue";
import NotificationBar from "@/components/NotificationBar.vue";
import TableCluster from "@/components/TableCluster.vue";
import CardBox from "@/components/CardBox.vue";
import LayoutAuthenticated from "@/layouts/LayoutAuthenticated.vue";
import SectionTitleLineWithButton from "@/components/SectionTitleLineWithButton.vue";
import Repo from "@/repository/resourceRepository";
import { onMounted, ref } from "vue";

const repo = new Repo();
const clusters = ref();
const getClusterInfo = async () => {
  repo.getClusterInfo().then((res) => {
    clusters.value = res.data;
    console.log(clusters.value);
  });
};

onMounted(() => {
  getClusterInfo();
});
</script>
