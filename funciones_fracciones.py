def maximo_comun(x,y):
    if x>y:
        menor=y
    else:
        menor=x
    for i in range(1, menor+1):
            if((x%i==0)and(y%i==0)):
                mcd=i
    return mcd

maximo_comun(12,3)


def simplificacion(a,b):
    c=maximo_comun(a,b)
    g=str(int(a/c))
    h=str(int(b/c))
    return('{0}/{1}'.format(g,h))

simplificacion(22,22)

def suma(numerador1,numerador2,denominador1,denominador2):
    x=numerador1*denominador2
    y=numerador2*denominador1
    z=denominador1*denominador2
    n=y+x
    if z==0:
        print("error,no se puede dividir por 0")

    pa=maximo_comun(n,z)
    tre=str(int(n/pa))
    brc=str(int(z/pa))
   
    if z/pa==1:
        return('{0}'.format(tre)) 
    else:
        return('{0}/{1}'.format(tre,brc)) 
    
suma(4,4,4,23)

        
        
def rest(numerador1,numerador2,denominador1,denominador2):
    x=numerador1*denominador2
    y=numerador2*denominador1
    z=denominador1*denominador2
    n=y-x
    if z==0:
        print("error, no se puede dividir por 0")
    ml=maximo_comun(n,z)
    arriba=str(int(n/ml))
    abajo=str(int(z/ml))
    
    if z/ml!=1:
        return('{0}/{1}'.format(arriba,abajo))
    else:
        return('{0}'.format(arriba))

rest(2,3,32,3)

        
def mul(numerador1,numerador2,denominador1,denominador2):
    x=numerador1*numerador2
    y=denominador1*denominador2mul(2,2,2,2)
    if y==0:
        print("error,no se puede dividir por 0")
    rt=maximo_comun(x,y)
    arriba=str(int(x/rt))
    abajo=str(int(y/rt))
    if y/rt !=1:
        return('{0}/{1}'.format(arriba,abajo))
    else:
        return('{0}'.format(arriba))
    
mul(2,2,2,2)

def div(numerador1,numerador2,denominador1,denominador2):
    x=numerador1*denominador2
    y=denominador1*numerador2
    if y==0:
        print("error,no se puede dividir por 0")
    rt=maximo_comun(x,y)
    arriba=str(int(x/rt))
    abajo=str(int(y/rt))
    if y/rt !=1:
        return('{0}/{1}'.format(arriba,abajo))
    else:
        return('{0}'.format(arriba))

div(23,4,42,3)