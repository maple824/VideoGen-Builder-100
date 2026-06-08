# VideoGen-Builder-100

一个面向“视频生成方向”的 100 天开源学习项目。

本项目不是模型清单，也不是提示词合集，而是一条从 Python 工程、视频处理、图像与视频分析、深度学习、生成模型、Diffusers、ComfyUI、视频生成评估，到 GitHub 作品集发布的完整工程化学习路径。

项目目标是通过 100 天连续实践，建立一套可以复现、可以解释、可以持续扩展、可以公开展示的视频生成学习仓库。

---

## 项目定位

视频生成不是单一技能。一个相对完整的视频生成学习路径，至少需要覆盖以下能力：

* Python 脚本与工程组织能力
* Git / GitHub 项目管理能力
* 视频文件与 FFmpeg 工具链基础
* OpenCV 图像与视频分析能力
* PyTorch 深度学习基础
* 生成模型与 Diffusion 基础
* Diffusers 图像与视频生成实验能力
* ComfyUI 工作流搭建与管理能力
* 视频生成结果评估与作品集整理能力

本项目的重点不是“尽快跑一个大模型”，而是建立一条面向新手读者也能理解的学习路径：每天为什么学、怎么学、做什么、产出什么，以及这些产出如何逐步组成最终作品集。

---

## 适合人群

本项目适合：

* 想系统进入视频生成方向的学习者
* Python 基础不够稳，但希望通过项目练习补齐工程能力的人
* 想把学习过程沉淀成 GitHub 作品集的人
* 想从图像生成逐步过渡到视频生成的人
* 想理解视频生成背后基础工具链的人

本项目暂时不适合：

* 只想快速调用商业视频生成 API 的用户
* 只想收集提示词模板的用户
* 不希望写代码、不希望做环境配置的人

---

## 学习原则

本项目遵循以下原则：

1. 每一天都要有明确产物。
2. 先保证能运行，再追求复杂功能。
3. 每个实验都记录输入、参数、输出和失败原因。
4. 不提交无法解释的代码。
5. 大文件、模型权重、视频输出不直接提交到 Git 仓库。
6. 所有重要步骤都尽量可复现。
7. 学习记录要能服务于后续作品集展示。
8. 每个阶段最终服务于一个可展示的小项目。
9. 文档面向外部新手读者，而不是只写给项目作者自己看。

---

## 每日文档体系

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

* `TASK.md` 说明当天的学习任务，包括今天学什么、为什么学、前置条件、推荐学习资料、实践任务、今日产物、完成标准和常见误区。
* `README.md` 记录当天实际学习过程，包括实际做了什么、创建或修改了哪些文件、运行了哪些命令、得到什么结果、遇到什么问题、关键理解、总结和下一步。

---

## 脚本存放约定

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

## 项目路线

### Phase 0：项目启动与可复现基线

| Day    | 主题          | 目标                             |
| ------ | ----------- | ------------------------------ |
| Day001 | 项目基线与环境可复现性 | 确认 Git、GitHub、Python 环境和项目结构可用 |
| Day002 | 仓库规范与每日学习模板 | 建立统一的每日记录模板                    |
| Day003 | 项目路线图与任务索引  | 完成课程地图和项目索引初版                  |

阶段产物：

* 项目根目录 README
* 每日学习文档模板
* 100 天路线图
* 项目作品规划
* 基础环境检查脚本

---

### Phase 1：Python 工程基础

| Day    | 主题                | 目标                          |
| ------ | ----------------- | --------------------------- |
| Day004 | Python 脚本结构       | 理解项目脚本的基本组织方式               |
| Day005 | 路径与文件扫描           | 扫描素材目录并输出文件列表               |
| Day006 | argparse 命令行参数    | 支持 `--input`、`--output` 等参数 |
| Day007 | JSON / YAML 配置    | 用配置文件管理项目参数                 |
| Day008 | logging 日志系统      | 保存脚本运行日志                    |
| Day009 | 异常处理              | 处理文件不存在、路径错误、格式错误           |
| Day010 | 函数拆分              | 将脚本逻辑拆成可复用函数                |
| Day011 | Python 包结构        | 建立 `src/videogen_builder/`  |
| Day012 | pytest 最小测试       | 为工具函数写测试                    |
| Day013 | requirements 管理   | 规范依赖管理方式                    |
| Day014 | Asset Scanner CLI | 完成第一个小型命令行项目                |

阶段产物：

* `scripts/day004/` 至 `scripts/day014/`
* `src/videogen_builder/`
* `tests/`
* `projects/asset_scanner_cli/`
* Project 01：Asset Scanner CLI

---

### Phase 2：视频工程基础

