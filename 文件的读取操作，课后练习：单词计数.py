# f = open("D:/word.txt","r",encoding = "UTF_8")

# l = 0
# for i in f.read().replace("\n"," ").split(" "):
#     if i == "itheima":
#         l += 1
# print(f"f中itheima有{l}个")
# print(f.read().count("itheima"))

#打开文件，以读取模式打开
# f = open("D:/word.txt","r",encoding = "UTF_8")
#方法1：读取全部内容，通过字符串count方法统计itheima单词数量
# countent = f.read()
# count = countent.count("itheima")
# print(count)

#方法2：读取内容，一行一行读取
#判断单词出现的次数并累计
# i = 0
# for line in f:
#     countent = line.strip()
#     count = countent.split(" ")
#     for word in count:
#         if word == "itheima":
#             i += 1
#
#
# print(i)

#关闭文件
# f.close()
