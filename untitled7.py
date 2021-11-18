from tkinter import *

root=Tk()
root.title("joe")
root.geometry("800x800")

imput1=Input(root)
imput2=Input(root)
imput3=Input(root)
amount=3
imput1.place(relx=0.5,rely=0.1,anchor=CENTER)
imput2.place(relx=0.5,rely=0.2,anchor=CENTER)
imput3.place(relx=0.5,rely=0.3,anchor=CENTER)

array1=["hugh","joe","mama"]
array2=[["hugh","A"],["joe","F"],["mama","F----"]]
array3=[[["hugh","A","acceptable"],["joe","F","failure"],["mama","F----","adopted"]]]

label=Label(root)
label.place(relx=0.5,rely=0.6,anchor=CENTER)
def getresults():
    label["text"]=""
    person = 0
    while person<3:
        label["text"]+=array1[person]+" got a "+array2[person][1]+",which is "+array3[0][person][2]
        person = 1 + person
def Push():
    array1.push(imput1)
    array2.push(imput1)
    array2[amount].push(imput2)
    array3.push(imput1)
    array3[amount].push(imput2)    
    array3[0][amount][2].push(imput3)
    
button=Button(root,text="test",command=getresults)
button.place(relx=0.5,rely=0.5,anchor=CENTER) 
button=Button(root,text="add",command=Push)


root.mainloop()