| Day    | 主题                   | 目标                               |
| ------ | -------------------- | -------------------------------- |
| Day015 | 视频文件基础               | 理解容器、编码、fps、分辨率                  |
| Day016 | FFmpeg 环境检查          | 确认 FFmpeg / ffprobe 可用           |
| Day017 | ffprobe 读取视频信息       | 输出 duration、fps、codec、resolution |
| Day018 | 视频抽帧                 | 将视频拆成图片帧                         |
| Day019 | 帧合成视频                | 将图片帧重新合成视频                       |
| Day020 | 视频裁剪                 | 截取指定时间段视频                        |
| Day021 | resize 与格式转换         | 统一视频尺寸和格式                        |
| Day022 | 视频转 GIF              | 生成轻量展示文件                         |
| Day023 | 音频提取                 | 从视频中提取音频                         |
| Day024 | 添加文字与水印              | 生成带基础标注的视频                       |
| Day025 | 批量视频预处理              | 批处理多个视频文件                        |
| Day026 | metadata 记录          | 生成视频清单和处理记录                      |
| Day027 | 错误案例整理               | 记录坏文件、空目录、编码异常                   |
| Day028 | Video Preprocess CLI | 完成第一个正式视频处理项目                    |

阶段产物：

* `scripts/day015/` 至 `scripts/day028/`
* `projects/video_preprocess_cli/`
* 视频信息读取工具
* 视频抽帧与合成工具
* 批量视频预处理工具
* Project 02：Video Preprocess CLI

---

### Phase 3：图像与视频处理基础

| Day    | 主题                   | 目标                   |
| ------ | -------------------- | -------------------- |
| Day029 | OpenCV 读取图片          | 掌握图像读取和保存            |
| Day030 | OpenCV 读取视频          | 逐帧读取视频               |
| Day031 | 色彩空间                 | 理解 RGB、BGR、HSV       |
| Day032 | resize / crop / pad  | 统一图像输入尺寸             |
| Day033 | 图像滤波                 | 实现模糊、锐化等基础操作         |
| Day034 | 边缘检测                 | 使用 Canny 提取边缘        |
| Day035 | 帧差法                  | 检测画面变化               |
| Day036 | 关键帧提取                | 从视频中选取代表帧            |
| Day037 | 光流基础                 | 观察简单运动信息             |
| Day038 | 视频缩略图                | 生成 contact sheet     |
| Day039 | 视频质量基础指标             | 检测亮度、模糊、分辨率          |
| Day040 | 数据集 manifest         | 建立视频数据索引             |
| Day041 | 批量分析报告               | 输出 CSV / Markdown 报告 |
| Day042 | Video Frame Analyzer | 完成视频帧分析项目            |

阶段产物：

* `projects/video_frame_analyzer/`
* 视频关键帧提取工具
* 视频分析报告生成脚本
* Project 03：Video Frame Analyzer

---

### Phase 4：深度学习基础

| Day    | 主题                   | 目标                    |
| ------ | -------------------- | --------------------- |
| Day043 | NumPy 与图像数组          | 理解图像如何表示为数组           |
| Day044 | PyTorch Tensor       | 掌握 shape、dtype、device |
| Day045 | Dataset / DataLoader | 读取图像帧数据               |
| Day046 | 简单线性模型               | 理解最小训练流程              |
| Day047 | CNN 基础               | 完成小型图像分类模型            |
| Day048 | Loss 与 Optimizer     | 理解训练循环                |
| Day049 | 保存和加载模型              | 使用 checkpoint         |
| Day050 | GPU 检查               | 检查 CUDA 是否可用          |
| Day051 | 推理脚本                 | 编写模型推理入口              |
| Day052 | batch 推理             | 对多张图像进行推理             |
| Day053 | embedding 概念         | 理解向量表示                |
| Day054 | CLIP 基础              | 理解文本-图像相似度            |
| Day055 | 模型实验记录               | 保存参数、结果和 metadata     |
| Day056 | Frame Classifier     | 完成帧分类小项目              |

阶段产物：

* `projects/frame_classifier/`
* PyTorch 最小训练与推理脚本
* 模型实验记录模板
* Project 04：Frame Classifier

---

### Phase 5：生成模型基础

