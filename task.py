tasks= []
task_name=input('Enter your tasks: ')
task = {
    'task' : task_name,
    'status' : False}
tasks.append(task)
print('Your tasks: ', tasks)
for task in tasks:
    status = 'completed' if task['status'] else 'not completed'
    print('Task:', task['task'],  'status:', status)

task_find= input('what tasks have been completed?')
for t in tasks:
    if t['task'] == task_find:
        t['status'] = True
print('Updated tasks: ', tasks)