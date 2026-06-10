# Day005 - pathlib 与最小文件扫描

## 今天学什么

今天的目标是正式学习 Python 项目中的路径处理，并完成一个最小文件扫描脚本。

你将学习：

* 如何使用 `pathlib.Path` 表示文件和目录路径
* 如何理解 `__file__`
* 如何根据当前脚本位置定位项目根目录
* 如何使用 `/` 拼接路径
* 如何检查目录是否存在
* 如何判断一个路径是不是目录
* 如何遍历一个目录下的直接内容
* 如何判断一个路径是不是文件
* 如何获取文件名和文件扩展名

今天会创建：

```text
scripts/day005/file_scanner.py
```

这个脚本会扫描上一天的脚本目录：

```text
scripts/day004/
```

并输出其中发现的文件信息。

## 为什么学

后续项目会频繁处理文件和目录，例如：

* 扫描素材文件
* 处理视频文件
* 拆分视频帧
* 分析图像文件
* 保存模型输出
* 整理评估结果
* 发布 GitHub Pages 作品集资源

这些任务都依赖一个基础能力：

> Python 脚本能不能稳定地找到项目中的文件。

很多工程问题不是模型问题，而是路径问题：

* 文件放在哪里
* 当前脚本在哪里
* 相对路径相对于谁
* 为什么在 VS Code 里能运行，换一个终端位置就失败
* 为什么本机路径不能给别人复现

Day005 先解决这些问题的最小版本。

今天不是实现完整 Asset Scanner CLI，而是为它建立路径和文件扫描基础。

## 前置条件

本项目默认你已经完成前面学习日的基础环境准备，并能够：

* 使用 VS Code 打开项目文件夹
* 在 VS Code 终端运行 Python 脚本
* 理解 Day004 中的 `main()` 和 `if __name__ == "__main__"`

今天没有新增外部工具依赖。

今天只使用 Python 标准库，不需要安装第三方包。

今天正式学习 Python 标准库中的 `pathlib`。

建议你已经完成 Day004，并保留以下文件：

```text
scripts/day004/hello_project.py
```

Day005 的脚本会扫描：

```text
scripts/day004/
```

如果这个目录或文件不存在，脚本可以运行，但输出结果会和示例不同。

## 推荐学习资料

今天只需要阅读和理解以下资料中的相关部分，不需要完整学完。

### Python 官方文档：pathlib

