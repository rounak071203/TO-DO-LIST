print('lets make a To Do List')
todo = []
while True:
    c = input('Type a To-Do item or type "exit" to quit: ').strip().lower()
    if c == 'exit':
        break
    elif c:
        todo.append(c)
    else:
        print('Please enter a valid to-do item.')

print('Your To-Do List:')
for item in todo:
    print(f'- {item}')