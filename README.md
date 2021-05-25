# Lola
### `lola` : A simple CLI for installing packages on Linux easily 

**lola is made for linux users who want to download software fast and easy!**

Now many will ask, Why use lola when we have those software managers?

Well, lola is a Command Line Interface and is used inside the terminal. And as we know, terminal downloads are way more faster than the software managers. While many softwares can be downloaded with a single `sudo apt install`, most common ones need some more commands.

So `lola` is here to make your life way more easier while installing software! This project targets both advanced and beginner users, because who doesn't like speedy and quicky stuff?

#### Dependencies
+ `click`

### Built with
+ `Python 3.8.5`


## Installation

#### Method 1 (Recommended):

If you dont have python3 and pip installed on your system, or are not that much of PYTHON CODER, use this method

- In your terminal-

```bash
curl https://raw.githubusercontent.com/arghyagod-coder/lola/master/lolacli/install.sh | sudo bash -
```

- Now `lola` is ready to work!

#### Method 2

If you have python and pip installed in your computer, execute the following

```bash
pip3 install lolacli
```

## Supported Platforms:

+ Operating System = Linux64
    - Ubuntu 20.04 and Derivatives
    - Mint 19.3
    - Mint 20.1
    - Debian 10 

## Screenshots

![](assets/help.png)

![](assets/check-apps.png)

![](assets/audacity-dl.png)

## Usage

**lola is made for linux users who want to download software fast and easy!**

Now many will tell, Why use lola when we have those software managers?

Well, lola is a Command Line Interface and is used inside the terminal. And as we know, terminal downloads are way more faster than the software managers. While many softwares can be downloaded with a single `sudo apt install`, most common ones need some more commands.

So `lola` is here to make your life way more easier while installing software! This project targets both advanced and beginner users, because who doesn't like speedy and quicky stuff?

### Guide

Enter `sudo` mode first in the kernel

```bash
sudo su
```
It will ask for your system password, enter your password and you will enter sudo mode

- The help command

```bash
>lola --help


  I am Lola! Your assistant who can help you setup your Linux in an easy way!
  You can know more about me in https://github.com/arghyagod-coder/lola.

  I can help you install apps through terminal, and you need to know almost
  nothing about the terminal to do so! Just simple prompts will be enough

Options:
  --version  Show the version and exit.
  --help     Show this message and exit.

Commands:
  check-apps  Check the list of supported apps!
  install     Install an app

```

- Check all supported apps in lola by using the `lola check-apps` command.

```bash
> lola check-apps


gimp
da-vinci-resolve
wine
libreoffice-full
krita
brave-browser
brave-beta
brave-nightly
edge-beta
firefox
chrome
lutris
g-drive
blender
python3
miniconda
anaconda
pip3
java-development-kit-11
java-development-kit-14-oracle
vscode
atom-editor
...
```

- Install an app through lola with the `lola install <appname>` command

