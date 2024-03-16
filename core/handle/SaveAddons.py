import os
import yaml
from core.g_var import Addons

def SaveAddons():
    # 切换os所在目录
    os.chdir(Addons.data["dir"])
    # 写下附属
    file_list=["groups.yml","recipe_types.yml","items.yml"]
    for file in file_list:
        # 判断是否存在
        if file.split(".")[0] in Addons.data.keys():
            file_open=open(file,"w")
            file_open.write(yaml.safe_dump(Addons.data[file.split(".")[0]]))
            file_open.close()