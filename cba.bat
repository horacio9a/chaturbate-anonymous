@ECHO OFF
SETLOCAL EnableDelayedExpansion
:START
ECHO.
SET /P MODE=EXIT(4) CBR(3) CBM(2) CBFF(1) CB(0)(ENTER)(%MODE%): 
IF "%MODE%"=="" GOTO CB
IF "%MODE%"=="0" GOTO CB
IF "%MODE%"=="1" GOTO CBFF
IF "%MODE%"=="2" GOTO CBM
IF "%MODE%"=="3" GOTO CBR
IF "%MODE%"=="4" GOTO EXIT
:CB
SET MODELNAME=%MODEL% #####################################
SET _MODEL_=%MODELNAME:~0,33%
ECHO.
CLS && ECHO #################################################
ECHO ### CB ######## R E C O R D I N G ###############
ECHO ############### %_MODEL_%
ECHO #################################################
cd C:/
COLOR 0F
cd -cba-py
python cb.py
ECHO.
PAUSE
GOTO START
:CBFF
SET MODELNAME=%MODEL% #####################################
SET _MODEL_=%MODELNAME:~0,33%
ECHO.
CLS && ECHO #################################################
ECHO ### CBFF ###### R E C O R D I N G ###############
ECHO ############### %_MODEL_%
ECHO #################################################
cd C:/
COLOR 0F
cd -cba-py
python cbff.py
ECHO.
PAUSE
GOTO START
:CBM
SET MODELNAME=%MODEL% #####################################
SET _MODEL_=%MODELNAME:~0,33%
ECHO.
CLS && ECHO #################################################
ECHO ### CBM ####### R E C O R D I N G ###############
ECHO ############### %_MODEL_%
ECHO #################################################
cd C:/
COLOR 0F
cd -cba-py
python cbm.py
ECHO.
PAUSE
GOTO START
:CBR
SET n=0
FOR /F "tokens=*" %%A IN (C:/-cba-py/CB_Model.txt) DO (
SET /A n=n+1
SET _fav!n!=%%A
ECHO !n! %%A
)
ECHO.
SET /P MODEL=Choose CB MODEL Name (%M%:%MODEL%): 
FOR /L %%f IN (1,1,!n!) DO (
IF /I '%MODEL%'=='%%f' SET M=%%f
)
SET n=0
FOR /F "tokens=*" %%A IN (C:/-cba-py/CB_Model.txt) DO (
SET /A n=n+1
IF !n!==%M% SET MODEL=%%A
)
ECHO.
SET MODELNAME=%MODEL% #####################################
SET _MODEL_=%MODELNAME:~0,33%
ECHO.
CLS && ECHO #################################################
ECHO ### CB-R ###### R E C O R D I N G ###############
ECHO ############### %_MODEL_%
ECHO #################################################
cd C:/
COLOR 0F
cd -cba-py
python cbr.py %MODEL%
TIMEOUT 5
GOTO CBR
:EXIT
GOTO :EOF
ENDLOCAL
