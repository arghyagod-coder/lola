cd ~;
wget https://github.com/vlang/v/releases/latest/download/v_linux.zip ;
unzip ~/v_linux.zip;
shell="$0"
echo "export PATH=$PATH:$HOME/v" >> ~/.bashrc