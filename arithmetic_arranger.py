def error_parser(problems):

    if len(problems) > 5:
        return 'Error: Too many problems.'

    for problem in problems:
        problem = problem.split()

        if problem[1] not in ['+','-']:
            return "Error: Operator must be '+' or '-'."
        
        if len(problem[0]) > 4:
            return 'Error: Numbers cannot be more than four digits.'
        if len(problem[2]) > 4:
            return 'Error: Numbers cannot be more than four digits.'

        if problem[0].isdigit() == False:
            return 'Error: Numbers must only contain digits.'
        if problem[2].isdigit() == False:
            return 'Error: Numbers must only contain digits.'
            
def spaces(x):
    return ' '*(x)

def underlines(x):
    return '-'*(x)


def arithmetic_arranger(problems,return_answers=False):

    # Error parsing
    if error_parser(problems) != None:
        return error_parser(problems)

    # Defining Lists
    first_numbers = list()
    second_numbers = list()
    operators = list()
    maxlength = list()
    result = list()

    # Defining variables
    first_row = ''
    second_row = ''
    lines = ''
    answers = ''
    
    # Filling the lists
    for problem in problems:
        problem = problem.split()

        maxlength.append(max([len(problem[0]),len(problem[2])]))

        first_numbers.append(problem[0])
        second_numbers.append(problem[2])
        operators.append(problem[1])
    
    # Defining the first row of numbers
    for index in range(len(problems)):

        if index == 0:
            first_row += spaces( 2 + maxlength[index] - len(first_numbers[index]))
            first_row += first_numbers[index]
        else:
            first_row += spaces( 6 + maxlength[index] - len(first_numbers[index]))
            first_row += first_numbers[index]

    # Defining the second row
    for index in range(len(problems)):

        length = len(second_numbers[index])

        second_row += operators[index] + spaces(maxlength[index] - length + 1)

        if index != (len(problems) - 1):
            second_row += second_numbers[index] + spaces(4)
        else:
            second_row += second_numbers[index]


    # Defining the lines
    for index in range(len(problems)):
        if index == len(problems) - 1:
            lines += underlines(2 + maxlength[index])
        else:
            lines += underlines(2 + maxlength[index])
            lines += spaces(4)
    
    # Defining the answers

    for index in range(len(problems)):

        first_numbers[index] = int(first_numbers[index])
        second_numbers[index] = int(second_numbers[index])
        temp = ''

        if operators[index] == '+':
            temp = str(first_numbers[index] + second_numbers[index])
        else:
            temp = str(first_numbers[index] - second_numbers[index])


        if index == 0:
            answers += spaces( 2 + maxlength[index] - len(temp))
            answers += temp
        else:
            answers += spaces( 6 + maxlength[index] - len(temp))
            answers += temp
    

    # Add the answers to the result if optional argument given is True
    if return_answers == True:
        result = first_row, second_row, lines, answers
    else:
        result = first_row, second_row, lines

    arranged_problems = '\n'.join(result)
    
    return arranged_problems
