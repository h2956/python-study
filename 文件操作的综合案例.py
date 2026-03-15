#读取文件
f = open("D:/word.txt","r",encoding = "UTF-8")

#命名一个备份文件
f2 = open("D:/word.txt.bak","w",encoding = "UTF-8")

#将文件标记为测试的数据行丢弃
#for循环内容，判断是否为测试不是就用write写出，是测试就用continue跳过
for line in f:
    line = line.strip()

    if line.split("，")[4] == "测试":
        continue


    f2.write(line)
    f2.write("\n")


#关闭文件对象
f.close()
f2.close()