from collections import defaultdict
from operator import itemgetter
import sys

wordcount_dict = defaultdict(lambda:0)

for line in sys.stdin:
    word, count = line.strip("' \n").split('=')
    wordcount_dict[word] += int(count)

for word, count in sorted(wordcount_dict.items(), key=lambda x:x[1]):
    print '{0}\t{1}'.format(word, count)
