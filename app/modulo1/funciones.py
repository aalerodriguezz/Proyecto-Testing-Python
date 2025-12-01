import unicodedata

def esPalindromo(cadena):

    # 1. Protección contra tipos nulos o incorrectos
    if cadena is None:
        return False
    
    # 2. Permitir números tratándolos como texto
    if isinstance(cadena, (int, float)):
        cadena = str(cadena)
        
    # 3. Si no es texto ni número, rechazar (Fail-safe)
    if not isinstance(cadena, str):
        return False

    # 4. Normalización Unicode (NFD separa la letra de la tilde: 'á' -> 'a' + '´')
    # Esto permite filtrar los caracteres que no son letras base.
    cadena_normalizada = unicodedata.normalize('NFD', cadena)
    
    # 5. Filtrado: Solo letras y números, y todo a minúsculas
    # unicodedata.category(c) != 'Mn' elimina las marcas de acentos
    limpia = ''.join(
        c.lower() for c in cadena_normalizada
        if unicodedata.category(c) != 'Mn' and c.isalnum()
    )

    # 6. Comparación (Pythonic slicing)
    return limpia == limpia[::-1]
