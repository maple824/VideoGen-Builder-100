# Day002 - 仓库规范与每日学习模板

## 今日定位

Day002 的目标不是学习具体的视频生成模型，而是建立后续 100 天学习所需的记录规范。

从 Day003 开始，每一天都会产生代码、命令、输出、错误记录、实验结果或复盘。如果没有统一模板，学习记录会很快变成零散笔记，不利于复盘，也不利于后续作为 GitHub 项目展示。

因此，Day002 的核心价值是：为后续学习建立统一的记录格式，让每一天的内容都可读、可检查、可复现。

---

## 今日目标

今天需要完成三类模板：

1. 每日学习模板
   用于记录每天的学习目标、任务、命令、输出和复盘。

2. Debug 记录模板
   用于记录环境配置、代码运行、依赖安装、模型推理过程中遇到的问题。

3. 实验 metadata 模板
   用于记录后续生成实验中的模型名称、输入、参数、输出路径、运行时间和失败原因。

---

## 为什么需要模板

视频生成方向的学习会涉及大量实验，例如：

* FFmpeg 视频转码
* OpenCV 抽帧与图像处理
* PyTorch 模型训练与推理
* Diffusers 图像生成与视频生成
* ComfyUI 工作流调试
* Prompt、seed、steps、guidance 等参数对比
* 生成结果评估与失败案例整理

这些内容如果只写成普通笔记，后期很难复现。

统一模板可以帮助我做到：

* 每天知道该记录什么
* 每个实验都能追溯输入和输出
* 每个错误都能形成排障经验
* 每次 commit 都有明确目的
* GitHub 访客可以快速理解项目进展

---

## 今日产物

今天需要创建以下文件：

```text
docs/day-template.md
docs/debug-template.md
docs/experiment-metadata-template.md
days/day002/README.md
```

其中：

* `docs/day-template.md`：每日学习记录模板
* `docs/debug-template.md`：问题排查记录模板
* `docs/experiment-metadata-template.md`：实验参数记录模板
* `days/day002/README.md`：Day002 当天学习记录

---

## 今日任务

* [ ] 编写 `docs/day-template.md`
* [ ] 编写 `docs/debug-template.md`
* [ ] 编写 `docs/experiment-metadata-template.md`
* [ ] 检查模板是否适合后续 Python、FFmpeg、OpenCV、PyTorch、Diffusers 和 ComfyUI 阶段
* [ ] 提交 Day002 文件
* [ ] 推送到 GitHub

---

## 模板设计原则

模板需要遵循以下原则：

1. 简洁
   每天都要能填写，不能过重。

2. 可执行
   每个任务都要尽量对应命令、代码或输出。

3. 可复现
   关键环境、输入、参数和输出路径要记录清楚。

4. 可排障
   遇到问题时，要记录报错、原因分析和解决方式。

5. 可展示
   内容要适合作为公开 GitHub 项目的一部分。

---

## 今日完成情况

* [ ] 已创建 `days/day002/README.md`
* [ ] 已创建 `docs/day-template.md`
* [ ] 已创建 `docs/debug-template.md`
* [ ] 已创建 `docs/experiment-metadata-template.md`
* [ ] 已完成 Git commit
* [ ] 已 push 到 GitHub

---

## 今日结论

已完成。

完成 Day002 后，项目将具备统一的学习记录规范。
从 Day003 开始，可以正式进入 Python 工程基础阶段。
