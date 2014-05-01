import sys
import csv
import math
import random
import cPickle as pickle
import matplotlib.pylab as plt

def test():
	file1 = open(sys.argv[1])
	str = csv.reader(file1)
	data = []
	for s in str:
		data.append([float(s[0]), float(s[1]), float(s[2])])
	tree = pickle.load(open(sys.argv[2],'rb'))
	correct = 0
	incorrect = 0
	profit = [[0.2, -0.07, -0.07, -0.07], [-0.07, 0.15, -0.07, -0.07], [-0.07, -0.07, 0.05, -0.07], [-0.03, -0.03, -0.03, -0.03]]
	conf = []
	for i in range(4):
		conf.append([0,0,0,0])
	
	for d in data:
		prob = [0.0,0.0,0.0,0.0]
		for t in tree:
			if d[t[0]] <= t[1]:
				if d[t[2]] <= t[3]:
					prob[t[6]-1] += t[7]
				else :
					prob[t[8]-1] += t[9]
			else:
				if d[t[4]] <= t[5]:
					prob[t[10]-1] += t[11]
				else:
					prob[t[12]-1] += t[13]
		for i in range(len(prob)):
			prob[i] = prob[i] / len(tree)
		res = prob.index(max(prob)) +1
		conf[int(d[2])-1][int(res)-1] += 1
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
	for i in range (51):
		for j in range(51):
			data.append([i/50.0, j/50.0])
	tree = pickle.load(open(sys.argv[2],'rb'))
	for d in data:
		prob = [0.0,0.0,0.0,0.0]
		for t in tree:
			if d[t[0]] <= t[1]:
				if d[t[2]] <= t[3]:
					prob[t[6]-1] += t[7]
				else :
					prob[t[8]-1] += t[9]
			else:
				if d[t[4]] <= t[5]:
					prob[t[10]-1] += t[11]
				else:
					prob[t[12]-1] += t[13]
		for i in range(len(prob)):
			prob[i] = prob[i] / len(tree)
		res = prob.index(max(prob)) +1
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
		print 'Usage : >python trainDT.py test_Data.csv maxTree.p'
	else:
		test()
		region()

if __name__ == '__main__':
	main()
