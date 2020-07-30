<h2>支持向量机</h2>
<h3>1. 线性svm</h3>
<div>
<p>原理：求解能够正确划分数据集并且几何间隔最大的分割超平面</p>
<div>
<p>
对于给定数据集和超平面W*X + b = 0, 则集合样本点(X<sub>i</sub>, y)（x<sub>i</sub>为特征向量， y为标签）的集合空间为：
</p>
<pre>
    r<sub>i</sub> = y<sub>i</sub> * (w * x<sub>i</sub> / ||w|| + b / ||w||)
</pre>
<p>
支持向量到超平面的距离为：           
</p>
<pre>
    r = Min(r<sub>i</sub>)
</pre>
<p>
最大分割超平面： Max(r), 即
</p>
<pre>
    y<sub>i</sub> * (w * x<sub>i</sub> / ||w|| + b / ||w||) >= r
    ==》y<sub>i</sub> * (w * x<sub>i</sub> / ||w|| * r + b / ||w|| * r) >= 1
    ==》y<sub>i</sub> * (w * X<sub>i</sub> + b) >= 1, 其中w = w / ||w|| * r,    b = b / ||w|| * r
</pre>

<pre>
    Max(r) ==> Max(1 / ||w||) ==> Min(1 / 2 * ||w||<sup>2</sup>)
</pre>
<p>
得到如下的含有不等式的凸二次规划问题：
</p>
<pre>
    Min<sub>w, b</sub>   1 / 2 * ||w||<sup>2</sup>  
    s.t.   y<sub>i</sub> * (w * X<sub>i</sub> + b) >= 1 
</pre>
<p>
使用拉格朗日乘子法求解其对偶问题：
</p>
<pre>
    L(w, b, a) = 1 / 2 * ||w||<sup>2</sup> - sum(a<sub>i</sub> * (y<sub>i</sub> * (w * x<sub>i</sub> + b) - 1))
，   其中a<sub>i</sub>为拉格朗日乘子， 且a<sub>i</sub> >= 0
</pre>
<p>
令O(x) = Max<sub>a<sub>i</sub> >= 0</sub> L(w, b. a)， 可以得到：
</p>
<pre>
    O(x) = 1 / 2 * ||w||<sup>2</sup>   , x 在可行域内  （y<sub>i</sub> * (w * X<sub>i</sub> + b) >= 1 ）
            +oo , x 不在可行域内，（y<sub>i</sub> * (w * X<sub>i</sub> + b) <= 1 ）
</pre>

<p>
原约束问题：
</p>
<pre>
    Min<sub>w, b</sub>(O(x)) ==> Min<sub>w, b</sub>(Max<sub>a<sub>i</sub> >= 0</sub>( L(w, b, a))) = p*
</pre>
<p>
使用拉格郎日函数对偶性得：
</p>
<pre>
    Max<sub>a<sub>i</sub> >= 0</sub>(Min<sub>w, b</sub>( L(w, b, a))) = b*
</pre>
<p>
使得 p* = b* 需满足：
</p>
<p>
1.优化问题是图优化<br>
2.KKT条件, == ><br>
<pre>
   a<sub>i</sub> >= 0
   y<sub>i</sub> * (w * X<sub>i</sub> + b) >= 1
   a<sub>i</sub> * (y<sub>i</sub> * (w * x<sub>i</sub> + b) - 1) = 0
</pre>
<p>
L(w, b, a) 对 w, b, 求导， 并令其等于 0得：
</p>
<pre>
    w = sum(a<sub>i</sub> * y<sub>i</sub> * x<sub>i</sub>)
    0 = sum(a<sub>i</sub> * y<sub>i</sub>)
