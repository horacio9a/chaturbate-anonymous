@ECHO OFF
SETLOCAL EnableDelayedExpansion
:START
CLS
ECHO.
SET /P MODE=EXIT(6) CBSLR(5) CBYTR(4) CBR(3) CBSL(2) CBYT(1) CB(0)(ENTER)(%MODE%): 
IF "%MODE%"=="" GOTO CB
IF "%MODE%"=="0" GOTO CB
IF "%MODE%"=="1" GOTO CBYT
IF "%MODE%"=="2" GOTO CBSL
IF "%MODE%"=="3" GOTO CBR
IF "%MODE%"=="4" GOTO CBYTR
IF "%MODE%"=="5" GOTO CBSLR
IF "%MODE%"=="6" GOTO EXIT
:CB
ECHO.
CLS && ECHO #################################################
ECHO ### CB ######## R E C O R D I N G ###############
ECHO #################################################
cd C:/
COLOR 0F
cd -cba-py
python cb.py
ECHO.
PAUSE
GOTO START
:CBYT
ECHO.
CLS && ECHO #################################################
ECHO ### CBYT ###### R E C O R D I N G ###############
ECHO #################################################
cd C:/
COLOR 0F
cd -cba-py
python cbyt.py
ECHO.
PAUSE
GOTO START
:CBSL
ECHO.
CLS && ECHO #################################################
ECHO ### CBSL ###### R E C O R D I N G ###############
ECHO #################################################
cd C:/
COLOR 0F
cd -cba-py
python cbsl.py
ECHO.
PAUSE
GOTO START
:CBR
SET n=0
FOR /F "tokens=*" %%A IN (C:/Windows/CB_Model.txt) DO (
SET /A n=n+1
SET _fav!n!=%%A
ECHO !n! %%A
)
ECHO.
SET /P MODEL=Choose CB Model Name (%M%): 
FOR /L %%f IN (1,1,!n!) DO (
IF /I '%MODEL%'=='%%f' SET M=%%f
)
SET n=0
FOR /F "tokens=*" %%A IN (C:/Windows/CB_Model.txt) DO (
SET /A n=n+1
IF !n!==%M% SET MODEL=%%A
)
:CBR_
ECHO.
SET MODELNAME=%MODEL% #####################################
SET _MODEL_=%MODELNAME:~0,33%
ECHO.
CLS && ECHO #################################################
ECHO ### CBR ####### R E C O R D I N G ###############
ECHO ############### %_MODEL_%
ECHO #################################################
cd C:/
COLOR 0F
cd -cba-py
python cbr.py %MODEL%
TIMEOUT 30
GOTO CBR_
:CBYTR
SET n=0
FOR /F "tokens=*" %%A IN (C:/Windows/CB_Model.txt) DO (
SET /A n=n+1
SET _fav!n!=%%A
ECHO !n! %%A
)
ECHO.
SET /P MODEL=Choose CB Model Name (%M%): 
FOR /L %%f IN (1,1,!n!) DO (
IF /I '%MODEL%'=='%%f' SET M=%%f
)
SET n=0
FOR /F "tokens=*" %%A IN (C:/Windows/CB_Model.txt) DO (
SET /A n=n+1
IF !n!==%M% SET MODEL=%%A
)
ECHO.
SET MODELNAME=%MODEL% #####################################
SET _MODEL_=%MODELNAME:~0,33%
:CBYTR_
ECHO.
CLS && ECHO #################################################
ECHO ### CBYTR ##### R E C O R D I N G ###############
ECHO ############### %_MODEL_%
ECHO #################################################
cd C:/
COLOR 0F
cd -cba-py
python cbytr.py %MODEL%
TIMEOUT 30
GOTO CBYTR_
:CBSLR
SET n=0
FOR /F "tokens=*" %%A IN (C:/Windows/CB_Model.txt) DO (
SET /A n=n+1
SET _fav!n!=%%A
ECHO !n! %%A
)
ECHO.
SET /P MODEL=Choose CB Model Name (%M%): 
FOR /L %%f IN (1,1,!n!) DO (
IF /I '%MODEL%'=='%%f' SET M=%%f
)
SET n=0
FOR /F "tokens=*" %%A IN (C:/Windows/CB_Model.txt) DO (
SET /A n=n+1
IF !n!==%M% SET MODEL=%%A
)
ECHO.
SET MODELNAME=%MODEL% #####################################
SET _MODEL_=%MODELNAME:~0,33%
:CBSLR_
ECHO.
CLS && ECHO #################################################
ECHO ### CBSLR ##### R E C O R D I N G ###############
ECHO ############### %_MODEL_%
ECHO #################################################
cd C:/
COLOR 0F
cd -cba-py
python cbslr.py %MODEL%
TIMEOUT 30
GOTO CBSLR_
:EXIT
GOTO :EOF
ENDLOCAL
