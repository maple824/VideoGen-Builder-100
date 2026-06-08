# GitHub 同步流程

本文档记录 `VideoGen-Builder-100` 项目从本地同步到 GitHub 的标准流程。

它适用于日常学习记录、文档修改、脚本新增、阶段项目整理和问题修复后的提交。

---

## 适用场景

当出现以下情况时，可以参考本文档完成 GitHub 同步：

* 新增或修改了根目录 `README.md`
* 新增或修改了 `COURSE_MAP.md`、`PROJECTS.md`、`GROWTH_ROADMAP.md`
* 新增或修改了 `docs/*.md`
* 新增或修改了 `days/dayXXX/TASK.md`
* 新增或修改了 `days/dayXXX/README.md`
* 新增或修改了 `scripts/dayXXX/*.py`
* 新增或修改了 `src/`、`tests/` 或 `projects/` 下的文件
* 完成了某一天学习任务后，需要把改动提交到 GitHub
* 修复了文档、脚本或项目结构中的问题

---

## 一、前置条件

在使用本文档之前，需要确认 Git 和 GitHub 仓库已经可用。

### 1. Git 是否已安装

检查命令：

```bash
git --version
```

如果 Git 已安装，会看到类似输出：

```text
git version 2.x.x
```

如果未安装，可能出现：

```text
git: command not found
```

或：

```text
'git' is not recognized as an internal or external command
```

安装教程：

```text
https://git-scm.com/book/en/v2/Getting-Started-Installing-Git
```

安装后再次执行：

```bash
git --version
```

确认 Git 可以正常使用。

---

### 2. 当前项目是否已经绑定 GitHub 远程仓库

在项目根目录执行：

```bash
git remote -v
```

预期能看到类似内容：

```text
origin  https://github.com/maple824/VideoGen-Builder-100.git (fetch)
origin  https://github.com/maple824/VideoGen-Builder-100.git (push)
```

如果没有看到 `origin`，说明本地仓库还没有绑定 GitHub 远程仓库。

---

### 3. 当前分支是否为 main

检查命令：

```bash
git branch
```

如果当前在 `main` 分支，会看到：

```text
* main
```

本项目默认使用：

```text
main
```

作为主分支。

---

## 二、项目基本信息

本地项目路径：

```text
/root/Workspace/VideoGen-Builder-100
```

Conda 环境：

```text
videogen
```

GitHub 仓库：

```text
https://github.com/maple824/VideoGen-Builder-100.git
```

主分支：

```text
main
```

说明：Git 同步不一定需要激活 Conda 环境。只有在运行 Python 脚本、测试或环境检查时，才需要确认当前 Python / Conda 环境是否正确。

---

## 三、本项目文件约定

从 Day004 开始，正式学习日采用双文档体系：

```text
days/dayXXX/TASK.md
days/dayXXX/README.md
```

其中：

* `TASK.md` 用于说明当天学习任务。
* `README.md` 用于记录当天实际学习过程。

如果当天需要写脚本，脚本必须放在当天对应目录下：

```text
scripts/dayXXX/
```

示例：

```text
days/day004/TASK.md
days/day004/README.md
scripts/day004/hello_project.py
```

不要把 Day004 之后的每日脚本直接放在 `scripts/` 根目录。

Phase 0 的仓库级脚本可以保留在 `scripts/` 根目录，例如：

```text
scripts/check_env.py
```

---

## 四、日常同步的标准流程

每次完成一组相关改动后，建议按下面顺序同步到 GitHub：

```text
查看改动
→ 添加到暂存区
→ 再次确认暂存区
→ 提交 commit
→ 拉取远程最新版本
→ 推送到 GitHub
→ 确认同步成功
```

对应命令：

```bash
git status
git add .
git status
git commit -m "本次改动说明"
git pull --rebase origin main
git push origin main
git status
```

如果你还没有进入项目根目录，先执行：

```bash
cd /root/Workspace/VideoGen-Builder-100
```

后续命令默认都在项目根目录执行。

---

## 五、查看当前改动

执行：

```bash
git status
```

常见输出包括：

```text
modified:   某个文件
```

表示已有文件被修改。

```text
untracked files: 某个新文件
```

表示新建文件还没有被 Git 跟踪。

```text
nothing to commit, working tree clean
```

表示当前没有需要提交的改动。

在执行 `git add` 前，应先看清楚 `git status` 中列出的文件，确认这些改动是否都属于本次提交。

---

## 六、添加改动到暂存区

在执行 `git commit` 之前，需要先用 `git add` 把本次要提交的文件加入暂存区。

可以理解为：

```text
修改了文件
→ git add 选择这次要提交哪些文件
→ git commit 生成一次本地提交
→ git push 同步到 GitHub
```

`git add` 只是把文件加入“本次提交的准备区”，还没有真正提交，也没有同步到 GitHub。

---

### 1. 添加当前项目下所有改动

命令：

```bash
git add .
```

这里的 `.` 表示当前所在目录。

如果你当前在项目根目录，`git add .` 会添加整个项目中的改动，例如：

