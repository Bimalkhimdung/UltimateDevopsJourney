def check_age(age):
    if age  <=18:
        raise Exception("You are not eligible")
    else:
        print("you are eligible")

check_age(22)