#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import tkinter as tk
from tkinter import *
import qrcode
import os
from PIL import Image,ImageTk
from io import BytesIO
import winclip32
def str_qrgen():
    try:
        r = tk.Tk()
        result = r.selection_get(selection="CLIPBOARD")
        if result:
            img = qrcode.make(result.strip())
            img.save("test.png")        
            r.title("二维码生成器")
            
            '''
            主窗体居中显示
            '''
            screenwidth = r.winfo_screenwidth()
            screenheight = r.winfo_screenheight()
            dialog_width = 500
            dialog_height = 500
            r.geometry("%dx%d+%d+%d" % (dialog_width, dialog_height, (screenwidth-dialog_width)/2, (screenheight-dialog_height)/2))
            
            '''
            固定窗体大小,让其最前显示
            '''        
            r.resizable(0,0)
            r.attributes('-topmost',True)
            
            '''
            读取图片,修改图片显示尺寸,并写入Label
            '''        
            
            img_open = Image.open("test.png")
            w,h = img_open.size
            t = 500/w
            img_open.thumbnail((w*t,h*t))
            img_jpg = ImageTk.PhotoImage(img_open)
            image_label = Label(r,image=img_jpg,width=500,height=500).pack()
            
            '''
            将生成的图片拷贝到剪贴板
            '''
            output = BytesIO()
            img_open.convert("RGB").save(output,"BMP")
            data = output.getvalue()[14:]
            output.close()
            winclip32.set_clipboard_data(winclip32.BITMAPINFO_STD_STRUCTURE, data) 
            
            r.mainloop()
    except:
        pass
        
        
if __name__ == '__main__':
    str_qrgen()
        
