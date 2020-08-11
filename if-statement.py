is_male = True
is_tall = True

if is_male or is_tall:
    print("You are a Male or Tall or Both")
elif is_male and not(is_tall):
    print("You are a short male")
else:
    print("You are nither a male or tall")