# COURSE_MAP

本文件记录 `VideoGen-Builder-100` 的 100 天学习路线。

本路线不是模型清单，也不是工具堆叠，而是按照能力成长顺序设计的一条工程化学习路径：

```text
项目启动
Python 工程基础
视频工程基础
图像与视频处理基础
深度学习基础
生成模型基础
Diffusers 图像与视频生成
ComfyUI 工作流
评估、作品集与发布
```

这条路线的目标是让学习者从可复现的项目环境开始，逐步积累视频生成方向所需的工程能力、实验能力和作品集展示能力。

---

## 总体路线

| 阶段      |            天数 | 主题                | 核心目标                             |
| ------- | ------------: | ----------------- | -------------------------------- |
| Phase 0 | Day001-Day003 | 项目启动与可复现基线        | 建立仓库、模板、路线图                      |
| Phase 1 | Day004-Day014 | Python 工程基础       | 能写可维护的项目脚本                       |
| Phase 2 | Day015-Day028 | 视频工程基础            | 掌握 FFmpeg 与视频文件处理                |
| Phase 3 | Day029-Day042 | 图像与视频处理基础         | 掌握 OpenCV 和帧级分析                  |
| Phase 4 | Day043-Day056 | 深度学习基础            | 理解 PyTorch、张量、训练和推理              |
| Phase 5 | Day057-Day070 | 生成模型基础            | 理解 AutoEncoder、VAE、GAN、Diffusion |
| Phase 6 | Day071-Day084 | Diffusers 图像与视频生成 | 跑通可复现的图像和视频生成实验                  |
| Phase 7 | Day085-Day092 | ComfyUI 工作流       | 管理节点式生成工作流                       |
| Phase 8 | Day093-Day100 | 评估、作品集与发布         | 整理项目、评估结果、发布作品集                  |

---

## 每日文档规则

Day001-Day003 属于 Phase 0，用于建立项目基线、文档模板和整体路线图。这三天可以保持单文档结构：

```text
days/day001/README.md
days/day002/README.md
days/day003/README.md
```

从 Day004 开始，正式学习日采用双文档体系：

```text
days/dayXXX/TASK.md
days/dayXXX/README.md
```

其中：

* `TASK.md` 用于说明当天的学习任务，包括今天学什么、为什么学、前置条件、推荐学习资料、实践任务、今日产物、完成标准和常见误区。
* `README.md` 用于记录当天实际学习过程，包括实际做了什么、创建或修改了哪些文件、运行了哪些命令、得到什么结果、遇到什么问题、关键理解、总结和下一步。

---

## 脚本存放规则

Phase 0 的仓库级环境检查脚本可以保留在 `scripts/` 根目录下，例如：

```text
scripts/check_env.py
```

从 Day004 开始，如果某一天需要写脚本，脚本必须放在当天对应目录下：

```text
scripts/dayXXX/
```

例如：

```text
scripts/day004/hello_project.py
scripts/day005/file_scanner.py
scripts/day006/cli_args_demo.py
```

如果某一天没有脚本任务，就不需要创建对应的 `scripts/dayXXX/` 目录。

---

# Phase 0：项目启动与可复现基线

目标：让项目具备可运行、可记录、可提交、可同步的基础条件。

| Day    | 主题          | 产物                                                                                     |
| ------ | ----------- | -------------------------------------------------------------------------------------- |
| Day001 | 项目基线与环境可复现性 | `scripts/check_env.py`、环境记录                                                            |
| Day002 | 仓库规范与每日学习模板 | `docs/day-template.md`、`docs/debug-template.md`、`docs/experiment-metadata-template.md` |
| Day003 | 项目路线图与任务索引  | `COURSE_MAP.md`、`PROJECTS.md`、`GROWTH_ROADMAP.md`                                      |

阶段完成标准：

* [x] 本地 Git 仓库可用
* [x] GitHub 远程仓库可用
* [x] Python 环境可用
* [x] 每日记录模板可用
* [x] 100 天路线图完成
* [x] 项目作品索引完成
* [x] 能力成长路线完成

---

# Phase 1：Python 工程基础

目标：掌握后续视频生成项目会反复使用的 Python 工程能力。

这一阶段不追求复杂算法，重点是写出稳定、可复用、可维护的脚本。

