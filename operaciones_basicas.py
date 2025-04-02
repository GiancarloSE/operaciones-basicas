"""
Este módulo proporciona dos clases para realizar operaciones matemáticas básicas:
suma, resta y cálculo de promedio.

Clases:
    OperacionesBasicas: Realiza operaciones de suma y resta.
    CalculadoraPromedio: Calcula el promedio de una lista de números.

Uso:
    - La clase `OperacionesBasicas` permite sumar y restar dos números.
    - La clase `CalculadoraPromedio` calcula el promedio de una lista de valores.
"""


class OperacionesBasicas:
    """
    Clase para realizar operaciones aritméticas básicas.

    Atributos:
        resultado (int o float): Almacena el resultado de la última operación.

    Métodos:
        sumar(a, b): Suma dos números y almacena el resultado.
        restar(a, b): Resta dos números y almacena el resultado.
        obtener_resultado(): Retorna el último resultado calculado.
    """

    def __init__(self):
        """Inicializa la clase con un resultado de 0."""
        self.resultado = 0

    def sumar(self, a, b):
        """
        Suma dos números y almacena el resultado.

        Parámetros:
            a (int o float): Primer número.
            b (int o float): Segundo número.
        """
        self.resultado = a + b

    def restar(self, a, b):
        """
        Resta dos números y almacena el resultado.

        Parámetros:
            a (int o float): Primer número.
            b (int o float): Segundo número.
        """
        self.resultado = a - b

    def obtener_resultado(self):
        """
        Retorna el resultado de la última operación realizada.

        Retorna:
            int o float: Último resultado almacenado.
        """
        return self.resultado


# pylint: disable=too-few-public-methods
class CalculadoraPromedio:
    """
    Clase para calcular el promedio de una lista de números.

    Atributos:
        valores (list): Lista de números para calcular el promedio.

    Métodos:
        calcular_promedio(): Calcula y retorna el promedio de los valores proporcionados.
    """

    def __init__(self, valores):
        """
        Inicializa la clase con una lista de valores.

        Parámetros:
            valores (list): Lista de números.
        """
        self.valores = valores

    def calcular_promedio(self):
        """
        Calcula el promedio de los valores almacenados.

        Retorna:
            float: Promedio de los valores.

        Excepciones:
            ZeroDivisionError: Si la lista de valores está vacía.
        """
        if not self.valores:
            raise ZeroDivisionError(
                "La lista de valores está vacía, no se puede calcular el promedio."
            )

        suma = sum(self.valores)
        promedio_calculado = suma / len(self.valores)
        return promedio_calculado


# Variables globales
NUMEROS = [1, 2, 3, 4, 5]
NUM1 = 10
NUM2 = 20

# Ejecución principal
if __name__ == "__main__":
    # Usar la clase OperacionesBasicas
    operaciones = OperacionesBasicas()
    operaciones.sumar(NUM1, NUM2)
    print(
        "El resultado de la suma es: "
        f"{operaciones.obtener_resultado()}"
    )

    operaciones.restar(NUM1, NUM2)
    print(
        "El resultado de la resta es: "
        f"{operaciones.obtener_resultado()}"
    )

    # Usar la clase CalculadoraPromedio
    calculadora_promedio = CalculadoraPromedio(NUMEROS)
    promedio_general = calculadora_promedio.calcular_promedio()
    print(
        "El promedio de los números es: "
        f"{promedio_general}"
    )
