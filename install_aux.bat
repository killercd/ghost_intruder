@echo off
SET auxfolder=aux_m

echo Cloning projects...
rd /s /q %auxfolder%
mkdir %auxfolder%
cd %auxfolder%
git clone git@github.com:killercd/sshscan.git
git clone git@github.com:killercd/qmail.git

cd ..

:req_inst

echo Installing requirements
cd %auxfolder%\sshscan
pip install -r requirements.txt
cd ..\..



:runner_c
echo Generating runners...
cscript //nologo gen_runner.vbs %auxfolder% sshscan %CD% sshscan.py sshscan.bat 



:set_env
echo Setting env variables...
cscript //nologo set_env_dir.vbs