</pre>
<p>
带入拉格朗日目标函数得：
</p>
<pre>
    Min<sub>w, b</sub> L(w, b, a) = -1 / (2 * sum<sub>i</sub>(sum<sub>j</sub>(a<sub>i</sub> * a<sub>j</sub> * y<sub>i</sub> * y<sub>j</sub> * (x<sub>i</sub> . x<sub>i</sub>))) + sum(a<sub>i</sub>) 
</pre>
<p>
最大化并取反使得原问题转化为：
</p>
<pre>
    Minn<sub>a</sub>(1 / (2 * sum<sub>i</sub>(sumn<sub>j</sub>(a<sub>i</sub>a<sub>j</sub>y<sub>i</sub>y<sub>j</sub>(x<sub>i</sub> . x<sub>j</sub>))))) - sum(a<sub>i</sub>)
    s.t.  sum(a<sub>i</sub>y<sub>i</sub>) = 0
          a<sub>i</sub> >= 0
</pre>
<p>
使用序列最小优化算法(SMO) (启发式)
</p>
<pre>
    L = Min 1/ 2(sum<sub>i</sub>(sum<sub>j</sub>(a<sub>i</sub>a<sub>j</sub> y<sub>i</sub>y<sub>j</sub> x<sub>i</sub> . x<sub>j</sub>))) - sum(a<sub>i</sub>) 
    s.t.  sum(a<sub>i</sub>y<sub>i</sub>) = 0
    令: K<sub>i</sub><sub>j</sub> = x<sub>i</sub> . x<sub>j</sub>
    则：
        L(a<sub>1</sub>, a<sub>2</sub>) = 1 / 2(a<sub>1</sub><sup>2</sup>k<sub>1</sub><sub>1</sub> + a<sub>2</sub><sup>2</sup>k<sub>2</sub><sub>2</sub> + 2sum(a<sub>2</sub>a<sub>1</sub>y<sub>2</sub>y<sub>1</sub>) + 2sum<sub>i=1, j>=3</sub>(a<sub>1</sub>y<sub>1</sub>a<sub>j</sub>y<sub>j</sub>K<sub>1</sub><sub>j</sub>) + 2sum<sub>i=2, j>=3</sub>(a<sub>2</sub>y<sub>2</sub>a<sub>j</sub>y<sub>j</sub>K<sub>2</sub><sub>j</sub>) + sum<sub>i>=3</sub>(sum<sub>j>=3</sub>(a<sub>i</sub>a<sub>j</sub> y<sub>i</sub>y<sub>j</sub> k<sub>i</sub><sub>j</sub>))) - a<sub>1</sub> - <sub>2</sub> - sum<sub>j>=3</sub>(a<sub>j</sub>)
    由：sum(a<sub>i</sub>y<sub>i</sub>) = 0 可得：
        a<sub>1</sub>y<sub>1</sub> + a<sub>2</sub>y<sub>2</sub> + sum<sub>i>=3</sub>(a<sub>i</sub>y<sub>i</sub>) = 0
        令 sum<sub>i>=3</sub>(a<sub>i</sub>y<sub>i</sub>) = -C 得：
            a<sub>1</sub> = y<sub>1</sub>( C - a<sub>2</sub>y<sub>2</sub>)
            通过迭代可得：
                C = a<sub>1</sub><sup>old</sup>y<sub>1</sub> + a<sub>2</sub><sup>old</sup>y<sub>2</sub>
    令： L<sup>'</sup>(a<sub>2</sub>) = 0
    又：
        f(x) = w<sup>T</sup>x<sub>i</sub> + b
             = sum(a<sub>i</sub>y<sub>i</sub>x<sub>i</sub><sup>T</sup>x)
    得：
        a<sub>2</sub>(k<sub>1</sub><sub>1</sub> + k<sub>2</sub><sub>2</sub> - 2k<sub>1</sub><sub>2</sub>) 
        = y<sub>2</sub>(y<sub>2</sub> - y<sub>1</sub> + a<sub>1</sub><sup>old</sup>y<sub>1</sub>k<sub>1</sub><sub>1</sub> + a<sub>2</sub><sup>old</sup>y<sub>2</sub>k<sub>1</sub><sub>1</sub> - a<sub>1</sub><sup>old</sup>y<sub>1</sub>k<sub>1</sub><sub>2</sub> - a<sub>2</sub><sup>old</sup>y<sub>2</sub>k<sub>1</sub><sub>2</sub> + f(x<sub>1</sub>) - a<sub>1</sub><sup>old</sup>y<sub>1</sub>k<sub>1</sub><sub>1</sub> - a<sub>2</sub><sup>old</sup>y<sub>2</sub>k<sub>1</sub><sub>2</sub> - b - f(x<sub>2</sub>) + a<sub>1</sub><sup>old</sup>y<sub>1</sub>k<sub>1</sub><sub>2</sub> + a<sub>2</sub><sup>old</sup>y<sub>2</sub>k<sub>2</sub><sub>2</sub> + b))
        =  y<sub>2</sub>((f(x<sub>1</sub>) - y<sub>1</sub>) - (f(x<sub>2</sub>) - y<sub>2</sub>) + a<sub>2</sub><sup>old</sup>y<sub>2</sub>(k<sub>1</sub><sub>1</sub> +  k<sub>2</sub><sub>2</sub> - 2k<sub>1</sub><sub>2</sub>))
        = y<sub>2</sub>(E1 - E2 + va<sub>2</sub><sup>old</sup>y<sub>2</sub>)
    解得：
        a<sub>2</sub><sup>new</sup> = a<sub>2</sub><sup>old</sup> + y<sub>2</sub>(E1 - E2) / v
        a<sub>1</sub><sup>new</sup> = y<sub>1</sub>( C - a<sub>2</sub><sup>new</sup>y<sub>2</sub>)
   
   
