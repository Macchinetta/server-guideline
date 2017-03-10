cd /D %~dp0
rd /S /Q build

SET SPHINXOPTS=-c conf\html_for_githubpages
call make.bat html
pause