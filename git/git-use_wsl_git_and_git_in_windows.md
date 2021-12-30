# 使用wsl中的git和windows中的git的注意事项

这两者的git使用是不同的，会将对方的没有任何更改的内容识别为新的文件，导致不方便

> 产生这个问题的原因是unix和windows的换行符不同([原因](https://blog.csdn.net/u012109105/article/details/51252242))，我们也不用去关心具体的细节了

为了解决这个问题，建议使用如下的方法

* 首先在wsl和windows中都下载git
* 当编写程序时，牢记一点，**不要在windows中使用git**

## 原因解释

为什么不在Windows中使用git还需要进行下载呢？

这是因为当我们使用vscode+git进行开发时，会利用到vscode中的一些插件，比如`git graph`和`github`等，这些插件在加载时会检测git环境，如果检测不到git会在右下方提示报错，十分讨厌（如果可以忍受，那么便不用在Windows中安装git）。所以下载git只是为了这些插件的使用环境不报错

## 注意

vscode目前虽然可以支持wsl，但是wsl和windows系统使用的是相同的配置，也就是说，无法单独在Windows环境中禁用插件同时又希望在wsl中使用插件，比较麻烦
