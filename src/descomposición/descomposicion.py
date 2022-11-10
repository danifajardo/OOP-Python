
class Automovil:

    def __init__ (self, modelo, marca, color):
        self.modelo = modelo
        self.marca = marca
        self.color = color
        self._estado = "En reposo"
        self._motor = Motor(cilindros=4)
        self._indicadores = Indicadores(self._motor, False, False)
    
    def acelerar(self, tipo='despacio'):

        if (self._indicadores.mostrarIndicadorGasolina()):
            if (tipo == 'rapido'):
                self._motor.inyecta_gasolina(10)
            else:
                self._motor.inyecta_gasolina(3)
        
            self._estado = 'en movimiento'
        else: 
            self._estado = 'en reposo'
    
    def mostrarEstadoAutomovil(self):

        return self._estado

class Motor:

    def __init__ (self, cilindros, tipo='gasolina'):
        self.cilindros = cilindros
        self.tipo = tipo 
        self._temperatura = 0
        self._nivel_gasolina = 10
    
    def inyecta_gasolina(self, cantidad):

        self._nivel_gasolina -= cantidad 

class Indicadores:

    def __init__ (self, motor:Motor, freno_mano:bool, puertas_abiertas:bool):
        self._motor = motor
        self.freno_mano = freno_mano
        self.puertas_abiertas = puertas_abiertas
    
    def mostrarIndicadorGasolina(self):
        return self._motor._nivel_gasolina

if __name__ == "__main__":

    miAuto = Automovil('Tesla S', 'Telsa', 'Rojo')
    print(miAuto.mostrarEstadoAutomovil())
    miAuto.acelerar(tipo="rapido")
    print(miAuto.mostrarEstadoAutomovil())    