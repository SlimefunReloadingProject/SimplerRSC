import os
import yaml
import customtkinter as ctk
from CTkToolTip import *

# 弹窗
class info_window(ctk.CTkToplevel):
    def __init__(self,master,title:str,text:str):
        super().__init__()
        master.wm_attributes("-topmost",False)
        self.wm_attributes("-topmost",True)
        self.resizable(0,0)
        self.title(title)
        ctk.CTkLabel(self,text=text).grid(row=0,column=0,padx=50,pady=50)
        ctk.CTkButton(self,text="确定").grid(row=1,column=0)

# 创建附属
class CreateAddons(ctk.CTkToplevel):
    def __init__(self,master,top_win):
        super().__init__(master)
        self.resizable(0,0)
        self.wm_attributes("-topmost", True)
        self.title("SimplerRSC - 创建新的附属")
        # 关闭上个窗口
        top_win.destroy()
        # 附属id
        ctk.CTkLabel(self,text="附属id[必填]").grid(row=0,column=0,padx=10,pady=(10,0),sticky="w")
        self.addon_id=ctk.CTkEntry(self,width=160)
        self.addon_id.grid(row=1,column=0,padx=10,sticky="w")
        # 附属名称
        ctk.CTkLabel(self,text="附属名称[必填]").grid(row=0,column=1,padx=10,pady=(10,0),sticky="w")
        self.addon_name=ctk.CTkEntry(self,width=160)
        self.addon_name.grid(row=1,column=1,padx=10,sticky="w")
        # 附属作者
        ctk.CTkLabel(self,text="附属作者[必填]").grid(row=2,column=0,padx=10,pady=(10,0),sticky="w")
        self.addon_author=ctk.CTkEntry(self,width=160)
        self.addon_author.grid(row=3,column=0,padx=10,sticky="w")
        # 附属版本
        ctk.CTkLabel(self,text="附属版本").grid(row=2,column=1,padx=10,pady=(10,0),sticky="w")
        self.addon_version=ctk.CTkEntry(self,width=160)
        self.addon_version.grid(row=3,column=1,padx=10,sticky="w")
        # 位置
        ctk.CTkLabel(self,text="生成附属位置[必填]").grid(row=4,column=0,padx=10,pady=(10,0),sticky="w")
        self.addon_dir=ctk.CTkEntry(self)
        self.addon_dir.grid(row=5,column=0,padx=8,columnspan=2,sticky="ew")
        #GitHub位置
        ctk.CTkLabel(self,text="GitHub存储库位置[可选]").grid(row=6,column=0,padx=10,pady=(10,0),sticky="w")
        self.addon_repo=ctk.CTkEntry(self)
        self.addon_repo.grid(row=7,column=0,padx=8,columnspan=2,sticky="ew")
        CTkToolTip(self.addon_repo, "格式: 作者/存储库名称")
        # 创建按钮
        ctk.CTkButton(self,text="创建附属",command=self.addon_create,height=33).grid(row=8,column=0,padx=10,pady=(10,15),columnspan=2,sticky="ew")

    # 创建
    def addon_create(self):
        if self.addon_id.get()!="" and self.addon_name.get()!="" and self.addon_author.get()!="" and self.addon_dir!="":
            try:
                # 创建附属文件夹
                os.chdir(self.addon_dir.get())
                os.makedirs(self.addon_id.get())
                # 必要数据处理
                data={
                    "id":str(self.addon_id.get()),
                    "name":str(self.addon_name.get()),
                    "authors":[str(self.addon_author.get())]
                }
                # 非必要数据处理
                arglist=[
                    {"arg":"version","GUI":self.addon_version},
                    {"arg":"repo","GUI":self.addon_repo}
                ]
                for arg in arglist:
                    if arg["GUI"].get()!="":
                        data[arg["arg"]]=arg["GUI"].get()
                # 写入info.yml
                file=open(self.addon_dir.get()+"/"+self.addon_id.get()+"/info.yml","w")
                file.write(yaml.safe_dump(data))
                file.close()
                info_window(self,"info","创建成功")
                self.destroy()
            except:
                info_window(self,"bushi","你TM往输入框里填了什么奇奇怪怪的东西")
        else:
            info_window(self,"info","必要参数未填写")

class Mian(ctk.CTkToplevel):
    def __init__(self,master):
        super().__init__(master)
        self.title("SimplerRSC")
        self.resizable(0,0)
        self.wm_attributes("-topmost", True)
        # 创建
        ctk.CTkButton(self,text="创建新附属",command=lambda:CreateAddons(master,self),width=200,anchor="center").grid(row=0,column=0,padx=30,pady=17)
        # 分割
        ctk.CTkLabel(self,text="或").grid(row=1,column=0)
        # 打开
        ctk.CTkButton(self,text="打开现有附属",width=200,anchor="center").grid(row=2,column=0,padx=30,pady=15)
        