| Day    | 主题                | 核心任务                    | 产物                                                                |
| ------ | ----------------- | ----------------------- | ----------------------------------------------------------------- |
| Day004 | Python 脚本结构       | 编写第一个项目脚本               | `scripts/day004/hello_project.py`                                 |
| Day005 | 路径与文件扫描           | 扫描素材目录                  | `scripts/day005/file_scanner.py`                                  |
| Day006 | argparse 命令行参数    | 支持 `--input`、`--output` | `scripts/day006/cli_args_demo.py`                                 |
| Day007 | JSON / YAML 配置    | 用配置文件管理参数               | `configs/project.yaml`                                            |
| Day008 | logging 日志系统      | 保存脚本运行日志                | `scripts/day008/logging_demo.py`                                  |
| Day009 | 异常处理              | 处理路径错误、空目录、格式错误         | `scripts/day009/safe_file_check.py`                               |
| Day010 | 函数拆分              | 将脚本拆成函数                 | `scripts/day010/refactor_demo.py`、`src/videogen_builder/utils.py` |
| Day011 | Python 包结构        | 建立基础包结构                 | `src/videogen_builder/`                                           |
| Day012 | pytest 最小测试       | 为工具函数写测试                | `tests/test_paths.py`                                             |
| Day013 | requirements 管理   | 规范依赖文件                  | `requirements.txt`                                                |
| Day014 | Asset Scanner CLI | 完成第一个小型命令行项目            | `projects/asset_scanner_cli/`                                     |

阶段项目：

```text
Project 01：Asset Scanner CLI
```

阶段完成标准：

* [ ] 能写命令行脚本
* [ ] 能处理输入输出路径
* [ ] 能记录日志
* [ ] 能处理基础异常
* [ ] 能写最小测试
* [ ] 能提交一个可运行的小型 CLI 工具

---

# Phase 2：视频工程基础

目标：理解视频文件的基本结构，并掌握 FFmpeg / ffprobe 的常用能力。

这一阶段解决一个核心问题：视频生成不是只和模型有关，输入输出视频本身也需要工程处理能力。

| Day    | 主题                   | 核心任务                             | 产物                                   |
| ------ | -------------------- | -------------------------------- | ------------------------------------ |
| Day015 | 视频文件基础               | 理解容器、编码、fps、分辨率                  | 视频基础笔记                               |
| Day016 | FFmpeg 环境检查          | 检查 FFmpeg / ffprobe 是否可用         | `scripts/day016/check_ffmpeg.py`     |
| Day017 | ffprobe 读取视频信息       | 输出 duration、fps、codec、resolution | `scripts/day017/video_info.py`       |
| Day018 | 视频抽帧                 | 将视频拆成图片帧                         | `scripts/day018/extract_frames.py`   |
| Day019 | 帧合成视频                | 将图片帧合成视频                         | `scripts/day019/frames_to_video.py`  |
| Day020 | 视频裁剪                 | 截取指定时间段                          | `scripts/day020/trim_video.py`       |
| Day021 | resize 与格式转换         | 统一分辨率和格式                         | `scripts/day021/resize_video.py`     |
| Day022 | 视频转 GIF              | 生成轻量展示文件                         | `scripts/day022/video_to_gif.py`     |
| Day023 | 音频提取                 | 从视频中提取音频                         | `scripts/day023/extract_audio.py`    |
| Day024 | 添加文字与水印              | 给视频添加基础标注                        | `scripts/day024/add_watermark.py`    |
| Day025 | 批量视频预处理              | 批处理多个视频文件                        | `scripts/day025/batch_preprocess.py` |
| Day026 | metadata 记录          | 生成视频处理清单                         | `outputs/manifest.csv`               |
| Day027 | 错误案例整理               | 记录坏文件、空目录、编码异常                   | Debug 记录                             |
| Day028 | Video Preprocess CLI | 整合视频预处理工具                        | `projects/video_preprocess_cli/`     |

阶段项目：

```text
Project 02：Video Preprocess CLI
```

阶段完成标准：

* [ ] 能读取视频基本信息
* [ ] 能抽帧
* [ ] 能合成视频
* [ ] 能裁剪视频
* [ ] 能转换格式
* [ ] 能批量处理视频
* [ ] 能生成处理记录

