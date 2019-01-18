from PIL import Image,ImageDraw,ImageFont,ImageFilter

import random
#字母随机
def rndChar():
    return chr(random.randint(65,90))
#颜色随机
def rndColor():
    return (random.randint(64,255),random.randint(64,255),random.randint(64,255))
# 随机颜色2
def rndColor2():
    return (random.randint(32,127),random.randint(32,127),random.randint(32,127))

width=60*4
height=60
# 创建图片对象

image=Image.new("RGB",(width,height),(255,255,255))
# 创建point对象
font=ImageFont.truetype(r"C:\Windows\Fonts\Arial.ttf",36)
# 创建draw对象
draw=ImageDraw.Draw(image)
# 填充每个像素
for x in range(width):
    for y in range(height):
        draw.point((x,y),fill=rndColor())
        
# 写字
for t in range(0,4):
    draw .text((60*t+10,10),rndChar(),font=font,fill=rndColor2())

# 模糊
image=image.filter(ImageFilter.BLUR)
# 保存
image.save('code.png','png')
