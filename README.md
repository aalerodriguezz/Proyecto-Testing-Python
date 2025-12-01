Actividad de Evaluación sobre Testing en Python 3

Autor: Alejandro Rodriguez

Asignatura: Puesta en Producción Segura

Estado: Finalizado ✅

📋 Descripción de la Actividad

Este proyecto implementa una aplicación robusta en Python 3 para detectar palíndromos (frases que se leen igual al derecho y al revés). El objetivo principal no es solo la funcionalidad, sino la implementación de una suite de Testing Unitario (unittest) exhaustiva que garantice la calidad del software ante entradas inesperadas.

La práctica simula un entorno profesional donde el código debe ser modular, organizado y testeable.

🚀 Estructura del Proyecto

nombre_del_proyecto/
├── app/
│   ├── __init__.py
│   ├── charfun.py           # Script principal de ejecución (Interfaz CLI)
│   ├── modulo1/
│   │   ├── __init__.py
│   │   └── funciones.py     # Lógica de negocio: función esPalindromo()
│   └── modulo2/
│       ├── __init__.py
│       └── clases.py        # Módulo auxiliar (Estructura)
├── tests/
│   ├── __init__.py
│   └── test_modulo1.py      # Suite de pruebas unitarias
├── .gitignore               # Archivos ignorados por Git
├── requirements.txt         # Dependencias del proyecto
└── README.md                # Documentación


🛠️ Instalación y Ejecución en Kali Linux

Clonar o descargar el proyecto:

git clone [https://github.com/tu-usuario/nombre-repo.git](https://github.com/tu-usuario/nombre-repo.git)
cd nombre-repo


Crear entorno virtual (Recomendado):

python3 -m venv venv
source venv/bin/activate


Ejecutar la aplicación:
Puedes ejecutarlo desde la raíz del proyecto:

python3 app/charfun.py


Deberás ver el mensaje de bienvenida con el nombre del autor: Alejandro Rodriguez.

🧪 Cómo Ejecutar los Tests

El proyecto incluye pruebas unitarias que cubren:

Palíndromos simples y complejos.

Frases con tildes, diéresis y signos.

Inyección de tipos incorrectos (None, int, list).

Cadenas vacías.

Para correr las pruebas con detalle (verbosity):

python3 -m unittest tests/test_modulo1.py -v


Ejemplo de salida esperada:

test_cadenas_vacias (tests.test_modulo1.TestPalindromo) ... ok
test_frases_complejas (tests.test_modulo1.TestPalindromo) ... ok
test_numeros (tests.test_modulo1.TestPalindromo) ... ok
...
----------------------------------------------------------------------
Ran 8 tests in 0.001s

OK


👤 Autor

Alejandro Rodriguez Estudiante de Máster en Ciberseguridad.
