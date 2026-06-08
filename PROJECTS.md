# PROJECTS

本文件记录 `VideoGen-Builder-100` 的项目作品规划。

本仓库不是只做学习笔记，而是要在 100 天过程中逐步形成可以展示的 GitHub 项目作品集。

`COURSE_MAP.md` 关注“每天学什么”。
`GROWTH_ROADMAP.md` 关注“能力如何逐步成长”。
`PROJECTS.md` 关注“最终做出什么项目作品”。

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

7. 有阶段关联
   每个项目都要对应到明确的 Phase 和 Day，不脱离 100 天主路线。

---

## 与每日文档体系的关系

本文件只记录最终项目作品规划，不承担每日任务说明和实际学习记录的职责。

从 Day004 开始，正式学习日采用双文档体系：

```text
days/dayXXX/TASK.md
days/dayXXX/README.md
```

其中：

* `TASK.md` 用于说明当天的学习任务、前置条件、推荐资料、实践任务、今日产物、完成标准和常见误区。
* `README.md` 用于记录当天实际学习过程、运行命令、实际结果、问题、关键理解、总结和下一步。

每日学习脚本必须放在当天对应目录下：

```text
scripts/dayXXX/
```

例如：

```text
scripts/day004/hello_project.py
scripts/day005/file_scanner.py
scripts/day006/cli_args_demo.py
```

项目完成阶段可以把前面多个学习日积累的脚本、函数和说明整合到 `projects/` 下，形成最终可展示项目。例如：

```text
projects/asset_scanner_cli/
projects/video_preprocess_cli/
projects/video_frame_analyzer/
```

因此，本文件中的 `projects/...` 是最终项目作品目录；`scripts/dayXXX/...` 是每日学习过程中的脚本目录。两者用途不同，不应把每日脚本直接放到 `scripts/` 根目录。

如果某个项目涉及外部工具，例如 FFmpeg、OpenCV、PyTorch、Diffusers 或 ComfyUI，具体的检查命令、未安装现象、安装教程链接和安装后验证方式，应写在对应 Day 的 `TASK.md` 中。本文件只保留项目层面的目标、功能、文件规划和完成标准。

---

# 项目总览

| 编号         | 项目名称                          | 所属阶段    | 对应 Day        | 目标               |
| ---------- | ----------------------------- | ------- | ------------- | ---------------- |
| Project 01 | Asset Scanner CLI             | Phase 1 | Day014        | 扫描素材目录，输出文件清单    |
| Project 02 | Video Preprocess CLI          | Phase 2 | Day028        | 批量处理视频文件         |
| Project 03 | Video Frame Analyzer          | Phase 3 | Day042        | 分析视频帧、关键帧和基础质量   |
| Project 04 | Frame Classifier              | Phase 4 | Day056        | 训练和推理一个小型帧分类模型   |
| Project 05 | Mini Diffusion Lab            | Phase 5 | Day070        | 记录生成模型基础实验       |
| Project 06 | Text / Image-to-Video Lab     | Phase 6 | Day084        | 跑通图像生成与视频生成实验    |
| Project 07 | ComfyUI Workflow Zoo          | Phase 7 | Day092        | 管理 ComfyUI 工作流集合 |
| Project 08 | VideoGen Evaluation Dashboard | Phase 8 | Day093-Day097 | 整理视频生成评估结果       |
| Project 09 | GitHub Pages Portfolio        | Phase 8 | Day098-Day100 | 发布项目作品集页面        |

---

# Project 01：Asset Scanner CLI

## 所属阶段

```text
Phase 1：Python 工程基础
Day014
```

## 项目目标

实现一个素材扫描命令行工具。

输入一个目录，扫描其中的视频、图片、音频、文本、配置和 workflow 文件，输出文件清单和格式统计。

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

这个项目用于训练 Python 工程中的基础能力：路径处理、文件扫描、命令行参数、异常处理、日志记录、输出 manifest 和最小测试。

## 计划功能

* [ ] 支持输入目录
* [ ] 递归扫描文件
* [ ] 统计文件类型
* [ ] 输出文件路径清单
* [ ] 保存 CSV 或 JSON manifest
* [ ] 对空目录给出提示
* [ ] 对不存在路径给出错误信息
* [ ] 记录扫描日志
* [ ] 提供最小测试

