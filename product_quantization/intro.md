# Product Quanzitation

## 0 Intro

​	pq 主要用于简化向量化搜索中的检索阶段，比较朴素的算法是knn，然后pq的算法就是简化knn流程加速检索。

## 1 源码阅读

​	这里分析这个仓库代码: https://github.com/matsui528/nanopq

## 2  asymmetric distance 非对称距离

​	这里的思路是 对于两个质心c0，c1 的距离d是固定的

​	对于新来的点x  ，根据三角形的定律  dc0 + dc1 > d 这里dc0和dc1是x到c0和c1的距离

​	所以只算其中一个，就得到靠近哪个质心

