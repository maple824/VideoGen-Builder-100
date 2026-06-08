# Day004：Python 脚本结构

## 1. 今日主题

Python 脚本结构。

Day004 是 Phase 1：Python 工程基础 的第一天。

今天不学习视频生成模型，也不进入视频处理算法，而是先建立一个最小、稳定、可复用的 Python 脚本写法。

---

## 2. 今日目标

完成后应该理解：

* Python 脚本应该从哪里运行
* 为什么常见脚本会写 `main()` 函数
* `if __name__ == "__main__":` 的作用
* 如何在脚本中定位项目根目录
* `scripts/`、`days/`、`src/` 在项目中的分工

---

## 3. 今日文件

本日新增文件：

```text
scripts/day004/hello_project.py
days/day004/README.md
```

其中：

```text
scripts/day004/hello_project.py
```

用于练习最小 Python 脚本结构。

```text
days/day004/README.md
```

用于记录 Day004 的学习内容、运行方式和理解总结。

---

## 4. 项目目录中的三个关键位置

当前项目中，后续会长期使用三个目录：

```text
scripts/
days/
src/
```

它们的作用不同。

### 4.1 scripts/

`scripts/` 用来放可以直接运行的脚本。

例如：

```text
scripts/day004/hello_project.py
```

运行方式：

```bash
python scripts/day004/hello_project.py
```

后续项目中的很多工具雏形，都会先从 `scripts/` 开始。

例如：

```text
素材扫描脚本
视频信息检查脚本
批量预处理脚本
生成结果整理脚本
```

---

### 4.2 days/

`days/` 用来记录每天的学习过程。

例如：

```text
days/day004/README.md
```

这里不是放主要业务代码的地方，而是放学习记录、实验说明、问题总结。

后续每一天的学习，都应该在对应目录中留下 README。

---

### 4.3 src/

`src/` 后续用于放可复用的 Python 包代码。

Day004 暂时不深入 `src/`，只先知道它的定位：

```text
scripts/：直接运行的脚本
src/：可复用的项目代码
days/：每天的学习记录
```

后续当脚本中的逻辑变多时，会逐步把可复用函数从 `scripts/` 移到 `src/` 中。

---

## 5. 今日脚本

今日脚本路径：

```text
scripts/day004/hello_project.py
```

核心结构：

```python
from pathlib import Path


def get_project_root() -> Path:
    """Return the project root directory."""
    return Path(__file__).resolve().parents[1]


def main() -> None:
    project_root = get_project_root()

    print("VideoGen-Builder-100")
    print(f"Project root: {project_root}")
    print(f"Script file: {Path(__file__).resolve()}")


if __name__ == "__main__":
    main()
```

---

## 6. 代码结构说明

### 6.1 `from pathlib import Path`

这行代码引入 Python 的路径处理工具。

相比直接拼接字符串，`Path` 更适合处理文件路径。

例如：

```python
Path(__file__).resolve()
```

可以得到当前脚本文件的绝对路径。

---

### 6.2 `get_project_root()`

```python
def get_project_root() -> Path:
    """Return the project root directory."""
    return Path(__file__).resolve().parents[1]
```

这个函数的作用是返回项目根目录。

其中：

```python
__file__
```

表示当前 Python 文件本身。

```python
Path(__file__).resolve()
```

表示当前 Python 文件的绝对路径。

```python
.parents[1]
```

表示当前文件路径向上两级。

因为当前脚本在：

```text
VideoGen-Builder-100/scripts/day004/hello_project.py
```

所以：

```text
Path(__file__).resolve()
```

对应：

```text
/root/Workspace/VideoGen-Builder-100/scripts/day004/hello_project.py
```

它的上一级是：

```text
/root/Workspace/VideoGen-Builder-100/scripts
```

再上一级是：

```text
/root/Workspace/VideoGen-Builder-100
```

这就是项目根目录。

---

### 6.3 `main()`

```python
def main() -> None:
    project_root = get_project_root()

    print("VideoGen-Builder-100")
    print(f"Project root: {project_root}")
    print(f"Script file: {Path(__file__).resolve()}")
```

`main()` 是脚本的主函数。

它的好处是：

* 把脚本主要逻辑集中到一个入口函数中
* 避免把代码全部写在文件顶层
* 后续更容易改造成命令行工具
* 后续更容易测试和复用

这是工程化 Python 脚本中非常常见的写法。

---

### 6.4 `if __name__ == "__main__":`

```python
if __name__ == "__main__":
    main()
```

这段代码表示：

```text
只有当这个文件被直接运行时，才执行 main()
```

例如直接运行：

```bash
python scripts/hello_project.py
```

此时会执行：

```python
main()
```

但如果未来这个文件被其他 Python 文件导入：

```python
import scripts.hello_project
```

则不会自动执行 `main()`。

这样可以避免导入模块时出现意外运行。

---

## 7. 运行方式

在项目根目录执行：

```bash
cd /root/Workspace/VideoGen-Builder-100
conda activate videogen

python scripts/hello_project.py
```

预期输出类似：

```text
VideoGen-Builder-100
Project root: /root/Workspace/VideoGen-Builder-100
Script file: /root/Workspace/VideoGen-Builder-100/scripts/hello_project.py
```

如果看到项目名、项目根目录、脚本文件路径，说明 Day004 的最小脚本结构已经正常。

---

## 8. 今日理解重点

Day004 的重点不是写多少代码，而是形成下面这个基本结构：

```python
def main() -> None:
    ...


if __name__ == "__main__":
    main()
```

后续本项目中的很多脚本都会沿用这个结构。

例如：

```text
Day005：路径与文件扫描
Day006：argparse 命令行参数
Day014：素材扫描 CLI
Day017：ffprobe 读取视频信息
Day028：Video Preprocess CLI
```

Day004 是这些后续 CLI 工具的基础。

---

## 9. 今日练习

完成下面任务：

1. 创建 `scripts/hello_project.py`
2. 创建 `days/day004/README.md`
3. 从项目根目录运行脚本
4. 确认脚本能输出项目根目录和脚本路径
5. 理解 `main()` 和 `if __name__ == "__main__":` 的作用

---

## 10. 今日总结

今天完成了 VideoGen-Builder-100 项目的第一个 Python 工程基础脚本。

这个脚本虽然很小，但建立了后续项目中会反复使用的结构：

```text
导入模块
定义函数
定义 main()
使用 if __name__ == "__main__" 控制入口
从项目根目录运行脚本
```

这为后续构建素材扫描工具、视频处理工具、批量分析工具和生成实验工具打下基础。

---

## 11. 延伸学习资料

### Python 官方文档：`__main__`

链接：

https://docs.python.org/3/library/__main__.html

建议阅读重点：

* 什么是 top-level code environment
* 为什么 `__name__ == "__main__"` 可以判断脚本是否被直接运行
* 脚本入口和模块导入之间的区别

---

### Python 官方教程：Modules

链接：

https://docs.python.org/3/tutorial/modules.html

建议阅读重点：

* 什么是 Python module
* `.py` 文件和模块之间的关系
* `__name__` 变量的作用

---

### Python 官方文档：pathlib

链接：

https://docs.python.org/3/library/pathlib.html

建议阅读重点：

* `Path`
* `Path.resolve()`
* `Path.parent`
* `Path.parents`

目前只需要理解路径定位，不需要完整阅读 pathlib 的全部 API。
