# Day003：项目路线图与任务索引

## 1. 今日定位

Day003 是 Phase 0：项目启动与可复现基线 的最后一天。

前两天已经完成了两个基础工作：

```text
Day001：确认项目能运行、能提交、能同步到 GitHub
Day002：建立每日学习记录模板、Debug 模板和实验 metadata 模板
```

Day003 要解决的是另一个更重要的问题：

```text
这个 100 天项目到底学什么？
为什么这样安排？
最后要沉淀成哪些 GitHub 作品？
```

如果没有路线图，视频生成方向很容易变成随机学习：

```text
今天看一个模型
明天试一个 API
后天安装一个 ComfyUI 插件
遇到问题后不知道是 Python、视频处理、深度学习、模型推理还是显存管理的问题
```

Day003 的作用就是把学习路线固定下来。

完成 Day003 后，Phase 0 结束。
从 Day004 开始，正式进入 Phase 1：Python 工程基础。

---

## 2. 今日目标

完成 Day003 后，项目应该具备三个核心路线文档：

```text
COURSE_MAP.md
PROJECTS.md
GROWTH_ROADMAP.md
```

这三个文件的职责不同。

---

### 2.1 `COURSE_MAP.md`

作用：

记录 100 天学习路线。

它回答的问题是：

```text
每天学什么？
每个阶段覆盖什么内容？
Day001 到 Day100 如何衔接？
```

这个文件是整个项目的课程地图。

---

### 2.2 `PROJECTS.md`

作用：

记录最终要完成的项目作品。

它回答的问题是：

```text
这个 100 天学习项目最终能产出什么？
哪些内容可以作为 GitHub 作品集展示？
每个阶段的学习最终服务于哪个项目？
```

这个文件不是简单的任务列表，而是作品规划文档。

---

### 2.3 `GROWTH_ROADMAP.md`

作用：

记录能力成长路径。

它回答的问题是：

```text
从 Day001 到 Day100，能力如何逐步增长？
每个阶段应该获得什么能力？
为什么先学 Python 工程，再学视频处理，再进入生成模型？
```

这个文件帮助读者理解学习顺序背后的逻辑。

---

## 3. 今日前置条件

开始 Day003 前，需要先满足以下条件。

---

### 前置条件 1：已经完成 Day001

Day001 应该已经完成：

```text
项目文件夹已创建
VS Code 已打开项目
Git 仓库已初始化
GitHub 远程仓库已绑定
Conda 环境 videogen 可用
环境检查脚本可以运行
```

可以在项目根目录执行：

```bash
python scripts/day001/check_env.py
```

如果可以正常输出 Python、Conda 和项目路径信息，说明 Day001 基线正常。

---

### 前置条件 2：已经完成 Day002

Day002 应该已经创建以下模板文件：

```text
docs/day-template.md
docs/debug-template.md
docs/experiment-metadata-template.md
```

可以在项目根目录检查：

```bash
ls docs
```

预期至少能看到：

```text
day-template.md
debug-template.md
experiment-metadata-template.md
```

如果这些文件还没有创建，需要先回到 Day002 完成模板建设。

---

### 前置条件 3：会编辑 Markdown 文件

Day003 主要是写路线文档，不涉及 Python 脚本。

因此，需要能在 VS Code 中创建和编辑 Markdown 文件。

如果不熟悉 Markdown，可以先查看：

```text
https://www.markdownguide.org/basic-syntax/
```

建议先掌握：

```text
标题
列表
代码块
链接
任务列表
```

---

### 前置条件 4：Git 可以正常使用

Day003 完成后，需要把新增或修改的路线文档提交到 GitHub。

先检查 Git 是否可用：

```bash
git --version
```

如果能看到类似：

```text
git version 2.x.x
```

说明 Git 可用。

如果不能识别 `git` 命令，需要先安装 Git：

```text
https://git-scm.com/
```

---

## 4. 今日产物

Day003 需要完成以下文件：