* [pathlib - Object-oriented filesystem paths](https://docs.python.org/3/library/pathlib.html)

重点理解：

* `Path` 可以表示文件路径或目录路径
* `Path(__file__)` 可以表示当前脚本文件路径
* `Path.resolve()` 可以得到更明确的路径
* `path.parent` 和 `path.parents` 可以获取上级目录
* `path / "name"` 可以拼接路径
* `path.exists()` 可以检查路径是否存在
* `path.is_dir()` 可以判断路径是否为目录
* `path.is_file()` 可以判断路径是否为文件
* `path.iterdir()` 可以遍历目录内容
* `path.name` 可以获取文件名
* `path.suffix` 可以获取文件扩展名

### Path 对象
* [pathlib.Path](https://docs.python.org/3/library/pathlib.html#pathlib.Path)

重点理解：

* Path.cwd() 表示当前工作目录，也就是你运行命令时所在的目录
* Path.home() 表示当前用户的主目录
* Path("some/path") 可以把字符串路径转换成 Path 对象
* Path 对象可以继续使用 .exists()、.is_file()、.is_dir() 等方法做路径判断

### Python 官方文档：`__main__`

* [`__main__` - Top-level code environment](https://docs.python.org/3/library/__main__.html)

Day004 已经学习过 `if __name__ == "__main__"`。

今天只沿用这个写法，不再把它作为重点展开。

## 今日核心概念

### 1. `Path` 对象

`Path` 是 Python 标准库 `pathlib` 中的路径对象。

示例：

```python
from pathlib import Path

path = Path("scripts/day004/hello_project.py")
```

它比普通字符串路径更适合工程项目，因为它提供了很多路径相关方法。

例如：

```python
path.name
path.suffix
path.parent
path.is_file()
```

今天只学习脚本会用到的最小方法，不展开 `pathlib` 的全部功能。

### 2. `__file__`

`__file__` 表示当前 Python 脚本文件的位置。

如果当前脚本是：

```text
scripts/day005/file_scanner.py
```

那么在脚本中使用：

```python
Path(__file__)
```

就可以得到当前脚本文件路径。

今天只需要理解：

> `__file__` 可以让脚本知道“自己在哪里”。

### 3. 当前脚本路径

常见写法：

```python
script_path = Path(__file__).resolve()
```

含义是：

> 找到当前脚本文件，并得到一个更明确的路径。

这可以避免脚本过度依赖终端当前所在目录。

### 4. 项目根目录

今天的脚本放在：

```text
scripts/day005/file_scanner.py
```

从这个文件向上回到项目根目录：

```text
file_scanner.py        当前脚本
day005/                parents[0]
scripts/               parents[1]
VideoGen-Builder-100/  parents[2]
```

因此可以写：

```python
project_root = Path(__file__).resolve().parents[2]
```

这依赖本项目的固定目录结构。

今天只需要掌握这个项目中的写法，不需要展开 Python 导入系统或包管理。

### 5. 路径拼接

`pathlib` 推荐使用 `/` 拼接路径。

示例：

```python
scan_dir = project_root / "scripts" / "day004"
```

不要写死本机绝对路径，例如：

```python
Path("/Users/yourname/Desktop/VideoGen-Builder-100/scripts/day004")
```

写死绝对路径会导致别人无法复现。

### 6. 检查目录是否存在

在扫描目录前，先检查路径是否存在：

```python
scan_dir.exists()
```

如果目录不存在，脚本应该输出提示，而不是直接报错。

### 7. 判断路径是否为目录

存在的路径不一定是目录。

可以使用：

```python
scan_dir.is_dir()
```

确认它是一个目录。

### 8. 遍历一层目录

今天只扫描一层目录，不做递归扫描。

示例：

```python
for path in scan_dir.iterdir():
    ...
```

`iterdir()` 会列出目录中的直接内容。

### 9. 判断路径是否为文件

目录中可能既有文件，也有子目录。

今天只统计文件：

```python
path.is_file()
```

### 10. 文件名和扩展名

对于文件：

```text
scripts/day004/hello_project.py
```

可以得到文件名：

```python
path.name
```

结果是：

```text
hello_project.py
```

也可以得到扩展名：

```python
path.suffix
```

结果是：

```text
.py
```

这会为后续识别图片、视频和配置文件打基础。

## 实践任务

### 任务 1：创建 Day005 脚本目录

创建目录：

```text
scripts/day005/
```

今天的脚本文件路径为：

```text
scripts/day005/file_scanner.py
```

不要把每日脚本直接放到 `scripts/` 根目录。

正确位置：

```text
scripts/day005/file_scanner.py
```

错误位置：

```text
scripts/file_scanner.py
```

### 任务 2：编写最小文件扫描脚本

脚本目标：

* 定位当前脚本路径
* 根据当前脚本路径定位项目根目录
* 定位扫描目录 `scripts/day004/`
* 检查扫描目录是否存在
* 检查扫描路径是否为目录
* 遍历扫描目录下的一层内容
* 找出其中的文件
* 输出文件数量
* 输出文件相对路径
* 输出文件名
* 输出文件扩展名
* 输出完成状态

脚本要求：

* 使用 `pathlib.Path`
* 使用 `__file__`
* 使用 `main()` 函数
* 使用 `if __name__ == "__main__"`
* 扫描目录固定为 `scripts/day004/`
* 只扫描一层目录
* 不接收命令行参数
* 不使用 `argparse`
* 不使用 `glob`
* 不使用 `rglob`
* 不递归扫描
* 不读取文件内容
* 不写入文件
* 不输出 JSON
* 不输出 CSV
* 不统计文件大小
* 不读取图片或视频元数据
* 不安装第三方包
* 不实现完整 Asset Scanner CLI

建议输出类似：

```text
Project: VideoGen-Builder-100
Day: Day005
Topic: pathlib and minimal file scan
Project root: <your-project-root>
Scan directory: scripts/day004
Files found: 1
File list:
- scripts/day004/hello_project.py | name: hello_project.py | suffix: .py
Status: OK
```

其中：

* `<your-project-root>` 会因电脑不同而不同
* 文件数量可能因你的 `scripts/day004/` 目录内容不同而不同
* 如果 Day004 文件不存在，输出结果会不同

### 任务 3：对照标准实践脚本

自己完成脚本编写并成功运行后，再对照标准实践脚本：scripts/day005/file_scanner.py

### 任务 4：填写 README 学习记录

运行脚本后，把实际运行命令和终端输出结果记录到：

```text
days/day005/README.md
```

README 中至少应该记录：

* 今天创建了哪些文件
* 实际运行的命令
* 终端输出结果
* 对 `Path` 的理解
* 对 `__file__` 的理解
* 对项目根目录定位方式的理解
* 对文件扩展名的理解
* 今天遇到的问题和解决方式

注意：README 中应记录你自己实际看到的结果，不要直接复制示例结果。

## 今日产物

完成后，项目中应该新增：

```text
days/day005/TASK.md
days/day005/README.md
scripts/day005/file_scanner.py
```

## 完成标准

完成 Day005 需要满足：

* [ ] `days/day005/TASK.md` 已创建
* [ ] `days/day005/README.md` 已创建
* [ ] `scripts/day005/file_scanner.py` 已创建
* [ ] 脚本没有放在 `scripts/` 根目录
* [ ] 脚本使用了 `pathlib.Path`
* [ ] 脚本使用了 `__file__`
* [ ] 脚本可以定位项目根目录
* [ ] 脚本扫描的是 `scripts/day004/`
* [ ] 脚本会检查扫描目录是否存在
* [ ] 脚本会检查扫描路径是否为目录
* [ ] 脚本只扫描一层目录
* [ ] 脚本不会递归扫描
* [ ] 脚本可以输出文件数量
* [ ] 脚本可以输出文件相对路径
* [ ] 脚本可以输出文件名
* [ ] 脚本可以输出文件扩展名
* [ ] 脚本可以从 VS Code 终端成功运行
* [ ] README 中记录了实际运行命令
* [ ] README 中记录了实际运行结果
* [ ] 没有提前引入命令行参数
* [ ] 没有提前引入 `argparse`
* [ ] 没有提前引入递归扫描
* [ ] 没有提前进入视频处理
* [ ] 没有实现完整 Asset Scanner CLI

## 常见误区

### 误区 1：写死本机绝对路径

不推荐：

```python
scan_dir = Path("/Users/yourname/Desktop/VideoGen-Builder-100/scripts/day004")
```

这样写只能在你的电脑上运行。

推荐：

```python
project_root = Path(__file__).resolve().parents[2]
scan_dir = project_root / "scripts" / "day004"
```

这样更适合开源项目。

### 误区 2：只写相对路径，不考虑脚本从哪里运行

例如：

```python
scan_dir = Path("scripts/day004")
```

这种写法在项目根目录运行时通常没问题。

但如果你从其他目录运行脚本，就可能失败。

今天推荐基于 `__file__` 定位项目根目录，让脚本更稳定。

### 误区 3：今天就做递归扫描

今天只扫描一层目录。

不要使用：

```python
rglob("*")
```

递归扫描会增加复杂度，后续再处理。

### 误区 4：今天就做命令行参数

今天不需要：

```bash
python scripts/day005/file_scanner.py --dir scripts/day004
```

也不需要使用：

```python
argparse
```

命令行参数更适合 Day006。

### 误区 5：今天就扫描视频或图片元数据

Day005 只处理路径、文件名和扩展名。

不要提前读取：

* 视频时长
* 视频分辨率
* 视频帧率
* 图片尺寸
* 图片颜色信息

这些内容属于后续视频工程和图像处理阶段。

### 误区 6：把文件扫描做成完整工具

今天不需要做完整 Asset Scanner CLI。

今天只需要完成最小闭环：

```text
当前脚本位置 -> 项目根目录 -> 固定扫描目录 -> 文件列表 -> 文件名和扩展名
```

## 和后续项目的关系

Day005 直接服务于：

* Project 01：Asset Scanner CLI
* Project 02：Video Preprocess CLI
* Project 03：Video Frame Analyzer

后续这些项目都会依赖路径和文件扫描能力。

今天建立的最小能力是：

* 找到项目根目录
* 找到目标目录
* 遍历目录中的文件
* 识别文件名和扩展名

Day005 只建立基础，不提前实现完整工具。

后续学习日可以在此基础上继续加入：

* 命令行参数
* 用户指定扫描目录
* 文件类型过滤
* 递归扫描
* 结构化输出
