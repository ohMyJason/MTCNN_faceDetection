from tkinter import *
from tkinter import messagebox
from tkinter import simpledialog
from tkinter import filedialog
from PIL import Image, ImageTk
from test import oneImg
from test import openCma
import cv2
import os
Flag = True #控制摄像头的变量
capture = cv2.VideoCapture(0)#摄像头对象作为全局变量会更快些


def ui_process():
    root =Tk()
    root.title("人脸检测系统")
    root.geometry("1000x850")

    tempImg=Image.open("D:/working/tensorflow_mtcnn_zip/tensorflow-MTCNN-master/bg.jpg")
    tempImg=tempImg.resize((1000,900))
    bgImg=ImageTk.PhotoImage(tempImg)
    theLabel = Label(root,image=bgImg,compound=CENTER)
    theLabel.pack()

#标签
    L_titile = Label(root,text='基于MTCNN的实时人脸检测系统',)
    L_titile.config(font='Helvetica -15 bold',fg='blue')
    L_titile.place(x=150,y=20,anchor="center")
    L_author = Label(root, text='作者:刘佳昇')
    L_author.config(font='Helvetica -10 bold')
    L_author.place(x=920,y=830)
    S_title = Label(root,text='图片识别模式')
    S_title.config(font='Helvetica -20 bold',fg='red')
    S_title.place(x=40,y=50)
    S_title = Label(root, text='摄像头实时识别模式')
    S_title.config(font='Helvetica -20 bold', fg='red')
    S_title.place(x=40, y=450)
    S_title = Label(root, text='图片识别结果')
    S_title.config(font='Helvetica -15 bold', fg='red')
    S_title.place(x=740, y=100)

#图区
    canvas = Canvas(root, bd=2, relief=SUNKEN)
    canvas.place(x=40,y=140)
    resultCanvas = Canvas(root,bd=2,relief=SUNKEN)
    resultCanvas.place(x=600,y=140)
    #摄像头
    cmaCanvas = Canvas(root,bd=2,relief=SUNKEN,height=350,width=580)
    cmaCanvas.place(x=400,y=470)



#按钮

    B_NO1 = Button(root, text="打开一张图片",command=lambda :OpenFile(canvas,resultCanvas))
    B_NO1.place(x=40, y=100)
    B_NO2 = Button(root, text="打开输出文件夹", command=lambda: openOutPut())
    B_NO2.place(x=600, y=100)
    B_OpenCma = Button(root,text="打开摄像头",command=lambda :openGuiCma(cmaCanvas,root))
    B_OpenCma.place(x=40,y=500)
    B_OpenCma = Button(root, text="关闭摄像头", command=lambda: closeGuiCma())
    B_OpenCma.place(x=140, y=500)


#菜单栏
    menubar = Menu(root)
    filemenu = Menu(menubar, tearoff=0)
    filemenu.add_command(label="Open", command=lambda :openOutPut())
    mainloop()



def openOutPut():
    os.system("start explorer D:\working\\tensorflow_mtcnn_zip\\tensorflow-MTCNN-master\\output")




#文件操作的对话框
def OpenFile(canvas,resultCanvas):
    File = filedialog.askopenfilename(title='打开图片', filetypes=[ ('All Files', '*')])
    print(type(File))
    # resultImg = ImageTk.PhotoImage(Image.fromarray(oneImg(File).astype('uint8')).convert('RGB')) #这个转换方式会导致颜色异常
    resultImg = ImageTk.PhotoImage(Image.fromarray(cv2.cvtColor(oneImg(File),cv2.COLOR_BGR2RGB)))  #这里需要把cv的图像格式转换成PIL.img
    filename = Image.open(File)
    # filename.resize((3500,300))
    filename = ImageTk.PhotoImage(filename)
    print(type(Image.open(File)))
    canvas.image = filename  # <--- keep reference of your image
    canvas.create_image(0, 0, anchor='nw', image=filename)
    resultCanvas.image = resultImg
    resultCanvas.create_image(0,0,anchor='nw',image=resultImg)
    print(File)


def closeGuiCma():
    global Flag
    print(Flag)
    Flag = False


def openGuiCma(resultCanvas,root):
    # 摄像头
    if(messagebox.askokcancel('Python Tkinter', '确认打开摄像头？')==True):
        global Flag
        Flag=True
        while Flag==True:
            ref, frame = capture.read()
            cvimage = cv2.cvtColor(openCma(frame), cv2.COLOR_BGR2RGBA)
            pilImage = Image.fromarray(cvimage)
            tkImage = ImageTk.PhotoImage(image=pilImage)
            resultCanvas.create_image(0, 0, anchor='nw', image=tkImage)
            root.update()
            root.after(100)



if __name__ == "__main__":
    print("开始")
    ui_process()
