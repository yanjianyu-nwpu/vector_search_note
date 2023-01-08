class PQ(object):
    '''
    pq主要是检索阶段数据库的向量
    初始的向量的维度为 D，要压缩到 M 向量
    每个子向量可以 压缩到一个简单的 int型的向量 ，并且由Ks 质心
    对于query，给一个新的D维度的向量，计算距离
    并且通过 asymmetric distance 非对称距离进行优化，
    '''
    def __init__(self) -> None:
        pass
    