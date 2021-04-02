from mcpi.minecraft import Minecraft
mc = Minecraft.create();
import time
import math
import random

t = 0

curPlayerPos = mc.player.getTilePos()
randX = random.randint(curPlayerPos.x-100, curPlayerPos.x+100)
randZ = random.randint(curPlayerPos.z-100, curPlayerPos.z+100)
randY = mc.getHeight(randX, randZ)

mc.postToChat("")

print(randX, randY, randZ)
mc.setBlock(randX, randY, randZ, 57)
mc.postToChat("Алмазный блок спрятан.")

curPlayerPos = mc.player.getTilePos()
mc.setBlock(curPlayerPos.x + 1, curPlayerPos.y, curPlayerPos.z + 1, 42)
mc.postToChat("Чтобы остановить игру, сломай железный блок,")
mc.postToChat("установленный рядом с тобой.")
mc.postToChat("Приятной игры!")

mc.postToChat("")

win = False

while (not win):

    pauseBlock = mc.getBlock(curPlayerPos.x + 1, curPlayerPos.y, curPlayerPos.z + 1)
    if (int(pauseBlock) == 0):
        print("Игра была остановлена пользователем.")
        mc.postToChat("Игра была остановлена.")

        #Удаление блока
        time.sleep(2)
        mc.setBlock(randX, randY, randZ, 0)
        mc.setBlock(curPlayerPos.x + 1, curPlayerPos.y, curPlayerPos.z + 1, 0)
        
        break
    
    pos = mc.player.getPos()
    dist = math.sqrt((pos.x - randX) ** 2 + (pos.z - randZ) ** 2)
    if dist < 3:

        if (pos.y > randY):
            mc.postToChat("Спустись вниз!")
            time.sleep(2)

        if (pos.y < randY):
            mc.postToChat("Поднимись наверх!")
            time.sleep(2)
        
        mc.postToChat("Молодец, ты выиграл! Блок найден за " + str(t) + " секунд.")
        mc.postToChat("Через 7 секунд блок исчезнет.")
        
        #Удаление блока
        time.sleep(7)
        mc.setBlock(randX, randY, randZ, 0)
        mc.setBlock(curPlayerPos.x + 1, curPlayerPos.y, curPlayerPos.z + 1, 0)
        
        win = True
    
    if dist > 100: mc.postToChat("Очень холодно - заморозишься!")
    elif dist > 50: mc.postToChat("Холодно...")
    elif dist > 25: mc.postToChat("Тепло")
    elif dist > 12: mc.postToChat("Горячо...")
    elif dist > 6: mc.postToChat("Кипяток - обожжёшься!")
    #else: print("Чё-то пошоло не так...")
    t = t+1
    time.sleep(1)

print("Завершено.")
input("Нажмите любую клавишу для закрытия программы...")