## 每日脚本来源

```text
scripts/day004/hello_project.py
scripts/day005/file_scanner.py
scripts/day006/cli_args_demo.py
scripts/day008/logging_demo.py
scripts/day009/safe_file_check.py
scripts/day010/refactor_demo.py
```

## 项目整合目录

```text
projects/asset_scanner_cli/
projects/asset_scanner_cli/README.md
projects/asset_scanner_cli/scripts/scan_assets.py
src/videogen_builder/assets.py
tests/test_assets.py
outputs/asset_manifest.csv
```

## 示例命令

```bash
python projects/asset_scanner_cli/scripts/scan_assets.py --input assets --output outputs/asset_manifest.csv
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

## 完成标准

* [ ] 可以通过命令行传入输入目录和输出路径
* [ ] 可以扫描多种类型的素材文件
* [ ] 可以输出 CSV 或 JSON manifest
* [ ] 对不存在路径和空目录有清晰提示
* [ ] 有项目 README
* [ ] 有至少一个错误案例记录
* [ ] 有最小测试或手动验证记录

---

# Project 02：Video Preprocess CLI

## 所属阶段

```text
Phase 2：视频工程基础
Day028
```

## 项目目标

实现一个视频预处理命令行工具。

支持读取视频信息、抽帧、帧合成视频、裁剪、resize、格式转换、音频提取和批量处理。

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
* [ ] 生成 metadata 或 manifest

## 每日脚本来源

```text
scripts/day016/check_ffmpeg.py
scripts/day017/video_info.py
scripts/day018/extract_frames.py
scripts/day019/frames_to_video.py
scripts/day020/trim_video.py
scripts/day021/resize_video.py
scripts/day022/video_to_gif.py
scripts/day023/extract_audio.py
scripts/day024/add_watermark.py
scripts/day025/batch_preprocess.py
```

## 项目整合目录

```text
projects/video_preprocess_cli/
projects/video_preprocess_cli/README.md
projects/video_preprocess_cli/scripts/video_info.py
projects/video_preprocess_cli/scripts/extract_frames.py
projects/video_preprocess_cli/scripts/frames_to_video.py
projects/video_preprocess_cli/scripts/trim_video.py
projects/video_preprocess_cli/scripts/resize_video.py
projects/video_preprocess_cli/scripts/batch_preprocess.py
projects/video_preprocess_cli/docs/error-cases.md
outputs/video_manifest.csv
```

## 示例命令

```bash
python projects/video_preprocess_cli/scripts/video_info.py --input assets/sample.mp4
python projects/video_preprocess_cli/scripts/extract_frames.py --input assets/sample.mp4 --output outputs/frames
python projects/video_preprocess_cli/scripts/frames_to_video.py --input outputs/frames --output outputs/rebuild.mp4
```

## 预期输出

```text
视频信息读取成功
抽帧完成
帧合成视频完成
```

## 完成标准

* [ ] 可以读取视频基本信息
* [ ] 可以抽帧
* [ ] 可以将帧重新合成为视频
* [ ] 可以裁剪视频
* [ ] 可以转换尺寸或格式
* [ ] 可以批量处理视频目录
* [ ] 可以生成处理记录
* [ ] 有项目 README
* [ ] 有至少一个 FFmpeg 相关错误案例记录

---

# Project 03：Video Frame Analyzer

## 所属阶段

```text
Phase 3：图像与视频处理基础
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
* [ ] 检测亮度变化
* [ ] 生成 Markdown 报告
* [ ] 输出 CSV 分析结果

## 每日脚本来源

```text
scripts/day029/read_image.py
scripts/day030/read_video.py
scripts/day032/image_resize_crop_pad.py
scripts/day034/canny_edges.py
scripts/day035/frame_diff.py
scripts/day036/keyframe_extract.py
scripts/day037/optical_flow_demo.py
scripts/day038/contact_sheet.py
scripts/day039/video_quality_basic.py
```

## 项目整合目录

