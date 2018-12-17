#/bin/bash
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py && python2.7 get-pip.py --force-reinstall
sudo pip install -r requirements.txt
cd file/python-networkmanager && sudo python setup.py install
cd ../..
sudo apt-get install python-dbus
wget -qO- https://raw.githubusercontent.com/creationix/nvm/v0.33.11/install.sh | bash
export NVM_DIR="${XDG_CONFIG_HOME/:-$HOME/.}nvm" [ -s "$NVM_DIR/nvm.sh" ] && \. "$NVM_DIR/nvm.sh"
nvm install
cd Front && npm install && npm run build
cd ..