# OPERADOR MORSA
El operador de morsa se representa con " := " y se utiliza de la siguiente manera:
 
# 1. Asignación condicional:
 
- Podemos asignar un valor a una variable basado en una condición utilizando el operador de morsa.
> Ejemplo:
```python
 Copiar
edad = 20
estado = "Mayor de edad" if edad >= 18 else "Menor de edad"
print(estado)
```

 En este ejemplo, se asigna el valor "Mayor de edad" a la variable "estado" si la edad es mayor o igual a 18; de lo contrario, se asigna el valor "Menor de edad".
# 2. Ignorar valores:
 
- Podemos utilizar el operador de morsa para ignorar valores que no nos interesan al desempaquetar una secuencia.
>Ejemplo:
```python
 Copiar
numeros = [1, 2, 3, 4, 5]
_, _, _, cuarto, _ = numeros
print(cuarto)
```
 En este ejemplo, utilizamos el operador de morsa para ignorar los primeros tres valores de la lista "numeros" y asignar el cuarto valor a la variable `"cuarto"`.
 
Recuerda que el operador de morsa solo está disponible a partir de la versión 3.8 de Python. Si estás utilizando una versión anterior, es posible que no puedas utilizar este operador.
 