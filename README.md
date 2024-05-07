# Prueba-Técnica-Bia-3

Proyecto creado para realizar el tercer punto de la prueba tecnica para Bia

## Descripción

Proyecto desarrollado con Robot Framework, Appium y Python para el tercer punto de la prueba técnica de Bia

### Dependencias

* Python version 3.0 o superior.
* Windows 10 en adelante.
* Appium instalado y activo en el equipo, con el emulador `uiautomator2`. Sigue las recomendaciones [AQUI](https://appium.io/docs/en/2.1/quickstart/uiauto2-driver/) 
* Android Studio, instalado con un emulador para Andorid que tenga version 13.

### Instalación

1. Clone el repositorio desde GitHub
2. En la consola, en la carpeta raiz del proyecto escriba: `python -m venv .venv` para crear un nuevo **virtual environment**.
3. Vaya a la carpeta scripts en el **virtual environment:** `cd .venv/Scripts`.
4. Active el **virtual environment** escribiendo `.\activate.ps1`. Virtual environment al ser activado, agrega el nombre en parentesis antes de la linea del cursor en la consola asi: 
`(.venv) PS ...`.
5. Salga hacia la carpeta raiz del proyecto usando `cd ..` dos veces.
6. Instale las dependencias escribiendo `pip3 install -r requirements.txt`.
7. Para desactivar el **virtual environment,** vaya de nuevo a la carpeta de scripts (`cd .venv/Scripts`) y luego escriba `.\deactivate.ps1`.

### Ejecución del programa

* Asegurese que el **virtual environment** este activado.
* Cambie en el archivo `ApiDemosTests.py` en la linea 16, parametro `'app'` la ruta local de la imagen .apk
* Escriba en la consola  `robot tests/api_demos_tests.robot` y pulse enter

### Autor

Catherine Rodriguez Cubillos [@crodriguezc1106](https://github.com/crodriguezc1106)