</pre>
<p>
可得a*, 由条件可知：至少由一个a<sub>j</sub>* > 0, 对此 j 有： 
</p>
<pre>
    y<sub>j</sub> (w * X<sub>j</sub> + b) - 1 = 0
</pre>
<p>
可以得到：
</p>
<pre>
    w* = sum(a<sub>i</sub>* y<sub>i</sub> x<sub>i</sub>)
    b* = y<sub>j</sub> - sum(a<sub>i</sub>* y<sub>i</sub> x<sub>i</sub> * x<sub>j</sub>)
</pre>
</div>
<div>
<p>
对于任意训练样本(x<sub>i</sub>, y<sub>i</sub>)  ，总有 a<sub>i</sub> = 0 或者 y<sub>j</sub> (w * X<sub>j</sub> + b) - 1 = 0 。<br />
若 a<sub>i</sub> = 0 ，则该样本不会在最后求解模型参数的式子中出现。若 a<sub>i</sub> = 0 ，则必有 y<sub>j</sub> (w * X<sub>j</sub> + b) - 1 = 0 ，<br />
所对应的样本点位于最大间隔边界上，是一个支持向量
</p>
<b><i>训练完成后，大部分的训练样本都不需要保留，最终模型仅与支持向量有关。</i></b>
<p>
在实际中，不存在完全的现行可分，对此引出“软间隔”, 使得：
</p>
<pre>
    y<sub>j</sub> (w * X<sub>j</sub> + b) - 1 > 0
</pre>
<p>
采用hinge损失， 将原优化问题改写为：
</p>
<pre>
    Min<sub>w, b, q</sub> = 1 / 2 * ||w||<sup>2</sup> + C * sum(q<sub>i</sub>)   
    s.t. y<sub>j</sub> (w * X<sub>j</sub> + b) - 1 > 0
</pre>
<p>
其中q为松弛变量， q = 1 - y<sub>j</sub> (w * X<sub>j</sub> + b)， 即一个hinge损失函数
<br />
C > 0 为惩罚参数
</p>
<p>
总结： 
</p>
<pre>
    1. 输入训练数据集，输出分离超平面和分类决策函数
    2. 选择惩罚参数c，构造并求解凸二次规划问题， 得到最优解a*
    3. 计算得出分类决策函数
</pre>
</div>
</div>

<h3>非线性svm</h3>
<div>
    <p>
        原理：由于在线性支持向量机学习的对偶问题里，目标函数和分类决策函数都只涉及实例和实例之间的内积，所以不需要显式地指定非线性变换，而是用核函数替换当中的内积
    </p>    
    <p>
        K(x, z) = O(x) . O(z), 从输入空间到特征空间的映射 
    </p>
    
    
</div>