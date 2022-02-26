from PIL import Image
import typer
import os
print("----------------------------------------------------------------------------------------------------------------------------")
print("|||||||| ||||||| ||||||| |||||||||||| |||||||||||| |||||||||| |||||||||||   |||||||||||||| ||||||||||  |||||||||| |||       ")
print("  |||    ||| ||| ||| ||| |||      ||| |||          |||        |||     |||        |||       |||    |||  |||    ||| |||       ")
print("  |||    ||| ||||||| ||| |||      ||| |||          |||||||    |||||||||||        |||       |||    |||  |||    ||| |||       ")
print("  |||    |||         ||| |||||||||||| |||    ||||| |||        ||| |||            |||       |||    |||  |||    ||| |||       ")
print("  |||    |||         ||| |||      ||| |||      ||| |||        |||   |||          |||       |||    |||  |||    ||| |||       ")
print("|||||||| |||         ||| |||      ||| |||||||||||| |||||||||| |||     |||        |||       ||||||||||  |||||||||| ||||||||||")
print("----------------------------------------------------------------------------------------------------------------------------")
print("\n")

#print("THE COMMANDS AVAIALABLE")
#print("python .\imagertool.py --help")
#print("python .\imagertool.py resize")
#print("python .\imagertool.py alterformat")
#print("python .\imagertool.py cropper")
#print("RUN THIS COMMANDS IN THE COMMAND LINE TO PERFROM THESE FUNCTIONS")

app=typer.Typer()

@app.command()
def resize():
    image=Image.open(input("Enter filepath : "))
    width,height=image.size
    print("The dimensions of the current image is",width,'x',height)
    new_width=int(input("Enter new width : "))
    new_height=int(input("Enter new height : "))
    resize_img=image.resize((new_width,new_height))
    new_img=input("Enter output file name with format : ")
    print("The output image has been saved in this location - ",os.getcwd())
    resize_img.save(new_img)

@app.command()
def alterformat():
    image=Image.open(input("Enter filepath : "))
    type_img=input("Enter which file format (jpeg,png,jpg) :")
    new_name=input("Enter output file name :")
    file=new_name+"."+type_img
    image.save(file)
    print("The output image has been saved in this location - ",os.getcwd())

@app.command()
def cropper():
    im=Image.open(input("Enter File Path :"))
    xcenter=im.width/2
    ycenter=im.height/2
    x1=xcenter-int(input("Enter a value for x1 :"))
    y1=ycenter-int(input("Enter a value for y1 :"))
    x2=xcenter+int(input("Enter a value for x2 :"))
    y2=ycenter+int(input("Enter a value for y2 :"))
    cropped=im.crop((x1,y1,x2,y2))
    new_name=input("Enter output file name with format : ")
    cropped.save(new_name)
    print("The output image has been saved in this location - ",os.getcwd())

if __name__ == "__main__":
    app()
