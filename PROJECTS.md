# PROJECTS

本文件记录 `VideoGen Builder 100` 的项目作品规划。

本仓库不是只做学习笔记，而是要在 100 天过程中逐步形成可以展示的 GitHub 项目作品集。

---

## 项目设计原则

每个项目都需要满足以下要求：

1. 有明确问题
   说明这个项目解决什么问题。

2. 有可运行代码
   不能只写说明文档。

3. 有输入和输出
   明确输入文件、参数和输出结果。

4. 有 README
   说明安装、运行、示例和限制。

5. 有错误记录
   记录至少一个实际遇到的问题或边界情况。

6. 有展示材料
   可以是截图、压缩 demo、metadata、报告或 GitHub Pages 页面。

---

# 项目总览

| 编号         | 项目名称                          | 所属阶段    | 目标               |
| ---------- | ----------------------------- | ------- | ---------------- |
| Project 01 | Asset Scanner CLI             | Phase 1 | 扫描素材目录，输出文件清单    |
| Project 02 | Video Preprocess CLI          | Phase 2 | 批量处理视频文件         |
| Project 03 | Video Frame Analyzer          | Phase 3 | 分析视频帧、关键帧和基础质量   |
| Project 04 | Frame Classifier              | Phase 4 | 训练和推理一个小型帧分类模型   |
| Project 05 | Mini Diffusion Lab            | Phase 5 | 记录生成模型基础实验       |
| Project 06 | Text / Image-to-Video Lab     | Phase 6 | 跑通图像生成与视频生成实验    |
| Project 07 | ComfyUI Workflow Zoo          | Phase 7 | 管理 ComfyUI 工作流集合 |
| Project 08 | VideoGen Evaluation Dashboard | Phase 8 | 整理视频生成评估结果       |
| Project 09 | GitHub Pages Portfolio        | Phase 8 | 发布项目作品集页面        |

---

# Project 01 - Asset Scanner CLI

## 所属阶段

```text
Phase 1 - Python 工程基础
Day014
```

## 项目目标

实现一个素材扫描命令行工具。

输入一个目录，扫描其中的视频、图片、音频和文本文件，输出文件清单和格式统计。

## 为什么需要这个项目

后续视频生成实验会产生大量素材，包括：

* 输入图片
* 输入视频
* 抽帧结果
* 生成结果
* metadata 文件
* prompt 文件
* workflow 文件

如果没有素材管理能力，后续实验会变得混乱。

## 计划功能

* [ ] 支持输入目录
* [ ] 递归扫描文件
* [ ] 统计文件类型
* [ ] 输出文件路径清单
* [ ] 保存 CSV 或 JSON manifest
* [ ] 对空目录给出提示
* [ ] 对不存在路径给出错误信息

## 计划文件

```text
scripts/scan_assets.py
src/videogen_builder/assets.py
tests/test_assets.py
outputs/asset_manifest.csv
```

## 示例命令

```bash
python scripts/scan_assets.py --input assets --output outputs/asset_manifest.csv
```

## 预期输出

```text
扫描完成
总文件数：12
视频文件：3
图片文件：6
音频文件：1
其他文件：2
输出文件：outputs/asset_manifest.csv
```

---

# Project 02 - Video Preprocess CLI

## 所属阶段

```text
Phase 2 - 视频工程基础
Day028
```

## 项目目标

实现一个视频预处理命令行工具。

支持读取视频信息、抽帧、裁剪、resize、格式转换和批量处理。

## 为什么需要这个项目

视频生成模型通常对输入视频或输入图片有格式要求，例如：

* 分辨率
* 帧率
* 视频时长
* 编码格式
* 文件大小
* 是否包含音频

视频预处理能力是后续图生视频、视频编辑、视频评估的基础。

## 计划功能

* [ ] 读取视频基本信息
* [ ] 抽帧
* [ ] 帧合成视频
* [ ] 裁剪视频
* [ ] resize 视频
* [ ] 转换格式
* [ ] 提取音频
* [ ] 添加水印或文字
* [ ] 批量处理目录
* [ ] 生成处理日志

## 计划文件

```text
projects/video_preprocess_cli/
scripts/video_info.py
scripts/extract_frames.py
scripts/frames_to_video.py
scripts/trim_video.py
scripts/resize_video.py
scripts/batch_preprocess.py
```

## 示例命令

```bash
python scripts/video_info.py --input assets/sample.mp4
python scripts/extract_frames.py --input assets/sample.mp4 --output outputs/frames
python scripts/frames_to_video.py --input outputs/frames --output outputs/rebuild.mp4
```

## 预期输出

```text
视频信息读取成功
抽帧完成
帧合成视频完成
```

---

# Project 03 - Video Frame Analyzer

## 所属阶段

```text
Phase 3 - 图像与视频处理基础
Day042
```

