def Average_Atomic_Mass():
    isotopes = input("How many isotopes?")
    average = 0
    for x in range(0,int(isotopes)):
        mass = input("What is the mass in amu?")
        percent = input("How abundant is it in %?")
        average += (float(mass)*(float(percent)/100))
    print(average)
Average_Atomic_Mass()