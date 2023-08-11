import sys

def inp_expression():
     input('Please input properly formatted expression:')
     
def arithm_arrange(exp):
    if len(exp) > 5:
              print('Error: Too many problems')
    else:
       operand1 = []
       operand2 = []
       operator = []
       len_max = []
       for item in exp:
           
            piece = item.split(' ')
            operand1.append(piece[0])
            operand2.append(piece[2])
            operator.append(piece[1])
            max_len = len(max(piece, key = len))
            len_max.append(max_len)
            print(len_max)
            
            
    return operand1, operand2, operator, len_max
def operator_error(operator):
     for op in operator:
          if op not in('+', '-'):
               print("Error: Operator must be '+' or '-'.")
               sys.exit(1)
               
def operand1_error(operand1):
     for op in operand1:
          if op.isdigit() != True:
               print('Error: Numbers must only contain digits.')
               sys.exit(2)

def operand2_error(operand2):
     for op in operand2:
          if op.isdigit() != True:
               print('Error: Numbers must only contain digits.')
               sys.exit(3)
def output_operand1(operand1, len_max):
      for pos in operand1:
          #print(f"{pos:>len_max[0]}")
         # print(f'{pos:> 6}', end = '    ')
          sym_len = len_max[0]
          print("{:>{}}".format(pos, sym_len), end = '    ')
def output_operand2(operand2, operator, len_max):
     sym_len = len_max[2] + 2
     for pos in operator:
          print("{:<{}}".format(pos, sym_len), end = ' ')

def main():
     
     operand1, operand2, operator, len_max = arithm_arrange(['45 - 456', '325 - 78', '46 + 5'])
     operator_error(operator)
     operand1_error(operand1)
     operand2_error(operand2)
     output_operand1(operand1, len_max)
     output_operand2(operand2, operator, len_max)
          
               
     
main()
