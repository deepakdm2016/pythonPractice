import logging

logging.basicConfig(filename="myLog.log",level=logging.DEBUG)

a,b=[int(x) for x in input("Enter two numbers").split()]
try:
    f=open("myFile","w")
    c=a/b
    logging.info(c)
    f.write("writing %d into a file" %c)

except ZeroDivisionError:
    logging.error("Division by 0 is not allowed")
    
else:
    logging.info("No exceptions occured")
    
finally:
    f.close()
    logging.info("File is closed")


    
logging.info("Division completed")
