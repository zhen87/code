class student():
    def __init__(self,name,score):
        self._name = name
        self._score = score
    def get_name(self):
        return self._name
    def get_score(self):
        return self._score
    def set_name(self):
        return self._name
    def set_score(self, score):
        if 0 <= score <= 100:
             self.__score = score
        else:
            raise ValueError('bad score')
    def get_grade(self):
        if self._score>90:
            return 'A'
        elif self._score>60:
            return 'B'
        else:
            return 'C'
    def __printscore__(self):
        print('%s %s' % (self._name ,self._score,self.get_grade()))

a= student('A',89)
print(a.get_name(),a.get_score(),a.get_grade())

print(a.set_score(60))
