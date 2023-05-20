@ECHO OFF
docker --version > NUL 2> NUL
IF %errorlevel% NEQ 0 (
    echo Docker non found
    echo Installing docker...
    
    winget install -e --id Docker.DockerDesktop
)


call install_aux