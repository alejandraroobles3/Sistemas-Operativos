vect=[
    {'tam':'0','dis':'','arc':'','o':'0'},
    {'tam':'0','dis':'','arc':'','o':'0'},
    {'tam':'0','dis':'','arc':'','o':'0'},
    {'tam':'0','dis':'','arc':'','o':'0'},
    {'tam':'0','dis':'','arc':'','o':'0'},
    {'tam':'0','dis':'','arc':'','o':'0'},
    {'tam':'0','dis':'','arc':'','o':'0'},
    {'tam':'0','dis':'','arc':'','o':'0'},
    {'tam':'0','dis':'','arc':'','o':'0'},
    {'tam':'0','dis':'','arc':'','o':'0'},
    {'tam':'0','dis':'','arc':'','o':'0'},
    {'tam':'0','dis':'','arc':'','o':'0'},
    {'tam':'0','dis':'','arc':'','o':'0'}
]
v=[
    {'tam':'','id':'1'},
    {'tam':'','id':'2'},
    {'tam':'','id':'3'},
    {'tam':'','id':'4'},
    {'tam':'','id':'5'}
]
p=True

b=input("Numero de bloques de memoria: ")
b2=int(b)
for a in vect:
    while b2>0:
        tam=input("Tamaño en kbs: ")
        a['tam']=tam
        di=input("1. disponible \n2. Ocupado\n ")
        a['dis']=di
        break
    b2-=1


for a in v:
    t2=input("Tamaño del archivo: ")
    a['tam']=t2

al=input("Que algoritmo deseas elegir \n1. Primer ajuste \n2. Mejor ajuste \n3. Peor Ajuste \n")
tam=0
tam2=0

if al=='1':
    for j in v:
        for h in vect:
            if int(h['tam']) >= int(j['tam']):
                if h['dis']=='1':
                    if h['o'] == '0':
                        h['arc']=j['id']
                        h['o']='1'
                        break
elif al=='2':
    #restar y comparar cual es mejor 
    r=[]
    for j in v:
        tam2=0
        for h in vect:
            if int(h['tam']) >= int(j['tam']):
                if h['dis']=='1':
                    if h['o'] == '0':
                        tam=int(h['tam'])-int(j['tam'])
                        if tam2==0:
                            tam2=int(h['tam'])-int(j['tam'])
                        elif tam < tam2:
                            tam2=tam
                            r=h
                            print("h",r)
                            print("j",j)
        print(r)
                            

elif al=='3':
    print()
    #se hace desde la posicion en la que se quedo 














