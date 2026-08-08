import os
import subprocess

# Nombres de tus carpetas
carpeta_origen = "videos"
carpeta_destino = "videos_recortados"

# Crea la carpeta nueva si no existe
if not os.path.exists(carpeta_destino):
    os.makedirs(carpeta_destino)

# Tus coordenadas perfectas para el Hablante 1
medidas_recorte = "900:900:150:60"

print("Iniciando el recorte masivo para el Hablante 1...")

# Revisa cada archivo en tu carpeta original
for archivo in os.listdir(carpeta_origen):
    # Filtro clave: Solo procesa los que sean mp4 y empiecen con "H1_"
    if archivo.startswith("H1_") and archivo.endswith(".mp4"):
        ruta_origen = os.path.join(carpeta_origen, archivo)
        ruta_destino = os.path.join(carpeta_destino, archivo)
        
        print(f"Recortando: {archivo}...")
        
        # El comando exacto que probaste, incluyendo la codificación segura para Windows/Web
        comando = f'ffmpeg -i "{ruta_origen}" -vf "crop={medidas_recorte}" -c:v libx264 -pix_fmt yuv420p -c:a copy "{ruta_destino}"'
        
        # Ejecuta el comando
        subprocess.run(comando, shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)

print("¡Listo! Todos los videos de H1 han sido recortados exitosamente con su nombre original.")