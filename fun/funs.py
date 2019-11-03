


def smallest_subsequence(test):
	'''
	i accept a string like this
	"0 0 0 0 0 0 1 1 0 0 0 1 1 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0"
	and I return 2 because the smallest subseq is 1 1
	'''
	# test = "0 0 0 0 0 0 1 1 0 0 0 1 1 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0"
	test = [x.strip() for x in test.split("0")]
	test = set(test)
	test = list(test)
	test = [len(x.split(' ')) for x in test if x != '']
	return min(test)
