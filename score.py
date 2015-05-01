__author__ = 'kamran'

from fuzzywuzzy import fuzz
from fuzzywuzzy import process
import json

"""This class will match keyword with all options in master
degree table and calculate the points
"""
class Score:


    def __init__(self, _dictionary_degrees, _keyword='', _institute=''):
        self.dictionary_degrees = _dictionary_degrees
        self.ratio_list = {}
        self.my_list = []
        self.keyword = _keyword
        self.institute = _institute

    def match_keyword(self):
        #make all possible groups
        max_list = []
        for id,options in self.dictionary_degrees.items():
            #pair_score = process.extract(self.keyword, options, limit=3)
            pair_score = process.extract(self.keyword, options)
            if pair_score:
                word,ratio = max(pair_score, key=lambda x:x[1])
                if ratio > 60:
                    max_list.append(pair_score)

        near_list = {}
        #need to filter items
        if max_list:
           for p in max_list:
               word,ratio = max(p, key=lambda x:x[1])
               if ratio > 70:
                   near_list[ratio] = p
               else:
                   self.ratio_list = {'keyword':self.keyword}
               '''
               if ratio == 100:
                   self.ratio_list = {'keyword':self.keyword,'options':p}
                   break
               elif ratio > 70:
                   near_list[ratio] = p
                   #self.ratio_list = {'keyword':self.keyword,'options':p}
               else:
                   self.ratio_list = {'keyword':self.keyword}
               '''
           if near_list:
              key,value = max(near_list.iteritems(), key=lambda x:x[0])
              #self.ratio_list = {'keyword':self.keyword,'items':json.dumps(value)}
              self.ratio_list = {'keyword':self.keyword,'institute':self.institute,'items':value , 'pairs': json.dumps(value)}
        else:
            self.ratio_list = {'keyword':self.keyword,'institute':self.institute}
            #self.ratio_list = {'keyword':self.keyword,'options':value}
            #word,ratio = max(near_list.iteritems(), key=near_list)

    def get_keyword_score(self):
        return self.ratio_list


    def pick_close_group(self):
        a=10


    def build_filter_pairs(self):
        filter_param = ['name','short','tags']
        if filter_param.count('name'):
            name = ''
        if filter_param.count('short'):
            shortname = ''





