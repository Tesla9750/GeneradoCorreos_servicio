import openpyxl

def leer_numeros_control_txt(archivo_txt):
    """Lee números de control desde un archivo TXT con formato 'número OR'"""
    numeros = []
    with open(archivo_txt, 'r', encoding='utf-8') as f:
        for linea in f:
            partes = linea.strip().split()
            if partes and partes[0].isdigit():
                numeros.append(partes[0])
    return numeros

def leer_numeros_control_xlsx(archivo_xlsx, hoja='Hoja1', columna='A'):
    """Lee números de control desde un archivo XLSX (ignorando el encabezado)"""
    numeros = []
    
    wb = openpyxl.load_workbook(archivo_xlsx)
    hoja = wb[hoja]
    
    for fila in hoja[columna][1:]:
        if fila.value is not None:
            numero = str(fila.value).strip()
            if numero.isdigit():
                numeros.append(numero)
    
    return numeros

def verificar_longitud(numeros):
    """Identifica números que no tienen exactamente 8 dígitos"""
    incorrectos = [num for num in numeros if len(num) != 8]
    return incorrectos

def imprimir_listas(numeros_txt, numeros_xlsx):
    """Imprime ambas listas para visualización comparativa"""
    print("\nVISUALIZACIÓN COMPARATIVA DE LISTAS")
    print("-"*50)
    print(f"{'TXT':<12} | {'XLSX':<12}")
    print("-"*25)
    
    max_len = max(len(numeros_txt), len(numeros_xlsx))
    
    for i in range(max_len):
        txt_num = numeros_txt[i] if i < len(numeros_txt) else ''
        xlsx_num = numeros_xlsx[i] if i < len(numeros_xlsx) else ''
        print(f"{txt_num:<12} | {xlsx_num:<12}")

def comparar_numeros(numeros_txt, numeros_xlsx):
    """Compara dos listas de números de control"""
    set_txt = set(numeros_txt)
    set_xlsx = set(numeros_xlsx)
    
    coinciden = set_txt & set_xlsx
    solo_txt = set_txt - set_xlsx
    solo_xlsx = set_xlsx - set_txt
    
    return {
        'coinciden': sorted(coinciden),
        'solo_txt': sorted(solo_txt),
        'solo_xlsx': sorted(solo_xlsx),
        'total_coinciden': len(coinciden),
        'total_solo_txt': len(solo_txt),
        'total_solo_xlsx': len(solo_xlsx)
    }

def generar_reporte(resultado, archivo_salida='reporte_comparacion.txt'):
    """Genera un archivo de texto con el reporte detallado"""
    with open(archivo_salida, 'w', encoding='utf-8') as f:  # Añadido encoding='utf-8'
        f.write("REPORTE DE COMPARACIÓN DE NÚMEROS DE CONTROL\n")
        f.write("="*50 + "\n\n")
        f.write(f"Total números en TXT: {len(resultado['solo_txt']) + resultado['total_coinciden']}\n")
        f.write(f"Total números en XLSX: {len(resultado['solo_xlsx']) + resultado['total_coinciden']}\n")
        f.write(f"Números que coinciden: {resultado['total_coinciden']}\n")
        f.write(f"Números solo en TXT: {resultado['total_solo_txt']}\n")
        f.write(f"Números solo en XLSX: {resultado['total_solo_xlsx']}\n\n")
        
        # Agregar verificación de longitud al reporte
        todos_numeros = resultado['coinciden'] + resultado['solo_txt'] + resultado['solo_xlsx']
        incorrectos = verificar_longitud(todos_numeros)
        f.write(f"\nNúmeros con longitud diferente a 8 dígitos: {len(incorrectos)}\n")  # Cambiado el símbolo
        for num in incorrectos:
            f.write(f"{num} ({len(num)} dígitos)\n")
        
        f.write("\nDETALLE:\n")
        f.write("-"*50 + "\n")
        f.write("\nNúmeros que coinciden:\n")
        for num in resultado['coinciden']:
            f.write(num + "\n")
        
        f.write("\nNúmeros solo en TXT:\n")
        for num in resultado['solo_txt']:
            f.write(num + "\n")
            
        f.write("\nNúmeros solo en XLSX:\n")
        for num in resultado['solo_xlsx']:
            f.write(num + "\n")
    
    print(f"\nReporte generado en: {archivo_salida}")

def main():
    print("COMPARADOR DE NÚMEROS DE CONTROL - TXT vs XLSX\n")
    
    archivo_txt = input("Ingrese la ruta del archivo TXT: ").strip()
    archivo_xlsx = input("Ingrese la ruta del archivo XLSX: ").strip()
    archivo_salida = input("Ingrese el nombre del archivo de reporte (opcional): ").strip()
    
    if not archivo_salida:
        archivo_salida = 'reporte_comparacion.txt'
    
    try:
        print("\nLeyendo archivos...")
        numeros_txt = leer_numeros_control_txt(archivo_txt)
        numeros_xlsx = leer_numeros_control_xlsx(archivo_xlsx)
        print(f"Leídos {len(numeros_txt)} números del TXT")
        print(f"Leídos {len(numeros_xlsx)} números del XLSX")
        
        # Verificar longitudes incorrectas
        incorrectos_txt = verificar_longitud(numeros_txt)
        incorrectos_xlsx = verificar_longitud(numeros_xlsx)
        
        if incorrectos_txt:
            print("\nNúmeros con longitud incorrecta en TXT:")
            for num in incorrectos_txt:
                print(f"{num} ({len(num)} dígitos)")
        
        if incorrectos_xlsx:
            print("\nNúmeros con longitud incorrecta en XLSX:")
            for num in incorrectos_xlsx:
                print(f"{num} ({len(num)} dígitos)")
        
        # Mostrar visualización comparativa
        if input("\n¿Desea ver la comparación visual de las listas? (s/n): ").lower() == 's':
            imprimir_listas(numeros_txt, numeros_xlsx)
        
    except Exception as e:
        print(f"\nError: {e}")
        return
    
    # Comparar los números
    resultado = comparar_numeros(numeros_txt, numeros_xlsx)
    
    # Mostrar resumen
    print("\nRESULTADOS:")
    print(f"Números que coinciden: {resultado['total_coinciden']}")
    print(f"Números solo en TXT: {resultado['total_solo_txt']}")
    print(f"Números solo en XLSX: {resultado['total_solo_xlsx']}")
    
    # Generar reporte detallado
    generar_reporte(resultado, archivo_salida)

if __name__ == "__main__":
    main()