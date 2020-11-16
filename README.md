##Prueba técnica Data Engineering

## Instrucciones

1. Haz un fork del repo.
2. Resuelve el problema.
3. Crea unas instrucciones con todo lo necesario para que el proyecto funcione.
4. Haz una PR con el código y todo lo que consideres necesario.
5. Avisanos cuando hayas terminado.

### ¿Qué será valorado?
Se valorará cómo se encara con código un problema de ingeniería de datos. La estructura del código y el testing del mismo.  

### Requisitos tecnológicos
- Elige el lenguaje de programación con el que más cómodo te sientas
- Usa las librerías que creas necesarias.
- Tests unitarios.

### La tarea
Nuestro cliente necesita recibir en un endpoint información sobre las visitas a las páginas de sus productos. 
El json con la información tendrá los siguientes campos: 

- user_id
- date
- product_name
- price
- purchased (boolean)

La información recibida por este endpoint debe ser guardada en local de forma persistente y acumulativa, es decir, cada vez que la aplicación se ejecute añadirá información a un fichero.

#### Importante!
- El problema es pequeño en concepto, pero tiene que estar preparado para trabajar con una gran cantidad de datos.
- 

#### Además...
- Queremos calcular de un mes a otro cuanto ha variado el tráfico por producto (durante un año, por ejemplo).
- Queremos calcular la media de venta mensual de todo un año.
- Queremos obtener todas las compras de un usuario.

#### Puntos extra
- ¿Existe una relación entre las variables y si el usuario termina comprando? Propón una forma de encontrar la relación entre ellas.
