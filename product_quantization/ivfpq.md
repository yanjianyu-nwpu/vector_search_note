## IVFPQ

## Intro

近似临近检索 ANN(Approximate Nearest Neighbor)

![img](https://pic3.zhimg.com/80/v2-0228d02bd404e9420f8f86b791c27572_720w.webp)

​	根据pq算法可以用 长度为M的向量，表示为D 的向量；在实际工程中还是需要倒排索引，质心为key对应其中所有的item 。

​	那么怎么较为精确计算的计算和文章的距离 d(x,y)的距离呢，SDC(symmetric case)就是用两个质心的距离d(q(x),q(y))替代，好处是质心的距离都是固定的，坏处是不很精准。

​	用ADC(asymmetric case)比较精准，首先是把 所有的文章转化为和质心的距离，比如质心（2.0，2.0）文章（2.1，2.1）那么存成（0.1，0.1）这样的好处是差别比较小，如果算欧式距离 一平方误差就小了，那么到实时计算的时候只要算 d(x,q(y))。

![image-20230111235326863](C:\Users\15929\AppData\Roaming\Typora\typora-user-images\image-20230111235326863.png)

复杂度大概就是这样了，前面是算vq的过程，后面是算那个簇里面所有的文章的距离。