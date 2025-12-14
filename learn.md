## python 
python 版本之间的差异:

## 虚拟环境搭建
env\Scripts\activate   激活
env\Scripts\deactivate 退出
py -m venv env  创建虚拟环境

## pip 镜像加速,提升安装包的速度.
腾讯云pip 镜像
全局使用: pip config set global.index-url https://mirrors.cloud.tencent.com/pypi/simple


全局使用: pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple/
临时使用: pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple/

阿里云pip 镜像
全局使用: pip config set global.index-url https://mirrors.aliyun.com/pypi/simple/
临时使用: pip install -r requirements.txt -i https://mirrors.aliyun.com/pypi/simple/

## LLMOPS 7 层架构
![alt text](image.png)






