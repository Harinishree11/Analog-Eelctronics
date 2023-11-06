print("Calculator For Depletion Type MOSFET Fixed Bias Configuration")
print("1.Gate Source-Voltage\n2.Gate Supply-Voltage\n3.Drain Source-Voltage\n4.Drain Supply-Voltage\n5.Drain-Current\n6.source-Resistance")
a=input("What value do you wish to calculate from the Above options(Serial Number)?\n")

if a== "1":
    vgg=input("What is the value of Gate Supply-Voltage?")
    vgs=(float(vgg))
    print("The Gate Source-Voltage is" + " " + str(vgs) + " " + "Volts.")

elif a== "2":
    vgs=input("What is the value of Gate Source-Voltage?")
    vgg=(float(vgs))
    print("The Gate Supply-Voltage is" + " " + str(vgg) + " " + "Volts.")

elif a== "3":
    vdd=input("What is the value of Drain Supply-Voltage?")
    id=input("What is the value of Drain-Current?")
    rs=input("What is the value of Source-Resistance?")
    vds=(float(vdd)-float(id)*float(rs))
    print("The Drain Source-Voltage is" + " " + str(vds) + " " + "Volts.")
    
elif a== "4":
    vds=input("What is the value of Drain Source-Voltage?")
    id=input("What is the value of Drain-Current?")
    rs=input("What is the value of Source-Resistance?")
    vdd=(float(vds)+float(id)*float(rs))
    print("The Drain Supply-Voltage is" + " " + str(vdd) + " " + "Volts.")

elif a== "5":
    vds=input("What is the value of Drain Source-Voltage?")
    vdd=input("What is the value of Drain Supply-Voltage?")
    rs=input("What is the value of Source-Resistance?")
    id=((float(vdd)-float(vds))/float(rs))
    print("The Drain-Current is" + " " + str(id) + " " + "Amperes.")

elif a== "6":
    vds=input("What is the value of Drain Source-Voltage?")
    vdd=input("What is the value of Drain Supply-Voltage?")
    id=input("What is the value of Drain-Current?")
    rs=((float(vdd)-float(vds))/float(id))
    print("The Source-Resistance is" + " " + str(rs) + " " + "Ohms.")