import pandas as pd
import re

def verificar_xlsx(archivo_path):
    try:
        # Leer el archivo Excel
        df = pd.read_excel(archivo_path)
        
        # Verificar que tenga las columnas necesarias
        columnas_requeridas = ['N°de Control', 'Coloca tu nombre comenzando por apellidos. (En mayúsculas)', 
                              'Género', 'Coloca la Carrera', 
                              'Inserta el semestre en el que vas a cursar el Servicio Social. (Con letra)', 
                              'Correo electrónico institucional', 'Teléfono']
        
        for col in columnas_requeridas:
            if col not in df.columns:
                return f"Error: Falta la columna '{col}' en el archivo."
        
        errores = []
        
        # Verificar cada fila
        for index, fila in df.iterrows():
            # Verificar Columna A (N°de Control): 8 dígitos
            if not re.fullmatch(r'\d{8}', str(fila['N°de Control'])):
                errores.append(f"Fila {index+2}: N°de Control debe tener exactamente 8 dígitos")
            
            # Verificar Columna C (Género): Masculino o Femenino
            genero = str(fila['Género']).strip().capitalize()
            if genero not in ['Masculino', 'Femenino']:
                errores.append(f"Fila {index+2}: Género debe ser 'Masculino' o 'Femenino'")
            
            # Verificar Columna D (Carrera): Licenciatura en Arquitectura
            carrera = str(fila['Coloca la Carrera']).strip()
            if carrera not in ['Licenciatura en Arquitectura', 'Ingeniería en Diseño Industrial']:
                errores.append(f"Fila {index+2}: Carrera debe ser 'Licenciatura en Arquitectura' o 'Ingeniería en Diseño Industrial'")
            
            # Verificar Columna E (Semestre): Valores permitidos
            semestres_permitidos = ['sexto','septimo', 'octavo', 'noveno', 'decimo', 'onceavo', 'treceavo']
            semestre = str(fila['Inserta el semestre en el que vas a cursar el Servicio Social. (Con letra)']).strip().lower()
            if semestre not in semestres_permitidos:
                errores.append(f"Fila {index+2}: Semestre no válido. Debe ser uno de: {', '.join(semestres_permitidos)}")
            
            # Verificar Columna F (Correo): l + 8 dígitos + @pachuca.tecnm.mx
            correo = str(fila['Correo electrónico institucional']).strip().lower()
            if not re.fullmatch(r'l\d{8}@pachuca\.tecnm\.mx', correo):
                errores.append(f"Fila {index+2}: Correo institucional no válido. Debe ser l[8 dígitos]@pachuca.tecnm.mx")
            
            # Verificar que el número de control coincida con el correo
            n_control = str(fila['N°de Control']).strip()
            if not correo.startswith(f'l{n_control}'):
                errores.append(f"Fila {index+2}: El número de control no coincide con el correo electrónico")
            
            # Verificar Columna G (Teléfono): 10 dígitos
            telefono = str(fila['Teléfono']).strip()
            if not re.fullmatch(r'\d{10}', telefono):
                errores.append(f"Fila {index+2}: Teléfono debe tener exactamente 10 dígitos")
        
        if errores:
            return "Se encontraron los siguientes errores:\n" + "\n".join(errores)
        else:
            return "El archivo cumple con todos los requisitos. No se encontraron errores."
    
    except Exception as e:
        return f"Error al procesar el archivo: {str(e)}"

# Ejemplo de uso
if __name__ == "__main__":
    archivo_path = input("Ingrese la ruta del archivo XLSX a verificar: ")
    resultado = verificar_xlsx(archivo_path)
    print(resultado)