
install_docker(){

    sudo apt-get update
    sudo apt-get install apt-transport-https ca-certificates curl gnupg lsb-release

    curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg
    echo "deb [arch=amd64 signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
    sudo apt-get update

    sudo apt-get install docker-ce docker-ce-cli containerd.io
}

docker --version 2> /dev/null
if [ $? -ne 0 ]; then
    while true; do
        read -p "This script requires docker to run correctly, do you want to install it? y/n" yn
        case $yn in
            [Yy]* ) install_docker; break;;
            [Nn]* ) exit;;
            * ) echo "Please answer yes or no.";;
        esac
    done
    
fi

chmod +x install_aux.sh && ./install_aux.sh