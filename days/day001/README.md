# Day001 - 项目基线与环境可复现性

## 今日定位

Day001 不是正式的视频生成模型学习日。

今天的目标是建立整个项目的启动基线，确认后续 100 天学习所需的基础条件可用，包括：

* 本地 Git 仓库
* GitHub 远程仓库
* Python / conda 环境
* 项目目录结构
* 最小可运行脚本
* 第一次 commit 和 push 流程

视频生成项目后续会涉及 FFmpeg、OpenCV、PyTorch、Diffusers、ComfyUI、模型权重、GPU 环境和大量实验记录。如果第一天不确认环境和 Git 工作流，后续问题会很难定位。

因此，Day001 的核心价值是：确保项目可运行、可记录、可提交、可复现。

---

## 今日目标

完成项目启动基线检查。

具体目标：

* 确认当前仓库路径正确
* 确认 Git 仓库已经初始化
* 确认 GitHub 远程仓库已经绑定
* 确认 `main` 分支可以正常 push
* 确认 `videogen` conda 环境中有可用 Python
* 创建并运行环境检查脚本
* 记录环境问题和解决方式

---

## 今日产物

今日完成的主要产物：

```text
scripts/check_env.py
days/day001/README.md
```

其中：

* `scripts/check_env.py` 用于检查当前 Python 环境和项目路径
* `days/day001/README.md` 用于记录项目启动基线

---

## 仓库状态

项目路径：

```text
/root/Workspace/VideoGen-Builder-100
```

Git 分支：

```text
main
```

远程仓库：

```text
https://github.com/maple824/VideoGen-Builder-100.git
```

已完成的 Git 操作：

```text
git init
git branch -m main
git remote add origin https://github.com/maple824/VideoGen-Builder-100.git
git push -u origin main
```

---

## 环境检查脚本

脚本路径：

```text
scripts/check_env.py
```

运行命令：

```bash
python scripts/check_env.py
```

实际输出：

```text
VideoGen Builder 100 - 环境检查
----------------------------------------
Python 版本: 3.10.20
Python 可执行文件: /root/miniconda3/envs/videogen/bin/python
操作系统: Linux-6.5.0-41-generic-x86_64-with-glibc2.35
当前工作目录: /root/Workspace/VideoGen-Builder-100
项目根目录: /root/Workspace/VideoGen-Builder-100
Conda 环境: videogen
```

---

## 今日遇到的问题

### 问题 1：本地仓库尚未初始化 Git

最初运行：

```bash
git status --short
```

出现：

```text
fatal: not a git repository (or any of the parent directories): .git
```

原因：

当前项目目录还没有执行 `git init`。

解决方式：

```bash
git init
git branch -m main
```

---

### 问题 2：Git 用户名和邮箱未配置

第一次 commit 时，Git 提示需要配置提交身份。

解决方式：

在当前仓库中配置 local 级别的 Git 身份：

```bash
git config --local user.name "maple824"
git config --local user.email "bingwang@shu.edu.cn"
```

说明：

这里使用的是仓库级别配置，不影响其他 Git 仓库。

---

### 问题 3：GitHub 远程仓库未绑定

运行：

```bash
git remote -v
```

没有任何输出。

原因：

本地 Git 仓库还没有配置远程地址。

解决方式：

```bash
git remote add origin https://github.com/maple824/VideoGen-Builder-100.git
```

---

### 问题 4：第一次 push 时 HTTPS 连接异常

运行：

```bash
git push -u origin main
```

曾出现 TLS 连接异常。

解决方式：

配置代理后重新执行 push，成功将本地 `main` 分支推送到 GitHub。

---

### 问题 5：conda 环境显示为 videogen，但没有自己的 Python

最初在 `videogen` 环境中运行：

```bash
which python
```

没有输出。

运行：

```bash
which python3
```

输出：

```text
/usr/bin/python3
```

这说明虽然命令行显示处于 `videogen` 环境，但实际使用的是系统 Python。

进一步检查：

```bash
conda list -n videogen python
```

发现 `videogen` 环境中没有安装 Python。

原因：

创建 conda 环境时没有指定 Python 版本，导致环境中没有可用 Python。

解决方式：

```bash
conda install -n videogen python=3.10 -y
conda deactivate
conda activate videogen
```

修复后检查：

```bash
which python
python --version
```

输出：

```text
/root/miniconda3/envs/videogen/bin/python
Python 3.10.20
```

---

## 今日完成情况

* [x] 创建项目仓库骨架
* [x] 创建第一版项目 README
* [x] 初始化 Git 仓库
* [x] 设置 main 分支
* [x] 完成第一次 commit
* [x] 创建 GitHub 远程仓库
* [x] 绑定 origin
* [x] 成功 push 到 GitHub
* [x] 创建 `scripts/check_env.py`
* [x] 发现并修复 conda 环境问题
* [x] 确认 `videogen` 环境中的 Python 可用
* [x] 完成 Day001 环境记录

---

## 今日结论

Day001 的重点不是学习视频生成模型，而是建立项目基础设施。

今天完成后，项目已经具备以下条件：

```text
可以运行 Python 脚本
可以进行 Git 提交
可以同步到 GitHub
可以记录每日学习过程
可以继续扩展后续视频生成学习内容
```

这为后续进入 Python 工程、视频处理、OpenCV、PyTorch、Diffusers 和 ComfyUI 打下了基础。

---

## 下一步

Day002 建议进入：

```text
仓库规范与每日学习模板
```

Day002 需要完成：

* 设计统一的每日 README 模板
* 设计每日任务检查表
* 设计 Debug 记录格式
* 设计实验记录 metadata 格式
* 更新 `COURSE_MAP.md`
