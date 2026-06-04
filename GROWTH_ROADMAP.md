# GROWTH_ROADMAP

本文件记录 `VideoGen Builder 100` 的能力成长路线。

`COURSE_MAP.md` 关注“每天学什么”。
`PROJECTS.md` 关注“最终做出什么”。
`GROWTH_ROADMAP.md` 关注“能力如何逐步成长”。

---

## 总体成长目标

通过 100 天学习，我希望从一个视频生成方向的初学者，逐步成长为能够独立完成以下任务的人：

* 能搭建可复现的 Python / GitHub 项目
* 能处理视频、图片、音频等多媒体素材
* 能理解视频文件的基本结构
* 能使用 FFmpeg 和 OpenCV 完成视频预处理与分析
* 能理解 PyTorch 深度学习项目的基本流程
* 能理解扩散模型和生成模型的核心概念
* 能使用 Diffusers 完成图像生成和视频生成实验
* 能使用 ComfyUI 管理节点式生成工作流
* 能记录、评估和复盘视频生成实验
* 能把学习成果整理成公开 GitHub 作品集

---

# 能力分层

本项目将能力拆成 6 层。

```text
Layer 1：项目与工程基础
Layer 2：视频工程基础
Layer 3：图像与视频分析基础
Layer 4：深度学习基础
Layer 5：生成模型与视频生成实验
Layer 6：作品集与公开展示
```

---

# Layer 1：项目与工程基础

## 对应阶段

```text
Phase 0：Day001-Day003
Phase 1：Day004-Day014
```

## 核心能力

这一层解决“能不能把学习过程变成一个可运行项目”的问题。

需要掌握：

* Git / GitHub 基础工作流
* Markdown 学习记录
* Python 脚本结构
* 命令行参数
* 文件路径处理
* 配置文件
* logging 日志
* 异常处理
* pytest 最小测试
* 基础项目目录组织

## 达标标准

完成这一层后，应该能够：

* [ ] 创建并维护一个 GitHub 仓库
* [ ] 每天完成 commit 和 push
* [ ] 写出可运行 Python 脚本
* [ ] 用参数控制脚本输入输出
* [ ] 对常见错误给出清晰提示
* [ ] 写出简单测试
* [ ] 形成第一个 CLI 小工具

## 代表项目

```text
Asset Scanner CLI
```

---

# Layer 2：视频工程基础

## 对应阶段

```text
Phase 2：Day015-Day028
```

## 核心能力

这一层解决“能不能处理视频文件”的问题。

需要掌握：

* 视频容器
* 编码格式
* fps
* 分辨率
* 视频时长
* FFmpeg
* ffprobe
* 抽帧
* 帧合成视频
* 裁剪
* resize
* 格式转换
* 音频提取
* 批量预处理

## 达标标准

完成这一层后，应该能够：

* [ ] 查看视频基本信息
* [ ] 抽取视频帧
* [ ] 将帧重新合成为视频
* [ ] 裁剪视频片段
* [ ] 统一视频格式和分辨率
* [ ] 处理一批视频文件
* [ ] 记录视频处理 metadata

## 代表项目

```text
Video Preprocess CLI
```

---

# Layer 3：图像与视频分析基础

## 对应阶段

```text
Phase 3：Day029-Day042
```

## 核心能力

这一层解决“能不能理解视频帧和画面变化”的问题。

需要掌握：

* OpenCV 读取图片
* OpenCV 读取视频
* RGB / BGR / HSV
* 图像 resize / crop / pad
* 图像滤波
* 边缘检测
* 帧差法
* 关键帧提取
* 光流基础
* 视频缩略图
* 基础画质分析
* 视频分析报告

## 达标标准

完成这一层后，应该能够：

* [ ] 用 OpenCV 逐帧读取视频
* [ ] 对图像做基础处理
* [ ] 提取关键帧
* [ ] 观察画面变化
* [ ] 生成缩略图展示
* [ ] 输出基础视频分析报告

## 代表项目

```text
Video Frame Analyzer
```

---

# Layer 4：深度学习基础

## 对应阶段

```text
Phase 4：Day043-Day056
```

## 核心能力

这一层解决“能不能看懂模型训练和推理流程”的问题。

需要掌握：

* NumPy 数组
* PyTorch Tensor
* shape / dtype / device
* Dataset
* DataLoader
* 简单模型
* CNN
* loss
* optimizer
* training loop
* checkpoint
* inference
* batch inference
* GPU 检查
* 实验记录

## 达标标准

完成这一层后，应该能够：

* [ ] 理解图像如何变成张量
* [ ] 理解 batch 和 device
* [ ] 写出 Dataset / DataLoader
* [ ] 跑通一个最小训练流程
* [ ] 保存和加载模型
* [ ] 编写推理脚本
* [ ] 记录模型实验结果

## 代表项目

```text
Frame Classifier
```

---

# Layer 5：生成模型与视频生成实验

## 对应阶段

```text
Phase 5：Day057-Day070
Phase 6：Day071-Day084
Phase 7：Day085-Day092
```

## 核心能力

这一层解决“能不能理解并运行视频生成实验”的问题。

需要掌握：

* 生成任务分类
* AutoEncoder
* VAE
* GAN
* Diffusion
* DDPM
* Scheduler
* CFG / guidance
* Latent Diffusion
* Prompt
* seed
* negative prompt
* Diffusers pipeline
* text-to-image
* image-to-image
* image-to-video
* text-to-video
* 显存优化
* ComfyUI workflow
* workflow JSON
* Python 调用 ComfyUI