```text
days/day003/README.md
COURSE_MAP.md
PROJECTS.md
GROWTH_ROADMAP.md
```

说明：

```text
days/day003/README.md
```

记录 Day003 当天的学习过程和操作指南。

```text
COURSE_MAP.md
```

记录 100 天学习路线。

```text
PROJECTS.md
```

记录最终项目作品规划。

```text
GROWTH_ROADMAP.md
```

记录能力成长路径。

---

## 5. Day003 不需要新增脚本

Day003 的任务是整理路线图和项目规划，不是编写 Python 脚本。

因此，Day003 不需要创建：

```text
scripts/day003/
```

本项目约定：

```text
只有当天确实需要写脚本时，才创建 scripts/dayXXX/ 目录。
```

例如：

```text
scripts/day001/check_env.py
scripts/day004/hello_project.py
scripts/day005/file_scanner.py
```

Day003 没有脚本任务，所以不创建 `scripts/day003/`。

---

## 6. 新手照做步骤

### 6.1 打开项目

用 VS Code 打开自己的 `VideoGen-Builder-100` 项目文件夹。

后续所有操作都在这个项目文件夹中完成。

打开 VS Code 终端后，确认当前在项目根目录：

```bash
pwd
```

预期看到的路径应该是你自己的项目路径，例如：

```text
.../VideoGen-Builder-100
```

只要当前路径指向 `VideoGen-Builder-100` 项目根目录即可。

---

### 6.2 创建 Day003 目录

在 VS Code 左侧文件管理器中创建：

```text
days/day003/
```

也可以在终端执行：

```bash
mkdir -p days/day003
```

创建完成后，项目中应该有：

```text
days/
├── day001/
├── day002/
└── day003/
```

---

### 6.3 创建 Day003 README

在下面路径创建文件：

```text
days/day003/README.md
```

这个文件用于记录 Day003 当天的学习过程。

也就是你现在正在阅读的这个文档。

---

### 6.4 创建 `COURSE_MAP.md`

在项目根目录创建：

```text
COURSE_MAP.md
```

这个文件记录 100 天学习路线。

它应该至少包含以下内容：

```text
Phase 0：项目启动与可复现基线
Phase 1：Python 工程基础
Phase 2：视频工程基础
Phase 3：图像与视频处理基础
Phase 4：深度学习基础
Phase 5：生成模型基础
Phase 6：Diffusers 图像与视频生成
Phase 7：ComfyUI 工作流
Phase 8：评估、作品集与发布
```

还应该说明每个 Phase 对应的天数范围：

```text
Phase 0：Day001-Day003
Phase 1：Day004-Day014
Phase 2：Day015-Day028
Phase 3：Day029-Day042
Phase 4：Day043-Day056
Phase 5：Day057-Day070
Phase 6：Day071-Day084
Phase 7：Day085-Day092
Phase 8：Day093-Day100
```

这个文件的重点不是写得复杂，而是让读者一眼看懂：

```text
100 天分成哪些阶段
每个阶段学什么
每天大致推进到哪里
```

---

### 6.5 创建 `PROJECTS.md`

在项目根目录创建：

```text
PROJECTS.md
```

这个文件记录最终项目作品规划。

它应该至少包含以下 9 个项目：

```text
Project 01：Asset Scanner CLI
Project 02：Video Preprocess CLI
Project 03：Video Frame Analyzer
Project 04：Frame Classifier
Project 05：Mini Diffusion Lab
Project 06：Text / Image-to-Video Lab
Project 07：ComfyUI Workflow Zoo
Project 08：VideoGen Evaluation Dashboard
Project 09：GitHub Pages Portfolio
```

这个文件要回答：

```text
最终会做出哪些项目？
这些项目分别对应哪些学习阶段？
为什么这些项目能体现视频生成工程能力？
```

注意：

`PROJECTS.md` 不是简单列项目名。
更好的写法是为每个项目说明：

```text
项目目标
对应阶段
核心能力
可能包含的功能
最终展示形式
```

---

