import sys
import csv
import math
import random
import cPickle as pickle
import matplotlib.pylab as plt

#Sigmoid function 
def sigmoid(x):
	return 1/(1 + 1/(math.e**x))


def test():
	file1 = open(sys.argv[1])
	str = csv.reader(file1)
	#read data
	Data = []
	for s in str:
		Data.append([float(s[0]), float(s[1]), float(s[2])])
	weight = pickle.load(open(sys.argv[2],'rb'))
	correct = 0
	incorrect = 0
	profit = [[0.2, -0.07, -0.07, -0.07], [-0.07, 0.15, -0.07, -0.07], [-0.07, -0.07, 0.05, -0.07], [-0.03, -0.03, -0.03, -0.03]]
	conf = []
	for i in range(4):
		conf.append([0,0,0,0])
	
	for d in Data:
		input0 = [float(d[0]), float(d[1]), 1.0]
		input1 = []#Hidden outputs
		#Hidden Layer
		for l in range(5):
			temp = 0.0
			for n in range(3):
				temp += (input0[n]*weight[0][n][l])
			input1.append(sigmoid(temp))
		#bias
		input1.append(1.0)
		assigned = []#outputs
		#Output Layer
		for l in range(4):
			temp = 0.0
			for n in range(6):
				temp += (input1[n]*weight[1][n][l])
			assigned.append(sigmoid(temp))
		res = assigned.index(max(assigned)) +1
		conf[int(res)-1][int(d[2])-1] += 1
		if(res == d[2]):
			correct += 1
		else:
			incorrect += 1
	
	total = 0.0
	for i in range(4):
		for j in range(4):
			total = total + conf[i][j]*profit[i][j]
	print 'Number of Errors: ',incorrect
	print 'Recognition Rate: ', (correct*100.0)/(correct + incorrect), '%'
	print 'Profit Obtained: $', total
	s = ['bolt','nut','ring','scrap']
	print 'Confusion Matrix: '
	print '\t',s[0],'\t',s[1],'\t',s[2],'\t',s[3]
	for i in range(4):
		print s[i],'\t',
		for j in range(4):
			print conf[i][j],'\t',
		print ''
	
def region():
	data = []
	for i in range (76):
		for j in range(76):
			data.append([i/75.0, j/75.0])
	weight = pickle.load(open(sys.argv[2],'rb'))
	for d in data:
		input0 = [float(d[0]), float(d[1]), 1.0]
		input1 = []#Hidden outputs
		#Hidden Layer
		for l in range(5):
			temp = 0.0
			for n in range(3):
				temp += (input0[n]*weight[0][n][l])
			input1.append(sigmoid(temp))
		#bias
		input1.append(1.0)
		assigned = []#outputs
		#Output Layer
		for l in range(4):
			temp = 0.0
			for n in range(6):
				temp += (input1[n]*weight[1][n][l])
			assigned.append(sigmoid(temp))
		res = assigned.index(max(assigned)) +1
		#bolt
		if(res == 1):
			plt.plot(d[0],d[1],'rs',ms=10)
		#nut
		if(res == 2):
			plt.plot(d[0],d[1],'bs',ms=10)
		#ring
		if(res == 3):
			plt.plot(d[0],d[1],'gs',ms=10)
		#scrap
		if(res == 4):
			plt.plot(d[0],d[1],'ks',ms=10)
	plt.title("bolt(red) nut(blue) ring(green) scrap(black)")
	plt.xlabel("Rotational Symmetry")
	plt.ylabel("Eccentricity")
	plt.show()
	
def main():
	if(len(sys.argv)<3):
		print 'Usage : >python trainMLP.py train_Data.csv [no. of epochs]'
	else:
		test()
		region()

if __name__ == '__main__':
	main()