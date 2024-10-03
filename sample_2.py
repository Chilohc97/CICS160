class candidate:
    def __init__(self, identifier, preferences, top_choices=1):
        self.identifier = identifier
        self.preferences = preferences
        self.top_choices = top_choices


class ListOfCandidates:
    def __init__(self, list_of_candidates, matching, list_of_preferences, list_top_choices):
        self.matching = matching
        self.list_of_preferences = list_of_preferences
        self.list_top_choices = [i.top_choices for i in list_of_candidates]

    def every_company(self):
        for i in range(len(self.matching)):
            if self.matching[i][1] != self.list_of_preferences[i][0]:
                return False
        return True
    
    def some_company(self):
        if len(self.matching) == len(self.list_of_preferences):
            for i in self.matching:
                if len(i) != 2:
                    return False
        else:
            return False
        
        return True
    
    def among_top_choices(self):
        for i in range(len(self.matching)):
            if self.matching[i][1] not in self.list_of_preferences[i][:self.list_top_choices+1]:
                return False
            
        return True



       
            

    





        