import matplotlib.pyplot as plt
import numpy as np

x = list(range(1,6))

insmsey = [93.589,75.667,74.667,71.591,75.194]
inspsnry = [33.537,34.064,34.015,34.211,34.319]

##plt.figure(1)
##plt.plot(x,insmsey)
##plt.show(block= False)
##
##
##plt.figure(2)
##plt.plot(x,inspsnry)
##plt.show()
##
##
rainmsey = [78.031,67.902,66.009,64.525,58.720]
rainpsnry = [33.947,34.254,34.458,34.559,34.835]
##
##plt.figure(3)
##plt.plot(x,rainmsey)
##plt.show()
##
##plt.figure(4)
##plt.plot(x,rainpsnr)
##plt.show()

######################################################


plt.figure(1)
plt.plot(x,insmsey)
plt.plot(x,rainmsey)
plt.legend(['AdaIn_MSE', 'RAIN_MSE'])
plt.xlabel("epoch")
plt.ylabel("MSE")
plt.xticks([1,2,3,4,5])
plt.show(block= False)


plt.figure(2)
plt.plot(x,inspsnry)
plt.plot(x,rainpsnry)
plt.legend(['AdaIn_PSNR', 'RAIN_PSNR'])
plt.xlabel("epoch")
plt.ylabel("PSNR")
plt.xticks([1,2,3,4,5])
plt.show(block=False)
