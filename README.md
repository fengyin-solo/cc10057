# 城市地下管网管理平台

面向管线段、检查井、泵站节点、检测维修、管线迁改与应急抢修的城市地下管网运维后台。

这是一个前后端分离的管理平台：前端 Vue 3 + Vite + TypeScript，后端 FastAPI（Python）。
两边各自独立启动，前端 dev server 已关掉自动打开页面，启动后按终端打印的地址手工打开。

## 目录结构

```text
.
├── frontend/                 Vue 3 + Vite + TypeScript 前端
│   ├── src/views/            每个业务模块一个页面
│   ├── src/api/              统一请求封装
│   ├── src/stores/           会话与筛选状态
│   └── vite.config.ts        dev server 配置（open: false）
├── backend/                  FastAPI（Python） 后端
│   ├── app/routers/          每个业务模块一组接口
│   ├── app/services/         业务规则与状态流转
│   └── app/store.py          内存数据仓库与示例数据
├── .gitignore
└── docker-compose.yml
```

## 启动

### 后端

```bash
cd backend
python3 -m venv .venv && .venv/bin/pip install -r requirements.txt
./run.sh
```

健康检查：`curl http://127.0.0.1:8000/api/health`

### 前端

```bash
cd frontend
npm install
npm run dev
```

前端默认监听 `http://127.0.0.1:5173/`，dev server 不会自动打开浏览器，
需要自己访问。`/api` 由 vite 代理到后端 `http://127.0.0.1:8000`。

## 业务模块

| 模块 | 目录 | 业务对象 | 主要字段 |
| --- | --- | --- | --- |
| 管线段管理 | `pipeline_section` | 管线段 | 管段编号、管网类型、管材 |
| 检查井管理 | `manhole` | 检查井 | 井编号、井盖型号、所属管段 |
| 泵站节点 | `pump_node` | 泵站 | 泵站编号、泵站类型、装机容量 |
| 管道检测 | `cctv_inspect` | 管道检测 | 检测编号、检测管段、检测方式 |
| 管道维修 | `repair` | 维修任务 | 任务编号、维修管段、缺陷描述 |
| 非开挖修复 | `trenchless_repair` | 修复施工 | 施工编号、修复管段、修复工艺 |
| 管线迁改 | `relocation` | 迁改申请 | 申请编号、申请单位、迁改原因 |
| 抢修队伍 | `emergency_crew` | 抢修队伍 | 队伍编号、队伍名称、驻点位置 |
| 爆管事件 | `emergency_event` | 爆管事件 | 事件编号、发生时间、事发管段 |
| 管网水质 | `water_quality` | 水质采样点 | 采样点编号、所属管段、浊度 |
| 流量计量 | `flow_meter` | 流量计 | 表计编号、安装位置、表计口径 |
| 阀门管理 | `valve` | 阀门 | 阀门编号、阀门类型、公称压力 |
| 消火栓管理 | `hydrant` | 消火栓 | 栓编号、安装位置、出水口径 |
| 道路开挖 | `trench_dig` | 开挖审批 | 审批编号、申请单位、开挖原因 |
| 物资仓库 | `material_store` | 应急物资 | 物资编号、物资名称、规格型号 |
| 管线巡查 | `patrol_task` | 巡查任务 | 任务编号、巡查区域、巡查日期 |
| 压力监测 | `pressure_monitor` | 压力监测点 | 测点编号、所属管网、安装位置 |
| 管线图层 | `gis_map` | GIS图斑 | 图斑编号、图层名称、要素类型 |

## 约定

- 每个模块的前端页面在 `frontend/src/views/<模块>/index.vue`，后端接口在
  `backend/app/routers/<模块>.py`，业务规则在 `backend/app/services/<模块>.py`。
- 列表接口统一返回 `{ items, total, page, size }`，动作接口统一返回 `{ ok, message }`。
- 状态流转只允许在 `app/services` 里改，路由层不做业务判断。
