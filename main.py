run = True
done = False
first_run = True
variables_dic = {
    "test": "error",
  }
def plus(lhs, rhs):
  return lhs + rhs

def minus(lhs, rhs):
  return lhs - rhs


print("Welcome to my cool language")
while run == True:
  def my_print(what_to_print):
        what_to_print = what_split[1]
        print(what_to_print)
  builtin = {
    "print": my_print,
    }

  what = input("My cool language >")
  #what = 'print "b"'
  what_split = what.split()
  try:
    if what_split[1] == "=":
        variable = what_split[0]
        value = what_split[2]
        variables_dic.update({variable : value})
        #print(variables_dic)
    elif what_split[0] == "print":
      if what_split[1] in variables_dic:
      #printer =
        print(variables_dic.get(what_split[1]))
      if what_split[1].startswith('"') and what.endswith('"'):
        wew = what_split[1].replace('"',"")
        print(wew)




  except:
    print("Err!")





