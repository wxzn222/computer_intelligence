# 实验 01：产生式规则推理与动物识别

## 实验内容

使用产生式规则表示动物识别知识，实现可追踪的多轮前向推理。系统从输入事实出发，先推导哺乳类、鸟类、食肉类、有蹄类等中间类别，再识别金钱豹、企鹅等具体动物，并保存完整推理轨迹。

## 已实现功能

- 15 条基础规则：R01～R15，其中 8 条类别规则、7 条动物规则
- 规则前提使用 `frozenset`，运行事实使用 `set`
- 通过 `fired_ids` 防止规则重复触发
- 按固定点条件结束推理，并记录轮次、规则编号、前提和结论
- 拒绝未知事实和空输入
- 输出 `outputs/inference_result.json`
- 身份登记与两张带学号运行截图
- 5 项自动测试全部通过
- 分析题扩展规则 R16，仅用于测试，不改变基础 15 条规则

## 文件说明

| 文件 | 作用 |
| :-- | :-- |
| `knowledge_base.py` | 事实标签、Rule 数据类、15 条基础规则和 R16 扩展规则 |
| `inference_engine.py` | 前向推理、规则触发、轨迹记录和动物提取 |
| `run_experiment.py` | 命令行输入、终端输出和 JSON 保存 |
| `test_inference.py` | 金钱豹、企鹅、无法确定、防重复触发和扩展规则测试 |
| `student_identity.py` | 学号登记、校验码生成和运行身份显示 |
| `outputs/` | 身份文件、JSON 结果和运行日志 |
| `screenshots/` | 环境、测试和最终验收截图 |
| `《计算智能》实验一报告.docx` | 完整实验报告 |

## 运行

```powershell
py -3.12 -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python -m unittest -v test_inference.py
python run_experiment.py
```

## 验收案例

```powershell
python run_experiment.py --facts "has_feathers,cannot_fly,swims,black_white"
python run_experiment.py --facts "long_legs"
python -c "from run_experiment import parse_facts; parse_facts('has_hair,unknown_fact')"
```

默认案例应识别为“金钱豹”，企鹅案例应识别为“企鹅”，信息不足案例应显示“无法确定”，非法事实应抛出 `ValueError`。

## 仓库

https://github.com/wxzn222/computer_intelligence