```text
README.md
COURSE_MAP.md
PROJECTS.md
GROWTH_ROADMAP.md
docs/*.md
days/dayXXX/TASK.md
days/dayXXX/README.md
scripts/dayXXX/*.py
src/*
tests/*
projects/*
```

适用场景：

* 你刚完成一天学习内容
* 当前所有改动都属于同一个任务
* `git status` 中显示的所有改动都可以一起提交

示例：

```bash
git status
git add .
git status
```

---

### 2. 只添加某一个文件

如果你只想提交某一个文件，不想把其他改动一起提交，可以指定文件路径。

格式：

```bash
git add 文件路径
```

示例：只添加 Day004 的任务说明：

```bash
git add days/day004/TASK.md
```

示例：只添加 Day004 的学习记录：

```bash
git add days/day004/README.md
```

示例：只添加 Git 同步流程文档：

```bash
git add docs/git-sync-workflow.md
```

示例：只添加 Day004 的 Python 脚本：

```bash
git add scripts/day004/hello_project.py
```

---

### 3. 添加多个文件

如果多个文件属于同一个任务，可以在一条命令中一次性添加多个路径。

格式：

```bash
git add 文件路径1 文件路径2 文件路径3
```

示例：同时添加 Day004 的任务说明、学习记录和脚本：

```bash
git add days/day004/TASK.md days/day004/README.md scripts/day004/hello_project.py
```

示例：同时添加文档和脚本：

```bash
git add docs/git-sync-workflow.md scripts/day004/hello_project.py
```

---

### 4. 添加整个目录

如果一个目录下的所有改动都属于本次提交，可以直接添加整个目录。

格式：

```bash
git add 目录路径/
```

示例：添加整个 `docs/` 目录：

```bash
git add docs/
```

示例：添加整个 Day004 学习文档目录：

```bash
git add days/day004/
```

示例：添加整个 Day004 脚本目录：

```bash
git add scripts/day004/
```

示例：添加某个项目目录：

```bash
git add projects/asset_scanner_cli/
```

---

### 5. 添加后再次检查

执行 `git add` 后，建议再次查看：

```bash
git status
```

如果看到：

```text
Changes to be committed:
```

说明这些文件已经进入暂存区，下一步可以执行 `git commit`。

如果还有：

```text
Changes not staged for commit:
```

说明还有一些已修改文件没有被加入暂存区。

如果还有：

```text
Untracked files:
```

说明还有一些新文件没有被加入暂存区。

---

### 6. 常见添加命令总结

添加当前项目下所有改动：

```bash
git add .
```

添加一个文件：

```bash
git add days/day004/README.md
```

添加 Day004 的任务说明和学习记录：

```bash
git add days/day004/TASK.md days/day004/README.md
```

添加 Day004 的脚本：

```bash
git add scripts/day004/hello_project.py
```

添加一个目录：

```bash
git add docs/
```

添加某一天的全部学习文档：

```bash
git add days/day004/
```

添加某一天的全部脚本：

```bash
git add scripts/day004/
```

添加多个目录：

```bash
git add docs/ days/day004/ scripts/day004/
```

---

## 七、提交改动

使用：

```bash
git commit -m "提交说明"
```

提交说明建议使用英文短句，格式保持清晰。

常用类型：

```text
docs: 文档修改
feat: 新增功能或脚本
fix: 修复问题
test: 新增或修改测试
refactor: 重构代码
chore: 项目结构、配置或杂项调整
```

示例：

```bash
git commit -m "docs: add day004 task and readme"
```

```bash
git commit -m "feat: add day004 hello project script"
```

```bash
git commit -m "docs: update git sync workflow"
```

---

## 八、推荐提交说明示例

更新每日学习记录：

```bash
git commit -m "docs: update day004 notes"
```

新增某一天任务说明和学习记录：

```bash
git commit -m "docs: add day004 task and readme"
```

新增 Python 脚本：

```bash
git commit -m "feat: add day004 hello project script"
```

新增或修改模板：

```bash
git commit -m "docs: update daily templates"
```

修改项目说明文档：

```bash
git commit -m "docs: update course map"
```

修复文档错误：

```bash
git commit -m "fix: correct roadmap typo"
```

调整项目结构：

```bash
git commit -m "chore: organize project files"
```

新增阶段项目：

```bash
git commit -m "feat: add asset scanner cli"
```

---

## 九、推送到 GitHub

推荐先拉取远程最新版本，再推送：

```bash
git pull --rebase origin main
```

然后：

```bash
git push origin main
```

原因：

* `git pull --rebase origin main` 会先同步 GitHub 上的最新提交。
* 可以减少本地和远程提交历史分叉的问题。
* `git push origin main` 会把本地提交上传到 GitHub。

如果你是一个人维护这个仓库，仍然建议保留 `git pull --rebase origin main` 这一步，避免 GitHub 页面或其他设备上出现新提交后发生冲突。

---

## 十、完整日常命令模板

每次完成一组改动后，可以在项目根目录按下面顺序执行：

