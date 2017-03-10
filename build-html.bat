cd /D %~dp0
rem rd /S /Q build

SET SPHINXOPTS=-c conf\html
call make.bat html
pause