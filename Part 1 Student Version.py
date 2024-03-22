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
    pass_ = validation1('Plesase enter your credit at pass :')
    defer = validation1('Plesase enter your credit at defer :')
    fail = validation1('Please enter your credit at fail :')
    if pass_ + defer + fail != 120:
        print('Total incorrect')
        continue
    else:
        if pass_ == 120:
            print('Progress')
        elif pass_ == 100:
            print('Progress (module trailer)')
        elif pass_ + defer >= fail:
            print('Do not Progress - module retriever')
        elif pass_ + defer < fail:
            print('Exclude')
        break
            
