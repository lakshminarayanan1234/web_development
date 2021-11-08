from tkinter import*
from PIL import Image,ImageTk
import PIL
class srd:
    def __init__(self,root):
        self.root=root
        self.root.title("student registration details")
        self.root.geometry("1350x700+0+0")
        self.root.config(bg="white")
        self.logo_dash=ImageTk.PhotoImage(image=PIL.Image.fromarray(logo_p.png))
        title=Label(self.root,text="student registration details",image=self.logo_dash,font=("goundy old style",20,"bold"),bg="#033054",fg="white").place(x=0,y=0,relwidth=1,height=50)








if __name__=="__main__":
    root=Tk()
    obj=srd(root)
    root.mainloop()
