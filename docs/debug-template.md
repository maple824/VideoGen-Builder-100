# Debug 记录模板

> 用途：记录环境配置、依赖安装、脚本运行、模型推理、视频处理过程中遇到的问题。
> 原则：不要只记录“解决了”，要记录“如何发现、如何判断、如何验证”。

---

# Debug - 问题标题

## 问题编号

```text
DEBUG-YYYYMMDD-001
```

示例：

```text
DEBUG-20260604-001
```

---

## 问题发生位置

说明问题发生在哪个阶段、哪个文件或哪个命令中。

* 日期：
* 阶段：
* 文件：
* 命令：
* 环境：

示例：

```text
日期：2026-06-04
阶段：Day001 - 项目基线与环境可复现性
文件：scripts/check_env.py
命令：python scripts/check_env.py
环境：conda videogen
```

---

## 问题现象

简要说明看到的异常现象。

示例：

```text
终端显示当前处于 videogen 环境，但运行 python 命令时提示 command not found。
```

---

## 报错信息

粘贴完整报错。不要只写一行结论。

```text
待填写
```

---

## 触发步骤

记录如何复现这个问题。

```bash
待填写
```

示例：

```bash
conda activate videogen
which python
python --version
```

---

## 初步判断

写下第一轮判断，不要求一定正确。

* 可能原因 1：
* 可能原因 2：
* 需要进一步确认的信息：

---

## 最小验证

记录用于缩小问题范围的最小命令。

```bash
待填写
```

示例：

```bash
which python
which python3
conda list -n videogen python
```

---

## 定位结果

写下最终确认的问题原因。

示例：

```text
videogen conda 环境中没有安装 Python。虽然终端前缀显示为 videogen，但实际没有该环境自己的 python 可执行文件。
```

---

## 解决方式

记录具体修改方式。

```bash
待填写
```

示例：

```bash
conda install -n videogen python=3.10 -y
conda deactivate
conda activate videogen
```

---

## 验证结果

记录如何确认问题已经解决。

```bash
待填写
```

示例：

```bash
which python
python --version
python scripts/check_env.py
```

预期结果：

```text
待填写
```

实际结果：

```text
待填写
```

---

## 是否影响项目

说明这个问题对项目的影响。

* [ ] 不影响，只是临时环境问题
* [ ] 影响当前 Day
* [ ] 影响后续多个阶段
* [ ] 需要更新 README 或模板
* [ ] 需要写入常见问题

说明：

```text
待填写
```

---

## 经验总结

回答下面几个问题：

1. 这个问题为什么会发生？
2. 下次如何更早发现？
3. 是否需要加入环境检查脚本？
4. 是否需要更新 `.gitignore`、`requirements.txt` 或文档？

---

## 关联文件

```text
待填写
```

示例：

```text
scripts/check_env.py
days/day001/README.md
```
