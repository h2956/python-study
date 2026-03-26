# Excel版学生管理系统

# 导入库
from openpyxl import Workbook, load_workbook
import os

from new_list import save_to_file

# 全局变量： 存所有学生
students = []

# ----------------------------
# 1. 初始化 Excel 文件(没有就创建)
# ----------------------------

def init_excel():
    # 如果文件不存在，创建一个带表头的 Excel
    if not os.path.exists("学生表.xlsx"):
        wb = Workbook()
        ws = wb.active
        ws.append(["姓名","年龄","成绩"]) # 表头
        wb.save("学生表.xlsx")
        print("首次运行已创建 学生表.xlsx")

# ----------------------------
# 2. 从 Excel 读取所有学生
# ----------------------------

def load_from_excel():
    global students
    wb = load_workbook("学生表.xlsx")
    ws = wb.active
    students.clear()
    for row in ws.iter_rows(min_row = 2,values_only=True):
        name , age , score = row
        stu = {
            "name" : name,
            "age" : age,
            "score" : score
        }
        students.append(stu)
    print("已从 Excel 加载学生数据")

# ----------------------------
# 3. 保存所有学生回 Excel
# ----------------------------

def save_to_excel():
    wb = Workbook()
    ws = wb.active
    # 再写表头
    ws.append(["姓名","年龄","成绩"])
    # 再写所有学生
    for stu in students:
        ws.append([stu["name"],stu["age"],stu["score"]])
        wb.save("学生表.xlsx")

# ----------------------------
# 4. 添加学生
# ----------------------------

def add_student():
    name = input("姓名：")
    age = input("年龄：")
    score = input("成绩: ")
    stu = {
        "name" : name,
        "age" : age,
        "score" : score
    }
    students.append(stu)
    save_to_excel()
    print("添加成功！\n")

# ----------------------------
# 5. 查看所有学生
# ----------------------------

def show_all():
    if not students:
        print("暂无学生信息！\n")
        return
    print("------ 所有学生------")
    for i,stu in enumerate(students,1):
        print(f"{i},姓名：{stu["name"]},年龄：{stu["age"]},成绩{stu["score"]}")
    print()

# ----------------------------
# 6. 查找学生
# ----------------------------

def find_student():
    name = input("输入要查找的姓名：")
    for stu in students:
        if stu["name"] == name:
            print(f"找到了，{stu["name"]},年龄：{stu["age"]},成绩：{stu["score"]}")
            print()
            return
        print("未找到该学生！\n")

# ----------------------------
# 7. 删除学生
# ----------------------------

def delete_student():
    name = input("输入要删除的姓名：")
    for stu in students:
        if stu["name"] == name:
            stu.remove(stu)
            print(f"已删除{name}\n")
            return
    print("未找到该学生！\n")

# ----------------------------
# 8. 修改成绩
# ----------------------------

def modify_score():
    name = input("输入要修改成绩的学生姓名：")
    for stu in students:
        if stu["name"] == name:
            new_score = input("输入修改后的成绩：")
            stu["score"] = new_score
            save_to_excel()
            print("修改成功！\n")
            return
    print("未找到该学生！\n")

# ----------------------------
# 9. 程序入口
# ----------------------------

if __name__ == '__main__':
    init_excel()
    load_from_excel()
    while True:
        print("------ 学生管理系统 ------")
        print("1. 添加学生")
        print("2. 查看所有学生")
        print("3. 查找学生")
        print("4. 删除学生")
        print("5. 修改成绩")
        print("6. 退出")
        choice = input("请输入序号：")
        if choice == "1":
            add_student()
        elif choice == "2":
            show_all()
        elif choice == "3":
            find_student()
        elif choice == "4":
            delete_student()
        elif choice == "5":
            modify_score()
        elif choice == "0":
            print("已退出，数据已保存到 Excel")
            break
        else:
            print("输入错误，请重新输入\n")








