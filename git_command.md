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
        reset --hard HEAD^             �ص���һ���汾    HEAD^~n
        reset --hard (��ǰ�汾��ID)      �ص���ǰ�汾
        reset HEAD (�ļ���)             ���ݴ������޸ĳ�����
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
        git merge --no-ff -m            --no-ff��������ʾ����Fast forward
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
<div>
    <p>windows</p>
    <pre>
        cd          ��ʾ��ǰĿ¼�����ƻ������
        dir         ��ʾһ��Ŀ¼�е��ļ�����Ŀ¼
        attrib      ��ʾ������ļ�����
        cls         �����Ļ
        copy        ������һ���ļ����Ƶ���һ��λ��
        date        ��ʾ����������
        del         ɾ������һ���ļ�
        diskpart    ��ʾ�����ô��̷�������
        driverquery ��ʾ��ǰ�豸��������״̬������
        echo        ��ʾ��Ϣ����������Դ򿪻����
        erase       ɾ��һ�������ļ�
        exit        �˳� CMD.EXE ����(������ͳ���)
        find        ��һ�������ļ�������һ���ı��ַ���
        findstr     �ڶ���ļ��������ַ���
        fsutil      ��ʾ�������ļ�ϵͳ������
        help        �ṩ Windows ����İ�����Ϣ
        md          ����һ��Ŀ¼
        mkdir       ����һ��Ŀ¼
        mklink      ����һ�������ӻ�Ӳ����
        mode        ����ϵͳ�豸
        more        ������ʾ���
        move        ��һ�������ļ���һ��Ŀ¼�ƶ�����һ��Ŀ¼
        path        Ϊ��ִ���ļ���ʾ����������·��
        print       ��ӡһ���ı��ļ�
        prompt      �ı� windows ������ʾ
        rd          ɾ��Ŀ¼
        recover     ���𻵵Ĵ����лָ��ɶ�ȡ����Ϣ
        rem         ��¼�������ļ��� config.sys �е�ע��
        ren/rename  ���������ļ�
        replace     �滻�ļ�
        rmdir       ɾ��Ŀ¼
        set         ��ʾ�����û�ɾ�� Windows ��������
        sc          ��ʾ�����÷���(��̨����)
        systeminfo  ��ʾ�����ľ�������Ժ�����
        tasklist    ��ʾ������������е�ǰ���е�����
        taskkill    ��ֹ�������еĽ��̻�Ӧ�ó���
        time        ��ʾ������ϵͳʱ��
        title       ���� CMD.EXE �Ự�Ĵ��ڱ���
        tree        ��ͼ����ʾ��������·����Ŀ¼�ṹ
        type        ��ʾ�ı��ļ�������
        ver         ��ʾ Windows �İ汾
        xcopy       ��ֵ�ļ���Ŀ¼��
    </pre>
</div>