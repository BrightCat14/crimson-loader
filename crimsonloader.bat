@Echo off
chcp 65001
setlocal
set APPDATA_FOLDER=%APPDATA%\crimsonloader

set settingstyle=default

cls

:Start
cls
echo.
echo     [41mCrimson Loader[0m
echo    1 - Show Mods
echo    2 - Settings
echo DEBUG : "%APPDATA_FOLDER%"
echo.

:: Display the prompt based on the current settingstyle
if "%settingstyle%"=="kali" (
    set /p input=[94m%username%[0m@[92m%computername% $[0m 
) else (
    set /p input=Выбор :
)

:: Handle the input for the main menu
if "%input%"=="2" (
    goto settings
) else if "%input%"=="1" (
    goto modmenu
) else (
    goto Start
)

:modmenu
cls
cls
echo.
echo     [41mCrimson Loader[0m
echo    1 - AimStar
echo    2 - Tkazer
echo    x - Exit to menu
echo.

if "%settingstyle%"=="kali" (
    set /p cheatchoose=[94m%username%[0m@[92m%computername% $$[0m 
) else if "%settingstyle%"=="default" (
    set /p cheatchoose=Выбор :
)

if "%cheatchoose%"=="1" (
    if not exist "%APPDATA%\crimsonloader" mkdir "%APPDATA%\crimsonloader"

    curl -L -o "%APPDATA%\crimsonloader\AimStar.zip" https://github.com/CowNowK/AimStar/releases/download/v4.5.0/AimStar_4.5.0.zip

    start "cmd" powershell -windowstyle hidden -command "Expand-Archive -Path '%APPDATA%\crimsonloader\AimStar.zip' -DestinationPath '%APPDATA%\crimsonloader' -Force"

    :check_cs2
    tasklist /FI "IMAGENAME eq cs2.exe" 2>NUL | find /I "cs2.exe" >NUL
    if not errorlevel 1 (
        timeout 4 /nobreak
        echo Процесс cs2.exe найден. Запускаем AimStar.
        start "" "%APPDATA%\crimsonloader\AimStar.exe"
    ) else (
        echo Процесс cs2.exe не найден. Запускаем КС.
        start "" "steam://rungameid/730"
        timeout 10 /nobreak >nul
        goto check_cs2
    )

) else if "%cheatchoose%"=="2" (
    if not exist "%APPDATA%\crimsonloader" mkdir "%APPDATA%\crimsonloader"

    curl -L -o "%APPDATA%\crimsonloader\Tkazer.exe" https://github.com/BrightCat14/crimson-loader/releases/download/fordownloadtkazer/TKazerAimStar_TKazer.exe

    :check_cs2_tkazer
    tasklist /FI "IMAGENAME eq cs2.exe" 2>NUL | find /I "cs2.exe" >NUL
    if not errorlevel 1 (
        timeout 4 /nobreak
        echo Процесс cs2.exe найден. Запускаем Tkazer.
        start "" "%APPDATA%\crimsonloader\Tkazer.exe"
    ) else (
        echo Процесс cs2.exe не найден. Запускаем КС.
        start "" "steam://rungameid/730"
        timeout 10 /nobreak >nul
        goto check_cs2_tkazer
    )

) else if "%cheatchoose%"=="x" (
goto Start
) else (
    goto modmenu
)

goto Start

:settings
cls
echo.
echo     [41mCrimson Loader[0m
echo    1 - Style Settings
echo.

:: Display the prompt based on the current settingstyle
if "%settingstyle%"=="kali" (
    set /p settingoption=[94m%username%[0m@[92m%computername% $[0m 
) else (
    set /p settingoption=Выбор :
)

:: Handle the input for the settings menu
if "%settingoption%"=="1" (
    goto styleoptions
) else (
    goto settings
)

:styleoptions
cls
echo.
echo     [41mCrimson Loader[0m
echo    1 - Kali Style
echo    2 - Default Style
echo.

:: Display the prompt based on the current settingstyle
if "%settingstyle%"=="kali" (
    set /p styleoption=[94m%username%[0m@[92m%computername% $[0m 
) else if "%settingstyle%"=="default" (
    set /p styleoption=Выбор :
)

:: Handle the input for the style options
if "%styleoption%"=="1" (
    set settingstyle=kali
    goto Start
) else if "%styleoption%"=="2" (
    set settingstyle=default
    goto Start
) else (
    goto styleoptions
)

pause
