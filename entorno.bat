@echo off
echo Creando entorno virtual...
python -m venv venv

echo Activando entorno virtual...
call venv\Scripts\activate

echo Instalando dependencias...
pip install -r requirements.txt

echo Entorno configurado y activado. Puedes ejecutar el proyecto ahora.
pause