```bash
> lola install cheese


--2021-05-25 13:16:45--  https://raw.githubusercontent.com/arghyagod-coder/lola/master/lolacli/scripts/cheese.sh
Resolving raw.githubusercontent.com (raw.githubusercontent.com)... 185.199.108.133, 185.199.111.133, 185.199.110.133, ...
Connecting to raw.githubusercontent.com (raw.githubusercontent.com)|185.199.108.133|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 53 [text/plain]
Saving to: ‘cheese.sh’

cheese.sh           100%[===================>]      53  --.-KB/s    in 0s      

2021-05-25 13:16:48 (2.20 MB/s) - ‘cheese.sh’ saved [53/53]
         
Hit:1 https://brave-browser-apt-release.s3.brave.com stable InRelease
Hit:2 http://packages.microsoft.com/repos/code stable InRelease                
Hit:3 http://security.ubuntu.com/ubuntu focal-security InRelease               
Hit:4 http://archive.canonical.com/ubuntu focal InRelease                      
Ign:5 http://packages.linuxmint.com ulyssa InRelease                           
Hit:6 http://archive.ubuntu.com/ubuntu focal InRelease
Hit:7 http://archive.ubuntu.com/ubuntu focal-updates InRelease
Hit:8 http://packages.linuxmint.com ulyssa Release
Hit:10 http://archive.ubuntu.com/ubuntu focal-backports InRelease
Reading package lists... Done
Reading package lists... Done
Building dependency tree       
Reading state information... Done
The following additional packages will be installed:
  cheese-common gnome-video-effects libcheese-gtk25 libcheese8
Suggested packages:
  gnome-video-effects-frei0r gnome-video-effects-extra
The following NEW packages will be installed:
  cheese cheese-common gnome-video-effects libcheese-gtk25 libcheese8
0 upgraded, 5 newly installed, 0 to remove and 6 not upgraded.
Need to get 628 kB of archives.
After this operation, 1,707 kB of additional disk space will be used.
Get:1 http://archive.ubuntu.com/ubuntu focal-updates/main amd64 cheese-common all 3.34.0-1ubuntu1 [390 kB]
Get:2 http://archive.ubuntu.com/ubuntu focal-updates/main amd64 libcheese8 amd64 3.34.0-1ubuntu1 [33.3 kB]
Get:3 http://archive.ubuntu.com/ubuntu focal-updates/main amd64 libcheese-gtk25 amd64 3.34.0-1ubuntu1 [27.0 kB]
Get:4 http://archive.ubuntu.com/ubuntu focal/main amd64 gnome-video-effects all 0.5.0-1ubuntu1 [38.8 kB]
Get:5 http://archive.ubuntu.com/ubuntu focal-updates/main amd64 cheese amd64 3.34.0-1ubuntu1 [139 kB]
Fetched 628 kB in 16s (39.2 kB/s)                                              
Selecting previously unselected package cheese-common.
(Reading database ... 328427 files and directories currently installed.)
Preparing to unpack .../cheese-common_3.34.0-1ubuntu1_all.deb ...
Unpacking cheese-common (3.34.0-1ubuntu1) ...
Selecting previously unselected package libcheese8:amd64.
Preparing to unpack .../libcheese8_3.34.0-1ubuntu1_amd64.deb ...
Unpacking libcheese8:amd64 (3.34.0-1ubuntu1) ...
Selecting previously unselected package libcheese-gtk25:amd64.
Preparing to unpack .../libcheese-gtk25_3.34.0-1ubuntu1_amd64.deb ...
Unpacking libcheese-gtk25:amd64 (3.34.0-1ubuntu1) ...
Selecting previously unselected package gnome-video-effects.
Preparing to unpack .../gnome-video-effects_0.5.0-1ubuntu1_all.deb ...
Unpacking gnome-video-effects (0.5.0-1ubuntu1) ...
Selecting previously unselected package cheese.
Preparing to unpack .../cheese_3.34.0-1ubuntu1_amd64.deb ...
Unpacking cheese (3.34.0-1ubuntu1) ...
Setting up gnome-video-effects (0.5.0-1ubuntu1) ...
Setting up cheese-common (3.34.0-1ubuntu1) ...
Processing triggers for bamfdaemon (0.5.3+18.04.20180207.2-0ubuntu2) ...
Rebuilding /usr/share/applications/bamf-2.index...
Processing triggers for desktop-file-utils (0.24+linuxmint1) ...
Processing triggers for mime-support (3.64ubuntu1) ...
Processing triggers for hicolor-icon-theme (0.17-2) ...
Processing triggers for gnome-menus (3.36.0-1ubuntu1) ...
Processing triggers for libglib2.0-0:amd64 (2.64.6-1~ubuntu20.04.3) ...
Processing triggers for libc-bin (2.31-0ubuntu9.2) ...
Processing triggers for man-db (2.9.1-1) ...
Setting up libcheese8:amd64 (3.34.0-1ubuntu1) ...
Setting up libcheese-gtk25:amd64 (3.34.0-1ubuntu1) ...
Setting up cheese (3.34.0-1ubuntu1) ...
Processing triggers for libc-bin (2.31-0ubuntu9.2) ...

```

## Developer Tools

- [Python 3.8.5](https://www.python.org/ftp/python/3.8.5/Python-3.8.5.tar.xz)
- [Sublime Text 3](https://www.sublimetext.com/3)
- [Visual Studio Code](https://code.visualstudio.com)
- [Git](https://git-scm.com/) 
- [Python Poetry](https://python-poetry.org/) for package management and publishing

## Release Notes

- **Current Release- 0.2.1**

### What's new?

- Larger app support
- Improved README
- Fixed Installation Script
- Fixed the 'File not Found' error

#### Developers
- 

## License

License © 2021-Present Arghya Sarkar

This repository is licensed under the MIT license. See [LICENSE](https://github.com/arghyagod-coder/lola/master/LICENSE) for details.

## Special Notes

- Contribution is appreciated! Visit the contribution guide in 
- If you don't find an app in the supported app list, file an issue in [the issue page](https://github.com/arghyagod-coder/lola/issues). Issues aren't ignored by the developers
- Thanks for seeing my project!