```bash
git status

git add .

git status

git commit -m "docs: update dayXXX notes"

git pull --rebase origin main

git push origin main

git status
```

其中：

```text
docs: update dayXXX notes
```

需要替换成当前这次改动的真实说明。

如果本次改动是 Day004 的任务说明、学习记录和脚本，可以使用：

```bash
git commit -m "feat: add day004 hello project script"
```

如果本次只修改了文档，可以使用：

```bash
git commit -m "docs: update project docs"
```

---

## 十一、如何确认同步成功

推送完成后，执行：

```bash
git status
```

如果看到：

```text
On branch main
Your branch is up to date with 'origin/main'.
nothing to commit, working tree clean
```

说明本地已经没有未提交改动，并且已经和 GitHub 远程分支同步。

也可以查看最近 5 次提交：

```bash
git log --oneline -5
```

确认最新 commit message 是否出现。

还可以打开 GitHub 仓库页面，确认最新提交已经显示在页面上。

---

## 十二、遇到问题时的处理原则

### 1. 如果 `git status` 显示没有改动

示例：

```text
nothing to commit, working tree clean
```

说明当前没有需要提交的内容，不需要执行 `git add`、`git commit`、`git push`。

---

### 2. 如果 `git commit` 提示没有内容可提交

示例：

```text
nothing to commit, working tree clean
```

常见原因：

* 文件没有实际变化。
* 改动已经提交过。
* 还没有保存文件。
* 当前不在项目目录中。

处理方式：

```bash
git status
```

确认当前状态即可。

---

### 3. 如果 `git push` 出现网络错误

常见原因：

* 网络不稳定
* GitHub 连接中断
* 代理配置异常

可以先重新执行：

```bash
git push origin main
```

如果仍然失败，再检查网络、代理或 GitHub 连接状态。

---

### 4. 如果 `git pull --rebase origin main` 出现冲突

不要继续执行 `git push`。

先执行：

```bash
git status
```

查看哪些文件冲突。

冲突文件里通常会出现类似内容：

```text
<<<<<<< HEAD
本地内容
=======
远程内容
>>>>>>> 分支信息
```

处理原则：

1. 手动打开冲突文件。
2. 判断保留本地内容、远程内容，还是合并两边内容。
3. 删除冲突标记。
4. 保存文件。
5. 执行：

```bash
git add .
git rebase --continue
git push origin main
```

如果不确定如何处理冲突，不要继续操作。先记录当前报错、冲突文件路径和 `git status` 输出。

---

### 5. 如果误用了 `git add .`

如果你执行了：

```bash
git add .
```

但发现有些文件不想放进本次提交，可以先取消暂存。

取消全部暂存：

```bash
git restore --staged .
```

取消某个文件暂存：

```bash
git restore --staged 文件路径
```

示例：

```bash
git restore --staged README.md
```

然后重新选择需要提交的文件：

```bash
git add days/day004/TASK.md days/day004/README.md scripts/day004/hello_project.py
```

---

## 十三、推荐的工作习惯

每次学习任务结束后，做一次同步即可。

推荐节奏：

```text
完成一个 Day 的内容
→ 检查文件
→ git status
→ git add
→ git commit
→ git pull --rebase origin main
→ git push origin main
→ git status
```

不要每修改一个小句子就提交一次。

比较合适的提交单位：

* 完成一天学习记录
* 完成一个脚本
* 完成一个阶段性文档
* 完成一个模板
* 完成一个阶段项目
* 修复一个明确问题

---

## 十四、当前项目建议提交粒度

本项目推荐：

```text
Day004 完成后提交一次
Day005 完成后提交一次
每个 docs 文档完成后提交一次
每个 scripts/dayXXX/ 脚本完成后提交一次
每个 projects/ 阶段项目完成后提交一次
```

从 Day004 开始，一个完整学习日通常至少包含：

```text
days/dayXXX/TASK.md
days/dayXXX/README.md
```

如果当天写了脚本，还应包含：

```text
scripts/dayXXX/
```

示例：Day004 完整提交：

```bash
git add days/day004/TASK.md days/day004/README.md scripts/day004/
git commit -m "feat: add day004 hello project script"
git pull --rebase origin main
git push origin main
```

示例：只提交 Git 同步流程文档：

```bash
git add docs/git-sync-workflow.md
git commit -m "docs: update git sync workflow"
git pull --rebase origin main
git push origin main
```

示例：只提交模板文件：

```bash
git add docs/task-template.md docs/day-template.md
git commit -m "docs: update daily templates"
git pull --rebase origin main
git push origin main
```

---

## 十五、最短记忆版

日常只需要记住：

```bash
git status
git add .
git status
git commit -m "本次改动说明"
git pull --rebase origin main
git push origin main
git status
```

如果只想提交某一天内容，可以更精确地添加：

```bash
git add days/dayXXX/ scripts/dayXXX/
git commit -m "docs: update dayXXX notes"
git pull --rebase origin main
git push origin main
```

完成后，如果 `git status` 显示：

```text
nothing to commit, working tree clean
```

说明本地工作区已经干净。
