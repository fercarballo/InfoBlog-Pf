# InfoBlog 
___
//Introducción
___
## _Primeros pasos_

Este repositorio contiene una instalación limpia de Django, es por esto que se deben configurar algunas cosas antes de comenzar a utilizarla.

## Instalando e iniciando el entorno virtual

Para asegurar la compatibilidad y autosuficiencia del código, es necesario crear un entorno virtual.

Una vez que tengamos creado un directorio de trabajo, se debe abrir una ventana del Símbolo del Sistema con privilegios de administrador y ejecutar el siguiente comando.
```sh
python -m venv .
```
Esto nos creará un entorno virtual utilizando [venv], en el mismo directorio donde se ejecuta el comando.

Una vez creado el entorno virtual, se lo debe iniciar con los siguientes comandos:

```sh
cd Scripts
activate.bat
```

> Nota: Es posible que este paso de un error si la política 
> de seguridad del sistema no permite la ejecución de scripts.
> De suceder, se debe ejecutar el siguiente comando en una 
> ventana de PowerShell con privilegios administrativos:
> 
> ```Set-ExecutionPolicy RemoteSigned -Scope CurrentUser```
> 
> Es común que solicite una confirmación, de ser así, se debe ingresar 
la letra `S` y presionar `Enter`.
> Esto además resolverá el problema si se presenta en el terminal
de Visual Studio Code.

Ahora, el entorno virtual está instalado y activado. No cierren este terminal, ya que nos servirá más adelante.

# Clonar el repositorio e instalar dependencias

Dentro de la carpeta `Scripts`, se debe crear una nueva carpeta donde se clonará el código.
El nombre de esta carpeta no importa y puede ser arbitrario, ya que solo sirve como un contenedor para ordenar mejor las cosas.

Una vez creada, se debe ingresar a la misma y ejecutar los siguientes comandos:

```sh
git init
git remote add origin https://github.com/maxacan/ProyectoDjangoInfo2021.git
git fetch origin
git checkout main
```

Una vez clonado el código, se deben instalar las dependencias descriptas en el archivo `requeriments.txt`, ejecutando el siguiente comando en el terminal del Símbolo del Sistema que dejamos abierto:

```sh
pip install -r requeriments.txt
```

# Creación de la base de datos, migración y creación de superuser

Ya tenemos todo lo que necesitamos para comenzar a utilizar Django, solamente faltan los últimos detalles:

## _Creación de la base de datos_

Si abrimos el archivo `BlogInfoBase\settings.py`, veremos que Django está esperando el poder conectarse a una base de datos de MySql llamada `Final_Info_Testing`.
Por lo tanto, debemos crear una base de datos con el mismo nombre.

En MySql WorkBench, ejecutamos el siguiente comando:

```sh
CREATE SCHEMA Final_Info_Testing;
```

> Nota: El nombre de esta base de datos también es arbitrario, pero 
se espera que sea `Final_Info_Testing` para evitar problemas de compatibilidad
al pushear cambios al repositorio.

## _Migración de datos_
Al cambiar de base de datos, Django nos pide aplicar las migraciones de datos desde cero.

Ya podemos comenzar a utilizar Visual Studio Code para facilitar la experiencia.

(A partir de este momento, todos los comandos van a ser corridos en el terminal de Visual Studio Code.)

Abrimos Visual Studio Code y navegamos hasta la carpeta `Scripts` del entorno virtual.
Una vez en ese directorio, ejecutamos el siguiente comando en el terminal de Visual Studio Code:
```sh
.\activate
```

Una vez que se activa el entorno virtual, navegamos hasta la carpeta donde clonamos el código, (la que tiene el archivo `manage.py`), y ejecutamos los siguientes comandos para hacer las migraciones a la nueva base de datos.

```sh
python .\manage.py makemigrations
python .\manage.py migrate
```

Una vez hechas las migraciones, procedemos a crear un `superuser`, que actuará como administrador en la página.

## _Creación del superuser_

Ejecutamos el comando: 
```sh
python .\manage.py createsuperuser
```

Esto nos dará un pequeño programa interactivo que nos pedirá ingresar un usuario, un correo electrónico y una contraseña.

Si precionamos enter sin haber ingresado nada cuando nos pide un usuario, el usuario se convierte en el nombre de usuario del sistema. De lo contrario, podemos ingresar el usuario que queramos, el cual se recomienda que sea sencillo, ya que se va a estar usando constantemente y escribir un usuario complicado cada vez que se necesite entrar al panel de administración se vuelve muy tedioso, muy rápido.

Luego, nos pide un correo, el cual puede estar en blanco, ya que no se usa para acceder al panel administrativo.

La contraseña puede ser arbitraria, aunque si Django detecta que es una contraseña muy sencilla, como `12345`, nos mostrará un mensaje preguntando si queremos confirmar o no el uso de la misma, si nos aparece este mensaje, simplemente escribimos `y` y presionamos `Enter `.
Como con el usuario, se recomienda una contraseña sencilla para que no se vuelva tedioso el trabajo de entrar al panel administrativo.


Una vez creado el `superuser`, procedemos a correr nuevamente los comandos para realizar la migración de los datos: 
```sh
python .\manage.py makemigrations
python .\manage.py migrate
```

# Pasos finales

Lo único que resta hacer para confirmar que todo funcione correctamente, es ejecutar el comando:
```sh
python .\manage.py runserver
```
Este comando abre el servidor en la dirección `127.0.0.1:8000/`.

Si nos vamos a esa dirección en nuestro navegador, deberíamos ver la página por defecto de Django, con la leyenda:
`The install worked successfully! Congratulations!`

[//]: #
[venv]: <https://docs.python.org/es/3/library/venv.html>

