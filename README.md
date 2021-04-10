#Natural Selection
class Person:
    traitlist = ['FAST','SLOW','EFFICIENT']
    nextid = 1
    def __init__(self,trait,mutationsallowed):
        self.mutationsallowed = mutationsallowed
        self.trait = trait #list
        self.food = 0
        self.id = Person.nextid
        self.lifelimit = 1000
        Person.nextid  += 1
        self.priority = 0
        if self.mutationsallowed != False:
            if (random.randint(1,20) == 1 and trait == None) or random.randint(1,30) == 1: 
                self.trait = (Person.traitlist[random.randint(0,len(Person.traitlist))-1])
        if self.trait == 'FAST':
            self.priority -= 1
        if self.trait == 'SLOW':
            self.priority += 1
    def reproduce(self):
        babyperson = Person(self.trait,self.mutationsallowed)
        Environment.addperson(babyperson)
   
    def terminate(self):
        Environment.terminate(self.id)
        
        
class Environment:
    occupants = {}
    availablefood = 0
    
    @classmethod
    def addperson(cls,person):
        cls.occupants[person.id] = person
        
    @classmethod
    def terminate(cls,id):
        del cls.occupants[id]
        
    @classmethod
    def newday(cls,foodperday):
        fastpop = 0
        slowpop = 0
        efficientpop = 0 
        normalpop = 0
        totalpop = 0
        cls.availablefood = foodperday
        toccupants = list(cls.occupants.keys())
        random.shuffle(toccupants)
        #print('occupants {}'.format([(id, cls.occupants[id].priority) for id in toccupants]))
        fastlist = []
        normlist = []
        slowlist = []
        for person in toccupants:
            if cls.occupants[person].priority == -1:
                fastlist.append(person)
            if cls.occupants[person].priority == 0:
                normlist.append(person)
            if cls.occupants[person].priority == 1:
                slowlist.append(person)
        effskips = 0
        ticks = 0
        while cls.availablefood >= 1 and ticks <10:
            ticks +=1
            for person in fastlist:
                temp = random.randint(1,100)
                if temp >= 1 and temp <= 50:
                    cls.availablefood -= 1
                    cls.occupants[person].food +=1
            for person in normlist:
                temp = random.randint(1,100)
                if cls.availablefood > 0:
                    if temp >= 1 and temp <= 50:
                        cls.availablefood -= 1
                        cls.occupants[person].food +=1
            for person in slowlist:
                temp = random.randint(1,100)
                if temp >= 1 and temp <= 50:
                    cls.availablefood -= 1
                    cls.occupants[person].food +=1
        for person in list(cls.occupants.values()):
            if person.food < 1:
                person.terminate()
                continue
            if person.food == 1:
                if person.trait == 'EFFICIENT' and random.randint(0,5) == 0:
                    person.reproduce()
                    person.food = 0
                    person.lifelimit -=1
                    if person.lifelimit <= 0:
                        person.terminate
                        continue
                else:
                    person.food = 0
                    person.lifelimit -= 1
                    if person.lifelimit <= 0:
                        person.terminate
                    continue
            elif person.food >= 2:
                person.reproduce()
                person.food = 0
                person.lifelimit -=1
                if person.lifelimit <= 0:
                    person.terminate
                continue
        for person in list(cls.occupants.values()):
            totalpop +=1
            if person.trait == 'FAST':
                fastpop += 1
            if person.trait == 'SLOW':
                slowpop +=1
            if person.trait == 'EFFICIENT':
                efficientpop +=1
            if person.trait == None:
                normalpop +=1
        return (totalpop,fastpop,slowpop,efficientpop,normalpop)
        


def main(simlength,startingnum,mutationsallowed,preset_trait,foodperday):
    #Mutations Allowed is True or False. 
    #Preset_trait is False or a trait ('FAST','SLOW','EFFICIENT')
    Environment.occupants = {}
    populationbyday = []
    fastpopulationbyday = []
    slowpopulationbyday = []
    efficientpopulationbyday = []
    normalpopulationbyday = []
    # initialize
    for i in range(startingnum):
        if preset_trait == False:
            if mutationsallowed == False:
                Environment.addperson(Person(None,False))
            else:
                Environment.addperson(Person(None,True))
        else:
            if mutationsallowed == False:
                Environment.addperson(Person(preset_trait,False))
            else:
                Environment.addperson(Person(preset_trait,True))
    # start simulation
    for i in range(simlength):
        data = Environment.newday(foodperday)
        #DATA STUFF
        populationbyday.append(data[0]) 
        fastpopulationbyday.append(data[1])
        slowpopulationbyday.append(data[2])
        efficientpopulationbyday.append(data[3])
        normalpopulationbyday.append(data[4])
        print (f'population: {data[0]}, fastpopulation: {data[1]}, slowpopulation: {data[2]}, efficientpopulation: {data[3]}, normalpopulation: {data[4]}')
        
