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
        resert --hard HEAD^             回到上一个版本    HEAD^~n
        resert --hard (当前版本的ID)      回到当前版本
        resert HEAD (文件名)             把暂存区的修改撤销掉
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