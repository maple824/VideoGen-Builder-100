# GitHub 同步流程

本文档记录 `VideoGen-Builder-100` 项目本地改动同步到 GitHub 的标准流程。

适用场景：

* 新增或修改了 `README.md`
* 新增或修改了 `days/dayXXX/README.md`
* 新增或修改了 `docs/*.md`
* 新增或修改了 `scripts/*.py`
* 完成了某一天学习任务后，需要提交到 GitHub

---

## 一、项目基本信息

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

---

## 二、日常同步的标准流程

每次完成一部分改动后，在终端执行下面流程。

### 1. 进入项目目录

```bash
cd /root/Workspace/VideoGen-Builder-100
```

### 2. 查看当前改动

```bash
git status
```

常见情况：

```text
modified:   某个文件
untracked files: 某个新文件
```

含义：

* `modified`：已有文件被修改
* `untracked files`：新建文件还没有被 Git 跟踪
* `nothing to commit, working tree clean`：当前没有需要提交的改动

---

## 三、添加改动到暂存区

在执行 `git commit` 之前，需要先用 `git add` 把本次要提交的文件加入 Git 暂存区。

可以理解为：

```text
修改了文件
→ git add 选择这次要提交哪些文件
→ git commit 生成一次本地提交
→ git push 同步到 GitHub
```

注意：

`git add` 只是把文件加入“本次提交的准备区”，还没有真正提交，也没有同步到 GitHub。

---

### 1. `git add .` 中的 `.` 是什么意思

命令：

```bash
git add .
```

这里的 `.` 表示：

```text
当前所在目录
```

也就是说，`git add .` 会把“当前目录及其子目录下”的所有改动都加入暂存区。

例如你当前在项目根目录：

```bash
cd /root/Workspace/VideoGen-Builder-100
```

然后执行：

```bash
git add .
```

它会添加整个项目里的改动，包括：

```text
README.md
COURSE_MAP.md
PROJECTS.md
GROWTH_ROADMAP.md
docs/*.md
days/dayXXX/README.md
scripts/*.py
src/*
```

只要这些文件位于当前项目目录下，并且有新增、修改或删除，都会被加入暂存区。

---

### 2. 日常最推荐的方式：在项目根目录执行 `git add .`

本项目通常建议先进入项目根目录：

```bash
cd /root/Workspace/VideoGen-Builder-100
```

然后查看改动：

```bash
git status
```

确认这些改动都是你这次想提交的内容后，执行：

```bash
git add .
```

适用场景：

* 你刚完成一天的学习内容
* 这次改动的文件都属于同一个任务
* 你确认当前所有改动都可以一起提交

例如 Day004 完成后，可能同时修改了：

```text
days/day004/README.md
scripts/day004/hello_project.py
docs/git-sync-workflow.md
```

这种情况下可以直接：

```bash
git add .
```

然后：

```bash
git commit -m "docs: update day004 notes"
```

---

### 3. 如果只想添加某一个文件

如果你只想提交某一个文件，不想把其他改动一起提交，可以指定文件路径。

格式：

```bash
git add 文件路径
```

示例 1：只添加 Day004 README

```bash
git add days/day004/README.md
```

示例 2：只添加 Git 同步流程文档

```bash
git add docs/git-sync-workflow.md
```

示例 3：只添加 Python 脚本

```bash
git add scripts/hello_project.py
```

然后提交：

```bash
git commit -m "feat: add hello project script"
```

---

### 4. 如果有多个不同路径的文件需要一起提交

如果多个文件属于同一个任务，可以在一条命令中一次性添加多个路径。

格式：

```bash
git add 文件路径1 文件路径2 文件路径3
```

示例：同时添加 Day004 README 和脚本

```bash
git add days/day004/README.md scripts/hello_project.py
```

然后提交：

```bash
git commit -m "feat: add day004 hello project script"
```

示例：同时添加文档和脚本

```bash
git add docs/git-sync-workflow.md scripts/hello_project.py
```

然后提交：

```bash
git commit -m "docs: add git sync workflow and hello script"
```

---

### 5. 如果想添加整个目录

如果一个目录下的所有改动都属于本次提交，可以直接添加整个目录。

格式：

```bash
git add 目录路径/
```

示例 1：添加整个 docs 目录下的改动

```bash
git add docs/
```

示例 2：添加整个 Day004 目录

```bash
git add days/day004/
```

示例 3：添加整个 scripts 目录

```bash
git add scripts/
```

这种方式比 `git add .` 范围更小，只会添加指定目录内的改动。

---

### 6. 推荐判断方法

在执行 `git add` 前，先看：

```bash
git status
```

如果显示的所有改动都是这次要提交的内容，可以用：

```bash
git add .
```

如果只想提交其中一部分文件，就用：

```bash
git add 指定文件路径
```

