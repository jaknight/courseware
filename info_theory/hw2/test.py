

from numpy import *
import numpy as np
from matplotlib import *
from matplotlib.mlab import *
from matplotlib.pyplot import *

close('all')

for N in [4] :

	C = zeros((N,N),float)
	myC = zeros((N,N),float)

	m_range = frange(N-1)
	n_range = m_range

	k = ones((N,N),float)
	for m in range(len(k)) :
		for n in range(len(k[m])) :
			if n == 0 :
				k[m,n] = sqrt(float(1)/float(N))
			else :
				k[m,n] = sqrt(float(2)/float(N))

	
	for i in range(N) :
		for j in range(N) :
			myC = k[i,j] * cos( (((2*i)+1) * j * pi) / (2*N) )

	C = k * cos( (multiply(multiply(2,m_range) + 1,n_range) * pi )/ 2*N )
	
	
	f,plots = subplots(N,N)
	for m in m_range :
		for n in n_range :
			
			print 'm= %d\t n= %d' % (m,n)
			Y=zeros((N,N),float)
			Y[m,n] = 1

			X = C.transpose() * Y * C
			print 'X = \n',X
			plots[m,n].imshow(X,cmap='gray')
			plots[m,n].get_xaxis().set_visible(False)
			plots[m,n].get_yaxis().set_visible(False)



show()




	