### 6.6 创建 `GROWTH_ROADMAP.md`

在项目根目录创建：

```text
GROWTH_ROADMAP.md
```

这个文件记录能力成长路径。

它应该说明从 Day001 到 Day100，能力如何逐步递进。

建议按照下面逻辑写：

```text
先建立项目和环境基线
再学习 Python 工程基础
再学习视频文件处理
再学习图像与视频分析
再进入深度学习基础
再理解生成模型
再使用 Diffusers 和 ComfyUI
最后完成评估、作品集和发布
```

这个文件的重点是解释：

```text
为什么这个学习路线不是从模型开始？
为什么要先学 Python、路径、文件、日志和 CLI？
为什么视频生成项目需要视频处理和评估能力？
```

---

### 6.7 检查 Day003 文件是否完整

在项目根目录执行：

```bash
ls
```

应该能看到：

```text
README.md
COURSE_MAP.md
PROJECTS.md
GROWTH_ROADMAP.md
days
docs
scripts
```

再执行：

```bash
ls days/day003
```

应该能看到：

```text
README.md
```

如果这些文件都存在，说明 Day003 的文件结构正确。

---

### 6.8 检查三个路线文档是否职责清晰

打开三个文件，分别确认：

```text
COURSE_MAP.md
```

是否回答了：

```text
100 天每天学什么？
每个 Phase 的时间范围是什么？
Day004 是否自然衔接到 Python 工程基础？
```

```text
PROJECTS.md
```

是否回答了：

```text
最终做哪些项目？
每个项目服务于哪个阶段？
这些项目如何组成 GitHub 作品集？
```

```text
GROWTH_ROADMAP.md
```

是否回答了：

```text
能力如何从基础环境逐步成长到视频生成项目？
为什么学习顺序是这样安排的？
```

如果三个文件的职责互相混乱，需要重新调整。

---

### 6.9 检查 Day003 是否和根目录 README 保持一致

打开根目录：

```text
README.md
```

检查其中的项目定位、Phase 划分、最终产物是否和下面三个文件一致：

```text
COURSE_MAP.md
PROJECTS.md
GROWTH_ROADMAP.md
```

重点检查：

```text
Phase 名称是否一致
Day001-Day100 的范围是否一致
最终项目名称是否一致
项目定位是否一致
```

如果根目录 README 和这三个文档说法不一致，后续读者会困惑。

---

### 6.10 提交 Day003 改动

前置条件：

* Git 已安装
* 项目已经初始化 Git 仓库
* 当前位于项目根目录
* Day003 文件已经创建或更新完成

先查看改动：

```bash
git status
```

正常情况下，应该能看到类似文件：

```text
days/day003/README.md
COURSE_MAP.md
PROJECTS.md
GROWTH_ROADMAP.md
```

将这些文件加入暂存区：

```bash
git add days/day003/README.md COURSE_MAP.md PROJECTS.md GROWTH_ROADMAP.md
```

提交：

```bash
git commit -m "docs: add day003 roadmap"
```

说明：

这里没有使用 `git add .`，是为了让新手清楚看到本次提交包含哪些文件。

如果你确认当前所有改动都属于 Day003，也可以使用：

```bash
git add .
```

---

### 6.11 推送到 GitHub

前置条件：

* 本地已经完成 commit
* 已经绑定 GitHub 远程仓库
* 当前网络可以访问 GitHub

执行：

```bash
git push origin main
```

推送完成后，可以打开自己的 GitHub 仓库页面，确认以下文件已经出现或更新：

```text
days/day003/README.md
COURSE_MAP.md
PROJECTS.md
GROWTH_ROADMAP.md
```

---

## 7. 今日检查点

完成 Day003 后，应该确认以下内容：

