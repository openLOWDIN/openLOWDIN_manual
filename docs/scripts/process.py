#!/usr/bin/pyhton
import sys

filename = sys.argv[1]
file = open (filename, "r" )
filelines = file.readlines()

newfilename = filename + ".rst"
newfile = open (newfilename , "w")

for line in filelines :
    if ("LowdinParameters" in line ):
        auxline = line
        auxline = auxline.replace("\n","") 
        auxline = auxline.replace("LowdinParameters_","") 
        variable = auxline.split("=")[0]
        variable = variable.replace(" ","")
        value = auxline.split("=")[1]
        value = value.replace(" ","")
        typeval = ""

        try :
            tmpfloat = float(value)
            if tmpfloat.is_integer():
                typeval = "integer"
            else:
                typeval = "float"
        except ValueError:

            if ".true." in value or ".false." in value:
                typeval = "logical"
            else:
                typeval = "character" 
        print( "* ``"+ variable +"=`` " + "*["+  typeval + "]*" + "\n" + "  *Default* ``"+ value + "`` \n" )
    else :
        auxline = line
        auxline = auxline.replace("\n","") 
        print (auxline)






