# Day004 - Python 工程入口：第一个可复现脚本

## 今天学什么

今天的目标是完成项目中的第一个正式 Python 工程脚本。

你将学习：

* 如何在项目约定目录下放置每日脚本
* 如何从 VS Code 终端运行 Python 文件
* 如何用 `main()` 组织脚本入口
* 如何理解 `if __name__ == "__main__"`
* 如何理解一个 `.py` 文件既可以作为脚本运行，也可以在未来作为模块被导入

今天不学习文件扫描，也不正式学习路径处理。路径相关内容会在 Day005 展开。

## 为什么学

`VideoGen-Builder-100` 后续会逐步进入视频处理、图像分析、深度学习、Diffusers 和 ComfyUI。

这些内容都会依赖一个基础能力：

> 你能不能把一个 Python 脚本放在正确的位置，并且稳定地运行它。

很多新手在后续阶段遇到的问题，并不是模型本身的问题，而是：

* 不知道脚本应该放在哪里
* 不知道应该从哪里运行脚本
* 代码直接散落在文件顶层，后续不好复用
* 分不清“直接运行脚本”和“被其他文件导入”的区别
* 没有记录运行结果，导致学习过程不可复现

Day004 先建立最小 Python 工程习惯。

## 推荐学习资料

今天只需要阅读和理解以下资料中的相关部分，不需要完整学完。

### Python 官方文档：`__main__`

