<h2>git</h2>
<div>
    <p>git</p>
    <pre>
        Git�Ƿֲ�ʽ�汾����ϵͳ
        Git��������޸�
    </pre>
    <p>2.commond</p>
    <pre>
        git config --global user name ""
        git config --global user email ""
        add                             ��ӵ��ֿ�   stage
        commit -m  ��xxx��                �ύ���ֿ�   ��ǰ��֧
        log                             �鿴�ύ��ʷ            git log --pretty=oneline  ����
        reflog                          �鿴��ʷ����
        status                          ״̬
        resert --hard HEAD^             �ص���һ���汾    HEAD^~n
        resert --hard (��ǰ�汾��ID)      �ص���ǰ�汾
        resert HEAD (�ļ���)             ���ݴ������޸ĳ�����
        diff HEAD -- (�ļ���)            �鿴�������Ͱ汾���������°汾������
        checkout -- (�ļ���)             �������������޸�      �ص����һ��git commit��git addʱ��״̬��
        rm                              �Ӱ汾����ɾ�����ļ��� ����git commit  �������ɾ�� git checkout -- (�ļ���)
        push origin master              ������GitHub
        clone                           ��¡ 
        checkout -b                     == git branch  + git checkout �������л�
        branch                          �鿴��ǰ��֧
        merge                           �ϲ���master��֧��
        branch -d                       ɾ����֧
        switch                          �л���֧    git switch -c  == git checkout -b
    </pre>
    <p>github</p>
    <pre>
        .git    git�İ汾��
        stage   �ݴ���
        ����Git�ֿ��GitHub�ֿ�֮��Ĵ�����ͨ��SSH���ܵ�
            ��1. ����SSH Key       ssh-keygen -t rsa -C "youremail@example.com"
                id_rsa��˽Կ��id_rsa.pub�ǹ�Կ��
            ��2. �򿪡�Account settings���� ��SSH Keys��ҳ�棺 ճ��id_rsa.pub�ļ�������
            ��3. ��һ�����еı��زֿ���֮������   git remote add origin git@github.com:(user account)/learngit.git
                ���� ��¡
    </pre>
</div>