import datetime

dt = datetime.date(2021,10,22)
print(dt.ctime())
dia = dt.day
mes = dt.month
ano = dt.year

print(dia,mes,ano)
hoje = datetime.date.today()
print(datetime.date.today())
print(datetime.datetime.now())

delta = hoje - dt


data_futuro = hoje+delta

print(data_futuro)


agora= datetime.datetime.now()
print(agora.hour)
print(type(agora.hour))