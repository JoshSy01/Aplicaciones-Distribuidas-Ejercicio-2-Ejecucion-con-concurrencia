# Ejecución Concurrente en Python con Asyncio: Lavado de Ropa

Este proyecto demuestra el funcionamiento de la **concurrencia** en Python utilizando la librería estándar `asyncio`, simulando el lavado simultáneo de 3 tandadas de ropa (`Ropa Blanca`, `Ropa de Color` y `Ropa Delicada`).

A diferencia de la ejecución secuencial (donde cada tandada espera a la anterior sumando 12 segundos), con `asyncio` el bucle de eventos inicia las 3 tareas de forma concurrente. Durante la espera no bloqueante (`await asyncio.sleep(4)`), todas las tandadas se procesan en paralelo lógico, reduciendo el tiempo total de ejecución a **4 segundos**.

## Estructura del Proyecto

```text
.
├── Concurrente_lavado_ropa.py  # Script en Python con concurrencia (asyncio)
├── docker-compose.yml          # Configuración del servicio con Docker Compose
└── README.md                   # Documentación e instrucciones de ejecución
```

## Requisitos Previos

* Tener instalado [Docker](https://docs.docker.com/get-docker/).

## Cómo ejecutar el script con Docker

Abre una terminal en la carpeta raíz del proyecto y elige cualquiera de las siguientes opciones:

### Opción 1: Usando Docker Compose (con montaje de volumen)

1. Ejecuta el contenedor directamente:
```bash
docker compose up
```

2. Para limpiar el contenedor una vez finalizado:
```bash
docker compose down
```

## Salida Esperada

En la consola se observará que las 3 tandadas inician inmediatamente sin esperar a que termine la anterior, completando todo el trabajo en ~4 segundos:

```text
Lavando Ropa Blanca...
Lavando Ropa de Color...
Lavando Ropa Delicada...
Ropa Blanca lavada.
Ropa de Color lavada.
Ropa Delicada lavada.
Tiempo total de lavado: 4.00 segundos
```