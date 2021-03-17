pip 是 python 的包管理器，负责python包的安装、卸载等。



1. 查看pip版本

```python
pip -V
```

2. 查看已经安装了的包及版本号

```python
pip list
```

3. 安装包

```python
pip install xxx				# 默认安装最新版本
pip isntall xxx==1.1.2		# 指定版本
```

4. 卸载包

```python
pip uninstall xxx
```

5. 批次安装包

```python
pip freeze > requirements.txt   # 将项目依赖的包输出到requrements.txt文件里面
pip install -r requirements.txt	# 批次安装requirements.txt里面的包
```

