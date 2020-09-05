def percent(string="500*20%"):
    if "%" == string[-1] and "*" in string:
        getnum = string[:-1]
        ops = getnum.split("*")
        result = int(ops[0])*int(ops[1]) / 100
        print("The {}% of {} is {}".format(ops[1], ops[0], result))
        return result
    else:
        print("The argument must be a string like '500*22%'")

percent("12000*20%")