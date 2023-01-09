import numpy as np
from scipy.cluster.vq import kmeans2,vq
class PQ(object):
    '''
    pq主要是检索阶段数据库的向量
    初始的向量的维度为 D，要压缩到 M 向量
    每个子向量可以 压缩到一个简单的 int型的向量 ，并且由Ks 质心
    对于query，给一个新的D维度的向量，计算距离
    并且通过 asymmetric distance 非对称距离进行优化

    这里的所有 float用 float32
    
    M(int) 子空间的数量
    Ks(int) 每个子空间里面的质心数量(一般是256，所以每个子向量会被压缩到bits=1 uint8)


    M 子空间数量
    Ks 每个子空间的质心数量
    Ds int 子空间向量的维度  Ds = D/M 就是每个空间向量的长度
    '''
    def __init__(self,M,Ks = 256) -> None:
        self.M = M
        self.Ks = Ks

        self.code_dtype = np.uint8
        if self.Ks > 256:
            self.Ks = np.uint16

        self.codewords = None
        self.Ds = None

        print("M {} Ks {}  code_type{}".format(M,Ks,self.code_dtype))
    def __eq__(self, __o: object) -> bool:
        pass
    def fit(self,vecs,iter=20, seed=123):
        '''
            这里是
        ''' 
        assert vecs.dtype == np.float32
        assert vecs.ndim == 2

        N,D = vecs.shape

        self.Ds = int(D/self.M)

        self.codewords = np.zeros((self.M,self.Ks,self.Ds),dtype=np.float32)

        for m in range(self.M):
            print("Training the subspace: {}/{}".format(m,self.M))
            vecs_sub = vecs[:,m*self.Ds:(m+1)*self.Ds]
            self.codewords[m], _ = kmeans2(vecs_sub, self.Ks, iter=iter, minit="points")
        return self
    def encode(self, vecs):
        """Encode input vectors into PQ-codes.
        Args:
            vecs (np.ndarray): Input vectors with shape=(N, D) and dtype=np.float32.
        Returns:
            np.ndarray: PQ codes with shape=(N, M) and dtype=self.code_dtype
        """
        assert vecs.dtype == np.float32
        assert vecs.ndim == 2
        N, D = vecs.shape
        assert D == self.Ds * self.M, "input dimension must be Ds * M"

        # codes[n][m] : code of n-th vec, m-th subspace
        codes = np.empty((N, self.M), dtype=self.code_dtype)
        for m in range(self.M):
            print("Encoding the subspace: {} / {}".format(m, self.M))
            vecs_sub = vecs[:, m * self.Ds : (m + 1) * self.Ds]
            codes[:, m], _ = vq(vecs_sub, self.codewords[m])

        return codes

    def decode(self, codes):
        """Given PQ-codes, reconstruct original D-dimensional vectors
        approximately by fetching the codewords.
        Args:
            codes (np.ndarray): PQ-cdoes with shape=(N, M) and dtype=self.code_dtype.
                Each row is a PQ-code
        Returns:
            np.ndarray: Reconstructed vectors with shape=(N, D) and dtype=np.float32
        """
        assert codes.ndim == 2
        N, M = codes.shape
        assert M == self.M
        assert codes.dtype == self.code_dtype

        vecs = np.empty((N, self.Ds * self.M), dtype=np.float32)
        for m in range(self.M):
            vecs[:, m * self.Ds : (m + 1) * self.Ds] = self.codewords[m][codes[:, m], :]

        return vecs
    

import pickle
f = open('./mnist.pkl','rb')
data = pickle.load(f)
f.close()
print(data)
train_d = data['train_img']
print(train_d.shape)
# Instantiate with M=8 sub-spaces
pq = PQ(M=8)

train_d =np.array(train_d,dtype=np.float32)
print(train_d.shape)
# Train codewords
pq.fit(train_d)

# Encode to PQ-codes
#X_code = pq.encode(X)  # (10000, 8) with dtype=np.uint8
#print(X_code)
# Results: create a distance table online, and compute Asymmetric Distance to each PQ-code 
#dists = pq.dtable(query).adist(X_code)  # (10000, ) 