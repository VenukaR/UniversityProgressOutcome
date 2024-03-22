#Author Name- Venuka Ranasinghe
#Purpose - Staff version only part 4 ( dictionary)
progress_count = 0
trailer_count = 0
retriever_count = 0
exclude_count = 0
student_marks = {}

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


while True:
    while True:

        student_id = input('Enter Student ID: ')
        if len(student_id) == 8 and student_id[0].lower() == 'w':
            if student_id.lower() not in student_marks:
                break
            else:
                print('You have entered the same Student ID before!')
        else:
            print('The Student ID needs 8 characters (Example : wXXXXXXX)')
    while True:
        pass_ = validation1('Enter your total PASS credits :')
        defer = validation1('Enter your total DEFER credits :')
        fail = validation1('Enter your total FAIL credits :')
        if pass_ + defer + fail != 120:
            print('Total incorrect')
            continue
        break


        # if sum of sum, defer and fail not equals to 120 repeat again

    if pass_ == 120:
        print('Progress')
        progress_count += 1
        student_marks[student_id] = "Progress -", pass_, defer, fail
    elif pass_ == 100:
        print('Progress (module trailer)')
        trailer_count += 1
        student_marks[student_id] = "Progress (module trailer) -", pass_, defer, fail
    elif pass_ + defer >= fail:
        print('Do not Progress - module retriever')
        retriever_count += 1
        student_marks[student_id] = "Module retriever -", pass_, defer, fail
    elif pass_ + defer < fail:
        print('Exclude')
        exclude_count += 1
        student_marks[student_id] = "Exclude -", pass_, defer, fail

    # here
    while True:
        print('\n Would  you like to enter another set of data?')
        answer = str(input("Enter 'y' for yes or 'q' to quit and view results:"))
        print('\n')
        if answer == 'q':
            break
        elif answer == 'y':
            break
        else:

            continue

    if answer == 'y':
        continue
    elif answer == 'q':
        break
print("-" * 60, "\nHistrogram")
print('Progress', progress_count, "   :", '*' * progress_count)
print('Trailer', trailer_count, "    :", '*' * trailer_count)
print('Retriever', retriever_count, "  :", '*' * retriever_count)
print('Excluded', exclude_count, "   :", '*' * exclude_count)
tot = progress_count + retriever_count + trailer_count + exclude_count
print('\n', tot, 'outcomes in total.\n', '-' * 60)

print('\n\npart 4:')

for (key, value) in student_marks.items():
    print(key, ":", value[0], value[1], ',', value[2], ',', value[3], ' ', end=(""))
