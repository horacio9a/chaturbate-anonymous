@ECHO OFF
SETLOCAL EnableDelayedExpansion
:START
CLS
ECHO.
SET /P MODE=EXIT(6) CHAT(5) CBFFRTS(4) CBFFR(3) CBR(2) CBFF(1) CB(0)(ENTER)(%MODE%): 
IF "%MODE%"=="" GOTO CB
IF "%MODE%"=="0" GOTO CB
IF "%MODE%"=="1" GOTO CBFF
IF "%MODE%"=="2" GOTO CBR
IF "%MODE%"=="3" GOTO CBFFR
IF "%MODE%"=="4" GOTO CBFFRTS
IF "%MODE%"=="5" GOTO CHAT
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
:CBFF
ECHO.
CLS && ECHO #################################################
ECHO ### CBFF ###### R E C O R D I N G ###############
ECHO #################################################
cd C:/
COLOR 0F
cd -cba-py
python cbff.py
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
SET /P MODEL=Choose CB MODEL Name (%M%:%MODEL%): 
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
ECHO ### CB-R ###### R E C O R D I N G ###############
ECHO ############### %_MODEL_%
ECHO #################################################
cd C:/
COLOR 0F
cd -cba-py
python cbr.py %MODEL%
TIMEOUT 30
GOTO CBR_
:CBFFR
SET n=0
FOR /F "tokens=*" %%A IN (C:/Windows/CB_Model.txt) DO (
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
FOR /F "tokens=*" %%A IN (C:/Windows/CB_Model.txt) DO (
SET /A n=n+1
IF !n!==%M% SET MODEL=%%A
)
ECHO.
SET MODELNAME=%MODEL% #####################################
SET _MODEL_=%MODELNAME:~0,33%
:CBFFR_
ECHO.
CLS && ECHO #################################################
ECHO ### CBFFR ##### R E C O R D I N G ###############
ECHO ############### %_MODEL_%
ECHO #################################################
cd C:/
COLOR 0F
cd -cba-py
python cbffr.py %MODEL%
TIMEOUT 30
GOTO CBFFR_
:CBFFRTS
SET n=0
FOR /F "tokens=*" %%A IN (C:/Windows/CB_Model.txt) DO (
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
FOR /F "tokens=*" %%A IN (C:/Windows/CB_Model.txt) DO (
SET /A n=n+1
IF !n!==%M% SET MODEL=%%A
)
ECHO.
SET MODELNAME=%MODEL% #####################################
SET _MODEL_=%MODELNAME:~0,33%
:CBFFRTS_
ECHO.
CLS && ECHO #################################################
ECHO ### CBFFRTS ### R E C O R D I N G ###############
ECHO ############### %_MODEL_%
ECHO #################################################
cd C:/
COLOR 0F
cd -cba-py
python cbffrts.py %MODEL%
TIMEOUT 30
GOTO CBFFRTS_
:CHAT
ECHO.
CLS && ECHO #################################################
ECHO ### CHAT ###### R E C O R D I N G ###############
ECHO #################################################
cd C:/
COLOR 0F
cd -chat
python chat.py
ECHO.
PAUSE
GOTO START
:EXIT
GOTO :EOF
ENDLOCAL
