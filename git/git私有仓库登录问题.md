# git 私有仓库登录

* 当没有vscode环境时（比如使用colab），这个时候想做自己的私有仓库代码同步，私有仓库代码需要密码才能，而有些平台（colab）又不提示输入代码，会直接报错，这个时候需要事先输入密码，其格式为`git clone https://username:passwd@github.com/username/project.git`。这样就可以在clone的时候直接输入密码，这个密码会被保存在.git的config中，在远程的url中保存着密码，这样的话，以后每次做操作都有权限了（也意味着你的密码是明文保存的）
* 对于上述操作，也可以直接通过修改clone项目后的config操作进行，（直接修改文件或者`git remote set-url origin "https://..."`）
* 可以通过`git config --list`查看仓库的所有信息
