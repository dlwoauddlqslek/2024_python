class Region:
    def __init__(self,name,total,male,female,group):
        self.name=name
        self.total=total
        self.male=male
        self.female=female
        self.group=group

    def percent1(self):
        result=(int( self.male ) / int( self.total))*100
        return result


