<h2>�����������������</h2>
<div class="1">
    <h4>1.��ѧ����</h4>
    <pre>
        E(x) = sum(x<sub>i</sub>p<sub>i</sub>)
               |<sub>-oo</sub><sup>+oo</sup> xf(x) dx
    </pre>
    <p>
        ���ʣ�
    </p>
    <pre>
        1. c�ǳ����� E(c)  = c
        2. x��һ����������� c�ǳ�����  E��cx�� = CE(x)
        3. x, y �������������   E��x + y�� = E(x) + E(y)
        4. ��x, y�Ƕ������������  E��xy�� = E(x) * E(y)
    </pre>
</div>
<hr/>
<div class="2">
     <h4>2.��ѧ����</h4>
     <pre>
        D(x) = E(x<sup>2</sup>) - E(x)<sup>2</sup>
     </pre>
     <p>
        ����
     </p>
     <pre>
        1. c�ǳ���   D(c) = 0
        2. x�����������c�ǳ�����  D��cx�� = c<sup>2</sup> D��x��      D(x + c)  = D(x)
        3. x, y ���������������  D(x + y) = D(x) + D(y) + 2cov(x, y) , ��x, y �໥������D(x + y) = D(x) +D(y)
        4. p(x = E(x)) = 1  => D(x) = 0
     </pre>
     <p>
        �б�ѩ�򲻵�ʽ��
     </p>
     <pre>
        p (|x - E| >= s) <= D<sup>2</sup> / s<sup>2</sup>
        p (|x - E| < s) >= 1 -  D<sup>2</sup> / s<sup>2</sup>
     </pre>
</div>
<hr/>
<div class="3">
     <h4>3.Э������ϵ��</h4>
     <pre>
        cov(x, y) = E{[x - E(x)][y - E(y)]} = E(xy) - E(x)E(y)
        P<sub>x, y</sub> = cov(x, y) / (D(x) * D(y))<sup>1/2</sup>
     </pre>
     <p>
        ����1��
     </p>
     <pre>
        cov(ax, by) = abCov(x, y)
        cov(x<sub>1</sub> + x<sub>2</sub>, y) = cov(x<sub>1</sub>, y) + cov(x<sub>2</sub>, y)
     </pre>
     <p>
        ����2��
     </p>
     <pre>
        |P<sub>x, y</sub>| <= 1
     </pre>
     <p>
        P<sub>x, y</sub> = 0, x, y �����<br />
     </p>
     <p>
        <b><i>
            cov(x, y) = 0  == > x, y�����<br/>
            �໥����   ==��   �����<br/>
            ����x�� y��������̬�ֲ�ʱ�� x, y �����  == x, y �໥����
         </i></b>
     </p>
</div>
<hr/>
<div class="4">
     <h4>4.�أ� Э�������</h4>
     <pre>
        1. k��ԭ���   E��x<sup>k</sup>��                     k=1, ==> E(x)
        2. k�����ľ�   E([x - E(x)]<sup>k</sup>)             k=2, ==> D(x)
        3. k+l�׻�����ľ�  E{[x - E(x)]<sup>k</sup>[y - E(y)]<sup>l</sup>}   k, l=2  ==> cov(x, y)
     </pre>
     <p>
        Э�������
     </p>
     <pre>
        C<sub>i</sub><sub>j</sub> = cov(x<sub>i</sub>, x<sub>j</sub>)
                                  = E{[x<sub>i</sub> - E(x<sub>i</sub>)][x<sub>j</sub> - E(x<sub>j</sub>)]}
     </pre>
</div>
<hr/>
<div class="5">
     <h4>5.���ֳ����ֲ��������ͷ���</h4>
     <div class="51">
        <pre>
            1. 0-1�ֲ���               E(x) = p,                D(x) = 1 - p
            2. ����ֲ�x-B(n, p)��      E(x) = np,               D(x) = np(1 - p)
            3. ���ɷֲ�x-P(q)��         E(x) = q,                D(x) = q
            4. ���ȷֲ�x-U(a, b)        E(x) = (a + b) / 2       D(x) = (b - a)<sup>2</sup> / 12
            5. ָ���ֲ�                 E(x) = o                 D(x) = o<sup>2</sup>
            6.��̬�ֲ�x-N��E, D��        E(x) = E,                D(x) = D
        </pre>
     </div>
     <div class="52">
        <p>
            ����
        </p>
        <pre>
            ��x-N(1, 3), y-N(2, 4), ��x��y�໥������ ��z = 2x - 3y Ҳ������̬�ֲ�
            E(z) = 2 x 1 - 3 x 2 = -4
            D(z) = 4D(x) + 9D(y) = 48
        </pre>
     </div>
</div>