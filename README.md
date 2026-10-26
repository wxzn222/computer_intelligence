# 计算智能实验

本仓库用于保存“计算智能”课程实验的个人实现、运行结果和实验报告。

- 姓名：何嘉欣
- 班级：24计科4班
- 学号：2410311411
- 仓库：https://github.com/wxzn222/computer_intelligence

## 实验目录

| 序号 | 实验 | 状态 |
| :--: | :-- | :--: |
| 01 | [产生式规则推理与动物识别](实验01_产生式规则推理与动物识别/README.md) | 已完成 |

## 实验一交付物

- 源代码：`knowledge_base.py`、`inference_engine.py`、`run_experiment.py`、`test_inference.py`、`student_identity.py`
- 运行结果：`outputs/inference_result.json`、`outputs/student_identity.json`
- 运行日志：`outputs/*.txt`
- 运行截图：`screenshots/*.png`
- 实验报告：[《计算智能》实验一报告.docx](实验01_产生式规则推理与动物识别/《计算智能》实验一报告.docx)

## 复现方式

```powershell
Set-Location -LiteralPath ".\实验01_产生式规则推理与动物识别"
py -3.12 -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python -m unittest -v test_inference.py
python run_experiment.py
```

实验一的基础知识库包含 15 条规则，另有 1 条仅用于分析题测试的扩展规则 R16。自动测试共 5 项，全部通过。
