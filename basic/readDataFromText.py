import numpy as np

# world_alcohol=np.genfromtxt("world_alcohol.txt",delimiter=",",dtype=str)
# print(type(world_alcohol))
# print(world_alcohol)
# print(help(np.genfromtxt))

# vector=np.array([5,10,15,20])
# matrix=np.array([[5,10,15],[20,25,30],[35,40,45]])
# print(vector)
# print(matrix)
#
# print(matrix.shape)
# print(np.array(200).shape)


'''
numpy的数据类型保持一致
'''
# numbers=np.array([1,2,3,4,5.0])
# print(numbers)
# print(numbers.dtype)

'''
numpy的下标操作
'''
# world_alcohol=np.genfromtxt("world_alcohol.txt",delimiter=",",dtype=str,skip_header=1)
# print(world_alcohol)
# print(world_alcohol[1,1]) #第一行的第一列
# print(world_alcohol[2,0])


# vector=np.array([5,10,15,20,10,34,2])
# print(vector[0:3])
# matrix=np.array([[5,10,15],[20,25,30],[35,40,45]])
# print(matrix[:,1])
# print(type(matrix[:,1]))
# equal_to_ten=vector==10
# print(vector[equal_to_ten])
# '''
# 找出矩阵的某一行,某一列等于一个值的那一行数值。
# '''
# second_column_25=(matrix[:,1]==25)
# print(second_column_25)
# print(matrix[second_column_25,:])


'''
两个vector之间的与或操作
'''
# vector=np.array([5,10,15,20,10,34,2])
# equal_to_ten_or_five=(vector==5) | (vector==10)
# print(equal_to_ten_or_five)
# print(vector[equal_to_ten_or_five])
# equal_to_ten_or_five=(vector==5) & (vector==10)
# print(equal_to_ten_or_five)
# print(vector[equal_to_ten_or_five])


'''
类型的装换
'''
# vector=np.array(["12.3","2","3"])
# print(vector.dtype)
# print(vector)
#
# vector=vector.astype(float)
# print(vector.dtype)
# print(vector)


'''
numpy的求和操作
'''
# matrix=[[5,10,15],
#         [20,25,30],
#         [35,40,45]]
#
# print(np.sum(matrix,axis=1))#axis 指定谁,那一维度就会消失。
# print(np.sum(matrix,axis=0))
#
# matrix=np.arange(24).reshape(2,3,4)
# print(matrix)
#
# print(np.sum(matrix,axis=0))
# print(np.sum(matrix,axis=1))
# print(np.sum(matrix,axis=2))


a=np.arange(15).reshape(3,5)
print(a)

print(a.shape)
print(a.ndim)
print(a.dtype.name)