@echo off
echo ===============================
echo Remove all containers
echo ===============================
docker ps -aq | for /f "delims=" %%i in ('findstr .') do docker rm -f %%i

echo ===============================
echo Remove all images
echo ===============================
docker images -aq | for /f "delims=" %%i in ('findstr .') do docker rmi -f %%i

echo ===============================
echo Remove all volumes
echo ===============================
docker volume ls -q | for /f "delims=" %%i in ('findstr .') do docker volume rm %%i

echo ===============================
echo Cleanup complete
echo ===============================
pause
