# Задача: Создай класс Task, который позволяет управлять задачами (делами). У задачи должны быть атрибуты:
# описание задачи, срок выполнения и статус (выполнено/не выполнено). Реализуй функцию для добавления задач,
# отметки выполненных задач и вывода списка текущих (не выполненных) задач.
class Task:
    def __init__(self, describe, term, status):
        self.describe = describe
        self.term = term
        self.status = status

class Task_manager:
    def __init__(self):
        self.task_list = []

    def new_task(self, descibe, term, status):
        
