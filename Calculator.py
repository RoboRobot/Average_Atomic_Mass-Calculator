def Average_Atomic_Mass():
    isotopes = input("How many isotopes?")
    average = 0
    for x in range(1,int(isotopes) + 1):
        mass = input("What is the isotope %s's mass in amu?" % x)
        percent = input("How abundant is it in %?")
        average += (float(mass)*(float(percent)/100))
    print("%s amu" %average)
Average_Atomic_Mass()