---

# Phase 3：图像与视频处理基础

目标：掌握 OpenCV 的基础图像和视频处理能力，为后续视频分析、生成结果评估和数据预处理打基础。

| Day    | 主题                   | 核心任务                 | 产物                                        |
| ------ | -------------------- | -------------------- | ----------------------------------------- |
| Day029 | OpenCV 读取图片          | 读取和保存图片              | `scripts/day029/read_image.py`            |
| Day030 | OpenCV 读取视频          | 逐帧读取视频               | `scripts/day030/read_video.py`            |
| Day031 | 色彩空间                 | 理解 RGB、BGR、HSV       | 色彩空间实验                                    |
| Day032 | resize / crop / pad  | 统一图像输入尺寸             | `scripts/day032/image_resize_crop_pad.py` |
| Day033 | 图像滤波                 | 模糊、锐化、降噪             | 图像滤波 demo                                 |
| Day034 | 边缘检测                 | 使用 Canny 提取边缘        | `scripts/day034/canny_edges.py`           |
| Day035 | 帧差法                  | 检测画面变化               | `scripts/day035/frame_diff.py`            |
| Day036 | 关键帧提取                | 从视频中选取代表帧            | `scripts/day036/keyframe_extract.py`      |
| Day037 | 光流基础                 | 可视化简单运动信息            | `scripts/day037/optical_flow_demo.py`     |
| Day038 | 视频缩略图                | 生成 contact sheet     | `scripts/day038/contact_sheet.py`         |
| Day039 | 视频质量基础指标             | 检测亮度、模糊度、分辨率         | `scripts/day039/video_quality_basic.py`   |
| Day040 | 数据集 manifest         | 建立视频数据索引             | `assets/video_manifest.csv`               |
| Day041 | 批量分析报告               | 输出 CSV / Markdown 报告 | `outputs/video_analysis_report.md`        |
| Day042 | Video Frame Analyzer | 整合视频帧分析工具            | `projects/video_frame_analyzer/`          |

阶段项目：

```text
Project 03：Video Frame Analyzer
```

阶段完成标准：

* [ ] 能用 OpenCV 读取图片和视频
* [ ] 能进行基础图像处理
* [ ] 能提取关键帧
* [ ] 能生成视频分析报告
* [ ] 能为后续视频生成评估准备基础指标

---

# Phase 4：深度学习基础

目标：理解后续生成模型所需的基本深度学习概念，包括张量、数据加载、训练循环、推理和 GPU 使用。

| Day    | 主题                   | 核心任务                  | 产物                                   |
| ------ | -------------------- | --------------------- | ------------------------------------ |
| Day043 | NumPy 与图像数组          | 理解图像如何表示为数组           | NumPy 图像实验                           |
| Day044 | PyTorch Tensor       | 理解 shape、dtype、device | Tensor demo                          |
| Day045 | Dataset / DataLoader | 读取图像帧数据               | `datasets/frame_dataset.py`          |
| Day046 | 简单线性模型               | 跑通最小训练流程              | toy model                            |
| Day047 | CNN 基础               | 完成小型图像分类模型            | CNN demo                             |
| Day048 | Loss 与 Optimizer     | 理解训练循环                | training loop                        |
| Day049 | 保存和加载模型              | 使用 checkpoint         | `outputs/checkpoints/`               |
| Day050 | GPU 检查               | 检查 CUDA 是否可用          | `scripts/day050/check_torch_cuda.py` |
| Day051 | 推理脚本                 | 编写模型推理入口              | `scripts/day051/predict.py`          |
| Day052 | batch 推理             | 对多张图像进行推理             | batch inference                      |
| Day053 | embedding 概念         | 理解向量表示                | embedding notes                      |
| Day054 | CLIP 基础              | 理解文本-图像相似度            | CLIP demo                            |
| Day055 | 模型实验记录               | 保存参数、结果和 metadata     | experiment metadata                  |
| Day056 | Frame Classifier     | 整合帧分类项目               | `projects/frame_classifier/`         |

阶段项目：

```text
Project 04：Frame Classifier
```

阶段完成标准：

* [ ] 理解 Tensor
* [ ] 能写 Dataset 和 DataLoader
* [ ] 能跑通一个最小训练流程
* [ ] 能保存和加载模型
* [ ] 能进行批量推理
* [ ] 能记录模型实验