| Day    | 主题                 | 目标                         |
| ------ | ------------------ | -------------------------- |
| Day057 | 生成任务分类             | 区分 T2I、I2I、T2V、I2V、V2V     |
| Day058 | AutoEncoder        | 理解重建任务                     |
| Day059 | VAE 概念             | 理解 latent space            |
| Day060 | GAN 基础             | 理解生成器和判别器                  |
| Day061 | Diffusion 直觉       | 理解加噪和去噪                    |
| Day062 | DDPM 最小实验          | 跑通 toy diffusion           |
| Day063 | Scheduler 概念       | 比较采样步数影响                   |
| Day064 | CFG / guidance     | 理解 guidance 参数             |
| Day065 | Latent Diffusion   | 理解为什么在 latent 中生成          |
| Day066 | Prompt 与 seed      | 做可复现实验                     |
| Day067 | Negative prompt    | 对比不同负面提示词                  |
| Day068 | 生成记录规范             | 保存 prompt、seed、model、steps |
| Day069 | 失败案例库              | 整理 bad cases               |
| Day070 | Mini Diffusion Lab | 完成生成模型基础实验项目               |

阶段产物：

* `projects/mini_diffusion_lab/`
* 生成实验记录规范
* Prompt / seed / steps 对比实验
* Project 05：Mini Diffusion Lab

---

### Phase 6：Diffusers 图像与视频生成

| Day    | 主题                        | 目标               |
| ------ | ------------------------- | ---------------- |
| Day071 | Diffusers 安装与最小推理         | 跑通 text-to-image |
| Day072 | Pipeline 结构               | 理解 pipeline 组件   |
| Day073 | seed 固定                   | 保证生成结果可复现        |
| Day074 | steps / guidance 对比       | 做参数对照实验          |
| Day075 | batch prompt              | 批量生成图片           |
| Day076 | metadata 自动保存             | 保存实验配置           |
| Day077 | image-to-image            | 尝试图像条件生成         |
| Day078 | ControlNet 概念             | 理解结构控制           |
| Day079 | LoRA 概念                   | 理解轻量微调和加载        |
| Day080 | image-to-video 入门         | 跑通短视频生成 demo     |
| Day081 | text-to-video 入门          | 跑通文生视频 demo      |
| Day082 | num_frames / fps 实验       | 比较时长和流畅度         |
| Day083 | 显存优化                      | 记录 offload、量化等策略 |
| Day084 | Text / Image-to-Video Lab | 完成视频生成实验项目       |

阶段产物：

* `projects/text_image_to_video_lab/`
* 视频生成参数实验表
* 生成结果 metadata
* Project 06：Text / Image-to-Video Lab

---

### Phase 7：ComfyUI 工作流

| Day    | 主题                    | 目标         |
| ------ | --------------------- | ---------- |
| Day085 | ComfyUI 基础概念          | 理解节点式工作流   |
| Day086 | workflow JSON         | 保存和复用工作流   |
| Day087 | 文生图 workflow          | 建立基础图像生成流程 |
| Day088 | 图生视频 workflow         | 建立基础图生视频流程 |
| Day089 | prompt variants       | 管理不同提示词版本  |
| Day090 | workflow 批量管理         | 组织多个工作流文件  |
| Day091 | Python 调用 ComfyUI API | 用脚本调用工作流   |
| Day092 | ComfyUI Workflow Zoo  | 完成工作流集合项目  |

阶段产物：

* `projects/comfyui_workflow_zoo/`
* `examples/workflows/`
* 可复用 workflow JSON
* Project 07：ComfyUI Workflow Zoo

---

### Phase 8：评估、作品集与发布

| Day    | 主题                   | 目标                   |
| ------ | -------------------- | -------------------- |
| Day093 | 视频生成评价维度             | 建立 evaluation rubric |
| Day094 | Temporal consistency | 记录时间一致性问题            |
| Day095 | Flicker 检测           | 实现简单帧差指标             |
| Day096 | Prompt adherence     | 建立人工评分表              |
| Day097 | Demo Gallery         | 整理生成结果展示页            |
| Day098 | GitHub Pages         | 发布项目网站               |
| Day099 | 项目讲解稿                | 准备 2 分钟介绍            |
| Day100 | v1.0 总结              | 发布 release notes     |

阶段产物：

* `projects/videogen_evaluation_dashboard/`
* `docs/`
* GitHub Pages
* v1.0 release
* Project 08：VideoGen Evaluation Dashboard
* Project 09：GitHub Pages Portfolio

---

## 预期最终作品

项目完成后，仓库应至少包含以下 9 个作品：

1. Project 01：Asset Scanner CLI
2. Project 02：Video Preprocess CLI
3. Project 03：Video Frame Analyzer
4. Project 04：Frame Classifier
5. Project 05：Mini Diffusion Lab
6. Project 06：Text / Image-to-Video Lab
7. Project 07：ComfyUI Workflow Zoo
8. Project 08：VideoGen Evaluation Dashboard
9. Project 09：GitHub Pages Portfolio

这些作品共同服务于一个目标：让外部读者不仅能看到学习记录，也能看到逐步积累出来的工程能力、实验能力和公开展示能力。

---

## 仓库结构

