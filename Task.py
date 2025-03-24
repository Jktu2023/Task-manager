# Задача: Создай класс Task, который позволяет управлять задачами (делами). У задачи должны быть атрибуты:
# описание задачи, срок выполнения и статус (выполнено/не выполнено). Реализуй функцию для добавления задач,
# отметки выполненных задач и вывода списка текущих (не выполненных) задач.
import tkinter as tk

class Task:
    def __init__(self, describe, term, status):
        self.describe = describe
        self.term = term
        self.status = status

class Task_manager:
    def __init__(self):
        self.task_list = []

    def new_task(self, descibe, term, status=False):
        new = Task(descibe, term, status)
        self.task_list.append(new)
        for task in self.task_list:
            if task.status == False:
                print(f'Описание из new: {task.describe}, срок: {task.term}, выполнение: {task.status}')

    def find_task(self, describe):
        for task in self.task_list:
            if task.describe == describe:
                task.status == True
        print(f'Описание из find_task: {task.describe}, срок: {task.term}, выполнение: {task.status}')


    def show_task(self,):
        list_box.delete(0, tk.END) # Очищаем Listbox (list_box) перед загрузкой нового содержимого
        for task in self.task_list:
            if task.status == False:
                print(f'Описание: {task.describe}, срок: {task.term}, выполнение: {task.status}')
                stroka = task.describe + ' до ' + task.term
                list_box.insert(tk.END, stroka.strip())   #  list_box.append(stroka)
                # print('stroka:',stroka)
        return list_box

def add_item(): # по кнопке добавить задачу
    task = task_entry.get() # присваеваем переменной значение из окна поля ввода task_entry
    if task: # если переменная не нулевая
        list_box.insert(tk.END, task) # встаавляем значение в конец списка list_box
        task_entry.delete(0, tk.END) # очищаем поле ввода
        descibe, term = task.split(',')
        manager.new_task(descibe, term, False)

def del_item(): # по кнопке удалиь задачу
    select_task_index = list_box.curselection()
    if select_task_index:
        task_content = list_box.get(select_task_index)  # Получаем текст выбранной задачи
        list_box.delete(select_task_index)
        # task_content = task_content.s
        manager.find_task(task_content)
        # descibe, term = select_task.split(',')
        print('task_content:',task_content)

manager = Task_manager() # создаем экземпляр менеджера задач
manager.new_task('Cделать задание по ООП,', '24/03', False)
manager.new_task('Прочитать книгу по ООП,', '24/03', False)
manager.new_task('Получить консультацию по ООП,', '24/03', True)

print()
# describe = input('Ведите описание задачи - ')
# term = input('Ведите выполнения задачи - ')
# manager.new_task(describe, term, False)


root = tk.Tk()
root.title('Задачи')
root.configure(bg='antique white')

text1 = tk.Label(root, text='Введите задачу:', bg='antique white')
text1.pack(pady=15)

frame = tk.Frame(root, bg='AntiqueWhite3', width=100, height= 10)
frame.pack(ipadx=5, ipady=5, pady=0)

task_entry = tk.Entry(frame, width=70, bg='antique white')
task_entry.pack(pady=5)

list_box = tk.Listbox(frame, width=50, bg='antique white')
list_box = manager.show_task()
list_box.pack(side=tk.LEFT, pady=0)

add_botton = tk.Button(frame, bg='AntiqueWhite2', text='Добавить', command=add_item) #manager.new_task
add_botton.pack(pady=5)

add_botton = tk.Button(frame, bg='AntiqueWhite2', text='Удалить', command=del_item)
add_botton.pack(side=tk.BOTTOM,pady=5)

# add_botton = tk.Button(frame, bg='AntiqueWhite2', text='Добавить', command=)
# add_botton.pack(side=tk.BOTTOM, pady=5)
manager.show_task()
root.mainloop()
