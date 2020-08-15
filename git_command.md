<h2>git</h2>
<div>
    <p>git</p>
    <pre>
        Git是分布式版本控制系统
        Git管理的是修改
    </pre>
    <p>2.commond</p>
    <pre>
        git config --global user name ""
        git config --global user email ""
        add                             添加到仓库   stage
        commit -m  “xxx”                提交到仓库   当前分支
        log                             查看提交历史            git log --pretty=oneline  整洁
        reflog                          查看历史命令
        status                          状态
        reset --hard HEAD^             回到上一个版本    HEAD^~n
        reset --hard (当前版本的ID)      回到当前版本
        reset HEAD (文件名)             把暂存区的修改撤销掉
        diff HEAD -- (文件名)            查看工作区和版本库里面最新版本的区别
        checkout -- (文件名)             丢弃工作区的修改      回到最近一次git commit或git add时的状态。
        rm                              从版本库中删除该文件， 并且git commit  如果是误删， git checkout -- (文件名)
        push origin master              推送至GitHub
        clone                           克隆 
        checkout -b                     == git branch  + git checkout 创建并切换
        branch                          查看当前分支
        merge                           合并到master分支上
        branch -d                       删除分支
        switch                          切换分支    git switch -c  == git checkout -b
        git merge --no-ff -m            --no-ff参数，表示禁用Fast forward
    </pre>
    <p>github</p>
    <pre>
        .git    git的版本库
        stage   暂存区
        本地Git仓库和GitHub仓库之间的传输是通过SSH加密的
            》1. 创建SSH Key       ssh-keygen -t rsa -C "youremail@example.com"
                id_rsa是私钥，id_rsa.pub是公钥，
            》2. 打开“Account settings“， “SSH Keys”页面： 粘贴id_rsa.pub文件的内容
            》3. 把一个已有的本地仓库与之关联，   git remote add origin git@github.com:(user account)/learngit.git
                或者 克隆
    </pre>
</div>
<div>
    <p>windows</p>
    <pre>
        cd          显示当前目录的名称或将其更改
        dir         显示一个目录中的文件和子目录
        attrib      显示或更改文件属性
        cls         清除屏幕
        copy        将至少一个文件复制到另一个位置
        date        显示或设置日期
        del         删除至少一个文件
        diskpart    显示或配置磁盘分区属性
        driverquery 显示当前设备驱动程序状态和属性
        echo        显示消息，或将命令回显打开或关上
        erase       删除一个或多个文件
        exit        退出 CMD.EXE 程序(命令解释程序)
        find        在一个或多个文件中搜索一个文本字符串
        findstr     在多个文件里搜索字符串
        fsutil      显示或配置文件系统的属性
        help        提供 Windows 命令的帮助信息
        md          创建一个目录
        mkdir       创建一个目录
        mklink      创建一个软连接或硬链接
        mode        配置系统设备
        more        逐屏显示输出
        move        将一个或多个文件从一个目录移动到另一个目录
        path        为可执行文件显示或设置搜索路径
        print       打印一个文本文件
        prompt      改变 windows 命令提示
        rd          删除目录
        recover     从损坏的磁盘中恢复可读取的信息
        rem         记录批处理文件或 config.sys 中的注释
        ren/rename  重新命名文件
        replace     替换文件
        rmdir       删除目录
        set         显示、设置或删除 Windows 环境变量
        sc          显示或配置服务(后台处理)
        systeminfo  显示机器的具体的属性和配置
        tasklist    显示包括服务的所有当前运行的任务
        taskkill    终止正在运行的进程或应用程序
        time        显示和设置系统时间
        title       设置 CMD.EXE 会话的窗口标题
        tree        以图形显示启动器或路径的目录结构
        type        显示文本文件的内容
        ver         显示 Windows 的版本
        xcopy       赋值文件和目录树
    </pre>
</div>