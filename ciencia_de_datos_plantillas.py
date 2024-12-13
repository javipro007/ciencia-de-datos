# -*- coding: utf-8 -*-
"""Ciencia de datos plantillas.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1C0nmk3qTgZ7iTWsUdDZYLkS6zedV5O6m
"""

def promedio(lista):
  """
  Entrega el promedio de los datos de una lista de datos
  ---------------------------------------------
  Input:
    lista:lista con numeros
  Output:
    prom:promedio en float
  """
  x=+.0
  for elem in lista:
   x+=elem
  prom=x/(len(lista))
  return prom

def mediana(lista):
  """
  Función que regresa el valor correspondiente a la mediana de un grupo numérico
  ---------------------------------------------
  Input:
    lista:lista con datos numérios
  Output:
    media:valor entero correspondiente a la mediana
  """
lista.sort()
n=len(lista)
if n%2==0:
    media=sum(lista[n//2-1:n//2+1])// 2
else:
    media=lista[n//2]
return media

def moda(lista):
  """
  Función que regresa una lista con los valores que tengan mayor frecuencia en una lista de datos
  ---------------------------------------------
  Input:
    lista:lista con datos numérios
  Output:
    moda:lista con todos los valores con mayor frecuencia
  """
  dict_conteo = {}

  for elem in lista:
    if elem in dict_conteo:
      dict_conteo[elem]+=1
    else:
      dict_conteo[elem]=1

  max_frecuencia=0
  for frecuencia in dict_conteo.values():
    if frecuencia>max_frecuencia:
      max_frecuencia=frecuencia

  moda = []
  for elemento, frecuencia in dict_conteo.items():
    if frecuencia==max_frecuencia:
      moda.append(elemento)

  return moda

def rango(lista):
  """
  Función que regresa un valor numérico correspondiente a la diferencia entre
  el valor más grande con el valor más pequeño de una lista de datos
  ---------------------------------------------
  Input:
    lista:lista con datos numérios
  Output:
    rango:diferencia entre el valor máximo y el mínimo
  """
  if not lista:
    return 0

  val_min=lista[0]
  val_max=lista[0]

  for elem in lista:
    if elem<val_min:
      val_min=elem
    if elem>val_max:
      val_max=elem

  rango=val_max-val_min
  return rango

def varianza(lista):
  """
  Función que regresa el valor numérico de la varianza de una lista de datos
  ---------------------------------------------
  Input:
    lista:lista con datos numérios
  Output:
    varianza:la suma de las desviaciones cuadráticas respecto al promedio, dividido por el número de datos
  """
  x=promedio(lista)
  N=len(lista)
  sum=0
  for elem in lista:
    sumatoria=(elem-x)**2
    sum+=sumatoria

  varianza=(1/N)*(sum)

  return varianza

def desviacion_estandar(lista):
  """
  Función que regresa el valor numérico de la desviación estandar de una lista de datos
  ---------------------------------------------
  Input:
    lista: lista con datos numérios
  Output:
    desviacion: la raiz de la varianza
  """
  var=varianza(lista)
  desviacion=(var)**(1/2)
  return desviacion

def rango_intercuartilico(lista):
  """
  Función que calcula el rango intercuartilico de una lista de datos
  ---------------------------------------------
  Input:
    lista: lista con datos numérios
  Output:
    cuartiles: valor numérico correspondiente al rango intercuartílico
  """
  if len(lista)%2==0:
    Q1_index1=len(lista)//4
    Q1_index2=Q1_index1-1
    Q3_index1=(len(lista)*3)//4
    Q3_index2=Q3_index1-1
    Q1=(float(lista[Q1_index1])+float(lista[Q1_index2]))/2
    Q3=(float(lista[Q3_index1])+float(lista[Q3_index2]))/2

  else:
    Q1_index=len(lista)//4
    Q3_index=(len(lista)*3)//4
    Q1=float(lista[Q1_index])
    Q3=float(lista[Q3_index])

  IQR=Q3-Q1
  return IQR

def MAD(lista):
  """
  Función que calcula la desviación mediana absoluta de una lista de datos
  ---------------------------------------------
  Input:
    lista: lista con datos numérios
  Output:
    mad: desviación mediana absoluta de la lista
  """
  med=mediana(lista)
  deviacion=[abs(x-med) for x in lista]
  mad=mediana(deviacion)
  return mad

def covarianza(x,y):
  """
  Función que calcula la covarianza para dos listas con datos numéricos
  ---------------------------------------------
  Input:
    x: lista x con datos numérios
    y: lista y con datos numéricos
  Output:
    cov: valor numérico correspondiente a la covarianza de x e y
  """
  x_prom=promedio(x)
  y_prom=promedio(y)
  N=len(x)
  sum=0
  for i,j in zip(x,y):
    sum+=((i-x_prom)*(j-y_prom))
  cov=sum/N
  return cov

def coeficiente_correlacion(x,y):
  """
  Función que calcula el coeficiente de correlación entre dos listas con datos numéricos
  ---------------------------------------------
  Input:
    x: lista x con datos numérios
    y: lista y con datos numéricos
  Output:
    r: valor numérico correspondiente al coeficiente de correlación entre x e y
  """
  covar=covarianza(x,y)
  varx=varianza(x)
  vary=varianza(y)
  r=covar/(varx*vary)
  return r