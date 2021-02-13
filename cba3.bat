@ECHO OFF
SETLOCAL EnableDelayedExpansion
:START
CLS
ECHO.
CLS && ECHO ###################################################################################
ECHO ###   C H A T U R B A T E   A N O N Y M O U S   P Y T H O N   3   S C R I P T   ###
ECHO ###################################################################################
ECHO.
SET /P MODE=EXIT(6)  CBYTR3(5)  CBSLR3(4)  CBFFR3(3)  CB3(2)  GETOW3(1)  GETOA3(0)(ENTER)(%MODE%): 
IF "%MODE%"=="" GOTO GETOA3
IF "%MODE%"=="0" GOTO GETOA3
IF "%MODE%"=="1" GOTO GETOW3
IF "%MODE%"=="2" GOTO CB3
IF "%MODE%"=="3" GOTO CBFFR3
IF "%MODE%"=="4" GOTO CBSLR3
IF "%MODE%"=="5" GOTO CBYTR3
IF "%MODE%"=="6" GOTO EXIT
:GETOA3
ECHO.
CLS && ECHO ###################################################
ECHO ### GETOA3 ###  O N L I N E   A L L   L I S T  ####
ECHO ###################################################
cd C:/
COLOR 0F
cd -cba-py
python getOnlineAllModels3.py > CB_Online_All.txt
ECHO.
PAUSE
GOTO START
:GETOW3
ECHO.
CLS && ECHO #########################################################
ECHO ### GETOW3 ###  O N L I N E   W A N T E D   L I S T  ####
ECHO #########################################################
cd C:/
COLOR 0F
cd -cba-py
python getOnlineWantedModels3.py > CB_Online_Wanted.txt
ECHO.
PAUSE
GOTO START
:CB3
ECHO.
CLS && ECHO ################################################
ECHO ### CB3 ###### R E C O R D I N G ###############
ECHO ################################################
cd C:/
COLOR 0F
cd -cba-py
python cb3.py
ECHO.
PAUSE
GOTO START
:CBFFR3
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
:CBFFR3_
ECHO.
CLS && ECHO ##################################################
ECHO ### CBFFR3 #### R E C O R D I N G ################
ECHO ############### %_MODEL_%
ECHO ##################################################
cd C:/
COLOR 0F
cd -cba-py
python cbffr3.py %MODEL%
TIMEOUT 30
GOTO CBFFR3_
:CBYTR3
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
:CBYTR3_
ECHO.
CLS && ECHO ##################################################
ECHO ### CBYTR3 #### R E C O R D I N G ################
ECHO ############### %_MODEL_%
ECHO ##################################################
cd C:/
COLOR 0F
cd -cba-py
python cbytr3.py %MODEL%
TIMEOUT 30
GOTO CBYTR3_
:CBSLR3
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
:CBSLR3_
ECHO.
CLS && ECHO ##################################################
ECHO ### CBSLR3 #### R E C O R D I N G ################
ECHO ############### %_MODEL_%
ECHO ##################################################
cd C:/
COLOR 0F
cd -cba-py
python cbslr3.py %MODEL%
TIMEOUT 30
GOTO CBSLR3_
:EXIT
GOTO :EOF
ENDLOCAL
