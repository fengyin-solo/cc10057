"""接口出入参模型：列表分页、动作结果与各模块的明细结构。"""
from __future__ import annotations

from typing import Any, Generic, TypeVar

from pydantic import BaseModel, Field

T = TypeVar("T")


class PageResult(BaseModel, Generic[T]):
    items: list[T]
    total: int
    page: int = 1
    size: int = 20


class ActionResult(BaseModel):
    ok: bool
    message: str
    entry: dict[str, Any] | None = None


class EntryPayload(BaseModel):
    """登记或修改一条业务记录时提交的字段集合。"""

    values: dict[str, Any] = Field(default_factory=dict)
    remark: str | None = None



class PipelineSectionEntry(BaseModel):
    """管线段明细结构。"""

    field_0: str | None = None  # 管段编号
    field_1: str | None = None  # 管网类型
    field_2: str | None = None  # 管材
    field_3: str | None = None  # 管径
    field_4: str | None = None  # 铺设深度
    field_5: str | None = None  # 施工日期
    field_6: str | None = None  # 设计年限
    field_7: str | None = None  # 管段状态

class ManholeEntry(BaseModel):
    """检查井明细结构。"""

    field_0: str | None = None  # 井编号
    field_1: str | None = None  # 井盖型号
    field_2: str | None = None  # 所属管段
    field_3: str | None = None  # 井深
    field_4: str | None = None  # 坐标经度
    field_5: str | None = None  # 坐标纬度
    field_6: str | None = None  # 最近巡查日期
    field_7: str | None = None  # 井体状态

class PumpNodeEntry(BaseModel):
    """泵站明细结构。"""

    field_0: str | None = None  # 泵站编号
    field_1: str | None = None  # 泵站类型
    field_2: str | None = None  # 装机容量
    field_3: str | None = None  # 设计流量
    field_4: str | None = None  # 运行扬程
    field_5: str | None = None  # 集水池水位
    field_6: str | None = None  # 格栅状态
    field_7: str | None = None  # 运行状态

class CctvInspectEntry(BaseModel):
    """管道检测明细结构。"""

    field_0: str | None = None  # 检测编号
    field_1: str | None = None  # 检测管段
    field_2: str | None = None  # 检测方式
    field_3: str | None = None  # 检测日期
    field_4: str | None = None  # 检测人员
    field_5: str | None = None  # 缺陷等级
    field_6: str | None = None  # 检测报告编号
    field_7: str | None = None  # 检测状态

class RepairEntry(BaseModel):
    """维修任务明细结构。"""

    field_0: str | None = None  # 任务编号
    field_1: str | None = None  # 维修管段
    field_2: str | None = None  # 缺陷描述
    field_3: str | None = None  # 维修方案
    field_4: str | None = None  # 开工日期
    field_5: str | None = None  # 完工日期
    field_6: str | None = None  # 施工班组
    field_7: str | None = None  # 任务状态

class TrenchlessRepairEntry(BaseModel):
    """修复施工明细结构。"""

    field_0: str | None = None  # 施工编号
    field_1: str | None = None  # 修复管段
    field_2: str | None = None  # 修复工艺
    field_3: str | None = None  # 内衬材料
    field_4: str | None = None  # 修复长度
    field_5: str | None = None  # 固化时间
    field_6: str | None = None  # 气密检测结果
    field_7: str | None = None  # 施工状态

class RelocationEntry(BaseModel):
    """迁改申请明细结构。"""

    field_0: str | None = None  # 申请编号
    field_1: str | None = None  # 申请单位
    field_2: str | None = None  # 迁改原因
    field_3: str | None = None  # 迁改范围
    field_4: str | None = None  # 方案批复号
    field_5: str | None = None  # 开工条件
    field_6: str | None = None  # 接入位置
    field_7: str | None = None  # 申请状态

class EmergencyCrewEntry(BaseModel):
    """抢修队伍明细结构。"""

    field_0: str | None = None  # 队伍编号
    field_1: str | None = None  # 队伍名称
    field_2: str | None = None  # 驻点位置
    field_3: str | None = None  # 编制人数
    field_4: str | None = None  # 在岗人数
    field_5: str | None = None  # 值班班长
    field_6: str | None = None  # 值班电话
    field_7: str | None = None  # 队伍状态

