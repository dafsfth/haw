<h2>֧��������</h2>
<h3>1. ����svm</h3>
<div>
<p>ԭ������ܹ���ȷ�������ݼ����Ҽ��μ�����ķָƽ��</p>
<div>
<p>
���ڸ������ݼ��ͳ�ƽ��W*X + b = 0, �򼯺�������(X<sub>i</sub>, y)��x<sub>i</sub>Ϊ���������� yΪ��ǩ���ļ��Ͽռ�Ϊ��
</p>
<pre>
    r<sub>i</sub> = y<sub>i</sub> * (w * x<sub>i</sub> / ||w|| + b / ||w||)
</pre>
<p>
֧����������ƽ��ľ���Ϊ��           
</p>
<pre>
    r = Min(r<sub>i</sub>)
</pre>
<p>
���ָƽ�棺 Max(r), ��
</p>
<pre>
    y<sub>i</sub> * (w * x<sub>i</sub> / ||w|| + b / ||w||) >= r
    ==��y<sub>i</sub> * (w * x<sub>i</sub> / ||w|| * r + b / ||w|| * r) >= 1
    ==��y<sub>i</sub> * (w * X<sub>i</sub> + b) >= 1, ����w = w / ||w|| * r,    b = b / ||w|| * r
</pre>

<pre>
    Max(r) ==> Max(1 / ||w||) ==> Min(1 / 2 * ||w||<sup>2</sup>)
</pre>
<p>
�õ����µĺ��в���ʽ��͹���ι滮���⣺
</p>
<pre>
    Min<sub>w, b</sub>   1 / 2 * ||w||<sup>2</sup>  
    s.t.   y<sub>i</sub> * (w * X<sub>i</sub> + b) >= 1 
</pre>
<p>
ʹ���������ճ��ӷ�������ż���⣺
</p>
<pre>
    L(w, b, a) = 1 / 2 * ||w||<sup>2</sup> - sum(a<sub>i</sub> * (y<sub>i</sub> * (w * x<sub>i</sub> + b) - 1))
��   ����a<sub>i</sub>Ϊ�������ճ��ӣ� ��a<sub>i</sub> >= 0
</pre>
<p>
��O(x) = Max<sub>a<sub>i</sub> >= 0</sub> L(w, b. a)�� ���Եõ���
</p>
<pre>
    O(x) = 1 / 2 * ||w||<sup>2</sup>   , x �ڿ�������  ��y<sub>i</sub> * (w * X<sub>i</sub> + b) >= 1 ��
            +oo , x ���ڿ������ڣ���y<sub>i</sub> * (w * X<sub>i</sub> + b) <= 1 ��
</pre>

<p>
ԭԼ�����⣺
</p>
<pre>
    Min<sub>w, b</sub>(O(x)) ==> Min<sub>w, b</sub>(Max<sub>a<sub>i</sub> >= 0</sub>( L(w, b, a))) = p*
</pre>
<p>
ʹ���������պ�����ż�Եã�
</p>
<pre>
    Max<sub>a<sub>i</sub> >= 0</sub>(Min<sub>w, b</sub>( L(w, b, a))) = b*
</pre>
<p>
ʹ�� p* = b* �����㣺
</p>
<p>
1.�Ż�������ͼ�Ż�<br>
2.KKT����, == ><br>
<pre>
   a<sub>i</sub> >= 0
   y<sub>i</sub> * (w * X<sub>i</sub> + b) >= 1
   a<sub>i</sub> * (y<sub>i</sub> * (w * x<sub>i</sub> + b) - 1) = 0
</pre>
<p>
L(w, b, a) �� w, b, �󵼣� ��������� 0�ã�
</p>
<pre>
    w = sum(a<sub>i</sub> * y<sub>i</sub> * x<sub>i</sub>)
    0 = sum(a<sub>i</sub> * y<sub>i</sub>)