```text
projects/video_frame_analyzer/
projects/video_frame_analyzer/README.md
projects/video_frame_analyzer/scripts/read_video.py
projects/video_frame_analyzer/scripts/keyframe_extract.py
projects/video_frame_analyzer/scripts/frame_diff.py
projects/video_frame_analyzer/scripts/contact_sheet.py
projects/video_frame_analyzer/scripts/video_quality_basic.py
projects/video_frame_analyzer/docs/report-template.md
outputs/video_analysis_report.md
outputs/video_analysis.csv
```

## 示例命令

```bash
python projects/video_frame_analyzer/scripts/keyframe_extract.py --input assets/sample.mp4 --output outputs/keyframes
python projects/video_frame_analyzer/scripts/contact_sheet.py --input outputs/keyframes --output outputs/contact_sheet.jpg
```

## 预期输出

```text
关键帧提取完成
缩略图生成完成
分析报告已保存
```

## 完成标准

* [ ] 可以逐帧读取视频
* [ ] 可以提取关键帧
* [ ] 可以生成 contact sheet
* [ ] 可以计算基础帧级指标
* [ ] 可以输出 Markdown 或 CSV 报告
* [ ] 有项目 README
* [ ] 有至少一个视频分析错误案例记录

---

# Project 04：Frame Classifier

## 所属阶段

```text
Phase 4：深度学习基础
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

这个项目用于把 PyTorch 的最小训练、保存、加载和推理流程串起来。

## 计划功能

* [ ] 构建最小 Dataset
* [ ] 构建 DataLoader
* [ ] 编写 CNN 模型
* [ ] 编写训练循环
* [ ] 保存 checkpoint
* [ ] 加载 checkpoint
* [ ] 编写推理脚本
* [ ] 记录训练参数和结果

## 每日脚本来源

```text
scripts/day050/check_torch_cuda.py
scripts/day051/predict.py
```

说明：Phase 4 中有些练习可能更适合放在 `datasets/`、`src/`、`tests/` 或项目目录中，不一定每天都需要创建 `scripts/dayXXX/`。

## 项目整合目录

```text
projects/frame_classifier/
projects/frame_classifier/README.md
projects/frame_classifier/datasets/frame_dataset.py
projects/frame_classifier/scripts/train_classifier.py
projects/frame_classifier/scripts/predict.py
projects/frame_classifier/configs/frame_classifier.yaml
projects/frame_classifier/docs/experiment-log.md
outputs/checkpoints/
```

## 示例命令

```bash
python projects/frame_classifier/scripts/train_classifier.py --config projects/frame_classifier/configs/frame_classifier.yaml
python projects/frame_classifier/scripts/predict.py --checkpoint outputs/checkpoints/model.pt --input assets/sample.jpg
```

## 预期输出

```text
训练完成
checkpoint 已保存
推理完成
```

## 完成标准

* [ ] 可以构建 Dataset 和 DataLoader
* [ ] 可以跑通最小训练流程
* [ ] 可以保存 checkpoint
* [ ] 可以加载 checkpoint 并推理
* [ ] 可以记录训练参数和结果
* [ ] 有项目 README
* [ ] 有至少一个训练或推理错误案例记录

---

# Project 05：Mini Diffusion Lab

## 所属阶段

```text
Phase 5：生成模型基础
Day070
```

## 项目目标

建立一个生成模型基础实验室。

记录 AutoEncoder、VAE、Diffusion、Prompt、seed、steps 等基础实验。

## 为什么需要这个项目

视频生成模型建立在图像生成和扩散模型基础上。

如果不理解生成模型的基本逻辑，后续使用 Diffusers 或 ComfyUI 时就只能机械调参。

这个项目的重点不是训练大型模型，而是建立生成实验的基本理解和记录方式。

## 计划功能

* [ ] 记录生成任务分类
* [ ] 实现 AutoEncoder 重建实验
* [ ] 整理 VAE 笔记
* [ ] 整理 Diffusion 加噪和去噪示意
* [ ] 记录 seed 对结果的影响
* [ ] 记录 steps 对结果的影响
* [ ] 整理失败案例
* [ ] 保存实验 metadata

## 每日脚本来源

```text
scripts/day062/
scripts/day063/
scripts/day064/
scripts/day066/
scripts/day067/
```

说明：生成模型基础阶段可能包含笔记、实验配置、metadata 和小型脚本，不要求每天都创建脚本目录；只有当天确实写脚本时才创建 `scripts/dayXXX/`。

## 项目整合目录

```text
projects/mini_diffusion_lab/
projects/mini_diffusion_lab/README.md
projects/mini_diffusion_lab/scripts/run_toy_diffusion.py
projects/mini_diffusion_lab/configs/toy_diffusion.yaml
projects/mini_diffusion_lab/experiments/
projects/mini_diffusion_lab/docs/diffusion-notes.md
projects/mini_diffusion_lab/docs/failure-cases.md
outputs/experiments/
```

## 示例命令

```bash
python projects/mini_diffusion_lab/scripts/run_toy_diffusion.py --config projects/mini_diffusion_lab/configs/toy_diffusion.yaml
```

## 预期输出

```text
实验完成
metadata 已保存
结果已保存到 outputs/experiments/
```

## 完成标准

* [ ] 能说明 T2I、I2I、T2V、I2V、V2V 的区别
* [ ] 能解释 diffusion 的基本流程
* [ ] 能记录 prompt、seed、steps、guidance 等参数
* [ ] 能保存实验 metadata
* [ ] 能整理至少一个失败案例
* [ ] 有项目 README
* [ ] 有基础实验记录

---

# Project 06：Text / Image-to-Video Lab

## 所属阶段

```text
Phase 6：Diffusers 图像与视频生成
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

