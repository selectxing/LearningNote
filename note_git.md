## 克隆项目到本地

- 下载安装git bash
- 配置git

  1. 配置user.name、email。配置完毕后，在“C:\Users\Administrator”中生成.gitconfig文件

     ```bash
     $ git config --global user.name "Your Name"
     
     $ git config --global user.email "email@example.com"
     ```
  
  2. 配置SSH Key。配置完毕后，在“C:\Users\Administrator”中生成.ssh目录。将id_rsa.pub（公钥）添加至GitHub的Key中
  
     ```bash
     $ ssh-keygen -t rsa -C "email@example.com"
     ```

- 克隆项目到本地

  1. 打开git bash，cd进入保存项目所在目录；或者右键该目录git bash here
  
  2. 克隆项目
     
     ```bash
     $ git clone git@github.com:selectxing/LearningNote.git
     ```

## 入门
- 创建仓库，初始化目录为git仓库

  ```bash
  $ git init
  ```

- 将文件add至暂存区。.将工作区所有文件add至暂存区

  ```bash
  $ git add readme.txt
  $ git add .   
  ```

- 将文件commit至版本库

  ```bash
  $ git commit -m"commit comment"
  ```

  > 注意：提交修改至版本库，均需add、commit两步
  >
  > 涉及工作区（working copy）、暂存区（stage index）、版本库（commit history）三个概念
  >
  > ```bash
  > $ git diff   工作区与暂存区差异
  > $ git diff head    工作区与版本库差异
  > $ git diff -–cached	暂存区与版本库差异
  > ```

- 查看git当前状态、冲突等信息

  ```bash
  $ git status
  ```

- 查看git日志

  ```bash
  $ git log <--graph --pretty=oneline>
  $ git reflog    查看完整日志
  ```

  撤销修改

  ```bash
  $ git checkout lisence.txt   撤销工作区文件（未add）的修改
  $ git checkout -- lisence.txt   撤销暂存区（已add）、版本库（已commit）文件的删除（手工或rm删除，非git rm）。--后需有空格
  $ git reset head lisence.txt   撤销暂存区（已add）的修改
  $ git reset --hard head^    head为当前版本，head^为上个版本，head^^为上上个版本，head~100为往前100个版本
  $ git reset --hard a9a06    id号回退。id号可以只输入前几位，git自动查找
  ```

- 工作区、暂存区、版本库回退

  ```bash
  $ git reset –-soft	暂存区->工作区
  $ git reset –-mixed	版本库->暂存区
  $ git reset –-hard	版本库->暂存区->工作区
  ```

- 删除文件

  ```bash
  $ git rm del.txt    删除commit至版本库的文件。git rm删除的文件，不管是否commit，都无法通过git checkout --撤销删除
  $ git commit -m"delete"
  ```

- 重命名文件

  ```bash
  $ git mv a.txt b.txt
  $ git commit -m"rename"
  ```

## 远程仓库
创建SSH Key。默认windows用户目录下.ssh目录。将id_rsa.pub（公钥）内容粘贴至GitHub设置的Key中
$ ssh-keygen -t rsa -C "email@example.com"

- 添加、查看远程库
  origin为与远程库（remote repository）对应的本地库（local repository）链接名称
  本地库默认名称origin，如果使用多个远程库，如github、gitee等，本地库名称可自定义不同名称用以区分

  ```bash
  $ git remote add origin git@github.com:selectxing/gittest.git
  $ git remote 查看远程库
  $ git remote -v	查看远程库信息
  $ git remote rm origin 删除本地库链接
  ```

- 从远程库克隆至本地

  ```bash
  $ git clone git@github.com:selectxing/gitskill.git  clone至git bash当前目录。拉取时碰到ssh port22错误，建议clone时远程库增加.git
  ```

- 从远程库拉取到本地

  ```bash
  $ git pull origin master
  ```