</pre>
<p>
������������Ŀ�꺯���ã�
</p>
<pre>
    Min<sub>w, b</sub> L(w, b, a) = -1 / (2 * sum<sub>i</sub>(sum<sub>j</sub>(a<sub>i</sub> * a<sub>j</sub> * y<sub>i</sub> * y<sub>j</sub> * (x<sub>i</sub> . x<sub>i</sub>))) + sum(a<sub>i</sub>) 
</pre>
<p>
��󻯲�ȡ��ʹ��ԭ����ת��Ϊ��
</p>
<pre>
    Minn<sub>a</sub>(1 / (2 * sum<sub>i</sub>(sumn<sub>j</sub>(a<sub>i</sub>a<sub>j</sub>y<sub>i</sub>y<sub>j</sub>(x<sub>i</sub> . x<sub>j</sub>))))) - sum(a<sub>i</sub>)
    s.t.  sum(a<sub>i</sub>y<sub>i</sub>) = 0
          a<sub>i</sub> >= 0
</pre>
<p>
ʹ��������С�Ż��㷨(SMO) (����ʽ)
</p>
<pre>
    L = Min 1/ 2(sum<sub>i</sub>(sum<sub>j</sub>(a<sub>i</sub>a<sub>j</sub> y<sub>i</sub>y<sub>j</sub> x<sub>i</sub> . x<sub>j</sub>))) - sum(a<sub>i</sub>) 
    s.t.  sum(a<sub>i</sub>y<sub>i</sub>) = 0
    ��: K<sub>i</sub><sub>j</sub> = x<sub>i</sub> . x<sub>j</sub>
    ��
        L(a<sub>1</sub>, a<sub>2</sub>) = 1 / 2(a<sub>1</sub><sup>2</sup>k<sub>1</sub><sub>1</sub> + a<sub>2</sub><sup>2</sup>k<sub>2</sub><sub>2</sub> + 2sum(a<sub>2</sub>a<sub>1</sub>y<sub>2</sub>y<sub>1</sub>) + 2sum<sub>i=1, j>=3</sub>(a<sub>1</sub>y<sub>1</sub>a<sub>j</sub>y<sub>j</sub>K<sub>1</sub><sub>j</sub>) + 2sum<sub>i=2, j>=3</sub>(a<sub>2</sub>y<sub>2</sub>a<sub>j</sub>y<sub>j</sub>K<sub>2</sub><sub>j</sub>) + sum<sub>i>=3</sub>(sum<sub>j>=3</sub>(a<sub>i</sub>a<sub>j</sub> y<sub>i</sub>y<sub>j</sub> k<sub>i</sub><sub>j</sub>))) - a<sub>1</sub> - <sub>2</sub> - sum<sub>j>=3</sub>(a<sub>j</sub>)
    �ɣ�sum(a<sub>i</sub>y<sub>i</sub>) = 0 �ɵã�
        a<sub>1</sub>y<sub>1</sub> + a<sub>2</sub>y<sub>2</sub> + sum<sub>i>=3</sub>(a<sub>i</sub>y<sub>i</sub>) = 0
        �� sum<sub>i>=3</sub>(a<sub>i</sub>y<sub>i</sub>) = -C �ã�
            a<sub>1</sub> = y<sub>1</sub>( C - a<sub>2</sub>y<sub>2</sub>)
            ͨ�������ɵã�
                C = a<sub>1</sub><sup>old</sup>y<sub>1</sub> + a<sub>2</sub><sup>old</sup>y<sub>2</sub>
    � L<sup>'</sup>(a<sub>2</sub>) = 0
    �֣�
        f(x) = w<sup>T</sup>x<sub>i</sub> + b
             = sum(a<sub>i</sub>y<sub>i</sub>x<sub>i</sub><sup>T</sup>x)
    �ã�
        a<sub>2</sub>(k<sub>1</sub><sub>1</sub> + k<sub>2</sub><sub>2</sub> - 2k<sub>1</sub><sub>2</sub>) 
        = y<sub>2</sub>(y<sub>2</sub> - y<sub>1</sub> + a<sub>1</sub><sup>old</sup>y<sub>1</sub>k<sub>1</sub><sub>1</sub> + a<sub>2</sub><sup>old</sup>y<sub>2</sub>k<sub>1</sub><sub>1</sub> - a<sub>1</sub><sup>old</sup>y<sub>1</sub>k<sub>1</sub><sub>2</sub> - a<sub>2</sub><sup>old</sup>y<sub>2</sub>k<sub>1</sub><sub>2</sub> + f(x<sub>1</sub>) - a<sub>1</sub><sup>old</sup>y<sub>1</sub>k<sub>1</sub><sub>1</sub> - a<sub>2</sub><sup>old</sup>y<sub>2</sub>k<sub>1</sub><sub>2</sub> - b - f(x<sub>2</sub>) + a<sub>1</sub><sup>old</sup>y<sub>1</sub>k<sub>1</sub><sub>2</sub> + a<sub>2</sub><sup>old</sup>y<sub>2</sub>k<sub>2</sub><sub>2</sub> + b))
        =  y<sub>2</sub>((f(x<sub>1</sub>) - y<sub>1</sub>) - (f(x<sub>2</sub>) - y<sub>2</sub>) + a<sub>2</sub><sup>old</sup>y<sub>2</sub>(k<sub>1</sub><sub>1</sub> +  k<sub>2</sub><sub>2</sub> - 2k<sub>1</sub><sub>2</sub>))
        = y<sub>2</sub>(E1 - E2 + va<sub>2</sub><sup>old</sup>y<sub>2</sub>)
    ��ã�
        a<sub>2</sub><sup>new</sup> = a<sub>2</sub><sup>old</sup> + y<sub>2</sub>(E1 - E2) / v
        a<sub>1</sub><sup>new</sup> = y<sub>1</sub>( C - a<sub>2</sub><sup>new</sup>y<sub>2</sub>)
   
   
