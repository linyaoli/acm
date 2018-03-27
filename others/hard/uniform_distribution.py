import random as rd
import operator
input = [('us', 3000), ('russia', 1000), ('china', 2000), ('japan', 4000)]
def calculateProb(input):
	total = 0
	population = []
	# get the total population
	for item in input:
		population.append(item[1])
	total = sum(population)

	population_to_country = {}
	for item in input:
		population_to_country[item[1] * 1.0 / total] = item[0]

	population_to_country = dict(sorted(population_to_country.items(), key=operator.itemgetter(0)))

	prob_distribution = [x for x in population_to_country][::-1]

	country_distribution = []
	# names of countries, corresponding to the prob distribution
	for key in population_to_country:
		country_distribution.append(population_to_country[key])

	for i in xrange(1, len(prob_distribution)):
		prob_distribution[i] += prob_distribution[i-1]

	random_val = rd.random() # 0~1
	print random_val, prob_distribution, country_distribution
	# binary search to find the insertion point
	start = 0
	end = len(prob_distribution) - 1
	mid = 0
	while start <= end:
		mid = start + (end - start) / 2
		if prob_distribution[mid] > random_val:
			end = mid - 1
		elif prob_distribution[mid] < random_val:
			start = mid + 1
		else:
			break
	if prob_distribution[mid] < random_val:
		mid += 1

	return prob_distribution[mid], country_distribution[mid]

print calculateProb(input)
