# expressions = []
def arifm_arrange(lst):
    for item in lst:
         exp = eval(item)
         piece = item.split(' ')
         for crumble in piece:
                print(crumble)
                
         print('---')
         print(exp)        
        
# user_input = input("Enter ariphmetic expression separated by comma: ")
# exp = user_input.split(',')
arifm_arrange(['45 + 25', '34 - 67'])