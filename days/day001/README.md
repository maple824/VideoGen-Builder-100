# Day001：项目基线与环境可复现性

## 1. 今日定位

Day001 不是正式学习视频生成模型。

今天的任务是先把整个项目的基础环境搭好，确保后续 100 天学习可以稳定进行。

可以把 Day001 理解为：

```text
先确认项目能运行
再确认代码能提交
再确认 GitHub 能同步
最后记录环境问题和解决方式
```

如果第一天不把这些基础问题处理好，后面学习 FFmpeg、OpenCV、PyTorch、Diffusers、ComfyUI 时，很多问题会混在一起，很难判断是代码问题、环境问题，还是 Git 问题。

---

## 2. 今日目标

完成 Day001 后，需要确认以下内容：

* 项目目录存在
* Git 仓库已经初始化
* GitHub 远程仓库已经绑定
* 当前分支是 `main`
* 本地代码可以 push 到 GitHub
* Conda 环境 `videogen` 可以正常使用
* Python 命令来自 `videogen` 环境
* 环境检查脚本可以运行
* Day001 的问题和解决过程已经记录下来

---

## 3. 今日文件

Day001 涉及两个主要文件：

```text
scripts/day001/check_env.py
days/day001/README.md
```

说明：

```text
scripts/day001/check_env.py
```

用于检查当前 Python 环境、Conda 环境、运行路径和项目根目录。

```text
days/day001/README.md
```

用于记录 Day001 的学习目标、执行步骤、遇到的问题和最终结果。

---

## 4. 为什么脚本放在 `scripts/day001/`

本项目约定：

```text
每天的练习脚本统一放在 scripts/dayXXX/ 目录下。
```

例如：

```text
scripts/day001/check_env.py
scripts/day004/hello_project.py
scripts/day005/file_scanner.py
```

这样做的原因是：

* 后续脚本会越来越多
* 按天数存放更容易查找
* 每天 README 和当天脚本可以一一对应
* 不容易把不同学习阶段的脚本混在一起

因此，Day001 的环境检查脚本放在：

```text
scripts/day001/check_env.py
```

而不是直接放在：

```text
scripts/check_env.py
```

---

## 5. 新手照做步骤

### 5.0 阅读前说明与前置条件

本项目默认阅读者已经掌握 VS Code 的基础使用方式，包括：

* 会用 VS Code 打开一个项目文件夹
* 会在 VS Code 中新建文件和文件夹
* 会在 VS Code 中打开终端
* 会复制、粘贴并运行基础命令
* 会查看终端输出结果

因此，本文档不会详细解释 VS Code 的安装、界面布局和基础操作。

如果还不熟悉 VS Code，可以先查看官方入门文档：

```text
https://code.visualstudio.com/docs/getstarted/getting-started
```

---

在开始 Day001 之前，需要先确认本机具备以下前置条件。

---
### 前置条件 1: 已安装Python

Python 是今天必须使用的工具。

检查命令：

```bash
python --version
```

如果你的系统使用 `python3`：

```bash
python3 --version
```

Windows 也可以尝试：

```bash
py --version
```

预期看到类似结果：

```text
Python 3.x.x
```

如果未安装或未正确配置，常见现象包括：

```text
python: command not found
```

或 Windows 中出现：

```text
'python' is not recognized as an internal or external command
```

官方安装资料：

