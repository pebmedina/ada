def filtrar_archivo_por_nivel(log_file, niveles_deseados):
    with open(log_file, 'r') as archivo:
        niveles_encontrados = set()
        for linea in archivo:
            for nivel in niveles_deseados:
                if nivel in linea:
                    niveles_encontrados.add(nivel)
                    print(linea.strip())
                    break

        for nivel in niveles_deseados:
            if nivel not in niveles_encontrados:
                print("No se encontraron registros de {} en el archivo.".format(nivel))

if __name__ == "__main__":
    log_file = "postgresql.log"
    niveles_deseados = ["ERROR", "FATAL", "PANIC"]
    filtrar_archivo_por_nivel(log_file, niveles_deseados)
