#1 - iterators
          #0  1  2  3  4
lessons = [1, 2, 3, 4, "Test5", 8, 10, 22, "Serhii", True, 1.0]
iterator = iter(lessons)
#print(iterator)
'''
try:
    print(next(iterator))
    print(next(iterator))
    print(next(iterator))
    print(next(iterator))
    print(next(iterator))
    print(next(iterator))
except StopIteration:
    print("StopIteration")
'''
try:
    print(next(iterator))
    print(next(iterator))
    print(next(iterator))
    for elem in iterator:
        print(f"from for: {elem}")
    print(next(lessons))
except TypeError as te:
    print(te)
    # 2 - counter
    from counter import Counter

    counter = Counter(13)

    '''
    for number in counter:
        print(number)
    '''
    while (True):
        try:
            print(next(counter))
        except StopIteration:
            break
            # 3 - generators
            from generator import Degree

            degree = Degree()
            res = degree.CountDegrees(5, 10)
            for i in res:
                print(i)
                # 4 - decorator
                from decorator import Checker

                checker = Checker()
                # calculate = checker.Check(checker.Calculate)
                digit1 = input("Enter digit1: ")
                digit2 = input("Enter digit2: ")
                operation = input("Operation: ")
                checker.Calculate(f"{digit1}{operation}{digit2}")