# 实验 Metadata 记录模板

> 用途：记录后续图像生成、视频生成、模型推理、参数对比实验的关键信息。
> 原则：每次实验都要能回答三个问题：用了什么输入、用了什么参数、得到了什么结果。

---

# Experiment - 实验标题

## 实验编号

```text
EXP-YYYYMMDD-001
```

示例：

```text
EXP-20260604-001
```

---

## 实验日期

```text
YYYY-MM-DD
```

---

## 所属阶段

```text
示例：
Phase 6 - Diffusers 图像与视频生成
Day080 - image-to-video 入门
```

---

## 实验目标

说明这次实验想验证什么。

示例：

```text
比较不同 num_frames 设置对视频时长、运动连续性和生成耗时的影响。
```

---

## 实验类型

* [ ] 视频预处理
* [ ] 图像处理
* [ ] 模型训练
* [ ] 图像生成
* [ ] 图生视频
* [ ] 文生视频
* [ ] ComfyUI workflow
* [ ] 评估实验
* [ ] 其他：

---

## 环境信息

```text
操作系统：
Python 版本：
Conda 环境：
GPU：
CUDA：
PyTorch：
Diffusers：
ComfyUI：
FFmpeg：
```

不相关的项目可以写“未使用”。

---

## 输入信息

### 输入文件

```text
待填写
```

示例：

```text
assets/input/sample.png
assets/input/sample.mp4
```

### 输入文本 / Prompt

```text
待填写
```

### Negative Prompt

```text
待填写
```

没有则写“无”。

---

## 模型信息

```text
模型名称：
模型来源：
模型版本：
本地路径：
是否使用 LoRA：
是否使用 ControlNet：
是否使用量化：
```

没有用到的项目写“未使用”。

---

## 核心参数

```yaml
seed:
steps:
guidance_scale:
width:
height:
num_frames:
fps:
scheduler:
dtype:
device:
```

不相关参数可以删除或写 `null`。

---

## 运行命令

```bash
待填写
```

---

## 输出信息

### 输出文件

```text
待填写
```

示例：

```text
outputs/experiments/EXP-20260604-001/result.mp4
outputs/experiments/EXP-20260604-001/metadata.json
```

### 运行耗时

```text
待填写
```

### 显存占用

```text
待填写
```

没有记录则写“未记录”。

---

## 实验结果

简要描述实验结果。

```text
待填写
```

---

## 质量观察

从以下维度记录结果。

### 画面质量

```text
待填写
```

### 运动连续性

```text
待填写
```

### Prompt 遵循程度

```text
待填写
```

### 闪烁 / 抖动

```text
待填写
```

### 身份一致性

```text
待填写
```

### 失败现象

```text
待填写
```

---

## 结论

本次实验得到的明确结论。

```text
待填写
```

---

## 后续改进

下一次实验要调整什么。

* [ ] 更换 prompt
* [ ] 固定 seed 后对比参数
* [ ] 调整 steps
* [ ] 调整 guidance scale
* [ ] 调整分辨率
* [ ] 调整 num_frames
* [ ] 调整 fps
* [ ] 更换模型
* [ ] 优化显存
* [ ] 增加评估指标

其他：

```text
待填写
```

---

## 关联文件

```text
待填写
```

示例：

```text
scripts/run_i2v.py
outputs/experiments/EXP-20260604-001/metadata.json
days/day080/README.md
```
