sudo dpkg --add-architecture i386
wget -nc https://dl.winehq.org/wine-builds/winehq.key
sudo apt-key add winehq.key
sudo add-apt-repository ‘deb https://dl.winehq.org/wine-builds/ubuntu/focal main’
sudo add-apt-repository ‘deb https://dl.winehq.org/wine-builds/ubuntu/bionic main’
sudo apt update
sudo apt install --install-recommends winehq-stable
