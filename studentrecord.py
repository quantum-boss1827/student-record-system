def add_students():
    name = input('Enter Student name: ').title()
    scores = []
    print('\nEnter 3 scores')
    
    for i in range(3):
        while True:
            try:             
                score = float(input('Enter score: '))
                scores.append(score) 
                break
            except ValueError:
                print('Invalid input,  Enter a number')
    avg = round(sum(scores) / len(scores), 2)
    if avg >= 70:
        grade = 'A'
    elif avg >= 60:
        grade = 'B'
    elif avg >= 50:
        grade = 'C'
    else:
        grade = 'F'        
    with open('results.txt', 'a') as file:
        file.write(f'Student Name: {name} - Average: {avg} - Grade: {grade}\n')
    print(f'{name} and his/her result has been saved!')
    
def view_students():
    try:
        with open('results.txt', 'r') as file:
                 
            for line in file:                                
                print(line.strip())                          
    except:
        print('No record found')
        
def search_students():
        name = input('Enter name to search: ').title()
        try:
            with open('results.txt', 'r') as file:
                for line in file:
                    parts = line.split(' - ')
                    student_name = parts[0].replace('Student Name: ', '')
                    print("Raw line:", line)
                    print("Split:", parts)
                    print("Name extracted:", student_name)
                    if name == student_name:
                        print('Found:', line.strip())
                        return 
            print('Student not found')
        except:
            print('No record found')

def delete_students():
    name = input('Enter name to delete: ').title()
    
    choice = input('Are you sure you want to delete (yes/no): ').strip().lower()
    found = False 
    if choice == 'yes':
        try:
            with open('results.txt', 'r')as file:
                lines = file.readlines()
            new_lines = []
            for line in lines:   
                parts = line.split(' - ')
                student_name = parts[0].replace('Student Name: ', '')
                if name == student_name:
                    found = True
                else:
                    new_lines.append(line)
            if found:
                print(f'{name} deleted!')
            else:
                print(f'{name} not found! ')                                                                                                       
                
            with open('results.txt', 'w') as file:
                file.writelines(new_lines)                                                                                    
                    
        except:
            print('No records found')
                
    else:
         print('Deleting process cancelled')                        

while True:
    print('\nStudent Result System')
    print('\nPlease, enter one of the options below\n1. Add Student\n2. View Students\n3. Search Students\n4. Delete Students\n5. Exit')
    choice = input('Enter: ').strip()
    if choice == '1':
        add_students()
    elif choice == '2':
        view_students()
    elif choice == '3':
        search_students()
    elif choice == '4':
        delete_students()
    elif choice == '5':
        print('Bye!')
        break 
    else:
        print('Invalid Input')