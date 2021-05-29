sudo apt -y update;
sudo apt install -y software-properties-common apt-transport-https wget;
wget -q https://packagecloud.io/AtomEditor/atom/gpgkey -O- | sudo apt-key add -;
sudo add-apt-repository "deb [arch=amd64] https://packagecloud.io/AtomEditor/atom/any/ any main";
sudo apt install -y atom