```text
VideoGen-Builder-100/
├── README.md
├── COURSE_MAP.md
├── GROWTH_ROADMAP.md
├── PROJECTS.md
├── requirements.txt
├── .gitignore
├── days/
│   ├── day001/
│   │   └── README.md
│   ├── day002/
│   │   └── README.md
│   ├── day003/
│   │   └── README.md
│   ├── day004/
│   │   ├── TASK.md
│   │   └── README.md
│   └── ...
├── scripts/
│   ├── check_env.py
│   ├── day004/
│   │   └── hello_project.py
│   ├── day005/
│   │   └── file_scanner.py
│   └── ...
├── src/
│   └── videogen_builder/
├── tests/
├── projects/
│   ├── asset_scanner_cli/
│   ├── video_preprocess_cli/
│   ├── video_frame_analyzer/
│   ├── frame_classifier/
│   ├── mini_diffusion_lab/
│   ├── text_image_to_video_lab/
│   ├── comfyui_workflow_zoo/
│   └── videogen_evaluation_dashboard/
├── examples/
│   └── workflows/
├── assets/
├── outputs/
└── docs/
```

---

## 当前进度

* [x] 创建项目仓库
* [x] 初始化 Git
* [x] 绑定 GitHub 远程仓库
* [x] 完成第一次 push
* [x] 修复 `videogen` conda 环境
* [x] 创建环境检查脚本
* [x] 完成 Day001 项目基线
* [x] 完成 Day002 仓库规范与每日学习模板
* [x] 完成 Day003 项目路线图与任务索引
* [ ] 从 Day004 开始进入正式学习日双文档体系

---

## 基础环境检查

本项目会逐步使用 Git、Python、Conda、FFmpeg、OpenCV、PyTorch、Diffusers 和 ComfyUI。不同阶段对工具的要求不同，不需要在 Day001 一次性安装全部工具。

| 工具              | 是否必须        | 主要使用阶段 | 检查命令                                   | 未安装时常见现象                       | 安装或文档链接                                                       |
| --------------- | ----------- | ------ | -------------------------------------- | ------------------------------ | ------------------------------------------------------------- |
| Git             | 必须          | 全项目    | `git --version`                        | 无法克隆仓库、提交版本或推送 GitHub          | https://git-scm.com/book/en/v2/Getting-Started-Installing-Git |
| Python          | 必须          | 全项目    | `python --version`                     | 无法运行 `.py` 脚本                  | https://www.python.org/downloads/                             |
| Conda           | 推荐          | 全项目    | `conda --version`                      | 无法使用 `conda activate videogen` | https://docs.conda.io/projects/miniconda/en/latest/           |
| FFmpeg          | Phase 2 后需要 | 视频处理   | `ffmpeg -version` 和 `ffprobe -version` | 无法读取视频信息、抽帧、合成视频               | https://ffmpeg.org/download.html                              |
| Python packages | 按阶段需要       | 全项目    | `pip list`                             | 运行脚本时出现 `ModuleNotFoundError`  | 使用本仓库 `requirements.txt`                                      |
| ComfyUI         | Phase 7 需要  | 工作流实验  | 按官方文档启动                                | 无法进行节点式工作流实验                   | https://github.com/comfyanonymous/ComfyUI                     |

运行仓库级环境检查脚本：

```bash
python scripts/check_env.py
```

预期输出应包含：

```text
VideoGen Builder 100 - 环境检查
Python 版本
Python 可执行文件
操作系统
当前工作目录
项目根目录
Conda 环境
```

如果出现 `python: command not found`、`conda: command not found` 或 `ModuleNotFoundError`，说明当前环境还没有正确配置，需要先完成对应工具或依赖安装。

---

## 文件管理约定

本项目不建议提交以下内容：

* 大型视频文件
* 模型权重
* 大量生成图片
* 临时输出文件
* 私人素材
* API token
* `.env` 文件

推荐提交：

* 源代码
* 配置模板
* 小型示例数据
* Markdown 学习记录
* 实验 metadata
* 结果截图的压缩版本
* workflow JSON
* 项目说明文档

---

## Commit 规范

建议使用以下 commit message：

```text
chore: initialize project structure
docs: add day001 environment baseline
docs: add day004 task and learning record
feat: add asset scanner
fix: handle missing input path
test: add path utility tests
refactor: split video utils
```

---

## 项目最终希望展示什么

这个仓库最终希望展示的不只是“我学过视频生成”，而是：

* 我能搭建可复现的 AI 项目环境
* 我能组织长期学习型 GitHub 仓库
* 我能处理视频数据
* 我能理解图像和视频的基本表示
* 我能运行和记录生成模型实验
* 我能管理 ComfyUI 工作流
* 我能评估视频生成结果
* 我能把学习过程整理成公开作品集
