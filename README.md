# CALCULADORA-DE-HIPOTECA-INVERSA
Sus colaboradores son: EMANUELA BENTANCUR E ISABELLA QUINTERO GUTIERREZ, clase de codigo limpio grupo 64

Los encargados de hacer la interfaz son: SEBASTIAN RENDON y CESAR VELASQUEZ, codigo limpio grupo 64


# Proyecto — Simulador de Hipoteca Inversa

##  Descripción del proyecto

Este proyecto consiste en el desarrollo de un modelo de simulación financiera que permite calcular los pagos periódicos que recibiría un propietario al contratar una hipoteca inversa en Colombia. El programa toma como base el valor del inmueble, la tasa de interés, el plazo y el porcentaje del valor que la entidad financiera está dispuesta a otorgar (LTV).

El objetivo principal es analizar cómo varían los pagos y el comportamiento de la deuda según distintos escenarios financieros, permitiendo evaluar la viabilidad del producto tanto desde el punto de vista del cliente como de la entidad prestamista.

---

##  ¿Qué es una hipoteca inversa?

Una hipoteca inversa es un producto financiero dirigido principalmente a personas adultas mayores que poseen una vivienda propia. A diferencia de una hipoteca tradicional, en lugar de que el propietario pague cuotas al banco, es el banco quien le paga al propietario una renta periódica usando el inmueble como garantía.

El préstamo se liquida cuando:

* el titular fallece,
* vende la vivienda,
* o deja de cumplir condiciones del contrato.

La deuda acumulada corresponde a los pagos recibidos más los intereses generados durante el tiempo del contrato.

---

##  Requisitos generales para aplicar

Aunque pueden variar según la entidad financiera, normalmente se exigen condiciones como:

* Ser propietario de un inmueble libre de gravámenes.
* Tener una edad mínima (usualmente mayor a 65 años).
* Que el inmueble tenga un avalúo comercial válido.
* Aceptar que el monto prestado será solo un porcentaje del valor del inmueble.
* Mantener el inmueble en buen estado y asegurado.

El porcentaje prestable nunca es el 100% del valor del inmueble, ya que el banco debe cubrir riesgos financieros, intereses acumulados y posibles variaciones del valor de la propiedad.

---

## Objetivo del modelo en Excel

El archivo Excel funciona como un simulador financiero que permite:

* calcular el monto máximo prestable,
* estimar el pago periódico que recibiría el cliente,
* analizar distintos escenarios cambiando variables de entrada,
* observar el impacto del tiempo y la tasa de interés en la deuda.

Este tipo de simulación es útil para comprender el comportamiento matemático de una hipoteca inversa antes de implementarla en un sistema real.

---

##  Qué se está calculando

El modelo calcula principalmente:

* el monto del préstamo inicial basado en el valor del inmueble,
* el pago periódico que el banco entregaría al cliente,
* el crecimiento de la deuda en el tiempo debido a los intereses.

El cálculo central corresponde a una fórmula financiera de anualidad, que determina el valor de los pagos periódicos en función de una tasa de interés y un número de periodos.

---

## Variables de entrada

Las variables que el usuario puede modificar son:

* **Valor del inmueble:** precio comercial estimado de la vivienda.
* **Porcentaje prestable (LTV):** proporción del valor del inmueble que la entidad acepta financiar.
* **Tasa de interés:** costo financiero aplicado al préstamo.
* **Plazo:** duración del contrato en años o periodos.
* **Frecuencia de pago:** periodicidad con la que se entregan los pagos (mensual, anual, etc.).

Estas variables determinan directamente el monto del pago y el comportamiento de la deuda.

---

## Variables de salida

El modelo genera como resultados:

* monto del préstamo otorgado,
* valor del pago periódico,
* evolución de la deuda en el tiempo,
* total acumulado pagado al beneficiario.

Estos resultados permiten evaluar si el producto es sostenible financieramente.

---

##  Operación matemática utilizada

El cálculo principal se basa en la fórmula de anualidades financieras:

Pago = (PV × r) / (1 − (1 + r)^(-n))

donde:

* **PV** es el valor presente del préstamo,
* **r** es la tasa de interés periódica,
* **n** es el número total de periodos.

Esta fórmula permite determinar cuánto dinero puede recibir el propietario periódicamente sin que el préstamo exceda el valor permitido del inmueble.

---

## Importancia del porcentaje prestable (LTV)

El porcentaje prestable es una variable crítica del modelo. Representa el nivel de riesgo que la entidad financiera está dispuesta a asumir.

Un porcentaje alto genera pagos mayores pero incrementa el riesgo de que la deuda final supere el valor del inmueble. Por esta razón, en la práctica los valores utilizados suelen ser moderados y dependen de factores como la edad del solicitante, la expectativa de vida y el comportamiento del mercado inmobiliario.