## 项目目标

实现一个视频帧分析工具。

对输入视频进行逐帧读取、关键帧提取、基础质量分析和报告生成。

## 为什么需要这个项目

视频生成结果评估需要观察：

* 是否明显闪烁
* 是否出现画面突变
* 是否有运动连续性问题
* 是否模糊
* 是否亮度异常
* 哪些帧可以代表整个视频

Frame Analyzer 是后续视频生成评估的基础工具。

## 计划功能

* [ ] 逐帧读取视频
* [ ] 计算帧数和 fps
* [ ] 提取关键帧
* [ ] 生成缩略图网格
* [ ] 计算帧间差异
* [ ] 检测模糊程度
* [ ] 生成 Markdown 报告
* [ ] 输出 CSV 分析结果

## 计划文件

```text
projects/video_frame_analyzer/
scripts/read_video.py
scripts/keyframe_extract.py
scripts/frame_diff.py
scripts/contact_sheet.py
scripts/video_quality_basic.py
```

## 示例命令

```bash
python scripts/keyframe_extract.py --input assets/sample.mp4 --output outputs/keyframes
python scripts/contact_sheet.py --input outputs/keyframes --output outputs/contact_sheet.jpg
```

## 预期输出

```text
关键帧提取完成
缩略图生成完成
分析报告已保存
```

---

# Project 04 - Frame Classifier

## 所属阶段

```text
Phase 4 - 深度学习基础
Day056
```

## 项目目标

训练一个小型图像帧分类模型。

目标不是追求高精度，而是掌握 PyTorch 项目的基本训练和推理流程。

## 为什么需要这个项目

后续使用生成模型时，需要理解：

* Tensor 是什么
* batch 是什么
* device 是什么
* checkpoint 是什么
* 推理和训练有什么区别
* 如何记录模型实验

## 计划功能

* [ ] 构建最小 Dataset
* [ ] 构建 DataLoader
* [ ] 编写 CNN 模型
* [ ] 编写训练循环
* [ ] 保存 checkpoint
* [ ] 编写推理脚本
* [ ] 记录训练参数和结果

## 计划文件

```text
projects/frame_classifier/
datasets/frame_dataset.py
scripts/train_classifier.py
scripts/predict.py
outputs/checkpoints/
```

## 示例命令

```bash
python scripts/train_classifier.py --config configs/frame_classifier.yaml
python scripts/predict.py --checkpoint outputs/checkpoints/model.pt --input assets/sample.jpg
```

## 预期输出

```text
训练完成
checkpoint 已保存
推理完成
```

---

# Project 05 - Mini Diffusion Lab

## 所属阶段

```text
Phase 5 - 生成模型基础
Day070
```

## 项目目标

建立一个生成模型基础实验室。

记录 AutoEncoder、VAE、Diffusion、Prompt、seed、steps 等基础实验。

## 为什么需要这个项目

视频生成模型建立在图像生成和扩散模型基础上。
如果不理解生成模型的基本逻辑，后续使用 Diffusers 或 ComfyUI 时就只能机械调参。

## 计划功能

* [ ] 记录生成任务分类
* [ ] 实现 AutoEncoder 重建实验
* [ ] 整理 VAE 笔记
* [ ] 整理 Diffusion 加噪和去噪示意
* [ ] 记录 seed 对结果的影响
* [ ] 记录 steps 对结果的影响
* [ ] 整理失败案例
* [ ] 保存实验 metadata

## 计划文件

```text
projects/mini_diffusion_lab/
experiments/
outputs/experiments/
docs/diffusion-notes.md
```

## 示例命令

```bash
python scripts/run_toy_diffusion.py --config configs/toy_diffusion.yaml
```

## 预期输出

```text
实验完成
metadata 已保存
结果已保存到 outputs/experiments/
```

---

# Project 06 - Text / Image-to-Video Lab

## 所属阶段

```text
Phase 6 - Diffusers 图像与视频生成
Day084
```

## 项目目标

建立一个可复现的视频生成实验项目。

支持记录 text-to-image、image-to-image、image-to-video、text-to-video 等实验。

## 为什么需要这个项目

这是本仓库进入视频生成方向的核心项目。

重点不是只生成一个视频，而是记录完整实验过程：

* 使用什么模型
* 使用什么 prompt
* 使用什么 seed
* 使用多少 steps
* 使用什么分辨率
* 生成多少帧
* 运行耗时多少
* 显存占用多少
* 输出结果有什么问题

## 计划功能

* [ ] 跑通 text-to-image
* [ ] 跑通 image-to-image
* [ ] 跑通 image-to-video
* [ ] 跑通 text-to-video
* [ ] 自动保存 metadata
* [ ] 对比 seed / steps / guidance
* [ ] 对比 num_frames / fps
* [ ] 记录显存优化方法
* [ ] 整理失败案例

