apt -y update;
apt install -y software-properties-common apt-transport-https wget;
wget -q https://packagecloud.io/AtomEditor/atom/gpgkey -O- | sudo apt-key add -;
add-apt-repository "deb [arch=amd64] https://packagecloud.io/AtomEditor/atom/any/ any main";
apt install -y atom

