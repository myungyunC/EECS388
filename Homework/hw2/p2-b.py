## EECS388 Homework 2
## question 2-b:	What is the population variance of the relative letter frequencies in the given plaintext?
## assumption:		assuming the plain text is in English


# use English letter frequency in part 2
letter_dist = { 'a': 0.08167, 'b': 0.01492, 'c': 0.02782, 'd': 0.04253, 'e': 0.12702, 
				'f': 0.02228, 'g': 0.02015, 'h': 0.06094, 'i': 0.06996, 'j': 0.00153, 
				'k': 0.00772, 'l': 0.04025, 'm': 0.02406, 'n': 0.06749, 'o': 0.07507, 
				'p': 0.01929, 'q': 0.00095, 'r': 0.05987, 's': 0.06327, 't': 0.09056, 
				'u': 0.02758, 'v': 0.00978, 'w': 0.02360, 'x': 0.00150, 'y': 0.01974, 
				'z': 0.00074 };

frequency = {	'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0, 'f': 0, 'g': 0, 'h': 0, 
				'i': 0, 'j': 0, 'k': 0, 'l': 0, 'm': 0, 'n': 0, 'o': 0, 'p': 0, 
				'q': 0, 'r': 0, 's': 0, 't': 0, 'u': 0, 'v': 0, 'w': 0, 'x': 0, 
				'y': 0, 'z': 0 };

plaintext = 'ethicslawanduniversitypoliciestodefendasystemyouneedt'\
			'obeabletothinklikeanattackerandthatincludesunderstand'\
			'ingtechniquesthatcanbeusedtocompromisesecurityhowever'\
			'usingthosetechniquesintherealworldmayviolatethelawort'\
			'heuniversitysrulesanditmaybeunethicalundersomecircums'\
			'tancesevenprobingforweaknessesmayresultinseverepenalt'\
			'iesuptoandincludingexpulsioncivilfinesandjailtimeourp'\
			'olicyineecsisthatyoumustrespecttheprivacyandpropertyr'\
			'ightsofothersatalltimesorelseyouwillfailthecourseacti'\
			'nglawfullyandethicallyisyourresponsibilitycarefullyre'\
			'adthecomputerfraudandabuseactcfaaafederalstatutethatb'\
			'roadlycriminalizescomputerintrusionthisisoneofseveral'\
			'lawsthatgovernhackingunderstandwhatthelawprohibitsyou'\
			'dontwanttoenduplikethisguyifindoubtwecanreferyoutoana'\
			'ttorneypleasereviewitsspoliciesonresponsibleuseoftech'\
			'nologyresourcesandcaenspolicydocumentsforguidelinesco'\
			'ncerningproperuseofinformationtechnologyatumaswellast'\
			'heengineeringhonorcodeasmembersoftheuniversitycommuni'\
			'tyyouarerequiredtoabidebyt';

LETTER = 'abcdefghijklmnopqrstuvwxyz';

# set population N = 26
N = 26;

for l in LETTER:
	frequency[l] = 1.0*plaintext.count(l)/plaintext.__len__();
	print frequency[l];

mu = 0.0;

for l in LETTER:
	frequency[l] = frequency[l] * 100;
	mu = mu + frequency[l];
mu = mu/N;

var = 0.0;
for l in LETTER:
	var = var + (frequency[l] - mu)**2;
var = var / N;

print var;




