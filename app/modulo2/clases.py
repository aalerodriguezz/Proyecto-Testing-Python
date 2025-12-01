class GestorResultados:
    
    def __init__(self):
        self.historial = []

    def guardar_resultado(self, frase, resultado):
        self.historial.append({'frase': frase, 'es_palindromo': resultado})
