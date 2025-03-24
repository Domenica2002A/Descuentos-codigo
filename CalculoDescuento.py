def calcular_descuento(monto_total, porcentaje_descuento=10):
    """Calcula el descuento aplicado a un monto total."""
    descuento = (porcentaje_descuento / 100) * monto_total
    return descuento

# Llamadas a la función
total_compra_1 = 100  # Ejemplo de monto total
descuento_1 = calcular_descuento(total_compra_1)

# Segunda llamada con porcentaje personalizado
total_compra_2 = 200  # Otro ejemplo de monto total
descuento_2 = calcular_descuento(total_compra_2, 15)

# Mostrar resultados
print(f"Compra 1: Monto total = ${total_compra_1}, Descuento = ${descuento_1}, Total a pagar = ${total_compra_1 - descuento_1}")
print(f"Compra 2: Monto total = ${total_compra_2}, Descuento = ${descuento_2}, Total a pagar = ${total_compra_2 - descuento_2}")