## 计划文件

```text
projects/text_image_to_video_lab/
scripts/run_t2i.py
scripts/run_i2i.py
scripts/run_i2v.py
scripts/run_t2v.py
configs/
outputs/experiments/
```

## 示例命令

```bash
python scripts/run_i2v.py --config configs/i2v_example.yaml
python scripts/run_t2v.py --config configs/t2v_example.yaml
```

## 预期输出

```text
视频生成完成
metadata 已保存
输出视频已保存
```

---

# Project 07 - ComfyUI Workflow Zoo

## 所属阶段

```text
Phase 7 - ComfyUI 工作流
Day092
```

## 项目目标

整理一组可复用的 ComfyUI 工作流。

包括文生图、图生视频、视频风格化、批量生成等 workflow。

## 为什么需要这个项目

ComfyUI 是视频生成和图像生成中常用的工作流工具。
它适合把复杂的生成流程可视化、模块化和复用化。

这个项目用于展示：

* 能理解节点式生成流程
* 能保存和管理 workflow JSON
* 能用版本管理维护工作流
* 能通过 Python 调用 ComfyUI API

## 计划功能

* [ ] 保存基础文生图 workflow
* [ ] 保存基础图生视频 workflow
* [ ] 管理 prompt variants
* [ ] 记录每个 workflow 的输入输出
* [ ] 编写 workflow index
* [ ] 尝试 Python 调用 ComfyUI
* [ ] 整理常见报错

## 计划文件

```text
projects/comfyui_workflow_zoo/
examples/workflows/
scripts/comfyui_client.py
docs/comfyui-workflow-index.md
```

## 示例结构

```text
examples/workflows/
├── t2i_basic.json
├── i2v_basic.json
└── README.md
```

---

# Project 08 - VideoGen Evaluation Dashboard

## 所属阶段

```text
Phase 8 - 评估、作品集与发布
Day093-Day097
```

## 项目目标

建立一个视频生成结果评估看板。

重点记录不同模型、参数、prompt 和输入条件下的视频生成质量。

## 为什么需要这个项目

视频生成结果不能只靠“看起来不错”来判断。
至少需要从以下角度观察：

* 画面质量
* 运动连续性
* 闪烁程度
* Prompt 遵循程度
* 身份一致性
* 风格一致性
* 失败现象

这个项目用于把视频生成实验结果整理成可比较、可复盘的形式。

## 计划功能

* [ ] 建立评价维度
* [ ] 建立人工评分表
* [ ] 整理视频生成失败案例
* [ ] 记录 temporal consistency
* [ ] 记录 flicker 问题
* [ ] 保存结果截图和 metadata
* [ ] 生成 Markdown 或网页报告

## 计划文件

```text
projects/video_evaluation_dashboard/
docs/evaluation-rubric.md
outputs/evaluation/
docs/demo-gallery.md
```

---

# Project 09 - GitHub Pages Portfolio

## 所属阶段

```text
Phase 8 - 评估、作品集与发布
Day098-Day100
```

## 项目目标

发布项目作品集页面。

将 100 天学习过程中完成的项目、实验、结果和复盘整理成可以公开展示的网页。

## 为什么需要这个项目

GitHub 仓库适合保存代码和记录，但访客不一定会逐个打开文件。
GitHub Pages 可以把项目成果整理成更清晰的展示入口。

## 计划内容

* [ ] 项目简介
* [ ] 学习路线
* [ ] 作品列表
* [ ] Demo Gallery
* [ ] 关键实验
* [ ] 常见问题
* [ ] 下一阶段计划

## 计划文件

```text
docs/index.md
docs/demo-gallery.md
docs/pitch.md
docs/release-notes-v1.0.md
```

---

# 项目完成标准

每个正式项目完成时，需要至少包含：

```text
README.md
可运行脚本
示例命令
预期输出
实际输出记录
问题记录
限制说明
下一步计划
```

---

# 当前状态

| 项目                            | 状态  | 说明         |
| ----------------------------- | --- | ---------- |
| Asset Scanner CLI             | 未开始 | Phase 1 完成 |
| Video Preprocess CLI          | 未开始 | Phase 2 完成 |
| Video Frame Analyzer          | 未开始 | Phase 3 完成 |
| Frame Classifier              | 未开始 | Phase 4 完成 |
| Mini Diffusion Lab            | 未开始 | Phase 5 完成 |
| Text / Image-to-Video Lab     | 未开始 | Phase 6 完成 |
| ComfyUI Workflow Zoo          | 未开始 | Phase 7 完成 |
| VideoGen Evaluation Dashboard | 未开始 | Phase 8 完成 |
| GitHub Pages Portfolio        | 未开始 | Phase 8 完成 |
