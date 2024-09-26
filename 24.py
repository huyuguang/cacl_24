from fractions import Fraction
import copy

def calc(numbers, current, step):
    # print("try current:", current, step)

    if len(current) == 1:
        if current[0]==Fraction(24):
            return (True,step)
        else:
            return (False,step)
    else:
        nlen = len(current)
        for i in range(nlen-1):
            for j in range(i+1,nlen):
                first = current[i]
                second = current[j]
                # try +
                result = first + second
                this_step = str(first) + "+" + str(second) + "=" + str(result)
                # print(this_step)
                new_current = copy.deepcopy(current)
                del new_current[j]
                new_current[i]=result
                new_step = copy.deepcopy(step)
                new_step.append(this_step)
                success = calc(numbers, new_current, new_step)
                if success[0]: return success
            
                # try -
                result = first - second
                this_step = str(first) + "-" + str(second) + "=" + str(result)
                # print(this_step)
                new_current = copy.deepcopy(current)
                del new_current[j]
                new_current[i]=result
                new_step = copy.deepcopy(step)
                new_step.append(this_step)
                success = calc(numbers, new_current, new_step)
                if success[0]: return success

                if (first != second):
                    result = second - first
                    this_step = str(second) + "-" + str(first) + "=" + str(result)
                    # print(this_step)
                    new_current = copy.deepcopy(current)
                    del new_current[j]
                    new_current[i]=result
                    new_step = copy.deepcopy(step)
                    new_step.append(this_step)                    
                    success = calc(numbers, new_current, new_step)
                    if success[0]: return success
                                
                # try *
                result = first * second
                this_step = str(first) + "*" + str(second) + "=" + str(result)
                # print(this_step)
                new_current = copy.deepcopy(current)
                del new_current[j]
                new_current[i]=result
                new_step = copy.deepcopy(step)
                new_step.append(this_step)                
                success = calc(numbers, new_current, new_step)
                if success[0]: return success
            
                # try /
                if (second != 0 and first != 0):
                    result = first / second
                    this_step = str(first) + "/" + str(second) + "=" + str(result)
                    # print(this_step)
                    new_current = copy.deepcopy(current)
                    del new_current[j]
                    new_current[i]=result
                    new_step = copy.deepcopy(step)
                    new_step.append(this_step)                
                    success = calc(numbers, new_current, new_step)
                    if success[0]: return success
            
                    if (first != second):
                        result = second / first
                        this_step = str(second) + "/" + str(first) + "=" + str(result)
                        # print(this_step)
                        new_current = copy.deepcopy(current)
                        del new_current[j]
                        new_current[i]=result
                        new_step = copy.deepcopy(step)
                        new_step.append(this_step)                    
                        success = calc(numbers, new_current, new_step)
                        if success[0]: return success

    return (False, step)


def run_one(num):
    numbers=[]
    for i in num:
        numbers.append(Fraction(i))
    current = copy.deepcopy(numbers)
    step=[]
    success = calc(numbers,current,step)
    print(num)
    if success[0] == False: 
        print("fail")
    else:
        print("ok")
        print(success[1])    
    

run_one([5,6,9,11])
run_one([1,4,7,11])
run_one([6,9,9,10])
run_one([7,8,11,10])    
