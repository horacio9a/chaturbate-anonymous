@ECHO OFF
SETLOCAL EnableDelayedExpansion
:START
CLS
ECHO.
CLS && ECHO ###################################################################################
ECHO ###   C H A T U R B A T E   A N O N Y M O U S   P Y T H O N   2   S C R I P T   ###
ECHO ###################################################################################
ECHO.
SET /P MODE=EXIT(6) CBYTR(5) CBSLR(4) CBFFR(3) CB(2) GETOW(1) GETOA(0)(ENTER)(%MODE%): 
IF "%MODE%"=="" GOTO GETOA
IF "%MODE%"=="0" GOTO GETOA
IF "%MODE%"=="1" GOTO GETOW
IF "%MODE%"=="2" GOTO CB
IF "%MODE%"=="3" GOTO CBFFR
IF "%MODE%"=="4" GOTO CBSLR
IF "%MODE%"=="5" GOTO CBYTR
IF "%MODE%"=="6" GOTO EXIT
:GETOA
ECHO.
CLS && ECHO ##################################################
ECHO ### GETOA ###  O N L I N E   A L L   L I S T  ####
ECHO ##################################################
cd C:/
COLOR 0F
cd -cba-py
python getOnlineAllModels.py > CB_Online_All.txt
ECHO.
PAUSE
GOTO START
:GETOW
ECHO.
CLS && ECHO ########################################################
ECHO ### GETOW ###  O N L I N E   W A N T E D   L I S T  ####
ECHO ########################################################
cd C:/
COLOR 0F
cd -cba-py
python getOnlineWantedModels.py > CB_Online_Wanted.txt
ECHO.
PAUSE
GOTO START
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
:CBFFR
SET n=0
FOR /F "tokens=*" %%A IN (C:/-cba-py/CB_Wanted.txt) DO (
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
FOR /F "tokens=*" %%A IN (C:/-cba-py/CB_Wanted.txt) DO (
SET /A n=n+1
IF !n!==%M% SET MODEL=%%A
)
ECHO.
SET MODELNAME=%MODEL% #####################################
SET _MODEL_=%MODELNAME:~0,34%
:CBFFR_
ECHO.
CLS && ECHO #################################################
ECHO ### CBFFR #### R E C O R D I N G ################
ECHO ############## %_MODEL_%
ECHO #################################################
cd C:/
COLOR 0F
cd -cba-py
python cbffr.py %MODEL%
TIMEOUT 30
GOTO CBFFR_
:CBYTR
SET n=0
FOR /F "tokens=*" %%A IN (C:/-cba-py/CB_Wanted.txt) DO (
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
FOR /F "tokens=*" %%A IN (C:/-cba-py/CB_Wanted.txt) DO (
SET /A n=n+1
IF !n!==%M% SET MODEL=%%A
)
ECHO.
SET MODELNAME=%MODEL% #####################################
SET _MODEL_=%MODELNAME:~0,34%
:CBYTR_
ECHO.
CLS && ECHO #################################################
ECHO ### CBYTR #### R E C O R D I N G ################
ECHO ############## %_MODEL_%
ECHO #################################################
cd C:/
COLOR 0F
cd -cba-py
python cbytr.py %MODEL%
TIMEOUT 30
GOTO CBYTR_
:CBSLR
SET n=0
FOR /F "tokens=*" %%A IN (C:/-cba-py/CB_Wanted.txt) DO (
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
FOR /F "tokens=*" %%A IN (C:/-cba-py/CB_Wanted.txt) DO (
SET /A n=n+1
IF !n!==%M% SET MODEL=%%A
)
ECHO.
SET MODELNAME=%MODEL% #####################################
SET _MODEL_=%MODELNAME:~0,34%
:CBSLR_
ECHO.
CLS && ECHO #################################################
ECHO ### CBSLR #### R E C O R D I N G ################
ECHO ############## %_MODEL_%
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
