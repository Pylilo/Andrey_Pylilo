
p={('16','2'):1, 
    ('25','2'):1.4,

    ('16','3'):1.6, 
    ('25','3'):2, 
    ('32','3'):3.2,

    ('16','4'):1.8,
    ('25','4'):2.3,
    ('32','4'):3.5,
    ('35','4'):3.8,
    
    ('16','5'):2,
    ('25','5'):2.5,
    ('32','5'):3.8,
    ('35','5'):4,
    ('40','5'):5
                }


l=input('Какая длина самореза? ')
d=input('Какой диаметр самореза? ')

print(p[(l,d)])

s=float(input('Сколько саморезов вам нужно? '))

print('Взвесте', p[(l,d)]*s,"грамм саморезов")