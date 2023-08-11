def arithm_arrange(lst):
    if len(lst) > 15:
              print('Error: Too many problems')
    else:
       operand1 = []
       operand2 = []
       operator = []
       len_max = []
       for item in lst:
              #print(item)
              #exp = eval(item)
              piece = item.split(' ')
              #print(piece)             
              #operand1.append(piece[0])
              #operand2.append(piece[2])
              #operator.append(piece[1])
              lst_i = []
              for i in piece:
                     #length.append(len(i))
                     #print(i)
                     lst_i.append(i)
                     print(lst_i)
              
              #print(operand1)
              #print(operand2)
              #print(operator)
              #return piece
'''def max_length(piece):
      
       print(length)

              #for crumble in piece:
                     #operand1.append(crumble)
                     #print(operand1)                     
              #print('---')
              #print(exp)
def main():        
       piece = arithm_arrange(['4569 + 25', '3476 - 67', '45 + 8'])
       max_length(piece)

main() 
'''    
arithm_arrange(['4569 + 25', '3476 - 67', '45 + 8'])