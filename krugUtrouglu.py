#poziv modula za matematicke funkcije
import math

#ispisuje sta radi ovaj program
tekst1='Ovo je program za izracunavanje da li je trougao u krugu'

#unosi koordinate centra kruga
tekst2='Unesite koordinate centra kruga S(p,q)'
print(tekst1)
print(tekst2)
p = input('Unesi p:')
p=float(p)
q = input('Unesi q:')
q=float(q)
Tekst3='Unesite poluprecnik'
print(Tekst3)
r = input('Unesi r:')
r=float(r)
#ispisuje krug
print("Uneli ste centar kruga S( %.2f, %.2f ), a poluprecnika r = %.2f"%(p,q,r))

#unos temena A
tekst1='Unesite koordinate temena trougla'
print(tekst1)
Tekst2='Unesite koordinate temena A(x1,y1)'
print(Tekst2)
x1 = input('Unesi x1:')
y1 = input('Unesi y1:')
Tekst2='Unesite koordinate temena B(x2,y2)'
print(Tekst2)
x2 = input('Unesi x2:')
y2 = input('Unesi y2:')
Tekst2='Unesite koordinate temena C(x3,y3)'
print(Tekst2)
x3 = input('Unesi x3:')
y3 = input('Unesi y3:')
x1=float(x1)
y1=float(y1)
x2=float(x2)
y2=float(y2)
x3=float(x3)
y3=float(y3)
#ispisuje temena trougla
print("Uneli ste teme A( %.2f, %.2f ), teme B( %.2f, %.2f ) i teme C( %.2f, %.2f )"%(x1,y1,x2,y2,x3,y3))

tekst1='Ispituje da li su unete tacke nekolinearne, jer ako su kolinearne one ne cine trougao'
print(tekst1)
tekst1='Ovo je deo programa izracunava rastojanje izmedju dve tacke'
print(tekst1)

#funkcija koja racuna rastojanje izmedju dve tacke
def rastojanje(a,b,c,d):
    x12=math.pow((a-c), 2)
    y12=math.pow((b-d), 2)
    rast=math.sqrt(x12+y12)
    return rast

a = rastojanje(x2,y2,x3,y3)
print('stranica a je:')
print (a)

b = rastojanje(x1,y1,x3,y3)
print('stranica b je:')
print (b)

c = rastojanje(x1,y1,x2,y2)
print('stranica c je:')
print (c)


if a+b > c and a+c>b and b+c>a : 
	print ("Ove 3 stranice cine trougao jer je zbir svake 2 veci od trece")
	i=0
else:
	print ("Ove 3 tacke trogla su kolinearne i ne cine trougao")
	
print ("Ispituje da li centar kruga S u oblasti pravougaonika kome pripada trougao")

#prvo malazi maximume i minimume koordinata trougla
max_x = max(x1,x2,x3)
max_y = max(y1,y2,y3)
min_x = min(x1,x2,x3)
min_y = min(y1,y2,y3)
print("minimum od x-koordinata je %.2f a maximum od x - koordinata je %.2f" %(min_x, max_x) )
print("minimum od y-koordinata je %.2f a maximum od y - koordinata je %.2f" %(min_y, max_y) )
if min_x<p and p<max_x:
    print("p je u oblasti pravougaonika!")
else:
    i=0 # i je pokazivac da krug nije u trouglu
    print("Centar kruga nije u oblasti trougla, jer p nije u oblasti trougla!")
if min_y<q and q<max_y:
    print ("q je u oblasti pravougaonika!")
else:
    i=0
    print ("Centar kruga nije u oblasti trougla jer q nije u oblasti trougla! Unesite neke druge tacke")

#pravi jednacine stranica
print("Pravi jednacine stranica")
def dodaj_zagrade_jerjenegativan(p):
    if p<0:
      p1=str( p )
    else:
        p1="+"+str(p)
    return p1

def jednacina_2tacke_k(a,b,c,d):
    if a-c==0:
        k=0
    else:
        k=(d-b)/(a-c)
    return k
def jednacina_2tacke_n(a,b,c,d):
    if a-c==0:
        k=0
    else:
        k=(d-b)/(a-c)
        n=b-k*a
    return n
kab=jednacina_2tacke_k(x1,y1,x2,y2)    
nab=jednacina_2tacke_n(x1,y1,x2,y2)
#ulepsavanje izlaza, ispisa jednacine ako je parametar negativan a ispred je +
if nab<0:
  nab1="(" +str( nab )+ ")"
