progress_count = 0
trailer_count = 0
retriever_count = 0
exclude_count = 0


tot=0
# UDF validation
def validation1(msg):
    while True:
        try:
            mark = int(input(msg))
            if mark not in range(0, 140, 20):
                print('Out of range.')
                continue
            break
        except ValueError:
            print('Integer Required')
            continue
    return mark


def print_histogram_table():
    print("Progress", progress_count, "|", "Trailer", trailer_count, "|", "Retriever", retriever_count, "|", "Exclude", exclude_count)
    

   
    

def histogram_print():
    print("\n")
    print("-" * 60)
    print("Vertical Histogram\n")
    print_histogram_table()
    print("\n")
    print(tot, "outcomes in total.")
    print("-" * 60)

close=""

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
                
        elif pass_ == 100:
            print('Progress (module trailer)')
            trailer_count += 1
                

        elif pass_ + defer >= fail:
            print('Do not Progress - module retriever')
            retriever_count += 1
        elif pass_ + defer < fail:
            print('Exclude')
            exclude_count += 1
                
        
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
            tot = progress_count + retriever_count + trailer_count + exclude_count
            histogram_print()
            
        break
           
        