El simulador desarrollado demuestra cómo un modelo matemático puede representar el funcionamiento real de un producto financiero complejo. Además, evidencia que el diseño de una hipoteca inversa requiere equilibrar tres factores principales:

* beneficio para el cliente,
* sostenibilidad financiera para la entidad,
* control del riesgo.

---
##  Justificación del porcentaje prestable menor al 100%

En una hipoteca inversa el porcentaje prestable (LTV) no puede ser del 100% del valor del inmueble, incluso si el propietario entrega su vivienda como garantía total. Esto se debe a razones financieras y actuariales fundamentales:

**1. Riesgo de longevidad**
La entidad financiera no puede predecir con exactitud cuánto tiempo vivirá el beneficiario. Si el cliente vive más de lo estimado, el banco deberá seguir pagando las rentas mientras la deuda continúa creciendo.

**2. Acumulación de intereses**
A diferencia de un préstamo tradicional, en la hipoteca inversa la deuda aumenta con el tiempo porque los intereses se capitalizan. Si se prestara el 100% del valor del inmueble desde el inicio, la deuda superaría rápidamente el valor de la vivienda.

**3. Protección del prestamista**
El valor del inmueble debe cubrir no solo el capital prestado, sino también:

* intereses acumulados,
* costos administrativos,
* riesgo financiero,
* posibles variaciones del mercado inmobiliario.

**4. Práctica financiera real**
En productos reales de hipoteca inversa, el porcentaje prestable suele oscilar aproximadamente entre 20% y 60% del valor del inmueble, dependiendo principalmente de la edad del solicitante. Personas de mayor edad suelen acceder a porcentajes más altos porque el riesgo temporal es menor.

El uso de un LTV inferior al 100% no es una limitación del modelo, sino una condición necesaria para que el producto financiero sea viable y sostenible. Por esta razón, el simulador implementado utiliza porcentajes moderados que reflejan escenarios realistas del mercado.

---
# Instrucciones Para ejecutar el programa sin necesidad de usar el Visual Studio Code

Para ejecutar el programa en Windows, primero es necesario clonar el repositorio en tu computadora. Puedes hacerlo abriendo una terminal (como CMD, PowerShell o Git Bash) y ejecutando el comando correspondiente para clonar el repositorio. Una vez finalizado este proceso, se descargará una carpeta que contiene todos los archivos del proyecto.

Después, debes ubicarte dentro de la carpeta del proyecto. Una forma sencilla de hacerlo es haciendo clic derecho dentro de la carpeta y seleccionando la opción “Abrir en Terminal”, lo que abrirá automáticamente la terminal en la ubicación correcta.

Con la terminal abierta en la carpeta del proyecto, el siguiente paso es ejecutar el programa. Para ello, debes ingresar el comando: 
- `py src/view/consola_hipoteca_inversa.py`

y presionar Enter. Esto iniciará la consola interactiva del programa.

En caso de que el sistema no reconozca el termino py, ingresar el siguiente comando: 
- `python src/view/consola_hipoteca_inversa.py.`

Una vez que el programa esté en ejecución, comenzará a solicitar diferentes datos. Solo debes seguir las instrucciones que aparecen en pantalla, ingresar la información requerida y presionar Enter después de cada dato. El programa te permitirá interactuar con distintas opciones y probar diferentes valores según lo necesites.

Como recomendación final, asegúrate de tener Python correctamente instalado y configurado en tu sistema, de modo que el comando py funcione sin inconvenientes.

# Ejecutar pruebas

Desde la raíz del proyecto, ejecuta:

- ``py test/test_calculadora_hipoteca_comentado.py``

En caso de que el sistema no reconozca el termino py, ingresar el siguiente comando: 
- `python test/test_calculadora_hipoteca_comentado.py`

---


## Estructura

```
CALCULADORA-DE-HIPOTECA-INVERSA/
│
├── src/
│   └── model/
│   │   └── logica_calculohipoteca_comentado.py
│   │
│   └── view/
│       ├── consola_hipoteca_inversa.py
│       └── gui/
│           ├── hipoteca_inversa_gui.py
│           └── grafica_gui.py
│
├── test/
│   └── test_calculadora_hipoteca_comentado.py
│
└── README.md

```
---
## Instrucciones para ejecutar la interfaz gráfica (GUI)

### Requisitos
- Python 3.x
- Kivy

### Instalación de dependencias
```bash
pip install kivy
```
```bash
pip install matplotlib
```
### Ejecución
Abre la terminal en la carpeta raíz del proyecto. Puedes verificar que estás en la carpeta correcta porque la terminal muestra:

```bash
" PS C:...\CALCULADORA-DE-HIPOTECA-INVERSA> "
```

Si no estás ahí, navega con:
```bash
cd CALCULADORA-DE-HIPOTECA-INVERSA
```
Luego ejecuta:
```bash
python src/view/gui/hipoteca_inversa_gui.py
```