else:
    nab1=str(nab)

if x2-x1==0:
    print ("Jednacina prave AB je: x =%.2f" %(x1))
else:
    print("ovde")
    xec=(q-nab)/kab
    print( "Jednacina prave AB je: y= " + str(kab) +  "*x+" + nab1 )

#probni deo
print ("ista jednacina preko sminke")
if x2-x1==0:
    print ("Jednacina prave AB je: x =%.2f" %(x1))
else:
    nab1 = dodaj_zagrade_jerjenegativan(nab)
    xec=(q-nab)/kab
    print( "Jednacina prave AB je: y= "+str(kab)+"*x "+nab1)
    
#kraj za ovaj probni deo
		
kac=jednacina_2tacke_k(x1,y1,x3,y3);
nac=jednacina_2tacke_n(x1,y1,x3,y3);
if kac<0:
    znak="-"
else:
    znak="+"
        
if x3-x1==0:
    print ("Jednacina prave AC je: x =$.2f" %(x1))
else:
    nac1 = dodaj_zagrade_jerjenegativan(nac)
    xeb=(q-nac)/kac
    print( "Jednacina prave AC je: y= %.2f*x"%(kac) +znak+"%.2f"%(nac))


kcb=jednacina_2tacke_k(x2,y2,x3,y3)
ncb=jednacina_2tacke_n(x2,y2,x3,y3)
if x3-x2==0:
    print ("Jednacina prave BC je: x =%.2f" %(x2))
else:
    ncb1 = dodaj_zagrade_jerjenegativan(ncb)
    xea=(q-ncb)/kcb
    print( "Jednacina prave BC je: y="+str(kcb)+ "*x  "+ncb1)


	
if min_x>xea or xea>max_x:
    xp1=xeb
    xp2=xec
elif min_x<xeb and xeb<max_x:
     xp1=xea
     xp2=xeb		
else :
    xp1=xea
    xp2=xec
    
if min(xp1,xp2)<p and max(xp1,xp2)>p and i>0:
    print("Centar kruga je u oblasti trougla")
else:
    print( "Centar kruga nije u oblasti trougla")

#Ispituje da li je prava AC ima presecne tacke sa krugom
a=-2*p
b=-2*q
c = p*p + q*q - r*r

a1=1+kac*kac
a2=1+kab*kab
a3=1+kcb*kcb

b1=2*kac*nac+a+b*kac
b2=2*kab*nab+a+b*kab
b3=2*kcb*ncb+a+b*kcb
c1=nac*nac+b*nac+c
c2=nab*nab+b*nab+c
c3=ncb*ncb+b*ncb+c
d1=b1*b1-4*a1*c1
d2=b2*b2-4*a2*c2
d3=b3*b3-4*a3*c3
if p<0:
    p1="(" + p + ")"
    print ("Jednacina kruga u kanonskom obliku je: (x- (%.2f) )**2+/(y- %.2f )**2 = %.2f" %(p,q,r*r))
print ("Jednacina kruga u opstem obliku je: x**2+y**2+%.2f *x+%.2f*y + %.2f =0" %(a,b,c))
print( "Jednacina prave AC je: y= %.2f x + %.2f" %(kac,nac))
print ("Koeficijenti kvadratne jednacine koja je resenje sistema su: a=%.2f, b=%.2f , c= %.2f "%(a,b,c))

print ("Jednacina prave AB je: y= %.2f x + %.2f" %(kab,nab))
print ("Koeficijenti kvadratne jednacine koja je resenje sistema su: a=%.2f, b=%.2f , c= %.2f "%(a2,b2,c2))

print ("Jednacina prave BC je: y= %.2f x + %.2f" %(kcb,ncb))
print ("Koeficijenti kvadratne jednacine koja je resenje sistema su: a=%.2f, b=%.2f , c= %.2f"%(a3,b3,c3))
if d1>=0:
   print ("Krug sece stranice trougla i nije ceo u oblasti trougla. Unesite neke druge tacke")
elif d2>=0:
    print ("Krug sece stranice trougla i nije ceo u oblasti trougla. Unesite neke druge tacke")
elif d3>=0:
    print ("Krug sece stranice trougla i nije ceo u oblasti trougla. Unesite neke druge tacke")
elif i>0:
    print (">Ceo krug je u trouglu")
 



