import os
cmd_beg = 'espeak '
ticket  = input('Entrer le numero de ticket : ') 
# text    = "ticket numero"+ticket+" va au gichet "+gichet
os.system(cmd_beg+ticket+" --voices") 
# from num2word import num2words
# from subspaces import call
# cmd_beg = 'espeak '
# ticket  = input('Entrer le numero de ticket : ') 
# gichet  = input('Entrer le numero de gichet : ') 
# text  = "ticket numero"+ticket+" va au gichet "+gichet
# call([cmd_beg+text]) 

