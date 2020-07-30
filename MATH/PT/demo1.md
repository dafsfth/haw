<h2>随机变量的数字特征</h2>
<div class="1">
    <h4>1.数学期望</h4>
    <pre>
        E(x) = sum(x<sub>i</sub>p<sub>i</sub>)
               |<sub>-oo</sub><sup>+oo</sup> xf(x) dx
    </pre>
    <p>
        性质：
    </p>
    <pre>
        1. c是常数， E(c)  = c
        2. x是一个随机变量， c是常数，  E（cx） = CE(x)
        3. x, y 是两个随机变量   E（x + y） = E(x) + E(y)
        4. 设x, y是独立的随机变量  E（xy） = E(x) * E(y)
    </pre>
</div>
<hr/>
<div class="2">
     <h4>2.数学方差</h4>
     <pre>
        D(x) = E(x<sup>2</sup>) - E(x)<sup>2</sup>
     </pre>
     <p>
        性质
     </p>
     <pre>
        1. c是常数   D(c) = 0
        2. x是随机变量，c是常数，  D（cx） = c<sup>2</sup> D（x）      D(x + c)  = D(x)
        3. x, y 是两个随机变量：  D(x + y) = D(x) + D(y) + 2cov(x, y) , 若x, y 相互独立，D(x + y) = D(x) +D(y)
        4. p(x = E(x)) = 1  => D(x) = 0
     </pre>
     <p>
        切比雪夫不等式：
     </p>
     <pre>
        p (|x - E| >= s) <= D<sup>2</sup> / s<sup>2</sup>
        p (|x - E| < s) >= 1 -  D<sup>2</sup> / s<sup>2</sup>
     </pre>
</div>
<hr/>
<div class="3">
     <h4>3.协方差及相关系数</h4>
     <pre>
        cov(x, y) = E{[x - E(x)][y - E(y)]} = E(xy) - E(x)E(y)
        P<sub>x, y</sub> = cov(x, y) / (D(x) * D(y))<sup>1/2</sup>
     </pre>
     <p>
        性质1：
     </p>
     <pre>
        cov(ax, by) = abCov(x, y)
        cov(x<sub>1</sub> + x<sub>2</sub>, y) = cov(x<sub>1</sub>, y) + cov(x<sub>2</sub>, y)
     </pre>
     <p>
        性质2：
     </p>
     <pre>
        |P<sub>x, y</sub>| <= 1
     </pre>
     <p>
        P<sub>x, y</sub> = 0, x, y 不相关<br />
     </p>
     <p>
        <b><i>
            cov(x, y) = 0  == > x, y不相关<br/>
            相互独立   ==》   不相关<br/>
            当（x， y）服从正态分布时， x, y 不相关  == x, y 相互独立
         </i></b>
     </p>
</div>
<hr/>
<div class="4">
     <h4>4.矩， 协方差矩阵</h4>
     <pre>
        1. k阶原点矩   E（x<sup>k</sup>）                     k=1, ==> E(x)
        2. k阶中心矩   E([x - E(x)]<sup>k</sup>)             k=2, ==> D(x)
        3. k+l阶混合中心距  E{[x - E(x)]<sup>k</sup>[y - E(y)]<sup>l</sup>}   k, l=2  ==> cov(x, y)
     </pre>
     <p>
        协方差矩阵：
     </p>
     <pre>
        C<sub>i</sub><sub>j</sub> = cov(x<sub>i</sub>, x<sub>j</sub>)
                                  = E{[x<sub>i</sub> - E(x<sub>i</sub>)][x<sub>j</sub> - E(x<sub>j</sub>)]}
     </pre>
</div>
<hr/>
<div class="5">
     <h4>5.几种常见分布的期望和方差</h4>
     <div class="51">
        <pre>
            1. 0-1分布：               E(x) = p,                D(x) = 1 - p
            2. 二项分布x-B(n, p)：      E(x) = np,               D(x) = np(1 - p)
            3. 泊松分布x-P(q)：         E(x) = q,                D(x) = q
            4. 均匀分布x-U(a, b)        E(x) = (a + b) / 2       D(x) = (b - a)<sup>2</sup> / 12
            5. 指数分布                 E(x) = o                 D(x) = o<sup>2</sup>
            6.正态分布x-N（E, D）        E(x) = E,                D(x) = D
        </pre>
     </div>
     <div class="52">
        <p>
            例：
        </p>
        <pre>
            若x-N(1, 3), y-N(2, 4), 且x，y相互独立， 则z = 2x - 3y 也服从正态分布
            E(z) = 2 x 1 - 3 x 2 = -4
            D(z) = 4D(x) + 9D(y) = 48
        </pre>
     </div>
</div>