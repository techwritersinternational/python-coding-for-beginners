def process_todo_list(filename):
    print("Space Captain's Todo List:")
    print("-" * 30)
   
    with open(filename, 'r') as todo_file:
        for i, line in enumerate(todo_file, 1):
            # Remove leading/trailing whitespace
            task = line.strip()
            
            # Check if task is urgent (starts with *)
            if task.startswith('*'):
                # Remove the * and add (Urgent!) to the end
                task = f"{task[1:]} (Urgent!)"
            
            # Print numbered task
            print(f"{i}. {task}")
                  
    print("-" * 30)


process_todo_list('todo.txt')