progress_list = []
trailer_list = []
retriever_list = []
exclude_list = []

progress_count = 0
trailer_count = 0
retriever_count = 0
exclude_count = 0
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

while True:
    pass_ = validation1('Enter your total PASS credits :')
    defer = validation1('Enter your total DEFER credits :')
    fail = validation1('Enter your total FAIL credits :')
    if pass_ + defer + fail != 120:
        print('Total incorrect')
        continue
    else:
        if pass_ == 120:
            print('Progress')
            progress_count += 1
            progress_list.append([pass_, defer, fail])
                
        elif pass_ == 100:
            print('Progress (module trailer)')
            trailer_count += 1
            trailer_list.append([pass_, defer, fail])
                

        elif pass_ + defer >= fail:
            print('Do not Progress - module retriever')
            retriever_list.append([pass_, defer, fail])
            retriever_count += 1
            
        elif pass_ + defer < fail:
            print('Exclude')
            exclude_count += 1
            exclude_list.append([pass_, defer, fail])
            
    
                
        
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


        break
           
        

