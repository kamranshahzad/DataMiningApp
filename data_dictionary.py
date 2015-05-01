__author__ = 'kamran'

import gc

from jobsearch.models import education
from jobsearch.models import dictionary_degrees
from datamining.dict_degree import Dict_Degree
from datamining.score import Score
from rawpaginator.paginator import Paginator


class Data_Dictionary:

    degree_list = []
    university_list = []


    def __init__(self, _page_number=1):
        self.dictionary_degree = {}
        self.result_list = {}
        self.page_number = int(_page_number)
        self.score_list = {}

    def __del__(self):
        self.page_number = 0

    def fill(self):
        degree_entries = dictionary_degrees.objects.all()
        for i in degree_entries:
            degree_obj = Dict_Degree(
                i.degree_id,
                i.name,
                i.short_notation,
                i.possibilities,
                i.subjects,
                i.levels,
                i.relevance
            )
            degree_obj.burn()
            self.dictionary_degree[i.degree_id] = degree_obj.get_dictionary_row()


    def get_row_pairs(self):
        return self.dictionary_degree


    def start_process(self):
        #educationObj = education.objects.raw("SELECT education_id,title FROM jobsearch_education where education_level NOT IN ('%s','%s','%s','%s','%s') AND title != '' LIMIT %s OFFSET 2" % ("Short Course","Diploma","Certification","Training","Diploma of Associate Engineering (DAE 3 Years)",str(offset_records) ))
        #for row in educationObj:
        educationObj = education.objects.raw(("SELECT education_id,title,institute FROM jobsearch_education where education_level NOT IN ('%s','%s','%s','%s','%s') AND title != '' " % ("Short Course","Diploma","Certification","Training","Diploma of Associate Engineering (DAE 3 Years)")))
        p = Paginator(educationObj , 10)
        for row in p.page(self.page_number):
        #for row in education.objects.raw("SELECT education_id,title,institute FROM jobsearch_education where education_level NOT IN ('%s','%s','%s','%s','%s') AND title != '' LIMIT 100" % ("Short Course","Diploma","Certification","Training","Diploma of Associate Engineering (DAE 3 Years)")):
            keyword = row.title.strip()
            if keyword:
                self.score_list[row.education_id] = self.get_keyword_ratio(keyword,row.institute)



    def get_keyword_ratio(self, keyword='',institute=''):
        score_obj = Score(self.dictionary_degree, keyword, institute)
        score_obj.match_keyword()
        return score_obj.get_keyword_score()


    def get_result_options(self):
        return self.score_list

    #util fnctions
    def group_suitable(self, option_list):
        close_list = {}

        for id,options in option_list:
            for word,ratio in options.items():
                if ratio == 100:
                    close_list[word] = ratio
                    return close_list;
                elif ratio > 70:
                    close_list[word] = ratio

        return close_list


