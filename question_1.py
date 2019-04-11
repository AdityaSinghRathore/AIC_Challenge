'''Question 1'''
type_braces_open = ['(','{','[']
type_braces_close = [')','}',']']
type_braces_all = type_braces_open + type_braces_close

def evaluate_expression(expression):
    is_balanced = 'N'
    
    expression = list(expression)
    evaluation_list = []

    # Simply list braces in order of appearence important for second output as well as evaluation

    for i in range(len(expression)):
        a = expression[i]
        if a in type_braces_all:
            evaluation_list.append(a)

    # Set is_balanced according to evaluation
    #print(evaluation_list)
    if list_evaluate(evaluation_list[:]) == True:
        is_balanced = 'Y'

    return is_balanced,evaluation_list

def list_evaluate(ls):
    '''
    Recursive logic to check for balanced braces
    -------------------------------------------- 
    '''
    for i in range(len(ls)):
        if ls[i] in type_braces_close:
            ls[i] = type_braces_open[type_braces_close.index(ls[i])]

    if len(ls) == 0:
        return True
    elif len(ls) == 1:
        return False
    elif ls[0] == ls[1]:
        return list_evaluate(ls[2:])
    elif ls[1] == ls[-1]:
        return list_evaluate(ls[1:-1])
    elif list_evaluate(ls[1:])==True:
        return False
    elif list_evaluate(ls[-1:])==True:
        return False
    else:
        print("Edge Case : ",ls)
        return False

if __name__=='__main__':
    #while True:
    expression = input('Expression Here:')
    is_balanced,eval_list = evaluate_expression(expression)
    print(is_balanced,''.join(eval_list))