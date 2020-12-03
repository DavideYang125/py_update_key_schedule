# 基于镜像基础
FROM python:3.7
  
# 设置代码文件夹工作目录 /app
WORKDIR /app
  
# 复制当前代码文件到容器中 /app
ADD . /app
  
# 安装所需的包
RUN pip install -r requirements.txt -i https://mirrors.aliyun.com/pypi/simple
  
# Run schedule.py when the container launches
CMD ["python", "schedule.py"]