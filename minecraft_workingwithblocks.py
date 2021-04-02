from mcpi.minecraft import Minecraft
mc = Minecraft.create()
import time

plpos = mc.player.getTilePos()

#Таким образом (последний аргумент в след.команде) можно указать т.н. значение данных.
#Например, можно уточнить цвет окрашенного стекла.

#setBlock  (x,           y,       z,       stained_glass ID, Data Value)
mc.setBlock(plpos.x - 1, plpos.y, plpos.z, 95, 11)
mc.postToChat("Перед Вами блок.")

print("Готово.")
