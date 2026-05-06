import sys
sys.path.append("src")
from model.logica_calculohipoteca_comentado import credito, calculadora_hipoteca_inversa

from view.gui.grafica_gui import mostrar_grafica

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.popup import Popup

class HipotecaInversaGUI(App):
    def build(self):

        self.title = "Calculadora de Hipoteca Inversa"

        layout = GridLayout(cols=2)
        # Campos de entrada
        self.valor_vivienda_input = TextInput(hint_text="Valor de la vivienda")
        self.tasa_interes_input = TextInput(hint_text=("Tasa de interés anual (%)"))
        self.plazo_input = TextInput(hint_text="Plazo del crédito (años)")
        self.edad_input = TextInput(hint_text="Edad del propietario")
        self.porcentaje_LTV_input = TextInput(hint_text="Porcentaje LTV (%)")

        calcular_button = Button(text="Calcular")
        calcular_button.bind(on_press=self.calcular)

        grafica_button = Button(text='Ver gráfica')
        grafica_button.bind(on_press=self.ver_grafica)


        self.resultado_monto_mensual = Label(text="La cuota mensual aparecerá aquí", color=(0, 1, 0, 1))

        self.resultado_total_acumulado = Label(text="El total acumulado aparecerá aquí", color=(0, 1, 0, 1))

        self.resultado_saldo_proyectado = Label(text="El saldo proyectado aparecerá aquí", color=(0, 1, 0, 1))

        layout.add_widget(Label(text="Valor de la vivienda:"))
        layout.add_widget(self.valor_vivienda_input)

        layout.add_widget(Label(text="Tasa de interés anual (%):"))
        layout.add_widget(self.tasa_interes_input)

        layout.add_widget(Label(text="Plazo del crédito (años):"))
        layout.add_widget(self.plazo_input)

        layout.add_widget(Label(text="Porcentaje LTV (%):"))
        layout.add_widget(self.porcentaje_LTV_input)

        layout.add_widget(Label(text="Edad del propietario:"))
        layout.add_widget(self.edad_input)

        

        layout.add_widget(Label(text="Cuota mensual:"))
        layout.add_widget(self.resultado_monto_mensual)
        layout.add_widget(Label(text="Total acumulado:"))
        layout.add_widget(self.resultado_total_acumulado)
        layout.add_widget(Label(text="Saldo proyectado:"))
        layout.add_widget(self.resultado_saldo_proyectado)


        layout.add_widget(calcular_button)

        descripcion = Label(text=(
        "Esta aplicacion le permite calcular la hipoteca inversa,\n"
        "ingresando el valor de la vivienda, la tasa de interés anual, el plazo del crédito, el porcentaje\n"
        "LTV y la edad del propietario. Al hacer clic en 'Calcular', se mostrarán la cuota mensual,\n"
        "el total acumulado y el saldo proyectado."), size_hint_y=2, size_hint_x=2, text_size=(400, None),halign='left')


        layout.add_widget(descripcion)
        layout.add_widget(grafica_button)   
        layout.add_widget(Label(text=""))


        return layout
    
    def calcular(self, sender):
        # Obtener los datos ingresados por el usuario y realizar los cálculos correspondientes
        # utilizando la lógica de la calculadora de hipoteca inversa. Luego, actualizar las 
        # etiquetas de resultado con los valores calculados.

        try:
            self.validar()

            print("Se realizaron los respectivos calculos")

            valor_inmueble = int(self.valor_vivienda_input.text)
            tasa_capitalizacion = float(self.tasa_interes_input.text)
            plazo_simulacion = int(self.plazo_input.text)
            porcentaje_LTV = float(self.porcentaje_LTV_input.text)
            edad = int(self.edad_input.text)
            resultado = credito(valor_inmueble=valor_inmueble, tasa_capitalizacion=tasa_capitalizacion, plazo_simulacion=plazo_simulacion, porcentaje_LTV=porcentaje_LTV, edad=edad)


            result_monto_mensual = calculadora_hipoteca_inversa.calcular_monto_mensual_recibido(resultado)
            result_total_recibido = calculadora_hipoteca_inversa.calcular_total_recibido_acumulado(resultado)
            result_saldo_proyectado = calculadora_hipoteca_inversa.calcular_saldo_proyectado(resultado)
        
            self.resultado_monto_mensual.text = f"${result_monto_mensual:.0f}"
            self.resultado_total_acumulado.text = f"${result_total_recibido:.0f}"
            self.resultado_saldo_proyectado.text = f"${result_saldo_proyectado:.0f}"

            print(f"El monto mensual recibido es: {result_monto_mensual}")
            print(f"El total recibido acumulado es: {result_total_recibido}")
            print(f"El saldo proyectado es: {result_saldo_proyectado}")

        except Exception as e:
            print("Ocurrió un error al realizar los cálculos. Por favor, revise los datos ingresados.")
            self.mostrar_error( "Error al calcular la hipoteca inversa. \n" + str(e) + "\nPor favor, revise los datos ingresados.")
            print(f"Error: {e}")

    def mostrar_error(self, err):
        """
        Abre una ventana emergente, con un texto y un botón para cerrar
        Parámetros:
        err: Mensaje de error que queremos mostrar en la ventana
        """

        # contenido es el contenedor donde vamos a agregar los widgets de la ventana
        contenido = GridLayout(cols=1)
        # Creamos el Label que contiene el mensaje de error
        contenido.add_widget(Label(text=str(err)))
        # Creamos el botón para cerrar la ventana
        cerrar = Button(text="Cerrar")
        contenido.add_widget(cerrar)
        # Creamos la ventana emergente con el widget Popup de Kivy
        popup = Popup(title="Error", content=contenido)
        # Conectamos el evento del botón con el método dismiss que cierra el popup
        cerrar.bind(on_press=popup.dismiss)
        # Mostramos la ventana emergente
        popup.open()   
    
    def validar(self):
        """
        Verifica que todos los datos ingresados por el usuario sean correctos
        """
        if not self.valor_vivienda_input.text.isnumeric():
            raise Exception("El valor de la vivienda debe ser un número válido, no se permiten caracteres especiales ni letras")
    
        if not self.tasa_interes_input.text.isnumeric():
            raise Exception("La tasa de interés debe ser un número válido, sin signo de porcentaje, no se permiten caracteres especiales ni letras.")
    
        if not self.plazo_input.text.isnumeric():
            raise Exception("El plazo del crédito debe ser un número válido, no se permiten caracteres especiales ni letras.")
        
        if not self.porcentaje_LTV_input.text.isnumeric():
            raise Exception("El porcentaje LTV debe ser un número válido, no se permiten caracteres especiales ni letras.")
    
        if not self.edad_input.text.isnumeric():
            raise Exception("La edad del propietario debe ser un número válido, no se permiten caracteres especiales ni letras.")

    def ver_grafica(self, sender):
        try:
            self.validar()
            valor_inmueble = int(self.valor_vivienda_input.text)
            tasa_capitalizacion = float(self.tasa_interes_input.text)
            plazo_simulacion = int(self.plazo_input.text)
            porcentaje_LTV = float(self.porcentaje_LTV_input.text)
            edad = int(self.edad_input.text)
            resultado = credito(valor_inmueble=valor_inmueble, tasa_capitalizacion=tasa_capitalizacion, 
                           plazo_simulacion=plazo_simulacion, porcentaje_LTV=porcentaje_LTV, edad=edad)
            mostrar_grafica(resultado)
        except Exception as e:
            self.mostrar_error(str(e))


if __name__ == '__main__':
    HipotecaInversaGUI().run()