# SISTEMA DE CONFIGURACION DE PROTOCOLO DE ENRUTAMIENTO BGP PARA LA INTERCONEXION ENTRE ISP

                                                  Manual de uso para la aplicacion
                          
Función: Establecer y configurar una sesion BGP entre proveedores de servicios de internet ISP dado sus numeros de sistemas autonomos

requisitos:
*Instalacion de Python 2.7.12 y su libreria telnetlib.
*Establecer la previa configuracion en los dispositivos locales y remotos que formara parte la sesion BGP.
*Obtener conocimientos previos acerca de la topologia fisica y logica de la red.

Opciones de la interfaz de usuario:
1)El usuario ingresa los números de AS (Sistema Autónomo) local y remoto cuando da click guardar AS entonces el sistema mostrará los sistemas autónomos establecidos para la sesión BGP.
Validacion:
*Dado a que el usuario no ingresa los números de AS cuando da click en guardar AS entonces el sistema mostrará un mensaje de error solicitando que se llene el campo requerido.

2)El usuario ingresa la dirección IP del dispositivo vecino cuando da click en vecino BGP entonces el sistema configurará el comando neighbor con el AS correspondiente.
Validacion: 
*Ingresar la direccion IP en un formato adecuado para efectuar la accion.

3)El usuario ingresa las redes a publicar cuando da click en configurar redes entonces el sistema configurará las redes en el dispositivo.
Validacion: 
*Ingresar la direccion de la red en un formato adecuado para efectuar la accion.

Recomendacion:
*Leer detalladamente el manual de usuario.
*Establecer las configuraciones previa en los dispositivos de manera adecuada.
