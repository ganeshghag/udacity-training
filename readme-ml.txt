weka tutorials - machine learning - ML
data discretization filter - converts discrete values in data into ranges
numeric transform filter - uses java methods like abs, floor, ceil to transform data that has too much precision, say 7 digits after decimal point


feature selection methods
	wrapper (data dimensionality)
	filter method

wrapper method (pref for ML, classifiers)
	go to select attribute tab
	select 1 attrib evaluator of type wrapper
	inside select, the algo as naive bayes
	select search method as "best first"
	use full training set or...
	select the output/label class
	click start

which features-classifier algo combo you select, matters a lot,for precision, recall, f-measure
hence automated attribute selection, is very imp first step


Filter method (pref for data mining only, where huge datasets and long feature vectors)
by this method, you choose a feature evaluator like infogain and a ranker algo
outout is recommendation of each feature with a rank or weight
you can choose, attributes/features with higher rank/weight

	go to select attribute tab
	select 1 attrib evaluator of type filter like infogain attrib eval
	inside select, choose default ranker algo
	use full training set or...
	select the output/label class
	click start
Ranked attributes:
 1.418  3 petallength
 1.378  4 petalwidth
 0.698  1 sepallength
 0.376  2 sepalwidth

	