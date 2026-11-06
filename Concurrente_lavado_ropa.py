import asyncio
import time

async def lavar_ropa(tipo_ropa):
    print(f"Lavando {tipo_ropa}...")
    await asyncio.sleep(4)  # Simula el tiempo de lavado sin bloquear el flujo
    print(f"{tipo_ropa} lavada.")

async def main():
    inicio = time.perf_counter()

    tandadas = [
        "Ropa Blanca",
        "Ropa de Color",
        "Ropa Delicada"
    ]

    # Ejecuta las 3 tandadas de forma concurrente
    tareas = [lavar_ropa(ropa) for ropa in tandadas]
    await asyncio.gather(*tareas)

    fin = time.perf_counter()
    print(f"Tiempo total de lavado: {fin - inicio:.2f} segundos")


asyncio.run(main())