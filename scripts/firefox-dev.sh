cd ~/Downloads
curl --location
"https://download.mozilla.org/?product=firefox-devedition-latest-ssl&os=linux64&lang=en-US" \
  | tar --extract --verbose --preserve-permissions --bzip2
mkdir -p ~/.local/opt
mv firefox ~/.local/opt
echo "export PATH=${PATH}:${HOME}/.local/bin" >> ~/.bashrc
ln -s ~/.local/opt/firefox/firefox ~/.local/bin/firefox-dev

echo "Firefox DE was installed in your computer, run 'firefox-dev' to launch the application"