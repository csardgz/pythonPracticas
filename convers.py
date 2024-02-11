import time
outime = [0,0,0,0,0]    #years, days, hours, minutes, seconds
const = [365*24*60*60,24*60*60,60*60,60,1]
constsrt = ['años, ','dias, ','horas, ','minutos, ','segundos']
k = 0
out_ = 'now'


seconds = int(input('segundos: '))
start = time.time()
if seconds != 0:
    out_ = ''
    for i in range(5):
        outime[i] = (seconds) // const[i]
        seconds -=  outime[i]*const[i]
        
    for j in range(5):
        if outime[j] != 0:
            out_ += str(outime[j]) + ' ' + constsrt[j]


end = time.time()

print(out_)
print(end-start)
#ahora sin salidas activas