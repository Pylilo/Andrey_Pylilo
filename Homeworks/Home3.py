lawn = str.lower(input("Добрый день, есть ли у Вас газон? "))

if lawn =="нет":
    Square = 0          
        
if lawn =="да":
    Square = int(input("Какова его площадь(сотки)? "))



dec_trees = str.lower(input("Есть ли у Вас лиственные деревья? "))

if dec_trees == "нет":
    Q_dec = 0

if dec_trees == "да":
    Q_dec = int(input("Сколько? "))



con_trees = str.lower(input("Есть ли у Вас хвойные деревья? "))

if con_trees == "нет":
    C_dec = 0

if con_trees == "да":
    C_dec = int(input("Сколько? "))



reservoir = str.lower(input("Есть водоём? "))
if reservoir == "нет":
    S_min = 0

if reservoir == "да":
    r_dec = int(input("Каков его объём(кубометры)? "))
    if r_dec <= 20:
        S_min = int((r_dec * 6) + 60)
    elif r_dec > 20:
        S_min = int((r_dec * 4) + 60)
     
 

sum = int(10+(Square*2)+(Q_dec*20)+(C_dec*8)+S_min)


print("Наши услуги будут стоить:", sum,"$")