* [Python Downloads](https://www.python.org/downloads/)
* [Python Setup and Usage](https://docs.python.org/3/using/index.html)

安装后再次运行版本检查命令，确认可以看到 Python 版本号。

#### 前置条件 2：已经安装 Git

Day001 会使用 Git 管理项目版本，并把代码同步到 GitHub。

后续会用到：

```bash
git init
git status
git add
git commit
git remote
git push
```

因此，必须先安装 Git。

检查方式：

```bash
git --version
```

如果已经安装 Git，会看到类似输出：

```text
git version 2.x.x
```

如果看到类似：

```text
git: command not found
```

或者：

```text
'git' is not recognized as an internal or external command
```

说明当前系统还没有安装 Git，或者 Git 没有正确加入环境变量。

Git 官方下载入口：

```text
https://git-scm.com/
```

Git 官方安装说明：

```text
https://git-scm.com/book/en/v2/Getting-Started-Installing-Git
```

安装完成后，重新打开终端，再执行：

```bash
git --version
```

确认可以看到 Git 版本号。

---

#### 前置条件 3：已经安装 Conda 或 Miniconda

Day001 会创建并激活 Python 环境：

```bash
conda create -n videogen python=3.10 -y
conda activate videogen
```

因此，需要提前安装 Conda 或 Miniconda。

检查方式：

```bash
conda --version
```

如果已经安装，会看到类似输出：

```text
conda 24.x.x
```

如果看到：

```text
conda: command not found
```

说明当前系统还不能使用 Conda。

推荐安装 Miniconda，因为它比完整 Anaconda 更轻量，适合学习项目。

Miniconda 官方安装说明：

```text
https://www.anaconda.com/docs/getting-started/miniconda/install/overview
```

Conda 官方安装文档：

```text
https://docs.conda.io/projects/conda/en/stable/user-guide/install/index.html
```

安装完成后，重新打开终端，再执行：

```bash
conda --version
```

确认可以看到 Conda 版本号。

---

#### 前置条件 4：已经有 GitHub 账号

Day001 后半部分需要把本地项目推送到 GitHub。

因此，需要提前准备：

```text
GitHub 账号
可以正常访问 GitHub
可以新建 GitHub 仓库
```

GitHub 官网：

```text
https://github.com/
```

GitHub 创建新仓库的官方文档：

```text
https://docs.github.com/en/repositories/creating-and-managing-repositories/creating-a-new-repository
```

如果还没有 GitHub 账号，需要先注册账号，再继续执行 GitHub 远程仓库相关步骤。

如果以上前置条件都满足，就可以继续 Day001 的项目创建、环境检查和 GitHub 同步流程。

---

### 5.1 新建项目文件夹并用 VS Code 打开

在自己的电脑上选择一个合适的位置，新建一个项目文件夹。

建议文件夹名称使用：

```text
VideoGen-Builder-100
```

创建好文件夹后，用 VS Code 打开这个文件夹。

后续所有文件和目录，都在这个项目文件夹中创建。

---

### 5.2 打开 VS Code 终端并确认当前位置

在 VS Code 中打开终端。

后续所有命令都默认在这个项目根目录下执行。

可以在终端执行：

```bash
pwd
```

预期看到的路径应该指向你刚才用 VS Code 打开的项目文件夹。

例如 macOS / Linux 用户可能看到：

```text
/Users/your-name/Workspace/VideoGen-Builder-100
```

或者：

```text
/home/your-name/Workspace/VideoGen-Builder-100
```

Windows 用户可能看到类似：

```text
D:\Projects\VideoGen-Builder-100
```

只要当前路径是你自己的 `VideoGen-Builder-100` 项目文件夹即可。

如果当前路径不是项目文件夹，需要在 VS Code 中重新打开正确的文件夹，或者切换终端目录。

---

### 5.3 创建基础目录结构

在 VS Code 左侧文件管理器中，创建以下目录：

```text
days/day001
scripts/day001
docs
```

创建完成后，项目结构应该类似：

```text
VideoGen-Builder-100/
├── days/
│   └── day001/
├── scripts/
│   └── day001/
└── docs/
```

说明：

```text
days/day001/
```

用于存放 Day001 的学习记录。

```text
scripts/day001/
```

用于存放 Day001 的 Python 脚本。

```text
docs/
```

用于存放项目通用文档。

也可以在 VS Code 终端中执行下面命令创建目录：

```bash
mkdir -p days/day001 scripts/day001 docs
```

---

### 5.4 创建项目 README

在项目根目录下创建文件：

```text
README.md
```

这个文件用于介绍整个项目。

可以先写入最小内容：

```markdown
# VideoGen-Builder-100

A 100-day learning project for video generation engineering.
```

此时项目结构应该变为：

```text
VideoGen-Builder-100/
├── README.md
├── days/
│   └── day001/
├── scripts/
│   └── day001/
└── docs/
```

---

### 5.5 创建 Day001 README

在下面路径创建文件：

```text
days/day001/README.md
```

这个文件用于记录 Day001 的学习过程。

可以先写入：

```markdown
# Day001：项目基线与环境可复现性

今天的目标是建立项目目录、Git 仓库、Python 环境和最小环境检查脚本。
```

注意：

项目根目录的 `README.md` 用于介绍整个项目。

`days/day001/README.md` 用于记录 Day001 当天的学习内容。

这两个文件的作用不同。

---

### 5.6 创建环境检查脚本

在下面路径创建文件：

```text
scripts/day001/check_env.py
```

写入以下代码：

```python
import os
import platform
import sys
from pathlib import Path


def get_project_root() -> Path:
    """Return the project root directory."""
    return Path(__file__).resolve().parents[2]


def main() -> None:
    project_root = get_project_root()

    print("VideoGen Builder 100 - 环境检查")
    print("-" * 40)
    print(f"Python 版本: {platform.python_version()}")
    print(f"Python 可执行文件: {sys.executable}")
    print(f"操作系统: {platform.platform()}")
    print(f"当前工作目录: {Path.cwd()}")
    print(f"项目根目录: {project_root}")
    print(f"Conda 环境: {os.environ.get('CONDA_DEFAULT_ENV', '未检测到 Conda 环境')}")


if __name__ == "__main__":
    main()
```

这里使用：

```python
Path(__file__).resolve().parents[2]
```

原因是当前脚本位于：

```text
scripts/day001/check_env.py
```

从脚本文件向上回到项目根目录的过程是：

```text
check_env.py
-> day001
-> scripts
-> VideoGen-Builder-100
```

对应代码中的：

```python
parents[2]
```

这样写的好处是：

即使不同用户把项目放在不同位置，脚本也可以根据自身位置找到项目根目录。

---

### 5.7 创建 Conda 环境

前置条件：

你已经安装 Conda 或 Miniconda，并且下面命令可以正常输出版本号：

```bash
conda --version
```

如果能看到类似输出：

```text
conda 24.x.x
```

说明 Conda 可用。

然后在 VS Code 终端中执行：

```bash
conda create -n videogen python=3.10 -y
```

这条命令会创建一个名为 `videogen` 的 Conda 环境，并安装 Python 3.10。

创建完成后，激活环境：

```bash
conda activate videogen
```

激活成功后，终端前面通常会显示：

```text
(videogen)
```

如果执行 `conda activate videogen` 后没有变化，可能需要重新打开 VS Code 终端，或者检查 Conda 是否已经正确初始化。

---

### 5.8 确认 Python 环境

前置条件：

你已经激活 Conda 环境：

```bash
conda activate videogen
```

然后执行：

```bash
which python
python --version
```

macOS / Linux 用户预期看到类似：

```text
.../envs/videogen/bin/python
Python 3.10.x
```

Windows 用户看到的 Python 路径格式可能不同，但重点是路径中应该包含：

```text
videogen
```

需要确认两件事：

```text
Python 路径来自 videogen 环境
Python 版本是 3.10.x
```

如果 `which python` 没有输出，或者输出的是系统 Python，例如：

```text
/usr/bin/python
/usr/bin/python3
```

说明当前没有正确使用 `videogen` 环境。

这种情况下，需要先重新执行：

```bash
conda activate videogen
```

如果仍然不正常，再检查 Conda 安装和初始化是否正确。

---

### 5.9 运行环境检查脚本

前置条件：

* 当前位于项目根目录
* 已经激活 `videogen` 环境
* 已经创建 `scripts/day001/check_env.py`

执行：

```bash
python scripts/day001/check_env.py
```

预期看到类似：

```text
VideoGen Builder 100 - 环境检查
----------------------------------------
Python 版本: 3.10.x
Python 可执行文件: .../envs/videogen/bin/python
操作系统: ...
当前工作目录: .../VideoGen-Builder-100
项目根目录: .../VideoGen-Builder-100
Conda 环境: videogen
```

重点确认三项：

```text
Python 可执行文件来自 videogen 环境
当前工作目录是项目根目录
项目根目录识别正确
```

如果这三项正确，说明 Day001 的 Python 环境基线正常。

---

### 5.10 初始化 Git 仓库

前置条件：

你已经安装 Git，并且下面命令可以正常输出版本号：

```bash
git --version
```

如果能看到类似输出：

```text
git version 2.x.x
```

说明 Git 可用。

然后在项目根目录执行：

```bash
git init
git branch -m main
```

这两行命令的作用是：

```text
把当前项目变成 Git 仓库
把默认分支命名为 main
```

执行后检查：

```bash
git status
```

正常情况下会看到当前分支是：

```text
main
```

如果出现：

```text
git: command not found
```

说明 Git 没有安装或没有正确配置，需要先安装 Git。

---

### 5.11 配置当前仓库的 Git 用户信息

前置条件：

* 已经安装 Git
* 已经进入项目根目录
* 当前目录已经执行过 `git init`

如果你是第一次在当前电脑上使用 Git，可能需要配置提交身份。

建议先使用仓库级别配置：

```bash
git config --local user.name "你的 GitHub 用户名"
git config --local user.email "你的邮箱"
```

示例：

```bash
git config --local user.name "your-github-name"
git config --local user.email "your-email@example.com"
```

说明：

```text
--local 表示这个配置只对当前项目生效。
```

可以用下面命令检查：

```bash
git config --local --list
```

如果能看到：

```text
user.name=...
user.email=...
```

说明配置成功。

---

### 5.12 进行第一次 Git 提交

前置条件：

* 已经安装 Git
* 已经初始化 Git 仓库
* 已经配置 Git 用户名和邮箱
* 当前位于项目根目录

先查看当前文件状态：

```bash
git status
```

你应该能看到新建的文件，例如：

```text
README.md
days/day001/README.md
scripts/day001/check_env.py
```

把文件加入暂存区：

```bash
git add .
```

提交：

```bash
git commit -m "chore: initialize project baseline"
```

这一步会在本地生成第一次提交。

如果 `git commit` 提示需要配置用户名和邮箱，说明还没有完成 Git 用户信息配置，需要回到 5.11 节。

---

### 5.13 创建 GitHub 远程仓库

前置条件：

* 已经有 GitHub 账号
* 可以正常访问 GitHub
* 已经知道自己的 GitHub 用户名

打开 GitHub：

```text
https://github.com/
```

新建一个仓库。

建议仓库名使用：

```text
VideoGen-Builder-100
```

GitHub 创建仓库官方说明：

```text
https://docs.github.com/en/repositories/creating-and-managing-repositories/creating-a-new-repository
```

创建后，GitHub 会给出一个远程地址，格式类似：

```text
https://github.com/你的用户名/VideoGen-Builder-100.git
```

注意：

不要直接复制本文档中的示例用户名。

你需要使用自己的 GitHub 仓库地址。

---

### 5.14 绑定 GitHub 远程仓库

前置条件：

* 本地已经完成第一次 Git 提交
* GitHub 上已经创建远程仓库
* 你已经拿到自己的远程仓库地址

把下面命令中的地址替换成你自己的 GitHub 仓库地址：

```bash
git remote add origin https://github.com/你的用户名/VideoGen-Builder-100.git
```

然后检查：

```bash
git remote -v
```

预期看到：

```text
origin  https://github.com/你的用户名/VideoGen-Builder-100.git (fetch)
origin  https://github.com/你的用户名/VideoGen-Builder-100.git (push)
```

如果 `git remote -v` 没有输出，说明还没有绑定远程仓库。

如果地址写错，可以先删除旧的远程地址，再重新添加：

```bash
git remote remove origin
git remote add origin https://github.com/你的用户名/VideoGen-Builder-100.git
```

---

### 5.15 推送到 GitHub

前置条件：

* 本地已经有 commit
* 已经绑定 GitHub 远程仓库
* 当前网络可以访问 GitHub
* GitHub 账号具备该仓库的推送权限

执行：

```bash
git push -u origin main
```

如果推送成功，说明本地项目已经同步到 GitHub。

之后可以打开自己的 GitHub 仓库页面，确认是否能看到：

```text
README.md
days/day001/README.md
scripts/day001/check_env.py
```

如果推送时要求登录 GitHub，需要根据终端提示完成认证。

如果出现网络错误，优先检查：

```text
网络是否能访问 GitHub
代理是否正确
远程仓库地址是否正确
GitHub 账号是否有权限
```

---

### 5.16 Day001 最终检查

前置条件：

* 当前位于项目根目录
* Conda 环境已经激活
* GitHub 推送已经完成

执行：

```bash
git status
```

如果看到：

```text
On branch main
nothing to commit, working tree clean
```

说明当前没有未提交改动。

再执行：

```bash
python scripts/day001/check_env.py
```

如果环境检查脚本能正常输出，并且路径与 Conda 环境正确，Day001 就完成了。

最终应确认：

```text
项目文件夹已创建
VS Code 已打开项目文件夹
基础目录已创建
基础 README 已创建
Git 仓库已初始化
Conda 环境可用
Python 来自 videogen 环境
环境检查脚本可运行
本地 commit 已完成
GitHub push 已完成
```


---

## 6. Day001 常见问题与排障记录

Day001 的重点是建立项目基线，因此常见问题主要集中在三类：

```text
Git 是否可用
Conda / Python 环境是否正确
项目路径和脚本路径是否正确
```

下面记录 Day001 可能遇到的问题、原因和解决方式。

---

### 6.1 问题 1：终端无法识别 `git` 命令

#### 现象

执行：

```bash
git --version
```

出现类似报错：

```text
git: command not found
```

或者 Windows 中出现：

```text
'git' is not recognized as an internal or external command
```

#### 原因

当前电脑没有安装 Git，或者 Git 没有正确加入系统环境变量。

#### 解决方式

先安装 Git。

Git 官方下载入口：

```text
https://git-scm.com/
```

Git 官方安装说明：

```text
https://git-scm.com/book/en/v2/Getting-Started-Installing-Git
```

安装完成后，重新打开 VS Code 终端，再执行：

```bash
git --version
```

如果能看到 Git 版本号，说明 Git 已经可用。

---

### 6.2 问题 2：执行 `git status` 提示不是 Git 仓库

#### 现象

执行：

```bash
git status
```

出现：

```text
fatal: not a git repository (or any of the parent directories): .git
```

#### 原因

当前项目文件夹还没有初始化为 Git 仓库。

#### 解决方式

确认当前终端位于项目根目录后，执行：

```bash
git init
git branch -m main
```

然后再次执行：

```bash
git status
```

如果能看到当前分支是 `main`，说明 Git 仓库初始化成功。

---

### 6.3 问题 3：第一次 `git commit` 提示需要配置用户名和邮箱

#### 现象

执行：

```bash
git commit -m "chore: initialize project baseline"
```

时，Git 提示需要配置 `user.name` 和 `user.email`。

#### 原因

Git 需要知道本次提交是谁完成的。

#### 解决方式

在项目根目录执行：

```bash
git config --local user.name "你的 GitHub 用户名"
git config --local user.email "你的邮箱"
```

示例：

```bash
git config --local user.name "your-github-name"
git config --local user.email "your-email@example.com"
```

然后检查：

```bash
git config --local --list
```

如果能看到：

```text
user.name=...
user.email=...
```

说明配置成功。

之后重新执行：

```bash
git commit -m "chore: initialize project baseline"
```

---

### 6.4 问题 4：终端无法识别 `conda` 命令

#### 现象

执行：

```bash
conda --version
```

出现：

```text
conda: command not found
```

或者 Windows 中出现类似：

```text
'conda' is not recognized as an internal or external command
```

#### 原因

当前电脑没有安装 Conda / Miniconda，或者 Conda 没有正确加入环境变量。

#### 解决方式

推荐安装 Miniconda。

Miniconda 官方安装说明：

```text
https://www.anaconda.com/docs/getting-started/miniconda/install/overview
```

Conda 官方安装文档：

```text
https://docs.conda.io/projects/conda/en/stable/user-guide/install/index.html
```

安装完成后，重新打开 VS Code 终端，再执行：

```bash
conda --version
```

如果能看到 Conda 版本号，说明 Conda 已经可用。

---

### 6.5 问题 5：Conda 环境激活后，Python 不是 `videogen` 环境中的 Python

#### 现象

已经执行：

```bash
conda activate videogen
```

但继续执行：

```bash
which python
python --version
```

看到的 Python 路径不是 `videogen` 环境中的路径。

例如 macOS / Linux 中可能看到：

```text
/usr/bin/python
/usr/bin/python3
```

#### 原因

可能是 Conda 环境没有正确激活，或者创建环境时没有正确安装 Python。

#### 解决方式

先重新激活环境：

```bash
conda deactivate
conda activate videogen
```

然后再次检查：

```bash
which python
python --version
```

如果仍然不正确，可以重新创建环境：

```bash
conda create -n videogen python=3.10 -y
conda activate videogen
```

预期结果是：

```text
Python 路径中包含 videogen
Python 版本是 3.10.x
```

---

### 6.6 问题 6：运行环境检查脚本时提示文件不存在

#### 现象

执行：

```bash
python scripts/day001/check_env.py
```

出现类似报错：

```text
No such file or directory
```

#### 原因

常见原因有两个：

```text
当前终端不在项目根目录
脚本文件没有创建在 scripts/day001/check_env.py
```

#### 解决方式

先确认当前终端位置：

```bash
pwd
```

当前路径应该是你自己的 `VideoGen-Builder-100` 项目根目录。

然后检查脚本文件是否存在：

```bash
ls scripts/day001
```

应该能看到：

```text
check_env.py
```

如果没有看到，需要回到第 5.6 节，重新创建：

```text
scripts/day001/check_env.py
```

---

### 6.7 问题 7：`git push` 失败

#### 现象

执行：

```bash
git push -u origin main
```

失败。

常见原因包括：

```text
没有绑定远程仓库
远程仓库地址写错
GitHub 没有登录或认证失败
当前网络无法访问 GitHub
没有该仓库的 push 权限
```

#### 解决方式

先检查远程仓库地址：

```bash
git remote -v
```

如果没有输出，说明还没有绑定远程仓库，需要执行：

```bash
git remote add origin https://github.com/你的用户名/VideoGen-Builder-100.git
```

如果地址写错，可以删除后重新添加：

```bash
git remote remove origin
git remote add origin https://github.com/你的用户名/VideoGen-Builder-100.git
```

然后再次推送：

```bash
git push -u origin main
```

如果仍然失败，需要根据具体报错判断是网络问题、认证问题，还是权限问题。

---

## 7. Day001 完成情况检查

完成 Day001 后，项目中应该至少包含以下文件和目录：

```text
VideoGen-Builder-100/
├── README.md
├── days/
│   └── day001/
│       └── README.md
├── docs/
└── scripts/
    └── day001/
        └── check_env.py
```

其中：

```text
README.md
```

用于介绍整个项目。

```text
days/day001/README.md
```

用于记录 Day001 的学习过程。

```text
scripts/day001/check_env.py
```

用于检查当前 Python 环境、Conda 环境和项目路径。

```text
docs/
```

用于存放后续项目通用文档。

---

## 8. Day001 最终验证命令

在 VS Code 终端中，确认当前位于项目根目录，并且已经激活 Conda 环境：

```bash
conda activate videogen
```

然后执行：

```bash
python scripts/day001/check_env.py
```

预期看到类似结果：

```text
VideoGen Builder 100 - 环境检查
----------------------------------------
Python 版本: 3.10.x
Python 可执行文件: .../envs/videogen/bin/python
操作系统: ...
当前工作目录: .../VideoGen-Builder-100
项目根目录: .../VideoGen-Builder-100
Conda 环境: videogen
```

重点检查：

```text
Python 可执行文件来自 videogen 环境
当前工作目录是项目根目录
项目根目录识别正确
Conda 环境是 videogen
```

然后检查 Git 状态：

```bash
git status
```

如果所有内容已经提交，通常会看到：

```text
On branch main
nothing to commit, working tree clean
```

最后检查远程仓库：

```bash
git remote -v
```

预期看到自己的 GitHub 仓库地址：

```text
origin  https://github.com/你的用户名/VideoGen-Builder-100.git (fetch)
origin  https://github.com/你的用户名/VideoGen-Builder-100.git (push)
```

---

## 9. 今日完成情况

完成 Day001 后，应该勾选以下内容：

* [x] 已创建本地项目文件夹
* [x] 已用 VS Code 打开项目文件夹
* [x] 已创建 `README.md`
* [x] 已创建 `days/day001/README.md`
* [x] 已创建 `scripts/day001/check_env.py`
* [x] 已安装并确认 Git 可用
* [x] 已安装并确认 Conda 可用
* [x] 已创建 `videogen` Conda 环境
* [x] 已确认 Python 来自 `videogen` 环境
* [x] 已成功运行环境检查脚本
* [x] 已初始化 Git 仓库
* [x] 已完成第一次本地 commit
* [x] 已创建 GitHub 远程仓库
* [x] 已绑定 GitHub 远程仓库
* [x] 已成功 push 到 GitHub

---

## 10. 今日总结

Day001 的重点不是学习视频生成模型，而是建立项目基础设施。

今天完成后，项目已经具备以下能力：

```text
可以在本地稳定运行 Python 脚本
可以确认 Python 和 Conda 环境是否正确
可以使用 Git 管理项目版本
可以把本地代码同步到 GitHub
可以按天记录学习过程
可以继续扩展后续学习内容
```

Day001 建立的是整个 100 天项目的基础。

如果 Day001 没有完成，后续学习中出现问题时，很难判断问题来自：

```text
代码本身
Python 环境
项目路径
Git 状态
还是 GitHub 同步
```

因此，Day001 的价值是让后续学习过程可运行、可记录、可追踪、可复现。

---

## 11. 下一步

Day002 进入：

```text
仓库规范与每日学习模板
```

Day002 需要完成：

* 设计统一的每日 README 模板
* 设计 Debug 记录模板
* 设计实验 metadata 模板
* 让后续每天的学习记录具备统一格式
* 为后续 Python、FFmpeg、OpenCV、PyTorch、Diffusers 和 ComfyUI 阶段建立记录规范

---

## 12. 延伸学习资料

### VS Code 官方入门文档

```text
https://code.visualstudio.com/docs/getstarted/getting-started
```

适合了解：

```text
如何打开项目文件夹
如何使用 VS Code 终端
如何管理文件和目录
```

---

### Git 官方文档

```text
https://git-scm.com/doc
```

适合了解：

```text
git init
git status
git add
git commit
git remote
git push
```

---

### Pro Git 在线书

```text
https://git-scm.com/book/en/v2
```

适合系统学习 Git 基础。

建议先阅读：

```text
Getting Started
Git Basics
```

---

### Miniconda 官方安装说明

```text
https://www.anaconda.com/docs/getting-started/miniconda/install/overview
```

适合了解如何安装 Miniconda。

---

### Conda 官方文档

```text
https://docs.conda.io/projects/conda/en/stable/user-guide/index.html
```

适合了解：

```text
创建环境
激活环境
安装 Python
管理依赖
```

---

### GitHub 创建仓库官方文档

```text
https://docs.github.com/en/repositories/creating-and-managing-repositories/creating-a-new-repository
```

适合了解如何在 GitHub 上创建远程仓库。