* [x] 已创建 `days/day003/README.md`
* [x] 已创建或更新 `COURSE_MAP.md`
* [x] 已创建或更新 `PROJECTS.md`
* [x] 已创建或更新 `GROWTH_ROADMAP.md`
* [x] `COURSE_MAP.md` 中有完整 Phase 划分
* [x] `PROJECTS.md` 中有最终作品列表
* [x] `GROWTH_ROADMAP.md` 中有能力成长路线
* [x] 根目录 `README.md` 与三个路线文档保持一致
* [x] Day004 能自然衔接到 Python 工程基础
* [x] 已完成 Git commit
* [x] 已 push 到 GitHub

---

## 8. Day003 常见问题

### 8.1 问题 1：不知道 `COURSE_MAP.md`、`PROJECTS.md`、`GROWTH_ROADMAP.md` 有什么区别

可以这样理解：

```text
COURSE_MAP.md：学什么
PROJECTS.md：做什么作品
GROWTH_ROADMAP.md：能力如何成长
```

更具体地说：

```text
COURSE_MAP.md
```

关注每天和每个阶段的学习内容。

```text
PROJECTS.md
```

关注最终能展示出来的项目成果。

```text
GROWTH_ROADMAP.md
```

关注为什么要按这个顺序学习。

---

### 8.2 问题 2：Day003 是否需要写 Python 代码

不需要。

Day003 是路线图建设日，不是代码实践日。

因此不需要创建：

```text
scripts/day003/
```

也不需要写 Python 脚本。

---

### 8.3 问题 3：为什么不从视频生成模型直接开始

因为视频生成项目不是只会调用模型就够了。

一个完整的视频生成工程项目通常还需要：

```text
Python 脚本能力
路径与文件管理能力
命令行工具能力
视频读取、转码、抽帧能力
图像和视频分析能力
模型推理能力
实验记录能力
结果评估能力
GitHub 展示能力
```

所以本项目先从工程基础开始，再逐步进入视频生成模型。

---

### 8.4 问题 4：路线图后续能不能修改

可以小范围修正表述，但不要随意改变整体路线。

本项目已经确定的整体方向是：

```text
Python 工程
视频工程
图像与视频处理
深度学习
生成模型
Diffusers
ComfyUI
评估与发布
```

后续每天的内容应该在这个路线内推进。

如果随意改路线，会导致项目失去连续性。

---

## 9. 今日总结

Day003 完成的是项目路线设计。

今天不是为了写代码，而是为了确定：

```text
100 天学什么
每个阶段为什么这样安排
最终要做出哪些项目
能力如何逐步成长
```

完成 Day003 后，Phase 0 正式结束。

此时项目已经具备：

```text
Day001：可运行、可提交、可同步的项目基线
Day002：统一的学习记录和实验记录模板
Day003：完整的 100 天路线图和项目产出规划
```

这为 Day004 进入 Python 工程基础做好准备。

---

## 10. 下一步

Day004 进入：

```text
Python 脚本结构
```

Day004 的重点不是算法，而是建立 Python 脚本的基础结构：

```text
脚本放在 scripts/day004/
使用 main() 作为入口函数
理解 if __name__ == "__main__"
确认脚本可以从项目根目录运行
为后续 CLI 工具打基础
```

Day004 建议产物：

```text
days/day004/README.md
scripts/day004/hello_project.py
```

---

## 11. 延伸学习资料

### Markdown 基础语法

```text
https://www.markdownguide.org/basic-syntax/
```

适合了解：

```text
标题
列表
代码块
链接
任务列表
```

---

### GitHub Markdown 官方文档

```text
https://docs.github.com/en/get-started/writing-on-github
```

适合了解：

```text
README 如何在 GitHub 上显示
如何写代码块
如何写任务列表
如何写文档链接
```

---

### GitHub README 相关说明

```text
https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-readmes
```

适合了解：

```text
README 在 GitHub 项目中的作用
为什么根目录 README 很重要
如何让别人快速理解项目
```

---

### Pro Git 在线书

```text
https://git-scm.com/book/en/v2
```

适合继续学习：

```text
Git 基础
提交记录
远程仓库
分支概念
```

Day003 不要求深入掌握 Git，只需要能完成文档提交和 GitHub 同步。
