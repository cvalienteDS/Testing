Instrucciones

1. Python

1.1	Instalación Python

Actualmente la versión de 64-bit para Windows para descargar se encuentra en esta url:
https://www.python.org/ftp/python/3.8.6/python-3.8.6-amd64.exe		
Ejecutar el fichero descargado y seguir las instrucciones. Cuando pregunte si añadir al PATH, marcar que sí.

1.2	Instalación de librerías

La mayor parte de las librerías que se usan son las que vienen con Python por defecto, no obstante, para instalar las librerías necesarias que no vienen con Python se usará el fichero de texto requirements.txt que se encuentra en la raíz (al mismo nivel que el "main.py"). Para instalar las librerías, desde el símbolo de sistema, situamos el directorio de trabajo en la misma ruta donde esté requirements.txt, y se ejecuta la siguiente instrucción:

pip install -r requirements.txt

2.	Ejecución de la aplicación

La aplicación puede ejecutarse desde un IDE como Pycharm o directamente desde el símbolo de sistema, situando el directorio de trabajo actual sobre la ruta en la que se encuentra el fichero “main.py”, y ejecutando la instrucción:

python main.py

Todos los parámetros se definen en los ficheros externos de configuración.

Para ejecutar los tests hay que ejecutar la instrucción:

python testing.py

Dada la naturaleza cambiante de los datos de entrada, para hacer tests creo e inserto datos en una base de datos sqlite "in memory" a partir de un script.sql.
De esta manera podemos mantener constantes los datos de entrada para hacer los tests, mientras que la base de datos de "producción" puede cambiar sin afectar a los mismos.
