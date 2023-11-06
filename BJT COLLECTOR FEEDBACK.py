print("Calculator for Collector Feedback Configuration")
print("1.Base-Current\n2.Forward-Resistance\n3.Forward-Gain\n4.Collector-Resistance\n5.Emitter-Resistance\n6.Collector-Voltage\n7.Collector-Emitter Voltage\n8.Collector- Current")
a = input("What value do you wish to calculate from the Above options(Serial Number):\n")

if a == "1":
    vcc=input("What is the value of Collector-Voltage? ")
    rf=input("What is the value of Forward-Resistance? ")
    beta=input("What is the value of Forward-Gain?")
    rc=input("What is the value of Collector-Resistance?")
    re=input("What is the value of Emitter-Resistance?")
    i=(float(vcc)-0.7)/float(rf)+(float(beta)*float(rc))+(float(beta)*float(re))
    print("The Base Current is" + " " + str(i) + " " + "Amperes.")
  
elif a == "2":
    vcc=input("What is the value of Collector-Voltage? ")
    beta=input("What is the value of Forward-Gain? ")
    ib=input("What is the value of Base-Current?")
    rc=input("What is the value of Collector-Resistance?")
    re=input("What is the value of Emitter-Resistance?")
    r=((float(vcc)-0.7)-(float(beta)*float(ib)*float(rc))-(float(beta)*float(ib)*float(re)))/float(ib)
    print("The Forward Resistance is" + " " + str(r) + " " + "Ohms.")
     
elif a == "3":
    ic=input("What is the value of Collector-Current? ")
    ib=input("What is the value of Base-Current? ")
    beta=(float(ic)/float(ib))
    print("The Forward Gain is" + " " + str(beta) + " " +".")

elif a == "4":
    vcc=input("What is the value of Collector Voltage? ")
    ic=input("What is the value of Collector Current? ")
    re=input("What is the value of Emitter-Resistance?")
    vce=input("What is the value of Collector Emitter Voltage? ")
    r=((float(vcc)-(float(ic)*float(re))-float(vce))/float(ic))
    print("The Collector Resistance is" + " " + str(r) + " " + "Ohms.")
  
elif a == "5":
    vcc=input("What is the value of Collector Voltage? ")
    ic=input("What is the value of Collector Current? ")
    rc=input("What is the value of Collector-Resistance?")
    vce=input("What is the value of Collector Emitter Voltage? ")
    r=((float(vcc)-(float(ic)*float(rc))-float(vce))/float(ic))
    print("The Emitter Resistance is" + " " + str(r) + " " + "Ohms.")
  
elif a == "6":
    vce=input("What is the value of Collector Emitter Voltage? ")
    ic=input("What is the value of Collector Current? ")
    rc=input("What is the value of Collector-Resistance?")
    re=input("What is the value of Emitter-Resistance?")
    vcc=float(vce)+(float(ic)*float(rc))+(float(ic)*float(re))
    print("The Collector Voltage is" + " " + str(vcc) + " " + "Volts.")

elif a == "7":
    vcc=input("What is the value of Collector Voltage? ")
    ic=input("What is the value of Collector Current? ")
    rc=input("What is the value of Collector-Resistance?")
    re=input("What is the value of Emitter-Resistance?")
    vce=float(vcc)-(float(ic)*float(rc))-(float(ic)*float(re))
    print("The Collector Emitter Voltage is" + " " + str(vce) + " " + "Volts.")

elif a == "8":
    beta=input("What is the value of Forward-Gain?")
    ib=input("What is the value of Base-Current?")
    ic=float(beta)*float(ib)
    print("The Collector Current is"+ " " + str(ic) + " " + "Amperes.")