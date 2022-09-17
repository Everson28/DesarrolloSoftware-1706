a=int(input('Introduzca el valor a: '))
b=int(input('Introduzca el valor b: '))
c=int(input('Introduzca el valor c: '))

def cuadratica_1(a,b,c):
  solucion=(-b+(b**2-4*a*c)**(1/2))/(2*a)
  return solucion
def cuadratica_2(a,b,c):
  solucion=(-b-(b**2-4*a*c)**(1/2))/(2*a)
  return solucion
def cuadratica_unicasolucion(a,b,c):
  solucion=(-b)/(2*a)
  return solucion

if b**2-4*a*c < 0:
  print('La ecuación no tiene soluciones reales')
elif b**2-4*a*c == 0:
  print(cuadratica_unicasolucion(a,b,c))
else:
  print(cuadratica_1(a,b,c))
  print(cuadratica_2(a,b,c))