# windows 下将wsl 当作ssh服务器

1. 安装wsl，注意先用admin安装wsl，然后用本用户下载一个发行版，放到一个可靠的地方，`Add-AppxPackage .\CanonicalGroupLimited.UbuntuonWindows_2004.2021.825.0.AppxBundle`，这样就给个人用户安装完成，且权限也是正确的
2. 以管理员身份打开ssh服务器服务`net start sshd`
3. 在wsl中安装ssh，打开ssh服务，`sudo service ssh start`，`service ssh status` , `service ssh stop`
4. 进入/etc/ssh/sshd_config ，修改PasswordAuthentication no为yes
5. 在windows下新建入站规则，开放一个端口（如果windows本身不用ssh服务，则可以开放22端口，否则不能与Windows被连接的端口相同）`netsh interface portproxy show all`查看端口转发
7. 建立映射
