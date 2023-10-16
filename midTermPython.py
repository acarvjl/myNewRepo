import random
from itertools import islice
from datetime import datetime

with open("animalNames.txt", 'r') as file:
    names = [line.strip() for line in file]
    counter = 0
    nameClance = []
    cleanerNames = []
    
    for line in names:
        if ' ' in line:
            nameClance.append(line)
            
    for index in nameClance:
        if counter % 2 != 0 :
            cleanerNames.extend(word for word in index.split() if ',' in word)
        counter = counter + 1
        
    counter = 0
    
    # cleaning vairables with strip()
    cleanerNames = [s.strip(',') for s in cleanerNames]
    
    len_to_split = [10, 11, 9, 9]
    input = iter(cleanerNames)
    cleanerNames = [list(islice(input, elem)) for elem in len_to_split]
    hy_names = cleanerNames[0]
    li_names = cleanerNames[1]
    be_names = cleanerNames[2]
    ti_names = cleanerNames[3]
    
    def nameRem(species, name):
        if species.lower == 'hyena':
            return hy_names.remove(name)
        elif species.lower() == 'lion':
            return li_names.remove(name)
        elif species.lower() == 'bear':
            return be_names.remove(name)
        elif species.lower() == 'tiger':
            return ti_names.remove(name)
        else:
            pass
        
        # Assign each new animal to a habitat. Each species must have its own habitat.
    def genZooHabitat(species):
        if species.lower() == 'hyena':
            return 'Hyena Habitat'
        elif species.lower() == 'lion':
            return 'Lion Habitat'
        elif species.lower() == 'bear':
            return 'Bear Habitat'
        elif species.lower() == 'tiger':
            return 'Tiger Habitat'
        else:
            return 'Temp Habitat'
    
    # Create an animal name based on input from a community fundraiser (animalNames.txt).
    def genAnimalName(species):
        if species.lower == 'hyena':
            return random.choice(hy_names)
        elif species.lower() == 'lion':
            return random.choice(li_names)
        elif species.lower() == 'bear':
            return random.choice(be_names)
        else:
            return random.choice(ti_names)

    # Calculate a unique ID to uniquely identify each animal in your zoo.
    def genUniqueAnimalId():
        num_id = 1  # Initialize the numerical ID
        with open('arrivingAnimals.txt', 'r') as file:
            lines = file.readlines()
            for line in lines:
                split_line = line.strip().split(',')
                species = split_line[0].split()[4]
                num_id_str = str(num_id).zfill(2)  # Convert num_id to a zero-padded string
                num_id += 1  # Increment the numerical ID
                numId = f"{species[:2]}{num_id_str}"
                #print(numId)

    # Calculate a birthday from the information
    # received from the originating zoo. Handle cases where the birth season is unknown (season).    
    def genBirthday(age, season):
    # make so first month of season is birth month, and birth year is age subtracted from current year 2022
        year = 2023 - age

        if season.lower() == 'spring':
            return f'{year}-03-20'
        elif season.lower() == 'summer':
            return f'{year}-06-21'
        elif season.lower() == 'fall':
            return f'{year}-09-22'
        elif season.lower() == 'winter':
            return f'{year}-12-21'
        else:
            return f'{year}-01-01'
        
# counter = 0

class Animal:
    numOfAnimals = 0
    def __init__(self, age=0, sex='male', color='undetermined', weight='1 pounds', species='undetermined', season='winter', origin='zoo'):
        self.age = age
        self.sex = sex
        self.color = color
        self.weight = weight
        self.id = genUniqueAnimalId()
        self.species = species
        self.habitat = genZooHabitat(self.species)
        self.name = genAnimalName(self.species)
        nameRem(self.species, self.name)
        self.season = season
        self.birthDay = genBirthday(age, season)
        self.origin = origin
        
        Animal.numOfAnimals += 1
        
    def __str__(self):
        # format text
        return f"Id: {self.id};{self.name};{self.age} year old: {self.birthDay}; {self.color}; {self.sex}; {self.weight}; from: {self.origin}; habitat: {self.habitat}\n"
        
instanceAnimals = []

with open('arrivingAnimals.txt', 'r') as file:
    lines = [line.strip().split(',') for line in file]
    
    for line in lines:
        origin = line[1::4][1]
        color = line[2::4][0]
        age = int(line[0][0:2:1])
        sex = line[0][10:18].find('female')
        if int(sex) == -1:
            sex = 'male'
        else:
            sex = 'female'
            
        season = line[1][9:]
        temp_species = line[0][17:]
        tmp = temp_species
        if tmp.endswith('hyena'):
            tpm = 'hyena'
        elif tmp.endswith('lion'):
            tmp = 'lion'
        elif tmp.endswith('tiger'):
            tmp = 'tiger'
        else:
            tmp = 'bear'
        species = tmp
        weight = weight = line[3]
        
        instanceAnimals.append(Animal(age, sex, color, weight, species, season, origin))
        
counter = 1

with open('zooPopulation.txt', 'w') as file:
    for animal in instanceAnimals:
        file.write(str(animal))
