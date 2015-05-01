__author__ = 'kamran'

import json


class Dict_Degree:


    def __init__(self, _degree_id = 0, _name='',_short_notation='',_possibilities='', _subjects='', _level=0 , _relevance=0 ):
        self.degree_id = _degree_id
        self.name = _name
        self.short_notation = _short_notation
        self.possibilities = _possibilities
        self.subjects = _subjects
        self.level = _level
        self.relevance = _relevance
        self.pair_list = []
        self.tag_list = []
        self.subject_list = []

    def burn(self):
        if self.possibilities:
            possibleValue = json.loads(self.possibilities)
            self.pair_list = possibleValue['pairs']
            self.tag_list = possibleValue['tags']
        if self.subjects:
            self.subject_list = json.loads(self.subjects)


    def get_dictionary_row(self):
        dict_row = []
        if self.name:
            dict_row.append(self.name)
        if self.short_notation:
            dict_row.append(self.short_notation)
        if len(self.get_pairs()) > 0:
            dict_row = dict_row + self.get_pairs()
        if len(self.tag_list) > 0:
            dict_row = dict_row + self.tag_list

        return dict_row


        #return pair_row


    def get_pairs(self):
        combination_words = []
        if self.pair_list:
            for i in self.pair_list:
                combination_words.append(self.short_notation +' '+i)
        return combination_words

    def get_name_pairs(self):
        combination_words = []
        if self.pair_list:
            for i in self.pair_list:
                combination_words.append(self.name +' '+i)
        return combination_words


    def get_tags(self):
        return self.tag_list


    def helper(self):
        return '_Degree_'
