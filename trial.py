import tkinter as tk
import sqlite3

##有關tkinter的部份(展示層)##

# 建立主視窗
root = tk.Tk()
root.title("tkinter for layer learning")   # 設定視窗標題
root.geometry("300x350")                   # 設定視窗大小

# 👉 建立標籤與輸入框：Student ID
lbl_id = tk.Label(root, text="Student ID:")
lbl_id.pack(pady=(15, 5))                  # 加入垂直間距
entry_id = tk.Entry(root, width=25)
entry_id.pack()

# 👉 建立標籤與輸入框：Student Name
lbl_name = tk.Label(root, text="Student Name:")
lbl_name.pack(pady=(10, 5))
entry_name = tk.Entry(root, width=25)
entry_name.pack()

conn = sqlite3.connect('Student.db')
cursor = conn.cursor()

# 👉 建立按鈕事件的邏輯
def create_student():
    """
    按下按鈕後執行的函式
    目的：
    1. 取得使用者輸入的 Student ID 與 Student Name。
    2. 在終端機印出（模擬將資料傳給下一層）。
    """
    student_id = entry_id.get()
    student_name = entry_name.get().lower()
        
    cursor.execute("INSERT INTO DB_student (db_student_id, db_student_name) VALUES(?, ?)", (student_id, student_name))
    conn.commit()

    ## 有關Python(應用層)的部份 ##
    # 印出結果（這裡可視為資料傳到應用層或資料層的動作）
    print("Student ID: {}".format(student_id))
    print("Student Name: {}".format(student_name))

    print("-" * 30)  # 分隔線


def overview_student():
    cursor.execute('SELECT * FROM DB_student;')
    records = cursor.fetchall()
    print (records)


# 👉 建立按鈕元件
btn_create = tk.Button(root, text="Create", command=create_student)
btn_create.pack(pady=15)

# 👉 建立按鈕元件
btn_overview = tk.Button(root, text="Overview", command=overview_student)
btn_overview.pack(pady=20)

# 👉 建立按鈕元件
btn_print = tk.Button(root, text="Print")
btn_print.pack(pady=25)

print ('hello world')
print ('hello world2')

# 啟動主迴圈
root.mainloop()