* [`__main__`](https://docs.python.org/3/library/__main__.html)[ - Top-level code environment](https://docs.python.org/3/library/__main__.html)

重点理解：

* 什么是顶层代码环境
* 为什么脚本中常见写法是 `if __name__ == "__main__"`
* 为什么直接运行一个 `.py` 文件时，它的 `__name__` 会变成 `"__main__"`

### Python 官方教程：Modules

* [Python Tutorial - Modules](https://docs.python.org/3/tutorial/modules.html)

重点理解：

* 一个 `.py` 文件可以作为脚本运行
* 一个 `.py` 文件也可以被其他 Python 文件导入
* 为什么不建议把所有逻辑都直接写在文件顶层

### Python 官方文档：`sys`

- [`sys` - System-specific parameters and functions](https://docs.python.org/3/library/sys.html)

重点理解：

- `sys` 是 Python 标准库模块
- `sys.version` 可以查看当前运行脚本所使用的 Python 版本
- 今天只需要用它打印版本号，不需要深入学习 `sys` 的其他功能

### VS Code Python 入门

* [Getting Started with Python in VS Code](https://code.visualstudio.com/docs/python/python-tutorial)

重点理解：

* 如何打开 VS Code 集成终端
* 如何运行 Python 文件
* 如何查看脚本输出结果

## 今日核心概念

### 1. 脚本位置

Day004 的脚本必须放在：

```text
scripts/day004/
```

今天需要创建：

```text
scripts/day004/hello_project.py
```

不要放在：

```text
scripts/hello_project.py
```

原因是本项目按天组织学习产物。后续会有很多脚本，如果全部放在 `scripts/` 根目录，项目会很快变得混乱。

### 2. Python 脚本

Python 脚本通常是一个可以直接运行的 `.py` 文件。

例如：

```bash
python scripts/day004/hello_project.py
```

它的作用可以很简单：打印项目名称、当前学习日、Python 版本和运行状态。

今天的重点不是写复杂功能，而是建立一个清晰、稳定、可复现的脚本入口。

### 3. `main()` 函数

推荐把脚本的主要逻辑放进 `main()` 函数：

```python
def main() -> None:
    ...
```

这样做的好处是：

* 脚本入口更清晰
* 后续更容易复用
* 后续更容易测试
* 避免所有逻辑都散落在文件顶层

今天只需要理解：`main()` 是脚本主要逻辑的入口函数。

### 4. `if __name__ == "__main__"`

常见写法：

```python
if __name__ == "__main__":
    main()
```

它的意思是：

> 只有当这个文件被直接运行时，才执行 `main()`。

如果这个文件未来被其他 Python 文件导入，`main()` 不会自动执行。

今天只需要理解到这个层面，不需要深入 Python 导入系统。

### 5. 模块意识

一个 `.py` 文件有两种常见使用方式：

第一种是直接运行：

```bash
python scripts/day004/hello_project.py
```

第二种是在未来被其他 Python 文件导入：

```python
import hello_project
```

Day004 先建立这个意识：写脚本时，不只是让它“现在能跑”，也要让它未来有机会被复用。

### 6. 可复现运行

今天的脚本应该能从终端稳定运行，并输出清晰结果。

README 中需要记录实际运行命令和实际输出结果。

应该记录类似：

```text
运行命令：
python scripts/day004/hello_project.py

运行结果：
Project: VideoGen-Builder-100
Day: Day004
Python: 3.x.x
Script: hello_project.py
Status: OK
```

## 实践任务

## 实践任务

### 任务 1：创建 Day004 脚本目录

创建目录：

```text
scripts/day004/
```

今天的脚本文件路径为：

```text
scripts/day004/hello_project.py
```

不要把每日脚本直接放到 `scripts/` 根目录。

正确位置：

```text
scripts/day004/hello_project.py
```

### 任务 2：编写第一个项目脚本

脚本目标：

* 打印项目名称
* 打印当前学习日
* 打印今日主题
* 打印 Python 版本
* 打印脚本名称
* 打印一个成功状态信息

今天的脚本只训练“如何写一个清晰、可运行的 Python 工程入口”。

今天不处理真实路径计算，也不定位项目根目录。

脚本要求：

* 使用 `main()` 函数组织主要逻辑
* 使用 `if __name__ == "__main__"` 调用 `main()`
* 可以使用 Python 标准库 `sys`
* 可以使用 `sys.version.split()[0]` 获取 Python 版本
* 脚本名称直接写成普通字符串 `"hello_project.py"`
* 不接收命令行参数
* 不读取文件
* 不写入文件
* 不扫描目录
* 不使用第三方 Python 包
* 不使用 `pathlib`
* 不使用 `Path`
* 不使用 `__file__`
* 不计算项目根目录
* 不输出项目根目录

建议脚本输出类似：

```text
Project: VideoGen-Builder-100
Day: Day004
Topic: Python project entry
Python: 3.x.x
Script: hello_project.py
Status: OK
```

其中：

* `3.x.x` 会根据你的本机 Python 版本自动变化
* `Script` 今天只写脚本文件名，不需要输出完整路径
* `Status` 只需要表示脚本成功运行

### 任务 3：对照标准实践脚本

自己完成脚本编写并成功运行后，再对照标准实践脚本：scripts/day004/hello_project.py


### 任务 4：填写 README 学习记录

运行脚本后，把实际运行命令和终端输出结果记录到：

```text
days/day004/README.md
```

README 中至少应该记录：

* 今天创建了哪些文件
* 实际运行的命令
* 终端输出结果
* 对 `main()` 的理解
* 对 `if __name__ == "__main__"` 的理解
* 今天遇到的问题和解决方式

注意：README 中应记录你自己实际看到的结果，不要直接复制示例结果。


## 完成标准

完成 Day004 需要满足：

* [ ] `days/day004/TASK.md` 已创建
* [ ] `days/day004/README.md` 已创建
* [ ] `scripts/day004/hello_project.py` 已创建
* [ ] 脚本没有放在 `scripts/` 根目录
* [ ] 脚本可以从 VS Code 终端成功运行
* [ ] 脚本中定义了 `main()` 函数
* [ ] 脚本中使用了 `if __name__ == "__main__"`
* [ ] 输出中包含项目名称、Day 编号、Python 版本、脚本名称和成功状态
* [ ] README 中记录了实际运行命令
* [ ] README 中记录了实际运行结果
* [ ] 没有提前引入文件扫描
* [ ] 没有提前引入 CLI 参数
* [ ] 没有提前引入视频处理
* [ ] 没有提前引入第三方库
* [ ] 没有把 `pathlib` 作为今天的学习内容

## 常见误区

### 误区 1：把每日脚本直接放到 `scripts/`

错误示例：

```text
scripts/hello_project.py
```

正确示例：

```text
scripts/day004/hello_project.py
```

本项目会持续 100 天，脚本必须按天归档。

### 误区 2：所有代码都写在文件顶层

不推荐：

```python
print("Project: VideoGen-Builder-100")
print("Day: Day004")
```

推荐：

```python
def main() -> None:
    print("Project: VideoGen-Builder-100")
    print("Day: Day004")


if __name__ == "__main__":
    main()
```

Day004 的目标之一，就是建立清晰的脚本入口习惯。

### 误区 3：今天就开始做文件扫描

Day004 只做 Python 工程入口。

文件路径和文件扫描会在 Day005 展开。

今天不要写：

```python
glob(...)
```

也不要写：

```python
rglob(...)
```

### 误区 4：今天就引入命令行参数

今天不需要：

```bash
python scripts/day004/hello_project.py --name demo
```

也不需要使用：

```python
argparse
```

命令行参数会在后续学习日再处理。

### 误区 5：今天就引入 `pathlib`

`pathlib` 很重要，但不属于 Day004 的核心任务。

今天只需要能稳定运行一个结构清晰的 Python 脚本。

路径处理会在 Day005 正式学习。

### 误区 6：只截图，不记录文本结果

README 中应该记录可复制的文本结果。

截图可以辅助，但不能替代命令和输出文本。

错误记录方式：

```text
运行成功，见截图。
```

更好的记录方式：

```text
运行命令：
python scripts/day004/hello_project.py

运行结果：
Project: VideoGen-Builder-100
Day: Day004
Topic: Python project entry
Python: 3.x.x
Script: hello_project.py
Status: OK
```

## 和后续项目的关系

Day004 是后续所有 Python 工程任务的入口。

它会直接服务于：

* Project 01：Asset Scanner CLI
* Project 02：Video Preprocess CLI
* Project 03：Video Frame Analyzer
* Project 08：VideoGen Evaluation Dashboard

后续项目都会依赖今天建立的习惯：

* 脚本放在清晰目录中
* 从终端运行脚本
* 使用 `main()` 管理入口
* 使用 `if __name__ == "__main__"` 控制直接运行行为
* 在 README 中记录运行命令和输出结果

Day004 先解决“一个 Python 工程脚本应该如何开始”。

Day005 再进入“Python 如何理解项目中的文件路径”。
