# Flask-htmlPy-pywebview
# 安装依赖
[//]: # (- (现在不需要)sudo pip install PySide (如果失败则运行 sudo apt-get install python-pyside) #htmlPy所需依赖)
- apt-get update && apt-get install curl #更新源并安装curl
[//]: # (- curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py && python2.7 get-pip.py --force-reinstall #如果pip有问题或者没有pip的话，重装pip)
- apt install python3-pip # 妈的，用python3没问题，python2各种问题。pywebview支持python3更好，用python3吧
- sudo pip3 install -r requirements.txt #安装依赖
- cd file/python-networkmanager && sudo python3 setup.py install  #安装 networkmanager
- cd ../.. # 返回项目根目录
- sudo apt-get install python-dbus #安装python-dbus

- (在本机运行，不要ssh远程连接运行)wget -qO- https://raw.githubusercontent.com/creationix/nvm/v0.33.11/install.sh | bash # 安装nvm
- command -v nvm # 如果出现nvm: command not found或者无返回内容就关闭terminal重新打开
- nvm install 8.9.1 # 安装nodejs 8.9.1 和 npm 5.5.1

- cd Front && npm install && npm run build # 进入Front安装前端依赖
- cd .. # 进入根目录

# 运行
## 生产环境
- config.ini BACKEND_SERVER 下的 mode 设置为 product（只要不是debug就行）
- python3 cloud_dashboard_end.py # 跑程序
## 开发环境
- config.ini BACKEND_SERVER 下的 mode 设置为 debug
- python3 cloud_dashboard_end.py #运行Flask（必须先运行，这是后台）
- python3 -m app.windows #打开窗口

# 文件
- 配置文件是config.ini文件，可以配置服务器的ip、端口，以及是否开启debug模式
- 日志文件是log/log