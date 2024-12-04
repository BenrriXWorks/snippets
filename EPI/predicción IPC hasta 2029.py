import matplotlib.pyplot as plt
import numpy as np

''' Datos extraidos de https://www.sii.cl/valores_y_fechas/utm/utm2024.htm utilizando
    el siguiente script por cada año:
    <js>
        var total = [];
        $('#table_export tr td:nth-child(4)').each(function() { 
            var valor = $(this).text().replaceAll(',', '.').trim(); 
            valor && total.push(Number(valor)); // Si valor no está vacío, lo convierte y lo agrega
        })
        console.log(promedio año ${$('.filter-option').text()}: ${total.reduce((acc, x) => acc + x) / total.length})
    <\js>

 '''
promedios_filtrados = [
    104.395,  # 2014
    108.93500000000002,  # 2015
    113.05999999999999,  # 2016
    115.52750000000002,  # 2017
    118.34083333333332,  # 2018
    122.96083333333333,  # 2022
    132.2833333333333,   # 2023
    132.2833333333333    # 2024
]

# Años a predecir
anios_prediccion = list(range(2025, 2030))
anios_filtrados = [2014, 2015, 2016, 2017, 2018, 2022, 2023, 2024]  # Sin 2019

# Ajustar los datos con un modelo de regresión lineal sin 2019
promedios_filtrados_pct = [x for x in promedios_filtrados]
coeficientes_filtrados = np.polyfit(anios_filtrados, promedios_filtrados_pct, 1)  # Ajuste lineal (grado 1)
modelo_filtrado = np.poly1d(coeficientes_filtrados)

# Predecir los próximos 5 años sin 2019
promedios_predichos_filtrados = modelo_filtrado(anios_prediccion)  # Valores predichos sin 2019
variacion_porcentual = []

# Agregar la variación de 2025 respecto a 2024
variacion_2025 = ((promedios_predichos_filtrados[0] - promedios_filtrados_pct[-1]) / promedios_filtrados_pct[-1]) * 100
variacion_porcentual.append(variacion_2025)

# Calcular las variaciones de los demás años de la predicción
for i in range(1, len(promedios_predichos_filtrados)):
    variacion = ((promedios_predichos_filtrados[i] - promedios_predichos_filtrados[i - 1]) / promedios_predichos_filtrados[i - 1]) * 100
    variacion_porcentual.append(variacion)

# Crear gráfico
fig, ax = plt.subplots(figsize=(10, 6))

# Graficar los datos históricos y las predicciones
ax.plot(anios_filtrados, promedios_filtrados_pct, 'o-', label='Datos históricos', color='blue')
ax.plot(anios_prediccion, promedios_predichos_filtrados, 'o--', label='Predicción (2025-2029)', color='orange')

# Agregar las variaciones porcentuales como etiquetas sobre los puntos de las predicciones
for i, anio in enumerate(anios_prediccion):
    ax.text(anio, promedios_predichos_filtrados[i], f"{variacion_porcentual[i]:.2f}%", ha='center', va='bottom', color='black')

# Configuración del gráfico
ax.set_xlabel('Año')
ax.set_ylabel('Promedio (%)')
ax.set_title('Evolución de Promedios Anuales y Predicción IPC con Variación Porcentual')
ax.legend()
ax.grid(True)

# Mostrar el gráfico
plt.show()