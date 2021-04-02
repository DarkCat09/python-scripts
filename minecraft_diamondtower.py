from mcpi.minecraft import Minecraft
mc = Minecraft.create()
import time

pos = mc.player.getTilePos()
xplayer = pos.x
yplayer = pos.y
zplayer = pos.z

blocksQuanStr = input("Сколько блоков поставить? ")

if (blocksQuanStr != ""):
    blocksQuan = int(blocksQuanStr)
else:
    blocksQuan = 50

i = 0
while i < blocksQuan:
    mc.setBlock(xplayer+1, yplayer+i, zplayer+1, 57)
    i = i+1

print("Sucessful!", blocksQuan)
