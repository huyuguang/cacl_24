给孩子写的计算24点程序

一些难题：   
2 3 5 12  
1 3 4 6  
1 4 5 6  
2 5 5 10  
3 5 7 13  
3 7 9 13  
2 4 10 10  
2 4 7 12  
1 8 12 12  
2 9 13 13  
3 6 6 11  
3 3 5 7  
9 11 12 13  
3 3 8 8  
1 6 6 8  
2 2 10 11  
2 3 8 13  
2 7 7 10  
5 7 11 11  
7 8 10 11  
3 3 7 13  
3 8 8 10  
4 8 8 13  
5 5 7 11  
4 8 8 11  
7 8 8 13  
2 5 7 8  
6 9 9 10  
1 4 7 11  
5 6 9 11 

去掉大小王，一共有52张牌，四个花色的1~13。
一共有 C(16，4) = 1820 种组合。

这是经典的可重复的组合计数问题：n的不同元素取m个，有多少种取法。
n个元素视做n个格子，中间有n-1个板。
把m个相同小球放入格子，视作选取m个数。
多个小球可以放入同一个格子。

格子和球一共有n+m-1个。对其进行全排列，就是(n+m-1)!。
每一种排列都是一种选法。

由于球和格子都是相同的，所以重复数为m!*(n-1)!。
也可以理解成是n+m-1个元素中找m个位置，也即C(n+m-1,m)
