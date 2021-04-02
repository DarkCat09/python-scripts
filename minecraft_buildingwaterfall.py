from mcpi.minecraft import Minecraft
mc = Minecraft.create()
import time

i = 0
j = 0
k = 0
pos = mc.player.getTilePos()

waterfallHeightStr = input("Введите высоту водопада: ")
if (waterfallHeightStr != ""):
    waterfallHeight = int(waterfallHeightStr)
else:
    waterfallHeight = 15

print("Постройка водопада...")

#Waterfall (ice)
while i < waterfallHeight:
    for j in range(11):
        mc.setBlock(pos.x + 1, pos.y + i, pos.z + j, 79)
    i = i+1

#Water on waterfall
for k in range(11):
    mc.setBlock(pos.x + 1, pos.y + waterfallHeight, pos.z + k, 8)

print("Завершено!")
