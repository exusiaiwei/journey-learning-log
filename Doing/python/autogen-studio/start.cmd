@echo off

:: Activate the autogenstudio environment and start the UI
call C:\Scoop\apps\anaconda3\current\App\condabin\conda.bat activate autogenstudio
autogenstudio ui
