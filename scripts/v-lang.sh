cd ~;
wget https://raw.githubusercontent.com/vlang/v/releases/latest/download/v_linux.zip ;
unzip ~/v_linux.zip;
sudo echo "PATH=$PATH:$HOME/v_linux" >> /etc/environment