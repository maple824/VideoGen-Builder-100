# Day002：仓库规范与每日学习模板

## 1. 今日定位

Day002 不是学习视频生成模型，也不是写算法代码。

今天的任务是为后续 100 天学习建立统一记录规范。

可以把 Day002 理解为：

```text
先设计记录模板
再用模板记录每天学习
最后让整个项目变得可复盘、可展示、可复现
```

从 Day003 开始，每一天都会产生学习笔记、代码、命令、运行结果、错误记录、实验参数或复盘内容。

如果没有统一模板，后续内容会很快变成零散笔记，不方便自己回顾，也不方便别人通过 GitHub 阅读这个项目。

---

## 2. 今日目标

完成 Day002 后，需要得到三类模板：

```text
每日学习模板
Debug 记录模板
实验 metadata 模板
```

它们分别解决不同问题。

---

### 2.1 每日学习模板

文件路径：

```text
docs/day-template.md
```

用途：

记录每天的学习内容。

后续每一天的 README 都可以参考这个模板来写。

适合记录：

* 今日主题
* 今日目标
* 今日任务
* 新增文件
* 执行命令
* 运行结果
* 遇到的问题
* 今日总结
* 下一步计划

---

### 2.2 Debug 记录模板

文件路径：

```text
docs/debug-template.md
```

用途：

记录遇到的问题和排障过程。

适合记录：

* 报错信息
* 触发场景
* 当前环境
* 尝试过的方法
* 最终解决方式
* 问题原因
* 后续如何避免

后续学习中会遇到很多问题，例如：

```text
Python 环境错误
依赖安装失败
FFmpeg 命令失败
OpenCV 读取视频失败
PyTorch CUDA 不可用
Diffusers 模型加载失败
ComfyUI workflow 报错
```

这些问题都应该用 Debug 模板记录下来。

---

### 2.3 实验 metadata 模板

文件路径：

```text
docs/experiment-metadata-template.md
```

用途：

记录实验参数和输出结果。

后续做视频生成实验时，不能只保存生成结果，还要记录生成过程。

适合记录：

* 模型名称
* 输入 prompt
* negative prompt
* seed
* steps
* guidance scale
* num_frames
* fps
* 输入图片路径
* 输出视频路径
* 运行时间
* 成功或失败
* 失败原因
* 主观观察结果

这样后续才能知道某个结果是如何生成出来的。

---

## 3. 今日产物

Day002 需要创建以下文件：

```text
docs/day-template.md
docs/debug-template.md
docs/experiment-metadata-template.md
days/day002/README.md
```

说明：

```text
docs/day-template.md
```

每日学习记录模板。

```text
docs/debug-template.md
```

问题排查记录模板。

```text
docs/experiment-metadata-template.md
```

实验参数记录模板。

```text
days/day002/README.md
```

Day002 当天学习记录。

---

## 4. 新手照做步骤

### 第一步：进入项目目录

在终端执行：

```bash
cd /root/Workspace/VideoGen-Builder-100
```

说明：

后续所有文件都应该在这个项目目录下创建。

---

### 第二步：确认当前项目结构

执行：

```bash
ls
```

应该能看到类似内容：

```text
README.md
COURSE_MAP.md
PROJECTS.md
GROWTH_ROADMAP.md
days
docs
scripts
```

如果没有看到这些文件或目录，说明当前不在项目根目录。

---

### 第三步：确认 Day002 目录存在

执行：

```bash
ls days
```

应该能看到：

```text
day001
day002
day003
```

如果没有 `day002`，需要创建目录：

```bash
mkdir -p days/day002
```

---

### 第四步：确认 docs 目录存在

执行：

```bash
ls docs
```

如果 `docs` 目录不存在，可以创建：

```bash
mkdir -p docs
```

Day002 的三个模板文件都放在 `docs/` 目录下。

---

### 第五步：创建三个模板文件

需要创建：

```text
docs/day-template.md
docs/debug-template.md
docs/experiment-metadata-template.md
```

这三个文件不是代码文件，而是 Markdown 文档。

它们的作用是规范后续学习记录。

---

### 第六步：创建 Day002 README

需要创建：

```text
days/day002/README.md
```

这个文件记录 Day002 当天做了什么。

它不是模板文件，而是 Day002 的学习记录。

---

### 第七步：检查文件是否创建成功

执行：

```bash
ls docs
ls days/day002
```

预期至少能看到：

```text
day-template.md
debug-template.md
experiment-metadata-template.md
```

以及：

```text
README.md
```

如果能看到这些文件，说明 Day002 的文件结构正确。

---

## 5. Day002 不需要新增脚本

Day002 的任务是建立文档模板，不是写 Python 脚本。

因此 Day002 不需要创建：

```text
scripts/day002/
```

只有当某一天确实需要写脚本时，才在对应目录下创建：

```text
scripts/dayXXX/
```

例如：

```text
scripts/day001/check_env.py
scripts/day004/hello_project.py
scripts/day005/file_scanner.py
```

