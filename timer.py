import time

print("О чём вам напомнить?")
text = input()
print("Через сколько минут?")
#local_time хранит время
local_time = float(input())
#переводим минуты в секунды
local_time = local_time*60
# ждём нужное время, программа - в режиме "спячки"
time.sleep(local_time)
# показывает текст напоминания
print(text)
