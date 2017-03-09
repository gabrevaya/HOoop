"""
Un generador de senal es el responsable de generar una senal portadora.

"""

class Generador(object):

    def __init__(self, amplitud, fase, frecuencia):
        self.amplitud = amplitud
        self.fase = fase
        self.frecuencia = frecuencia

        #  muestras por segundo
        self.frecuencia_muestreo = frecuencia*3


    def generar(self, tiempo_inicial, tiempo_final):

        import math

        cantidad_muestras = int(((tiempo_final - tiempo_inicial).seconds/\
        self.frecuencia_muestreo))

        muestras = range(cantidad_muestras)

        ret = [self.amplitud*math.sin(2*(1/self.frecuencia)*i+self.fase) \
        for i in muestras]
            
        # agrego ruido blanco ruido blanco
        mean = 0
        std = 0.01
        ruido = np.random.normal(mean, std, size=cantidad_muestras)

        return ret+ruido
