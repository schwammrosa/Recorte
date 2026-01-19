@echo off
echo ========================================
echo  Image Splitter - Divisor de Imagens
echo ========================================
echo.
echo Verificando instalacao do Python...
python --version
if errorlevel 1 (
    echo.
    echo [ERRO] Python nao encontrado!
    echo Por favor, instale o Python 3.7 ou superior.
    pause
    exit /b 1
)

echo.
echo Verificando dependencias...
python -m pip show Pillow >nul 2>&1
if errorlevel 1 (
    echo.
    echo Pillow nao encontrado. Instalando...
    python -m pip install Pillow
    if errorlevel 1 (
        echo.
        echo [ERRO] Falha ao instalar Pillow.
        pause
        exit /b 1
    )
)

echo.
echo Iniciando aplicacao...
echo.
python image_splitter.py

if errorlevel 1 (
    echo.
    echo [ERRO] Ocorreu um erro ao executar a aplicacao.
    pause
    exit /b 1
)

echo.
echo Aplicacao encerrada.
pause