- 从本地推送至远程库

  ```bash
  $ git push -u origin master <-f> -u指定默认origin。-f强制推送，会覆盖github远程库，不建议使用。首次使用clone或push时，会出现SSH警告
  $ git push origin master
  ```

- 远程库地址的两种写法
  git@github.com:selectxing/gitskill  使用ssh协议，速度快
  https://github.com/selectxing/gitskill  使用https协议，速度慢，只开放http端口使用

## 分支管理
```bash
$ git checkout -b dev   创建并切换分支dev
$ git branch dev        创建分支dev
$ git checkout dev      切换分支dev
$ git branch            查看分支，*号标识的为当前使用分支
```

Git在同一目录体现分支信息，如果多个分支某文件不一致时，切换分支后文件版本即时更新为当前分支对应内容

```bash
$ git merge dev                         切换至master分支后，merge分支dev。有冲突需要手动解决冲突
$ git branch -d dev                     删除分支dev
$ git branch -D feature1                未merge分支-d不能删除，-D强制删除
$ git merge --no-ff -m"merge注释" dev   禁用fast forward模式merge（直接merge删除dev分支后会丢失其信息）
$ git checkout -b dev origin/dev        clone默认只有master分支，其他分支需创建本地库与远程库链接的dev分支
```

```bash
$ git stash         将未add、commit的工作现场储藏
$ git stash list    查看临时保存的工作现场
$ git stash pop     恢复工作现场，并删除stash储藏
$ git stash apply   恢复工作现场，未删除stash储藏
$ git stash drop    删除stash储藏
```

stash实现了无需单独创建临时分支目录，可在同一目录临时新增A分支，且不影响未提交的B分支代码的功能

```bash
$ git branch --set-upstream-to <branch-name> origin/<branch-name>   建立本地库与远程库的链接。解决pull时no tracking information的报错
$ git rebase    变基
```

## 标签操作
```bash
$ git tag v1.0                      定义标签
$ git tag -a v0.9 -m"1.0版本"       定义带注释标签
$ git tag                           查看标签
$ git tag v0.9 f52c633              对历史某次commit定义标签
$ git show v0.9                     查看标签
$ git tag -d v0.9                   删除标签
$ git push origin v1.0              推送标签至远程库
$ git push origin --tag             推送所有未推送标签
$ git push origin :refs/tags/v1.0   删除远程库标签
```

## 自定义Git
- 忽略特殊文件
  使用.gitignore忽略某些不需要提交到代码库的文件。模板：https://github.com/github/gitignore

  ```bash
  $ git add -f App.class 强制添加被忽略的文件类型
  $ git check-ignore -v App.class 检查哪个规则忽略了.class文件类型
  ```

- 配置仓库语言
  创建.gitattributes文件，加上*.js linguist-language=java

- 配置颜色

  ```bash
  $ git config --global color.ui true
  ```

- 配置别名

  ```bash
  $ git config --global alias.co checkout
  $ git config --global alias.ci commit
  $ git config --global alias.br branch
  ```

  大牛的别名

  ```bash
  $ git config --global alias.last 'log -1'   末次日志
  $ git config --global alias.lg "log --color --graph --pretty=format:'%Cred%h%Creset -%C(yellow)%d%Creset %s %Cgreen(%cr) %C(bold blue)<%an>%Creset' --abbrev-commit"    高亮日志格式
  ```

- 配置文件位置：每个级别重写前一个级别的值
  系统配置文件：--system	目录位置：C:\Program Files\Git\mingw64\etc
  全局配置文件：--global	目录位置：C:\Users\Administrator
  本地配置文件：--local	目录位置：本地库.git

- 查看git配置文件目录

  ```bash
  $ git config --list --show
  $ git config --global --list
  ```

## 常用Linux命令
*cd		切换到目录*
*pwd		显示当前目录路径*
*ls		显示当前目录文件*
*mkdir	创建目录*
*touch	创建空文件*
*cat 	打开文件*
*rm -r	删除目录*
*rm 		删除文件*
*mv		重命名文件、移动、备份*