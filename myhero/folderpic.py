# -*-coding:utf-8-*-
import os
import shutil


pp = "D:\\hero"

for pic in os.listdir(pp):
    picdir = os.path.join(pp, pic[:4])
    if not os.path.exists(picdir):
        if not os.path.isdir(picdir):
            os.mkdir(picdir)

# 简单的for if 应用
for f in os.listdir(pp):
    # print 'start'
    if os.path.isdir(os.path.join(pp, f)):
        for d in os.listdir(pp):
            if os.path.isfile(os.path.join(pp, d)) and d[:4] == f:
                # print 'find it'
                shutil.move(os.path.join(pp, d), os.path.join(pp, f))