---

# Phase 5：生成模型基础

目标：理解生成模型的基本路线，尤其是扩散模型，为后续使用 Diffusers 和视频生成模型打基础。

| Day    | 主题                 | 核心任务                       | 产物                             |
| ------ | ------------------ | -------------------------- | ------------------------------ |
| Day057 | 生成任务分类             | 区分 T2I、I2I、T2V、I2V、V2V     | 生成任务笔记                         |
| Day058 | AutoEncoder        | 理解重建任务                     | AE demo                        |
| Day059 | VAE 概念             | 理解 latent space            | VAE 笔记                         |
| Day060 | GAN 基础             | 理解生成器和判别器                  | GAN 笔记                         |
| Day061 | Diffusion 直觉       | 理解加噪和去噪                    | diffusion notes                |
| Day062 | DDPM 最小实验          | 跑通 toy diffusion           | toy DDPM                       |
| Day063 | Scheduler 概念       | 比较采样步数影响                   | scheduler 对比                   |
| Day064 | CFG / guidance     | 理解 guidance 参数             | guidance 实验                    |
| Day065 | Latent Diffusion   | 理解 latent 生成               | latent diffusion notes         |
| Day066 | Prompt 与 seed      | 做可复现实验                     | prompt-seed 对比                 |
| Day067 | Negative prompt    | 对比不同负面提示词                  | negative prompt 实验             |
| Day068 | 生成记录规范             | 保存 prompt、seed、model、steps | metadata JSON                  |
| Day069 | 失败案例库              | 整理 bad cases               | failure cases                  |
| Day070 | Mini Diffusion Lab | 整合生成模型实验项目                 | `projects/mini_diffusion_lab/` |

阶段项目：

```text
Project 05：Mini Diffusion Lab
```

阶段完成标准：

* [ ] 理解主流生成任务类型
* [ ] 理解 latent 表示
* [ ] 理解扩散模型基本流程
* [ ] 能记录 prompt、seed、steps 等实验参数
* [ ] 能整理失败案例

---

# Phase 6：Diffusers 图像与视频生成

目标：正式进入可复现的图像生成和视频生成实验。

这一阶段重点不是追求复杂模型，而是建立生成实验规范。

| Day    | 主题                        | 核心任务             | 产物                                  |
| ------ | ------------------------- | ---------------- | ----------------------------------- |
| Day071 | Diffusers 安装与最小推理         | 跑通 text-to-image | T2I demo                            |
| Day072 | Pipeline 结构               | 理解 pipeline 组件   | pipeline notes                      |
| Day073 | seed 固定                   | 保证生成结果可复现        | seed demo                           |
| Day074 | steps / guidance 对比       | 做参数对照实验          | 参数对比表                               |
| Day075 | batch prompt              | 批量生成图片           | batch generation                    |
| Day076 | metadata 自动保存             | 保存实验配置           | metadata saver                      |
| Day077 | image-to-image            | 尝试图像条件生成         | I2I demo                            |
| Day078 | ControlNet 概念             | 理解结构控制           | ControlNet 笔记                       |
| Day079 | LoRA 概念                   | 理解轻量微调和加载        | LoRA 笔记                             |
| Day080 | image-to-video 入门         | 跑通短视频生成 demo     | I2V demo                            |
| Day081 | text-to-video 入门          | 跑通文生视频 demo      | T2V demo                            |
| Day082 | num_frames / fps 实验       | 比较时长和流畅度         | 视频参数实验                              |
| Day083 | 显存优化                      | 记录 offload、量化等策略 | 显存优化笔记                              |
| Day084 | Text / Image-to-Video Lab | 整合视频生成实验项目       | `projects/text_image_to_video_lab/` |

阶段项目：

```text
Project 06：Text / Image-to-Video Lab
```

阶段完成标准：

* [ ] 能跑通最小 Diffusers 推理
* [ ] 能固定 seed
* [ ] 能记录生成参数
* [ ] 能批量生成
* [ ] 能跑通至少一个短视频生成实验
* [ ] 能分析失败案例

---

# Phase 7：ComfyUI 工作流

目标：掌握节点式生成工作流，能够保存、复用、管理和调用 ComfyUI workflow。

