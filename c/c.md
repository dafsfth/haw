# 常量与变量
## 1.常量
### 1. 整形常量
    1. 10进制： 以非零开始的数。
    2. 8进制： 以0开头的数。
    3. 16进制： 以0x或0X开头的数
    注： 在c语言中， 只有10进制可以是负数。

### 2. 实型常量（浮点数）
    （1）小数形式：
        由数字。小数点，符号
    （2）指数形式：
        e 或 E 整数
        e的前后必须有数， 且后面必须为整数
        e与其前后的数字简不允许有空格
### 3.字符常量
    一个字符常量占一个字节
### 3.1 转义字符常量
    \t              横向制表符        
    \r              回车
    \b              退格
    \f              走纸换页
    \0              空字符
    \ddd            1-3位8进制数
    \xhh            1-2位16进制数
    注：\数字  表示的是ASCII， 运算的时候是按ASCII的
    字符常量的长度固定为1
### 4.字符串常量
### 5. 符号常量
    # define   符号常量名   常量     
    值不能改变
## 2.变量
###  1.整型变量
    1. 基本型： int         2     
    2. 短整型   short       2
    3. 长整型   long        4
    4. 无符号   unsigned    
    5. unsigned int       0---2^32 - 1
    6. int                -2^31---2^31 - 1
    7. unsigned short     0--- 2^16-1
    8. short             -2^15--- 2^15-1
    9. long          same to int

### 1.1 整形变量的定义
    变量的存储类别   变量的类型名   变量名
### 2.浮点变量
    名称       符号         字节   有效位数
    单精度：  float          4         7
    双精度：  double         8         15
            long double      16
    如果有整数部分超过有效位数： 小数点后面改0

### 3.字符型变量
    char 


# 运算符

## 1.赋值运算符
    可以连续赋值， 但不能连续赋初值
    当两边的类型不匹配时， 会自动类型转换
    整形赋予字符型：  只把低八位赋予字符变量， 其余为丢失
## 2.算术运算符
    在算数运算符中， 只有单目运算符"++", "--" 的结合方向是从右到左的
### 2.1 各种数据类型自动转换原则
    short, char——>int ->  unsigned  -> long  ->  unsigned long -> double  <-  float
### 2.2 自增自减
    自增自减的对象只能是变量
    例： 
        i = 1
        ++i = 2， i = 2
        i++ = 1， i = 2
## 3.关系运算符(relational operator)
    binary operator(双目)
    combination direction:  l -- r
    notes: 
        1. space are not allowed between two charters relational operators. 
           1. 'a'<'b'
        2. '>', '>=', '<', '<=' have a higher priority than '==', '!='
## 4.逻辑运算符
## 5.位运算符
    位运算符的操作对象只能是整形  
    运算符          结合方向  （优先级  高  ———— 低）
      ~                r - l        单目运算符
      <<,>>            l - r
      &                l - r
      ^                 l - r
      |                 l - r
### 5.1 补码
    正数的补码与源码一致
    计算方法：  取反   末位+1
### 5.2 按位与
    计算： 转换为补码， 再计算   有0为0， 全1为1
### 5.3 按位或
    转补码：  有1为1
### 5.4按位取反
    ~1 = 0， ~0 = 1
### 5.5 按位异或
    补码：  相同为0， 不同为1
### 5.6 左移， 右移
    12 << 2 = 12 * 2^2 = 48
    12 >> 2 = 12 / 2^2 = 3


## 6.条件运算符
## 7.逗号运算符
    优先级最低
    整个逗号表达式的值就是最后一个表达式的值
    例： 
        x1 = (3, 4, 5)    x1 = 5
        x2 = 3, 4, 5      x2 = 3
## 指针运算符
### 指针变量
    int *p, *q **r;
    求址： &， 去内容  *；
    注：&的作用对象只能是变量或数组， 不能是常量或表达式
        & 的类型必须和指针变量一致
        运算优先级和++ -- 相同， 结合方向  r - l
    int *p = &a
    (*p) ++     ==   a ++
    *p++        ==  *(p++)
    ++*p        ==  ++ a
    *++p        ==  * (++p) 
## 求字节运算符
## 强制转换运算符
    (类型名)  (表达式)
    例： (int) (x+y)
## 分量运算符
## 下标运算符

# 2.顺序结构程序设计

## 2.1 语句(setence)
### 2.1.1 express statement
### 2.1.2 control statement
### 2.1.3 Function call statement
### 2.1.4 Compound statement(复合)(also call block statement)
### 2.1.5 Empty statement

## 2.2 Input and Output
### 2.2.1 character
    output: putchar()
    input: getchar()
    carefully: 
        1. no data is allowed in () of the getchar() function.
        2. must include file "stdio.h".
        3. the getchar() function can only accept one character at most, so while continuous input two charters need care carriage return(回车符) and space charcter.