class EmergencyEventEntry(BaseModel):
    """爆管事件明细结构。"""

    field_0: str | None = None  # 事件编号
    field_1: str | None = None  # 发生时间
    field_2: str | None = None  # 事发管段
    field_3: str | None = None  # 爆管原因
    field_4: str | None = None  # 影响范围
    field_5: str | None = None  # 抢修队伍
    field_6: str | None = None  # 恢复供水平时
    field_7: str | None = None  # 事件状态

class WaterQualityEntry(BaseModel):
    """水质采样点明细结构。"""

    field_0: str | None = None  # 采样点编号
    field_1: str | None = None  # 所属管段
    field_2: str | None = None  # 浊度
    field_3: str | None = None  # 余氯值
    field_4: str | None = None  # pH值
    field_5: str | None = None  # 菌落总数
    field_6: str | None = None  # 铁锰含量
    field_7: str | None = None  # 采样点状态

class FlowMeterEntry(BaseModel):
    """流量计明细结构。"""

    field_0: str | None = None  # 表计编号
    field_1: str | None = None  # 安装位置
    field_2: str | None = None  # 表计口径
    field_3: str | None = None  # 瞬时流量
    field_4: str | None = None  # 累计流量
    field_5: str | None = None  # 压力值
    field_6: str | None = None  # 远传状态
    field_7: str | None = None  # 表计状态

class ValveEntry(BaseModel):
    """阀门明细结构。"""

    field_0: str | None = None  # 阀门编号
    field_1: str | None = None  # 阀门类型
    field_2: str | None = None  # 公称压力
    field_3: str | None = None  # 安装位置
    field_4: str | None = None  # 启闭状态
    field_5: str | None = None  # 操作记录
    field_6: str | None = None  # 润滑周期
    field_7: str | None = None  # 阀门状态

class HydrantEntry(BaseModel):
    """消火栓明细结构。"""

    field_0: str | None = None  # 栓编号
    field_1: str | None = None  # 安装位置
    field_2: str | None = None  # 出水口径
    field_3: str | None = None  # 静压值
    field_4: str | None = None  # 最近试水日期
    field_5: str | None = None  # 防盗链状态
    field_6: str | None = None  # 油漆状况
    field_7: str | None = None  # 栓状态

class TrenchDigEntry(BaseModel):
    """开挖审批明细结构。"""

    field_0: str | None = None  # 审批编号
    field_1: str | None = None  # 申请单位
    field_2: str | None = None  # 开挖原因
    field_3: str | None = None  # 开挖路段
    field_4: str | None = None  # 开挖面积
    field_5: str | None = None  # 计划工期
    field_6: str | None = None  # 交通疏导方案
    field_7: str | None = None  # 审批状态

class MaterialStoreEntry(BaseModel):
    """应急物资明细结构。"""

    field_0: str | None = None  # 物资编号
    field_1: str | None = None  # 物资名称
    field_2: str | None = None  # 规格型号
    field_3: str | None = None  # 安全存量
    field_4: str | None = None  # 当前存量
    field_5: str | None = None  # 存放仓库
    field_6: str | None = None  # 最近入库日
    field_7: str | None = None  # 物资状态

class PatrolTaskEntry(BaseModel):
    """巡查任务明细结构。"""

    field_0: str | None = None  # 任务编号
    field_1: str | None = None  # 巡查区域
    field_2: str | None = None  # 巡查日期
    field_3: str | None = None  # 巡查人员
    field_4: str | None = None  # 发现问题数
    field_5: str | None = None  # 导航轨迹
    field_6: str | None = None  # 巡查里程
    field_7: str | None = None  # 任务状态

class PressureMonitorEntry(BaseModel):
    """压力监测点明细结构。"""

    field_0: str | None = None  # 测点编号
    field_1: str | None = None  # 所属管网
    field_2: str | None = None  # 安装位置
    field_3: str | None = None  # 额定压力
    field_4: str | None = None  # 当前压力
    field_5: str | None = None  # 波动范围
    field_6: str | None = None  # 远传间隔
    field_7: str | None = None  # 运行状态

class GisMapEntry(BaseModel):
    """GIS图斑明细结构。"""

    field_0: str | None = None  # 图斑编号
    field_1: str | None = None  # 图层名称
    field_2: str | None = None  # 要素类型
    field_3: str | None = None  # 测绘日期
    field_4: str | None = None  # 数据来源
    field_5: str | None = None  # 更新方式
    field_6: str | None = None  # 坐标系统
    field_7: str | None = None  # 图层状态
