# Aplicación de Registro y Reconocimiento Facial
Esta es una aplicación simple para el registro y reconocimiento facial. Permite a los usuarios registrarse en el sistema y realizar reconocimiento facial.
Características

- Registro de Usuarios: Los usuarios pueden registrarse proporcionando información básica.
- Reconocimiento Facial: La aplicación utiliza reconocimiento facial para identificar a los usuarios registrados.

## Disponibilidad en Docker Hub

La imagen del contenedor está disponible en Docker Hub en la siguiente ubicación [carlosservi/python-reconocimiento:latest](https://hub.docker.com/r/carlosservi/python-reconocimiento).

Ejecutar en Ubuntu o Debian.

Para ejecutar en Mac es necesario instalar x11.

Asegúrate de tener x11 habilitado y configurado correctamente. Puedes usar el siguiente comando para permitir conexiones X11 desde Docker:

```bash
xhost +local:docker
```

Luego, ejecuta el contenedor de la siguiente manera:
```bash
docker run -e DISPLAY=$DISPLAY -v /tmp/.X11-unix:/tmp/.X11-unix --privileged carlosservi/python-reconocimiento:latest
```
Si quieres persistencia con los usuarios registrados (Vease Notas Importantes)
```bash
docker run -e DISPLAY=$DISPLAY -v /tmp/.X11-unix:/tmp/.X11-unix -v `pwd`/Data:/usr/src/app/Data --privileged carlosservi/python-reconocimiento:latest
```

## Descarga desde Github

### Ejemplo de construcción del contenedor a partir del repositorio de github (Tarda mucho en crearlo, tiene muchas dependencias)
```bash
docker build -t nombre-del-contenedor .
```

### Ejemplo de ejecución del programa con docker
```bash
docker run -e DISPLAY=$DISPLAY -v /tmp/.X11-unix:/tmp/.X11-unix --privileged nombre-del-contenedor
```

### Ejecución con python
También es posible ejecutarlo con python pero teneis que aseguraros de tener todas las dependencias como dlib, opencv, etc...
```bash
python3 main.py
```

## Notas Importantes
- Si quieres persistencia a la hora de guardar las personas registradas necesitas tener una carpeta Data en el directorio donde lo ejecutes.
- Esta aplicación ha sido probada en sistemas Ubuntu y Debian con X11 habilitado. Asegúrate de tener X11 configurado correctamente antes de ejecutar el contenedor.
- Se recomienda ejecutar el contenedor con la opción --privileged para garantizar el acces o adecuado a los recursos del sistema.

¡Disfruta usando la aplicación de registro y reconocimiento facial!