这个约定可以避免脚本混乱。

---

## 6. 模板设计原则

Day002 的模板需要遵循五个原则。

---

### 6.1 简洁

模板不能太复杂。

因为后续 100 天每天都要记录，如果模板太重，就很难长期坚持。

---

### 6.2 可执行

记录内容要尽量对应实际操作。

例如不要只写：

```text
学习了 Python 路径处理
```

更好的写法是：

```text
执行了 python scripts/day004/hello_project.py
确认项目根目录可以被正确识别
```

---

### 6.3 可复现

后续做实验时，需要知道当时使用了什么环境、输入、参数和输出路径。

例如：

```text
模型是什么
输入是什么
seed 是多少
输出文件保存在哪里
运行是否成功
```

没有这些信息，实验结果就很难复现。

---

### 6.4 可排障

遇到问题时，不能只写：

```text
报错了，后来解决了
```

更好的记录方式是：

```text
报错命令
完整报错信息
原因判断
解决命令
最终结果
```

这样以后遇到类似问题时，可以直接查记录。

---

### 6.5 可展示

这个项目最终会发布在 GitHub 上。

因此 README 不只是写给自己看，也要让别人能看懂：

```text
今天学什么
为什么学
做了哪些文件
如何运行
结果是什么
和后续项目有什么关系
```

---

## 7. 三个模板的使用方式

### 7.1 `docs/day-template.md` 怎么用

以后开始新的一天时，可以先参考：

```text
docs/day-template.md
```

然后创建当天 README：

```text
days/dayXXX/README.md
```

例如 Day004：

```text
days/day004/README.md
```

Day005：

```text
days/day005/README.md
```

每天的 README 不需要完全机械复制模板，但应该保留基本结构：

```text
今日主题
今日目标
今日文件
执行步骤
运行结果
问题记录
今日总结
下一步
```

---

### 7.2 `docs/debug-template.md` 怎么用

遇到报错时，可以复制 Debug 模板，记录到当天 README 或单独的 Debug 文档中。

例如：

```text
days/day017/README.md
```

中可以增加：

```text
## Debug 记录
```

然后按照模板记录问题。

适合记录的问题包括：

```text
命令无法运行
依赖安装失败
路径找不到
文件读取失败
模型加载失败
GPU 不可用
推理结果异常
```

---

### 7.3 `docs/experiment-metadata-template.md` 怎么用

后续做生成实验时，需要记录实验信息。

例如 Phase 6 中可能会生成图片或视频：

```text
Day071：Diffusers 安装与最小推理
Day080：image-to-video 入门
Day081：text-to-video 入门
Day084：Text / Image-to-Video Lab
```

这些任务都需要记录实验 metadata。

否则只保存生成结果，后续很难知道这个结果是怎么来的。

---

## 8. 今日完成情况

* [x] 编写 `docs/day-template.md`
* [x] 编写 `docs/debug-template.md`
* [x] 编写 `docs/experiment-metadata-template.md`
* [x] 编写 `days/day002/README.md`
* [x] 检查模板是否适合后续 Python、FFmpeg、OpenCV、PyTorch、Diffusers 和 ComfyUI 阶段
* [x] 提交 Day002 文件
* [x] 推送到 GitHub

---

## 9. Day002 最终检查命令

以后如果想确认 Day002 文件是否完整，可以执行：

```bash
cd /root/Workspace/VideoGen-Builder-100

ls docs
ls days/day002
```

预期看到：

```text
day-template.md
debug-template.md
experiment-metadata-template.md
```

以及：

```text
README.md
```

也可以检查 Git 状态：

```bash
git status
```

如果看到：

```text
nothing to commit, working tree clean
```

说明当前没有未提交改动。

---

## 10. 今日总结

Day002 完成的是项目记录规范。

它的价值不是某一个具体代码功能，而是让后续 100 天学习具备统一结构。

后续每一天都应该尽量做到：

```text
学习目标明确
文件路径清楚
命令可以复现
问题可以追踪
实验可以回看
GitHub 访客可以读懂
```

Day002 是后续所有学习记录的基础。

---

## 11. 下一步

Day003 进入：

```text
项目路线图与任务索引
```

Day003 需要明确：

* 100 天整体路线
* 每个阶段的学习范围
* 每个阶段最终服务于哪些项目
* 后续项目如何从基础脚本逐步发展成作品集

---

## 12. 延伸学习资料

### Markdown 基础语法

https://www.markdownguide.org/basic-syntax/

建议先掌握：

* 标题
* 列表
* 代码块
* 链接
* 表格

### GitHub Markdown 官方文档

https://docs.github.com/en/get-started/writing-on-github

建议了解：

* GitHub README 的显示方式
* 任务列表
* 代码块
* 文档链接

### YAML 简介

https://yaml.org/spec/

后续实验 metadata 可能会用到 YAML。现在只需要知道它常用于配置文件和实验记录，不需要深入学习完整规范。
