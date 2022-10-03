p=True 
while p==True:   
    vect=[
        {'tam':'0','dis':'','arc':'','id':'0'},
        {'tam':'0','dis':'','arc':'','id':'1'},
        {'tam':'0','dis':'','arc':'','id':'2'},
        {'tam':'0','dis':'','arc':'','id':'3'},
        {'tam':'0','dis':'','arc':'','id':'4'},
        {'tam':'0','dis':'','arc':'','id':'5'},
        {'tam':'0','dis':'','arc':'','id':'6'},
        {'tam':'0','dis':'','arc':'','id':'7'},
        {'tam':'0','dis':'','arc':'','id':'8'},
        {'tam':'0','dis':'','arc':'','id':'9'},
        {'tam':'0','dis':'','arc':'','id':'10'},
        {'tam':'0','dis':'','arc':'','id':'11'},
        {'tam':'0','dis':'','arc':'','id':'12'}
    ]
    v=[
        {'tam':'','id':'1'},
        {'tam':'','id':'2'},
        {'tam':'','id':'3'},
        {'tam':'','id':'4'},
        {'tam':'','id':'5'}
    ]

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
                            h['arc']=j['id']
                            h['dis']='2'
                            break
    elif al=='2':
        #restar y comparar cual es mejor 
        r=[]
        for j in v:
            tam2=0
            r=0
            for h in vect:
                if int(h['tam']) >= int(j['tam']):
                    if h['dis']=='1':
                        tam=int(h['tam'])-int(j['tam'])
                        if tam2==0:
                            tam2=int(h['tam'])-int(j['tam'])
                        elif tam < tam2:
                            tam2=tam
                            r=int(h['id']) 
            vect[r]['arc']=j['tam'] 
            vect[r]['dis']='2'               
        for y in vect:
            if y['tam']!='0':
                if y['dis']=='2':
                    print("Archivo: ",y['arc'])
                    print("Espacio en donde se almaceno: ",y['tam'])
                                

    elif al=='3':
        #se hace desde la posicion en la que se quedo 
        tam=0
        tam2=0
        t=0 
        i=0
        for c in v:
            tam2=0
            print('primer for',b2)
            for r in range(0,b2):
                print('segundo for')
                h=vect[r]
                print(h)
                tam2=0
                if int(h['tam']) >= int(c['tam']):
                    if h['dis']=='1': 
                        tam=int(h['tam'])+int(c['tam'])
                        if tam2==0:
                            print('llegue tam2')
                            tam2=int(h['tam'])+int(c['tam'])
                        elif tam > tam2:
                            print('llegue')
                            tam2=tam
                            i=r
            vect[i]['arc']=c['tam'] 
            vect[i]['dis']='2'
        print(vect)
        for y in vect:
            if y['tam']!='0':
                if y['dis']=='2':
                    print("Archivo: ",y['arc'])
                    print("Espacio en donde se almaceno: ",y['tam'])


    salida=input("Desea ejecutarlo de nuevo? \n 1. Si \n 2. No\n: ")
    if salida=='2':
        p=False













