<template>
  <div class="app-shell">
    <aside class="app-side">
      <h1 class="app-title">城市地下管网管理平台</h1>
      <nav class="nav-list">
        <RouterLink v-for="item in navItems" :key="item.path" :to="item.path" class="nav-item">
          {{ item.label }}
        </RouterLink>
      </nav>
    </aside>
    <main class="app-main">
      <header class="app-head">
        <span class="head-desc">面向管线段、检查井、泵站节点、检测维修、管线迁改与应急抢修的城市地下管网运维后台。</span>
        <span class="head-user">当前值班：{{ store.operator }} · {{ store.shiftLabel }}</span>
      </header>
      <RouterView />
    </main>
  </div>
</template>

<script setup lang="ts">
import { useSessionStore } from '@/stores/session'

const store = useSessionStore()

const navItems = [{ label: "运营概览", path: "/" }, { label: "管线段管理", path: "/pipeline_section" }, { label: "检查井管理", path: "/manhole" }, { label: "泵站节点", path: "/pump_node" }, { label: "管道检测", path: "/cctv_inspect" }, { label: "管道维修", path: "/repair" }, { label: "非开挖修复", path: "/trenchless_repair" }, { label: "管线迁改", path: "/relocation" }, { label: "抢修队伍", path: "/emergency_crew" }, { label: "爆管事件", path: "/emergency_event" }, { label: "管网水质", path: "/water_quality" }, { label: "流量计量", path: "/flow_meter" }, { label: "阀门管理", path: "/valve" }, { label: "消火栓管理", path: "/hydrant" }, { label: "道路开挖", path: "/trench_dig" }, { label: "物资仓库", path: "/material_store" }, { label: "管线巡查", path: "/patrol_task" }, { label: "压力监测", path: "/pressure_monitor" }, { label: "管线图层", path: "/gis_map" }]
</script>
