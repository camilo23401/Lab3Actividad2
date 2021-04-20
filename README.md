# Lab3Actividad2

te README explica el funcionamiento de las aplicaciones servidor y cliente desarrolladas para este laboratorio

-----------------------------------------------------------------Servidor-------------------------------------------------------------

Para correr el servidor basta con clonar el repositiorio al sitio donde se quiera correr, que puede ser un cliente windows o una máquina Ubuntu, pues se probó su funcionamiento en ambos ambientes.

Tras hacer esto, se deben crear los archivos que se enviaran en la transferencia. Para esto se debe ir al directorio ArchivosParaEnviar y crearlos. El Windows se puede utilizar la herramiento fsutil y en ubuntu truncate (Por ejemplo, en Ubuntu se puede poner el comando "truncate -s 100M "Archivo100M.txt"" para crear el archivo. Lo importante es que los archivos se deben llamar "Archivo100M.txt" y "Archivo250M.txt"

Una vez clonado, se debe ejecutar con una versión de Python 3, idealmente Python 3.8. Esto se hace a través del comando python3 Servidor.py

Una vez empieza a correr el servidor, se solicita que se escoja cual de los dos archivos enviar y a cuántos clientes se desea transmitir simultáneamente. Estas decisiones se escogen a través de la consola.

Tras esto, se crean los socket y la arquitectura Thread-per-client queda montada y en espera de los clientes. Tras esto, se debe correr el script de los clientes y asegurar que el del servidor sigue corriendo. En Windows esto se puede lograr corriendo dos ventanas de comando por separado y en Ubuntu se puede dormir el proceso con Ctrl+z y después enviarlo al segundo plano con "bg 1" y ahí si correr el cliente. Si se corre el servidor en una máquina y el cliente en otra, no debería haber mayor problema, siempre y cuando se mantenga corriendo el servidor.

Una vez se conecten los clientes, el servidor empieza y termina su transferencia satisfactoriamente.

----------------------------------------------------------------Cliente-------------------------------------------------------------

Para correr el cliente basta con clonar el repositiorio al sitio donde se quiera correr, que puede ser un cliente windows o una máquina Ubuntu, pues se probó su funcionamiento en ambos ambientes.

Dentro del código hay dos lineas importantes que se deben modificar de acuerdo a lo que se quiere hacer con el cliente. En primer lugar, se debe definir el host como la dirección IP en donde se encuentra corriendo el servidor. Por otro, se debe cambiar la constante NUM_HILOS para que represente el número de clientes que se busca conectar al servidor.

Una vez se define esto, al correr el script se hace la conexión con el servidor y se empiezan a recibir los paquetes de los archivos hasta que se completa la transferencia de forma exitosa.

Los archivos recibidos quedarán en la carpeta ArchivosRecibidos

-------------------------------------------------------------Extras-----------------------------------------------------------------

Todos los logs quedan guardados en el directorio Logs El hashing se hace con la encriptación SHA256 y se verifica después de recibir la totalidad del archivo
