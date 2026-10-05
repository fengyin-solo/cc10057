"""业务模块路由汇总。

这里统一按别名导入再暴露 ROUTERS：模块名有可能和内置名撞车（某个业务模块就叫 dict、list
这种名字时），按名字直接 import 会把内置类型覆盖掉，函数注解在运行时求值就会报
'module' object is not subscriptable。
"""
from __future__ import annotations

from app.routers import pipeline_section as router_pipeline_section
from app.routers import manhole as router_manhole
from app.routers import pump_node as router_pump_node
from app.routers import cctv_inspect as router_cctv_inspect
from app.routers import repair as router_repair
from app.routers import trenchless_repair as router_trenchless_repair
from app.routers import relocation as router_relocation
from app.routers import emergency_crew as router_emergency_crew
from app.routers import emergency_event as router_emergency_event
from app.routers import water_quality as router_water_quality
from app.routers import flow_meter as router_flow_meter
from app.routers import valve as router_valve
from app.routers import hydrant as router_hydrant
from app.routers import trench_dig as router_trench_dig
from app.routers import material_store as router_material_store
from app.routers import patrol_task as router_patrol_task
from app.routers import pressure_monitor as router_pressure_monitor
from app.routers import gis_map as router_gis_map

ROUTERS = [router_pipeline_section, router_manhole, router_pump_node, router_cctv_inspect, router_repair, router_trenchless_repair, router_relocation, router_emergency_crew, router_emergency_event, router_water_quality, router_flow_meter, router_valve, router_hydrant, router_trench_dig, router_material_store, router_patrol_task, router_pressure_monitor, router_gis_map]