### 2.2.2 Format input and output
    Format Charcter:
    d, i:     signed decimal integer
    o:        unsigned octal integer
    x, X:     unsigned hexadecimal integer, x: lowercase  ; X  capitalize;  
    u:        unsigned decimal integer
    c:        one charcter
    s:        string 
    f:        double, float
    e:        index
    g:        automatic selection 'e' or 'f' according to the size of real number.
    Additional 
    l, L      long integer
    h:        short
    m:        the width of data
    n:        for real number: how many decimal place, for string: the number of cahrcters.
    -:        Align left
    Example:
        printf("%8d");   the integer number of output occupies m columns and is right aligned.
        printf("%-8d");   align left.
        printf("%8.2s", "china");     (6 space)ch
        printf("%f");   the integer part is all output and the decimal part is reversed for 6 digits.
    Format Input:
        scanf("", & variable);
        while inputing many numbers, you should separate with 'space', 'tab', 'carriage return'.
        but if is charcter don't need.





# 3. Branch Structure Programming
## 3.1 switch satement
### 3.1.1 format:
    switch(express){
        case constant express1: statement group or space;
        case constant express2: statement group or space;
        default: default statement group;
    }

# 4.Array And Index
    Format: 
        (type of data) name [length]  
        length is symbolic constants or expression of  constants
    the name of array is a address constants.
## 4.1 character array and string
    string : end with '\0'
    use character arrays to stores strings, so the length of string is less 1 than length of character arrays. because string must end with '\0'.
### 4.1.1 the input and output of string
    scanf: scanf("%s", address);
        scanf function can't input the string with space. because it would regard the sign of end.
    printf: printf("%s", address);
    gets:   gets(address);
        end with enter
    puts:   puts(address);
## 4.2 String processing function
### 4.2.1 splicing function: stract
    stract(str1, str2)
    connect the str2 to the end of str1 and cover the '\0'
### 4.2.2 copy function: strcpy
    strcpy(str1, str2)
    replace the str1 with str1
### 4.2.3 string compare function: strcmp
    strcmp(str1, str2);
    if str1 == str2 return 0
    if str1 > str2 return 1
    if str1 < str2 return -1
    the ASCII of first character
    character by character comparison
### 4.2.4 the length of string: strlen
## 4.3 Array And Index
    traversal of array:
    a[i] or a+  ?(1, 2, ... strlen(a) -1)
### 4.3.1 Pointer variable with subscript
    *p = a; so p[1] equivalite a[1]
    *p = &a[2];   p[-2..strlen(a)-3]
### 4.3.2 the address of two_dimensional array
    a[2][2]   'a', 'a+1' have a higher lever than other
    *(a+1) == a[1]
    a[1] + 1 == &a[1][1]
    ================================================
    |  a0  |  a01   | |  a1  |  a11   |
    ==============================================
### 4.3.3  Array Index(Row Pointer)
    int (*p)[4];
    the length if the columns of two_dimensional array.
### 4.3.4 Index Array
    int *p[4];
    same storage type and pointer to the same data type.
    
### 4.3.5 String and Index
    char *str = "hello";
    char *str; str = "hello";  
        printf(str);
    char str[20]; str = "hello"; -------------> it is wrong, because str is a address constant.

    char *p, c[20] = "hello", d[3] = {'a', 'b', 'c'};
    int *q, a = 3, b[3] = {1, 2, 3}, e[2][3] = {1, 2, 3, 4, 5, 6};
    p = "3";
    printf(p);  // -----> 3
    q = &a;
    printf("%d", q);  // ---------> address
    p = c;
    printf(c);   //  ------------hello
    p = &d[0];
    printf("%c\n", p[0]);  // --------->a
    q = &e[0][0];
    printf("%d", q[1]);  // ------------>2



# 5.Function And Index
## 5.1 the storage  category of variable
    the definition of variable:
        1. the data type
        2. storage category----> determine the life cycle of variable.
    1. static
       1. global variable
    2. auto 
       1. local variable
    3. register(寄存器)
       1. local variable
    4. extern
       1. global variable

# 6. Compilation preprocessing
## 6.1 macro definition
    1.none parameter
        define identifier string
        undef
        nesting (嵌套)
            #define p printf
            #define d "%d\n"
            p(d, )
    2. with parameter
       1. #define Sp(n)  n*n
# 7.Structure and common body
## 7.1 structure
### 7.1.1 definition of structure type
    struct name{
        number list
    };
    it a type, no specific data, the system does't allocate the actual memory unit, but when define the variable.
### 7.1.2 body variable of structure
    struct (structure name) (list of variable name)
    intialization of structure variable
    struct stu{
        int num;
        char name[20];
        char sex;
        char addr[40];
    } stu1={1000, "wang li", 'M', "changjiangroad"};
