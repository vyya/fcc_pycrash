def arithm_arrange(lst):
    first_figures = []
    operators = []
    second_figure =[]
    dashes = []
    results = []

    for item in lst:
        exp = eval(item)
        piece = item.split(' ')
        longest = max(len(piece[0]), len(piece[1]))
        #print(longest)
        first_figures.append(piece[0])
        print(piece[0], end = ' ')
        operators.append(piece[1])
        print(piece[1], end = ' ')
        second_figure.append(piece[2])
        dashes.append('-' * len(item))
        results.append(str(exp))

    '''print(' ' * (longest - len(piece[0])), first_figures[0], ' ' * (longest - len(piece[1])), first_figures[1])
    print(' '.join(operators))
    print(' '.join(second_figure))
    print(' '.join(dashes))
    print(' '.join(results))'''

arithm_arrange(['45 + 25', '34 - 67'])