</pre>
<p>
�ɵ�a*, ��������֪��������һ��a<sub>j</sub>* > 0, �Դ� j �У� 
</p>
<pre>
    y<sub>j</sub> (w * X<sub>j</sub> + b) - 1 = 0
</pre>
<p>
���Եõ���
</p>
<pre>
    w* = sum(a<sub>i</sub>* y<sub>i</sub> x<sub>i</sub>)
    b* = y<sub>j</sub> - sum(a<sub>i</sub>* y<sub>i</sub> x<sub>i</sub> * x<sub>j</sub>)
</pre>
</div>
<div>
<p>
��������ѵ������(x<sub>i</sub>, y<sub>i</sub>)  ������ a<sub>i</sub> = 0 ���� y<sub>j</sub> (w * X<sub>j</sub> + b) - 1 = 0 ��<br />
�� a<sub>i</sub> = 0 ���������������������ģ�Ͳ�����ʽ���г��֡��� a<sub>i</sub> = 0 ������� y<sub>j</sub> (w * X<sub>j</sub> + b) - 1 = 0 ��<br />
����Ӧ��������λ��������߽��ϣ���һ��֧������
</p>
<b><i>ѵ����ɺ󣬴󲿷ֵ�ѵ������������Ҫ����������ģ�ͽ���֧�������йء�</i></b>
<p>
��ʵ���У���������ȫ�����пɷ֣��Դ�������������, ʹ�ã�
</p>
<pre>
    y<sub>j</sub> (w * X<sub>j</sub> + b) - 1 > 0
</pre>
<p>
����hinge��ʧ�� ��ԭ�Ż������дΪ��
</p>
<pre>
    Min<sub>w, b, q</sub> = 1 / 2 * ||w||<sup>2</sup> + C * sum(q<sub>i</sub>)   
    s.t. y<sub>j</sub> (w * X<sub>j</sub> + b) - 1 > 0
</pre>
<p>
����qΪ�ɳڱ����� q = 1 - y<sub>j</sub> (w * X<sub>j</sub> + b)�� ��һ��hinge��ʧ����
<br />
C > 0 Ϊ�ͷ�����
</p>
<p>
�ܽ᣺ 
</p>
<pre>
    1. ����ѵ�����ݼ���������볬ƽ��ͷ�����ߺ���
    2. ѡ��ͷ�����c�����첢���͹���ι滮���⣬ �õ����Ž�a*
    3. ����ó�������ߺ���
</pre>
</div>
</div>

<h3>������svm</h3>
<div>
    <p>
        ԭ������������֧��������ѧϰ�Ķ�ż�����Ŀ�꺯���ͷ�����ߺ�����ֻ�漰ʵ����ʵ��֮����ڻ������Բ���Ҫ��ʽ��ָ�������Ա任�������ú˺����滻���е��ڻ�
    </p>    
    <p>
        K(x, z) = O(x) . O(z), ������ռ䵽�����ռ��ӳ�� 
    </p>
    
    
</div>