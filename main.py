from PIL import Image
me = Image.open('myself.png')
bg = Image.open('burj-khalifa.jpg')
bg.paste(me, (0,0), me)
bg.save('burj-myself.png')