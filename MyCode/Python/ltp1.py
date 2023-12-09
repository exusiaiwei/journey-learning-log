# 使用ltp模块的pipeline函数，实现从一个文件夹(C:\Users\魏子超\OneDrive\学习\毕业论文\语料output)中，读取所有txt文件，逐一进行分析，最后将结果分析保存在对应txt文件名-dp.txt中

from ltp import LTP

# 实例化一个 LTP 类
ltp = LTP()
# 读取文件夹下的所有txt文件
import os
path = r''
corpus = os.listdir(path)
# 循环读取每一个txt文件，并输出分析后结果到‘文件名-dp.txt’
for file in corpus:
  with open(os.path.join(path, file), 'r',errors="ignore") as f:
    contents = f.readlines()
    # 利用pipeline函数分析每一个文件
    for content in contents:
      result = ltp.pipeline(content, tasks = ["cws","dep"])
      print(result.dep)