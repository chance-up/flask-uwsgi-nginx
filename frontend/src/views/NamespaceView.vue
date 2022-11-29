<template>
  <LayoutAuthenticated>
    <SectionMain>
      <SectionTitleLineWithButton
        :icon="mdiTableBorder"
        title="Namespaces"
        main
      />
      <CardBox class="mb-6" has-table>
        <TableSampleClients :namespaces="namespaces" checkable />
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
import TableSampleClients from "@/components/TableSampleClients.vue";
import CardBox from "@/components/CardBox.vue";
import LayoutAuthenticated from "@/layouts/LayoutAuthenticated.vue";
import SectionTitleLineWithButton from "@/components/SectionTitleLineWithButton.vue";
import Repo from "@/repository/resourceRepository";
import { onMounted, ref } from "vue";

const repo = new Repo();
const namespaces = ref();
const getAll = async () => {
  repo.getAll().then((res) => {
    namespaces.value = res.data;
    console.log(namespaces.value);
  });
};

onMounted(() => {
  getAll();
});
</script>
