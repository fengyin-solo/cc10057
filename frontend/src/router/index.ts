import { createRouter, createWebHistory } from 'vue-router'

import Dashboard from '@/views/Dashboard.vue'
const PipelineSection = () => import('@/views/pipeline_section/index.vue')
const Manhole = () => import('@/views/manhole/index.vue')
const PumpNode = () => import('@/views/pump_node/index.vue')
const CctvInspect = () => import('@/views/cctv_inspect/index.vue')
const Repair = () => import('@/views/repair/index.vue')
const TrenchlessRepair = () => import('@/views/trenchless_repair/index.vue')
const Relocation = () => import('@/views/relocation/index.vue')
const EmergencyCrew = () => import('@/views/emergency_crew/index.vue')
const EmergencyEvent = () => import('@/views/emergency_event/index.vue')
const WaterQuality = () => import('@/views/water_quality/index.vue')
const FlowMeter = () => import('@/views/flow_meter/index.vue')
const Valve = () => import('@/views/valve/index.vue')
const Hydrant = () => import('@/views/hydrant/index.vue')
const TrenchDig = () => import('@/views/trench_dig/index.vue')
const MaterialStore = () => import('@/views/material_store/index.vue')
const PatrolTask = () => import('@/views/patrol_task/index.vue')
const PressureMonitor = () => import('@/views/pressure_monitor/index.vue')
const GisMap = () => import('@/views/gis_map/index.vue')

const router = createRouter({
  history: createWebHistory(),
  routes: [
    { path: '/', name: 'dashboard', component: Dashboard },
    { path: '/pipeline_section', name: 'pipeline_section', component: PipelineSection },
    { path: '/manhole', name: 'manhole', component: Manhole },
    { path: '/pump_node', name: 'pump_node', component: PumpNode },
    { path: '/cctv_inspect', name: 'cctv_inspect', component: CctvInspect },
    { path: '/repair', name: 'repair', component: Repair },
    { path: '/trenchless_repair', name: 'trenchless_repair', component: TrenchlessRepair },
    { path: '/relocation', name: 'relocation', component: Relocation },
    { path: '/emergency_crew', name: 'emergency_crew', component: EmergencyCrew },
    { path: '/emergency_event', name: 'emergency_event', component: EmergencyEvent },
    { path: '/water_quality', name: 'water_quality', component: WaterQuality },
    { path: '/flow_meter', name: 'flow_meter', component: FlowMeter },
    { path: '/valve', name: 'valve', component: Valve },
    { path: '/hydrant', name: 'hydrant', component: Hydrant },
    { path: '/trench_dig', name: 'trench_dig', component: TrenchDig },
    { path: '/material_store', name: 'material_store', component: MaterialStore },
    { path: '/patrol_task', name: 'patrol_task', component: PatrolTask },
    { path: '/pressure_monitor', name: 'pressure_monitor', component: PressureMonitor },
    { path: '/gis_map', name: 'gis_map', component: GisMap },
  ],
})

export default router