| Day    | 主题                    | 核心任务             | 产物                               |
| ------ | --------------------- | ---------------- | -------------------------------- |
| Day085 | ComfyUI 基础概念          | 理解节点式工作流         | ComfyUI 笔记                       |
| Day086 | workflow JSON         | 保存和复用工作流         | workflow JSON                    |
| Day087 | 文生图 workflow          | 建立基础图像生成流程       | T2I workflow                     |
| Day088 | 图生视频 workflow         | 建立基础图生视频流程       | I2V workflow                     |
| Day089 | prompt variants       | 管理不同提示词版本        | prompt variants                  |
| Day090 | workflow 批量管理         | 组织多个 workflow 文件 | workflow index                   |
| Day091 | Python 调用 ComfyUI API | 用脚本调用工作流         | ComfyUI client                   |
| Day092 | ComfyUI Workflow Zoo  | 整合工作流集合项目        | `projects/comfyui_workflow_zoo/` |

阶段项目：

```text
Project 07：ComfyUI Workflow Zoo
```

阶段完成标准：

* [ ] 理解 ComfyUI workflow 的基本结构
* [ ] 能保存 workflow JSON
* [ ] 能管理多个 workflow
* [ ] 能通过 Python 调用 workflow
* [ ] 能整理成可展示的 workflow 集合

---

# Phase 8：评估、作品集与发布

目标：把前面所有学习内容整理成可展示的 GitHub 项目作品集。

| Day    | 主题                   | 核心任务                 | 产物                          |
| ------ | -------------------- | -------------------- | --------------------------- |
| Day093 | 视频生成评价维度             | 建立 evaluation rubric | `docs/evaluation-rubric.md` |
| Day094 | Temporal consistency | 记录时间一致性问题            | consistency cases           |
| Day095 | Flicker 检测           | 实现简单帧差指标             | flicker demo                |
| Day096 | Prompt adherence     | 建立人工评分表              | prompt adherence table      |
| Day097 | Demo Gallery         | 整理生成结果展示页            | demo gallery                |
| Day098 | GitHub Pages         | 发布项目网站               | `docs/index.md`             |
| Day099 | 项目讲解稿                | 准备 2 分钟介绍            | `docs/pitch.md`             |
| Day100 | v1.0 总结              | 发布 release notes     | release notes               |

阶段项目：

```text
Project 08：VideoGen Evaluation Dashboard
Project 09：GitHub Pages Portfolio
```

阶段完成标准：

* [ ] 有完整作品索引
* [ ] 有生成结果展示页
* [ ] 有视频生成评价维度
* [ ] 有项目讲解稿
* [ ] 有 v1.0 总结
* [ ] 仓库可以作为公开作品集展示

---

# 最终交付物

100 天结束后，本项目应至少包含以下 9 个作品：

```text
1. Project 01：Asset Scanner CLI
2. Project 02：Video Preprocess CLI
3. Project 03：Video Frame Analyzer
4. Project 04：Frame Classifier
5. Project 05：Mini Diffusion Lab
6. Project 06：Text / Image-to-Video Lab
7. Project 07：ComfyUI Workflow Zoo
8. Project 08：VideoGen Evaluation Dashboard
9. Project 09：GitHub Pages Portfolio
```

---

# 使用方式

阅读本文件时，可以先看“总体路线”，再进入具体 Phase 查看每天的主题、核心任务和产物。

开始一个新 Day 时，按以下规则创建文件：

Day001-Day003 使用单文档结构：

```text
days/day001/README.md
days/day002/README.md
days/day003/README.md
```

Day004 之后使用双文档结构：

```text
days/dayXXX/TASK.md
days/dayXXX/README.md
```

如果当天需要写脚本，则脚本放在当天对应目录下：

```text
scripts/dayXXX/
```

示例：

```bash
mkdir -p days/day004
mkdir -p scripts/day004
```

Day004 的文件示例：

```text
days/day004/TASK.md
days/day004/README.md
scripts/day004/hello_project.py
```

完成当天学习后，需要：

1. 完成 `TASK.md` 中定义的任务。
2. 在 `README.md` 中记录实际执行过程和结果。
3. 保存当天脚本、配置、实验记录或输出说明。
4. 提交 commit。
5. push 到 GitHub。
