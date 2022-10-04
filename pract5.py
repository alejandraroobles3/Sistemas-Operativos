p=True 
while p==True:   
    vect=[
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
        {'tam':'0','dis':'','arc':'','id':'12'},
        {'tam':'0','dis':'','arc':'','id':'13'}
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
    b3=int(b)
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
        print("TAMAÑO     ARCHIVO  ")
        for y in vect:
            if y['tam']!='0':
                    print(y['tam'],"    ",y['arc'])
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
        print("TAMAÑO     ARCHIVO  ")
        for y in vect:
            if y['tam']!='0':
                    print(y['tam'],"    ",y['arc'])
                                

    elif al=='3':
        #se hace desde la posicion en la que se quedo 
        tam=0
        tam2=0
        t=0 
        i=0
        nu=0 
        for c in v:
            tam2=0 
            tam=0
            r=0
            for z in range(nu,b3+1):
                g=vect[z]
                if int(g['tam']) >= int(c['tam']):

                    if g['dis']=='1': 
                        tam=int(g['tam'])+int(c['tam'])
                        if tam2==0:
                            tam2=int(g['tam'])+int(c['tam'])
                        print(c)
                        if tam > tam2:
                            print("llegue",tam2)
                            tam2=tam
                            i=int(g['id'])
                            r=1

            if r!=0:
                vect[i-1]['arc']=c['tam'] 
                vect[i-1]['dis']='2'
                nu=i-1
                
        print("TAMAÑO     ARCHIVO  ")
        for y in vect:
            if y['tam']!='0':
                    print(y['tam'],"    ",y['arc'])


    salida=input("Desea ejecutarlo de nuevo? \n 1. Si \n 2. No\n: ")
    if salida=='2':
        p=False













