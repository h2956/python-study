
#有如下列表对象
my_list = ['黑马程序员','传智播客','黑马程序员','传智播客'
        ,'itheima','itcast','itheima','itcast','best']

#定义一个空集合
n1 = set()

#通过for循环遍历列表
for i in my_list:
    #在for循环中将列表元素添加至集合
    n1.add(i)

#得到元素去重后的对象并打印输出
print(n1)