## 每日脚本来源

```text
scripts/day071/
scripts/day073/
scripts/day075/
scripts/day076/
scripts/day077/
scripts/day080/
scripts/day081/
scripts/day082/
```

说明：Diffusers 阶段可能需要较多实验脚本。每日实验脚本放在 `scripts/dayXXX/`，阶段最终整合版本放在 `projects/text_image_to_video_lab/`。

## 项目整合目录

```text
projects/text_image_to_video_lab/
projects/text_image_to_video_lab/README.md
projects/text_image_to_video_lab/scripts/run_t2i.py
projects/text_image_to_video_lab/scripts/run_i2i.py
projects/text_image_to_video_lab/scripts/run_i2v.py
projects/text_image_to_video_lab/scripts/run_t2v.py
projects/text_image_to_video_lab/configs/t2i_example.yaml
projects/text_image_to_video_lab/configs/i2v_example.yaml
projects/text_image_to_video_lab/configs/t2v_example.yaml
projects/text_image_to_video_lab/docs/experiment-log.md
projects/text_image_to_video_lab/docs/failure-cases.md
outputs/experiments/
```

## 示例命令

```bash
python projects/text_image_to_video_lab/scripts/run_i2v.py --config projects/text_image_to_video_lab/configs/i2v_example.yaml
python projects/text_image_to_video_lab/scripts/run_t2v.py --config projects/text_image_to_video_lab/configs/t2v_example.yaml
```

## 预期输出

```text
视频生成完成
metadata 已保存
输出视频已保存
```

## 完成标准

* [ ] 可以跑通至少一个 text-to-image 实验
* [ ] 可以跑通至少一个 image-to-video 或 text-to-video 实验
* [ ] 可以固定 seed
* [ ] 可以保存 metadata
* [ ] 可以记录模型、prompt、steps、guidance、num_frames 和 fps
* [ ] 可以记录显存限制和失败案例
* [ ] 有项目 README
* [ ] 有可展示的实验记录

---

# Project 07：ComfyUI Workflow Zoo

## 所属阶段

