from django.test import TestCase

from todos.models import Todo

class TodoTest(TestCase):

    def setUp(self):
        Todo.objects.create(title='first todo', body='a body goes here')
    
    def test_title_content(self):
        todo = Todo.objects.get(id=1)
        todo_str = f'{todo.title}'
        self.assertEqual(todo_str, 'first todo')

    def test_body_content(self):
        todo = Todo.objects.get(id=1)
        todo_str = f'{todo.body}'
        self.assertEqual(todo_str, 'a body goes here')
