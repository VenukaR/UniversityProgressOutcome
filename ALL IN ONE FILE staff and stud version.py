#all in one
#2 parts 1  student version
# 2 and 3 staff version multiple outcome with common histrogram ,list, dict and optional text file

progress_count = 0
trailer_count = 0
retriever_count = 0
exclude_count = 0

student_marks = {}

progress_list = []
trailer_list = []
retriever_list = []
exclude_list = []

stud = [1]
staff_only_text = [3]
staff_all = [2, 3]
stud_and_staff = [1, 2, 3]


# UDF validation
def validation1(msg):
    while True:
        try:
            mark = int(input(msg))
            if mark not in range(0, 140, 20):
                print('Out of range')
                continue
            break
        except ValueError:
            print('Integer Required')
            continue
    return mark

#user define function for file writing
def file_write(alist, output):
    for mark_set in alist:
        text_file.write(output)
        text_file.write(str(mark_set[0]))
        text_file.write(', ')
        text_file.write(str(mark_set[1]))
        text_file.write(', ')
        text_file.write(str(mark_set[2]))
        text_file.write('\n')


# it all start here
print(
    'Hello!,\n |Press "1" if you are a Student |\n |Press "2" if you are a staff member(Multiple Progress Outcome with Histrogram+ input lists) |\n |Press "3" if you are a staff member(Multiple Progress Outcomes With Histrogram And Text File) |\n')
while True:
    try:
        answer = int(input('Answer : '))
        if answer not in stud_and_staff:
            print('Try Again')
            continue
        else:
            while True:  # only 3 inputs 1,2,3
                if answer in stud_and_staff:
                    while True:
                        if answer in staff_all:
                            while True:
                                student_id = input('Enter Student ID: ')
                                if len(student_id) == 8 and student_id[0].lower() == 'w':

                                    if student_id.lower() in student_marks:
                                        print('You have entered the same Student ID before!')

                                        continue

                                    else:
                                        break
                                else:
                                    print('The Student ID needs 8 characters (Example : wXXXXXXX)')
                                    continue

                        if answer in stud_and_staff:
                            while True:
                                pass_ = validation1('Plesase enter your credit pass :')
                                defer = validation1('Plesase enter your credit defer :')
                                fail = validation1('Please enter your credit fail :')
                                if pass_ + defer + fail != 120:
                                    print('Total incorrect')
                                    continue
                                else:
                                    if pass_ == 120:
                                        print('Progress')
                                        if answer in staff_all:
                                            progress_count += 1
                                            progress_list.append([pass_, defer, fail])
                                            student_marks[student_id] = "Progress -", pass_, defer, fail
                                    elif pass_ == 100:
                                        print('Progress (module trailer)')
                                        if answer in staff_all:
                                            trailer_count += 1
                                            trailer_list.append([pass_, defer, fail])
                                            student_marks[student_id] = "Progress (module trailer) -", pass_, defer, fail

                                    elif pass_ + defer >= fail:
                                        print('Do not Progress - module retriever')
                                        if answer in staff_all:
                                            retriever_count += 1
                                            retriever_list.append([pass_, defer, fail])
                                            student_marks[student_id] = "Module retriever -", pass_, defer, fail


                                    elif pass_ + defer < fail:
                                        print('Exclude')
                                        if answer in staff_all:
                                            exclude_count += 1
                                            student_marks[student_id] = "Exclude -", pass_, defer, fail
                                            exclude_list.append([pass_, defer, fail])

                                    break

                        if answer in staff_all:
                            while True:
                                print('\n Would  you like to enter another set of data?')
                                final_input = str(input("Enter 'y' for yes or 'q' to quit and view results:"))
                                print('\n')
                                if final_input.lower() == 'q':
                                    break
                                elif final_input.lower() == 'y':
                                    break
                                else:
                                    continue
                            if final_input.lower() == 'y':
                                continue
                            elif final_input.lower() == 'q':
                                if answer in staff_all:

                                    print("-" * 60, "\nHistrogram")
                                    print('Progress', progress_count, "   :", '*' * progress_count)
                                    print('Trailer', trailer_count, "    :", '*' * trailer_count)
                                    print('Retriever', retriever_count, "  :", '*' * retriever_count)
                                    print('Excluded', exclude_count, "   :", '*' * exclude_count)
                                    tot = progress_count + retriever_count + trailer_count + exclude_count
                                    print('\n', tot, 'outcomes in total.\n', '-' * 60)

                                    # part 2 (list )
                                    print("\n\nPart 2 (List):\n")
                                    for mark_set in progress_list:
                                        print("Progress -", mark_set[0], ",", mark_set[1], ",", mark_set[2])
                                    for mark_set in trailer_list:
                                        print("Progress (module trailer) -", mark_set[0], ",", mark_set[1], ",",
                                              mark_set[2])
                                    for mark_set in retriever_list:
                                        print("Module retriever -", mark_set[0], ",", mark_set[1], ",", mark_set[2])
                                    for mark_set in exclude_list:
                                        print("Exclude -", mark_set[0], ",", mark_set[1], ",", mark_set[2])

                                    print('\n\npart 4')

                                    for (key, value) in student_marks.items():
                                        print(key, ":", value[0], value[1], ',', value[2], ',', value[3], ' ', end=(""))

                                    # if the user use No 3 option(+text file)
                                    if answer in staff_only_text:
                                        print(
                                            '\n\nYou Multiple Outcome Text file has been created , check your folder(report.txt)\n')
                                        # part3

                                        text_file = open('report.txt', 'w')
                                        text_file.write('Part 3 \nHere Is Your Report\n')

                                        # progress write

                                        file_write(progress_list, "Progress - ")
                                        file_write(trailer_list, "progress(module trailer)  -")
                                        file_write(retriever_list, "Module retriever - ")
                                        file_write(exclude_list, "Exclude -  ")

                                        text_file.close()

                                break # while true staff
                          
                        if answer in stud:
                            break
                        break #3rd while

                break #2nd while
            break #1 while


    except ValueError:
        print('Integer Required (1,2,3)')
        continue