```text
Phase 7：ComfyUI 工作流
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

## 每日脚本来源

```text
scripts/day091/comfyui_client.py
```

说明：ComfyUI 阶段的大部分产物可能是 workflow JSON、说明文档和调试记录，不一定每天都有 Python 脚本。只有 Day091 这类需要 Python 调用 API 的任务，才需要创建对应脚本目录。

## 项目整合目录

```text
projects/comfyui_workflow_zoo/
projects/comfyui_workflow_zoo/README.md
projects/comfyui_workflow_zoo/scripts/comfyui_client.py
projects/comfyui_workflow_zoo/docs/comfyui-workflow-index.md
projects/comfyui_workflow_zoo/docs/error-cases.md
examples/workflows/
examples/workflows/t2i_basic.json
examples/workflows/i2v_basic.json
examples/workflows/README.md
```

## 示例结构

```text
examples/workflows/
├── t2i_basic.json
├── i2v_basic.json
└── README.md
```

## 完成标准

* [ ] 有至少一个基础文生图 workflow
* [ ] 有至少一个基础图生视频 workflow
* [ ] 每个 workflow 有用途说明
* [ ] 每个 workflow 有输入输出说明
* [ ] 有 workflow index
* [ ] 有至少一个 ComfyUI 调试记录
* [ ] 有项目 README

---

# Project 08：VideoGen Evaluation Dashboard

## 所属阶段

```text
Phase 8：评估、作品集与发布
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

## 项目整合目录

```text
projects/videogen_evaluation_dashboard/
projects/videogen_evaluation_dashboard/README.md
projects/videogen_evaluation_dashboard/docs/evaluation-rubric.md
projects/videogen_evaluation_dashboard/docs/demo-gallery.md
projects/videogen_evaluation_dashboard/docs/failure-cases.md
projects/videogen_evaluation_dashboard/outputs/evaluation/
```

## 完成标准

* [ ] 有清晰的视频生成评价维度
* [ ] 有至少一份人工评分表
* [ ] 有生成结果展示
* [ ] 有失败案例记录
* [ ] 有 temporal consistency 或 flicker 相关观察
* [ ] 有项目 README
* [ ] 可以服务于最终 GitHub Pages 展示

---

# Project 09：GitHub Pages Portfolio

## 所属阶段

```text
Phase 8：评估、作品集与发布
Day098-Day100
```

## 项目目标

发布项目作品集页面。

将 100 天学习过程中完成的项目、实验、结果和复盘整理成可以公开展示的网页。

## 为什么需要这个项目

GitHub 仓库适合保存代码和记录，但访客不一定会逐个打开文件。

GitHub Pages 可以把项目成果整理成更清晰的展示入口，让外部读者快速理解：

* 这个项目是什么
* 100 天路线如何设计
* 每个阶段做出了什么
* 最终有哪些可展示作品
* 视频生成实验如何记录和评估

## 计划内容

* [ ] 项目简介
* [ ] 学习路线
* [ ] 作品列表
* [ ] Demo Gallery
* [ ] 关键实验
* [ ] 常见问题
* [ ] 下一阶段计划
* [ ] v1.0 release notes

## 计划文件

```text
docs/index.md
docs/demo-gallery.md
docs/pitch.md
docs/release-notes-v1.0.md
```

## 完成标准

* [ ] GitHub Pages 可以访问
* [ ] 页面能说明项目定位
* [ ] 页面能展示 100 天路线
* [ ] 页面能链接 9 个最终项目
* [ ] 页面能展示代表性实验结果
* [ ] 页面能说明项目限制和下一步计划
* [ ] 有 v1.0 总结或 release notes

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

对于涉及外部工具的项目，还应在对应 Day 的 `TASK.md` 中说明：

```text
是否必须安装
如何检查是否已安装
未安装时可能出现什么现象
官方教程或高质量安装链接
安装后如何验证
```

---

# 当前状态

| 项目                                       | 状态  | 说明                       |
| ---------------------------------------- | --- | ------------------------ |
| Project 01：Asset Scanner CLI             | 未开始 | Phase 1 完成               |
| Project 02：Video Preprocess CLI          | 未开始 | Phase 2 完成               |
| Project 03：Video Frame Analyzer          | 未开始 | Phase 3 完成               |
| Project 04：Frame Classifier              | 未开始 | Phase 4 完成               |
| Project 05：Mini Diffusion Lab            | 未开始 | Phase 5 完成               |
| Project 06：Text / Image-to-Video Lab     | 未开始 | Phase 6 完成               |
| Project 07：ComfyUI Workflow Zoo          | 未开始 | Phase 7 完成               |
| Project 08：VideoGen Evaluation Dashboard | 未开始 | Phase 8 Day093-Day097 完成 |
| Project 09：GitHub Pages Portfolio        | 未开始 | Phase 8 Day098-Day100 完成 |
