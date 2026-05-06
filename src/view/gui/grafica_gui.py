import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('Agg')
import io
from kivy.uix.image import Image
from kivy.uix.popup import Popup
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.core.image import Image as CoreImage

def mostrar_grafica(resultado):
    meses = list(range(1, resultado.plazo_simulacion * 12 + 1))
    
    monto_financiado = resultado.valor_inmueble * resultado.porcentaje_LTV
    tasa_mensual = resultado.tasa_capitalizacion / 12
    numero_pagos = resultado.plazo_simulacion * 12
    monto_mensual = (tasa_mensual * monto_financiado) / (1 - (1 + tasa_mensual) ** (-numero_pagos))

    saldos = [monto_financiado * (1 + resultado.tasa_capitalizacion) ** (mes / 12) for mes in meses]
    acumulados = [monto_mensual * mes for mes in meses]

    fig, ax = plt.subplots()
    ax.plot(meses, saldos, color='red', label='Saldo proyectado')
    ax.plot(meses, acumulados, color='green', label='Total acumulado recibido')
    ax.set_title("Hipoteca Inversa: Saldo vs Total recibido")
    ax.set_xlabel("Meses")
    ax.set_ylabel("Valor ($)")
    ax.legend()
    ax.grid(True)

    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)
    plt.close()

    img = CoreImage(buf, ext='png')
    imagen_widget = Image()
    imagen_widget.texture = img.texture

    explicacion = Label(text=(
        "Rojo: Saldo proyectado (lo que debes al banco, crece exponencialmente por interés compuesto)\n"
        "Verde: Total acumulado recibido (lo que recibes mes a mes, crece linealmente)\n"
        "La diferencia entre ambas líneas representa la ganancia del banco."
    ), opacity=0)

    contenido = GridLayout(cols=1)
    contenido.add_widget(imagen_widget)

    def toggle_explicacion(instance):
        if explicacion.opacity == 0:
            explicacion.opacity = 1
            instance.text = "Ocultar explicación"
        else:
            explicacion.opacity = 0
            instance.text = "Ver explicación"

    btn_explicacion = Button(text="Ver explicación", size_hint=(1, 0.1))
    btn_explicacion.bind(on_press=toggle_explicacion)

    contenido.add_widget(btn_explicacion)
    contenido.add_widget(explicacion)

    cerrar = Button(text="Cerrar", size_hint=(1, 0.1))
    contenido.add_widget(cerrar)

    popup = Popup(title="Gráfica de Hipoteca Inversa", content=contenido, size_hint=(0.9, 0.9))
    cerrar.bind(on_press=popup.dismiss)
    popup.open()