或：

```bash
git add 指定目录路径/
```

---

### 7. 添加后再次检查

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

### 8. 常见用法总结

添加当前项目下所有改动：

```bash
git add .
```

添加一个文件：

```bash
git add days/day004/README.md
```

添加多个文件：

```bash
git add days/day004/README.md scripts/hello_project.py docs/git-sync-workflow.md
```

添加一个目录：

```bash
git add docs/
```

添加多个目录：

```bash
git add docs/ scripts/ days/day004/
```

---

### 9. 本项目推荐用法

大多数情况下，建议使用：

```bash
cd /root/Workspace/VideoGen-Builder-100
git status
git add .
git status
```

前提是：

```text
git status 中显示的所有改动，都是你这次想提交的内容。
```

如果你当前同时改了多个不相关内容，例如：

```text
days/day004/README.md
scripts/hello_project.py
docs/git-sync-workflow.md
README.md
```

但你只想先提交 Git 同步流程文档，那么不要用 `git add .`，而应该用：

```bash
git add docs/git-sync-workflow.md
git commit -m "docs: add git sync workflow"
```

之后再单独提交 Day004 内容：

```bash
git add days/day004/README.md scripts/hello_project.py
git commit -m "feat: add day004 hello project script"
```

这样提交历史会更清晰。


---

## 四、提交改动

使用：

```bash
git commit -m "提交说明"
```

提交说明建议使用英文短句，格式保持清晰。

常用提交类型：

```text
docs: update day004 notes
docs: add git sync workflow
feat: add hello project script
fix: correct python environment notes
chore: update project structure
```

示例：

```bash
git commit -m "docs: add git sync workflow"
```

---

## 五、推送到 GitHub

### 推荐流程：先拉取远程最新版本，再推送

```bash
git pull --rebase origin main
```

然后：

```bash
git push origin main
```

原因：

* `git pull --rebase origin main` 会先同步 GitHub 上的最新提交
* 可以减少本地和远程提交历史分叉的问题
* `git push origin main` 会把本地提交上传到 GitHub

---

## 六、完整日常命令模板

每次完成改动后，可以按下面顺序执行：

```bash
cd /root/Workspace/VideoGen-Builder-100

git status

git add .

git status

git commit -m "docs: update dayXXX notes"

git pull --rebase origin main

git push origin main
```

其中：

```text
docs: update dayXXX notes
```

需要替换成当前这次改动的真实说明。

---

## 七、常见提交说明示例

### 更新每日学习记录

```bash
git commit -m "docs: update day004 notes"
```

### 新增某一天 README

```bash
git commit -m "docs: add day004 readme"
```

### 新增 Python 脚本

```bash
git commit -m "feat: add hello project script"
```

### 修改项目说明文档

```bash
git commit -m "docs: update course map"
```

### 修复文档错误

```bash
git commit -m "fix: correct roadmap typo"
```

### 调整项目结构

```bash
git commit -m "chore: organize project files"
```

---

## 八、如何确认同步成功

推送完成后，可以执行：

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

也可以执行：

```bash
git log --oneline -5
```

查看最近 5 次提交。

或者打开 GitHub 仓库页面，确认最新 commit message 已经出现。

---

## 九、遇到问题时的处理原则

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

说明文件没有实际变化，或者已经提交过。

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

处理方式：

先重新执行：

```bash
git push origin main
```

如果仍然失败，再检查代理或网络环境。

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

1. 手动打开冲突文件
2. 保留正确内容
3. 删除冲突标记
4. 保存文件
5. 执行：

```bash
git add .
git rebase --continue
git push origin main
```

如果不确定如何处理冲突，不要继续操作，先记录当前报错和 `git status` 输出。

---

## 十、推荐的工作习惯

每次学习任务结束后，只做一次同步即可。

推荐节奏：

```text
完成一个 Day 的内容
→ 检查文件
→ git status
→ git add .
→ git commit
→ git pull --rebase origin main
→ git push origin main
```

不要每修改一个小句子就提交一次。

比较合适的提交单位：

* 完成一天学习记录
* 完成一个脚本
* 完成一个阶段性文档
* 修复一个明确问题

---

## 十一、当前项目建议提交粒度

本项目推荐：

```text
Day004 完成后提交一次
Day005 完成后提交一次
每个 docs 文档完成后提交一次
每个 scripts 脚本完成后提交一次
```

示例：

```bash
git commit -m "docs: add git sync workflow"
git commit -m "feat: add day004 hello project script"
git commit -m "docs: add day004 readme"
```

---

## 十二、最短记忆版

日常只需要记住：

```bash
cd /root/Workspace/VideoGen-Builder-100

git status
git add .
git commit -m "本次改动说明"
git pull --rebase origin main
git push origin main
```

完成后用：

```bash
git status
```

确认工作区干净。
