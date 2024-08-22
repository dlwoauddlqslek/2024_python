class Region:
    def __init__(self,name,total,male,female,group):
        self.name=name
        self.total=total
        self.male=male
        self.female=female
        self.group=group

    def percent1(self):
        result=round(int(self.male ) / int(self.total)*100)
        return result
    def percent2(self):
        result=round(int(self.female)/ int(self.total)*100)
        return result

