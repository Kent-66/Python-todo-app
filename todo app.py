import tkinter as tk

window = tk.Tk()

window.title("ToDoリスト")
window.geometry("400x500")

label = tk.Label(window, text = "===== ToDo リスト =====")  #画面に文字を表示する部品を作る
label.pack()    #その部品をウィンドウに配置する

entry = tk.Entry(window)    #文字を入力するための箱
entry.pack()

todo_list = tk.Listbox(window)  #ToDoを一覧表示させるための箱
todo_list.pack()

#ToDoを追加する関数
def add_todo():
    task = entry.get()
    todo_list.insert(tk.END, task)  #ToDoを一覧の最後に追加する
    entry.delete(0, tk.END) #入力欄の文字を全部消す（0は入力欄の最初の位置、tk.ENDは最後の位置を表す。）

#ToDoを削除する関数
def delete_todo():
    selected = todo_list.curselection() #リストボックスで今選択されているToDo

    if selected:
        todo_list.delete(selected)
    else:
        print("削除するToDoを選択してください")

    todo_list.delete(selected)  #選択されているToDoを削除

#ToDoを完了させる関数
def complete_todo():
    selected = todo_list.curselection()

    if selected:
        index = selected[0]
        task = todo_list.get(index)

        if not task.startswith("✓"):   #taskの文字が✓から始まっているか
            todo_list.delete(index)
            todo_list.insert(index, f"✓ {task}")
    else:
        print("完了するToDoを選択して下さい")


#ToDo追加ボタン
button = tk.Button(window, text = "ToDoを追加", command = add_todo)
button.pack()

#ToDo削除ボタン
delete_button = tk.Button(window, text = "ToDoを削除", command = delete_todo)
delete_button.pack()

#ToDo完了ボタン
complete_button = tk.Button(window, text = "ToDoを完了", command = complete_todo)
complete_button.pack()


window.mainloop()