## 达标标准

完成这一层后，应该能够：

* [ ] 区分 T2I、I2I、T2V、I2V、V2V
* [ ] 解释扩散模型的基本流程
* [ ] 记录 prompt、seed、steps、guidance 等参数
* [ ] 跑通最小 Diffusers 图像生成实验
* [ ] 跑通至少一个短视频生成实验
* [ ] 记录显存和耗时
* [ ] 整理失败案例
* [ ] 保存和复用 ComfyUI workflow

## 代表项目

```text
Mini Diffusion Lab
Text / Image-to-Video Lab
ComfyUI Workflow Zoo
```

---

# Layer 6：作品集与公开展示

## 对应阶段

```text
Phase 8：Day093-Day100
```

## 核心能力

这一层解决“能不能把学习成果展示出来”的问题。

需要掌握：

* 项目 README 编写
* Demo Gallery 整理
* 视频生成结果评价
* temporal consistency 观察
* flicker 观察
* prompt adherence 评分
* GitHub Pages
* release notes
* 项目讲解稿

## 达标标准

完成这一层后，应该能够：

* [ ] 给每个项目写清楚 README
* [ ] 整理生成结果展示页
* [ ] 对视频生成结果进行基础评价
* [ ] 说明模型和参数限制
* [ ] 发布 GitHub Pages
* [ ] 写出 2 分钟项目介绍
* [ ] 发布 v1.0 release

## 代表项目

```text
VideoGen Evaluation Dashboard
GitHub Pages Portfolio
```

---

# 阶段性能力检查

## Day014 检查点

我应该已经具备：

* [ ] Python 脚本基础能力
* [ ] CLI 参数解析能力
* [ ] 文件路径处理能力
* [ ] GitHub 每日提交习惯
* [ ] 第一个 CLI 工具

如果没有达到，需要暂停进入视频工程阶段，先补齐 Python 工程基础。

---

## Day028 检查点

我应该已经具备：

* [ ] FFmpeg 基础能力
* [ ] 视频信息读取能力
* [ ] 抽帧和合成视频能力
* [ ] 视频裁剪和格式转换能力
* [ ] 批量预处理能力

如果没有达到，不建议进入 OpenCV 和视频分析阶段。

---

## Day042 检查点

我应该已经具备：

* [ ] OpenCV 图片读取能力
* [ ] OpenCV 视频读取能力
* [ ] 帧级分析能力
* [ ] 关键帧提取能力
* [ ] 基础视频质量分析能力

如果没有达到，不建议进入深度学习阶段。

---

## Day056 检查点

我应该已经具备：

* [ ] PyTorch Tensor 基础
* [ ] Dataset / DataLoader 基础
* [ ] 最小训练流程
* [ ] checkpoint 保存加载
* [ ] 模型推理脚本
* [ ] 实验记录习惯

如果没有达到，不建议进入扩散模型阶段。

---

## Day070 检查点

我应该已经具备：

* [ ] 生成模型基本概念
* [ ] Diffusion 基本流程理解
* [ ] prompt / seed / steps 记录习惯
* [ ] 失败案例整理能力

如果没有达到，不建议进入复杂视频生成模型实验。

---

## Day084 检查点

我应该已经具备：

* [ ] Diffusers 基础使用能力
* [ ] 图像生成实验能力
* [ ] 视频生成最小实验能力
* [ ] metadata 记录能力
* [ ] 显存限制意识

如果没有达到，不建议进入大规模 ComfyUI workflow 管理。

---

## Day092 检查点

我应该已经具备：

* [ ] ComfyUI 基础使用能力
* [ ] workflow JSON 管理能力
* [ ] 至少一个可复用图生视频 workflow
* [ ] 工作流调试记录能力

如果没有达到，需要补齐 workflow 管理，再进入最终作品集阶段。

---

## Day100 检查点

项目应当具备：

* [ ] 完整 100 天学习路线
* [ ] 多个可运行脚本
* [ ] 多个阶段项目
* [ ] 生成实验记录
* [ ] 视频生成评估记录
* [ ] GitHub Pages 展示页
* [ ] v1.0 release notes

---

# 自我评估维度

每个阶段结束时，用以下维度自评：

| 维度   | 说明                 | 评分  |
| ---- | ------------------ | --- |
| 可运行性 | 代码是否能在当前环境运行       | 1-5 |
| 可复现性 | 是否记录了输入、参数和输出      | 1-5 |
| 可解释性 | 是否能说明代码和实验的目的      | 1-5 |
| 工程性  | 文件结构、命名、日志、异常是否合理  | 1-5 |
| 展示性  | 是否适合放到 GitHub 给别人看 | 1-5 |

---

# 当前状态

| Layer   | 状态  | 说明                             |
| ------- | --- | ------------------------------ |
| Layer 1 | 进行中 | 已完成项目启动和模板建设，下一步进入 Python 工程基础 |
| Layer 2 | 未开始 | 视频工程基础                         |
| Layer 3 | 未开始 | 图像与视频分析基础                      |
| Layer 4 | 未开始 | 深度学习基础                         |
| Layer 5 | 未开始 | 生成模型与视频生成实验                    |
| Layer 6 | 未开始 | 作品集与公开展示                       |
