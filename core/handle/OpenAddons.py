import os
import yaml

from core.g_var import Addons
import core.main

def open_addons(dir:str):
    # 检查路径是否存在
    if os.path.isfile(dir) and os.path.exists(dir):
        return False,"路径不存在"
    # 切换os所在目录
    os.chdir(dir)
    # 检查是否为RSC附属
    if not os.path.isfile("info.yml"):
        return False,"此不是rsc附属"
    info:dict=yaml.safe_load(open("info.yml","r",encoding='utf-8').read())
    info_arg=info.keys()
    IPS_arg=["id","name","authors"]
    for arg in IPS_arg:
        if not(arg in info_arg):
            return False,"此不是rsc附属"
    # 附属路径写入内存
    Addons.data["dir"]=dir
    # info 写入内存
    Addons.data["info"]=info
    # 读取附属
    file_list=["groups.yml","recipe_types.yml","items.yml"]
    for file in file_list:
        # 判断是否存在
        if os.path.isfile(file):
            # 写入内存
            arg:dict=yaml.safe_load(open(file,"r",encoding='utf-8').read())
            Addons.data[file.split(".")[0]]=arg
    print(Addons.data)
    core.main.main.win_coverage()
    return True,None