#import time

# Datos de entrada
insumos = [
    {"ref": "A1", "valor": 150, "tipo": "estandar"},
    {"ref": "B2", "valor": 300, "tipo": "premium"},
    {"ref": "C3", "valor": 200,  "tipo": "critico"},
    {"ref": "D4", "valor": 500, "tipo": "critico"},
    {"ref": "E5", "valor": 120, "tipo": "estandar"},
]

def formatear_nombre(referencia):
    return f"ITEM-ID-{referencia}"

def aplicar_ajuste(monto, categoria):
    # ¿Qué hace esta lógica con los números?
    if categoria == "premium":
        return monto * 1.20
    elif categoria == "critico":
        return monto * 1.50
    return monto

def procesar_lote(lista_items):
    resultado_final = []
    acumulado_valor = 0
    
    print("Iniciando escaneo de inventario...")
    print("-" * 30)
    
    for item in lista_items:
        # Extraer datos
        codigo = item["ref"]
        precio_base = item["valor"]
        clase = item["tipo"]
        
        # Transformación
        nombre_nuevo = formatear_nombre(codigo)
        precio_final = aplicar_ajuste(precio_base, clase)
        
        # Guardar cambios
        registro = {
            "etiqueta": nombre_nuevo,
            "cobro": precio_final,
            "es_caro": precio_final > 200
        }
        
        resultado_final.append(registro)
        acumulado_valor += precio_final
        
        print(f"Analizando: {codigo}... OK")
        #time.sleep(0.3) # Simula una carga
        
    return resultado_final, acumulado_valor

# --- Ejecución ---
if __name__ == "__main__":
    analisis, total = procesar_lote(insumos)
    
    print("-" * 30)
    print("REPORTE GENERADO")
    
    for ficha in analisis:
        marca = "[!!!]" if ficha["es_caro"] else "[   ]"
        print(f"{marca} {ficha['etiqueta']}: ${ficha['cobro']}")
        
    print("-" * 30)
    print(f"VALOR TOTAL DEL LOTE: ${total}")
