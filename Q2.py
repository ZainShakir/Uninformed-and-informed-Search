import random
import matplotlib.pyplot as plt
import numpy as np

# Q2 part A
class Genetic_Algorithim:
    required = []
    population = []
    size_population = 0
    chromosome = 0
    fitness = {}

    def __init__(self, sc):
        # self.size_population = random.randint(4,10)
        self.size_population = 4
        self.chromosome = sc
        for i in range(0, self.chromosome):
            self.required.append(1)
        for i in range(0, self.size_population):
            self.population.append(0)

    def popultation_intial(self):

        for pop_size in range(0, self.size_population):
            chromosone = []
            for i in range(0, self.chromosome):
                chromosone.append(0)
            for chrom_size in range(0, self.chromosome):
                chromosone[chrom_size] = random.randint(0, 1)
            self.population[pop_size] = chromosone


    def fitness_calculate(self):
        fit = 0
        for chromosone in self.population:
            for i in range(0, self.chromosome):
                fit += chromosone[i] * pow(2, (self.chromosome - 1) - i)

            self.fitness[fit] = chromosone
            fit = 0
  
    def crossover(self):
        chromosones = []
        cr_chromosones = []
        for key in self.fitness:
            chromosones.append(self.fitness[key])

        for i in range(0, 2):
            si_chromo = []
            for h in range(0, int(self.chromosome / 2)):
                si_chromo.append(chromosones[i][h])
            for k in range(int(self.chromosome / 2), self.chromosome):
                si_chromo.append(chromosones[i + 1][k])
            cr_chromosones.append(si_chromo)

        for i in range(0, 2):
            si_chromo = []
            for h in range(int(self.chromosome / 2), self.chromosome):
                si_chromo.append(chromosones[i][h])
            for k in range(0, int(self.chromosome / 2)):
                si_chromo.append(chromosones[i + 1][k])
            cr_chromosones.append(si_chromo)

        self.population = cr_chromosones
        
        
    def selection(self):
        key_to_be_deleted = 0
        for i in sorted(self.fitness.keys()):
              key_to_be_deleted = i
              break
        del self.fitness[key_to_be_deleted]

    def mutation(self):

        for i in range(0, 4):
            while self.population[i][random.randint(0, self.chromosome - 1)] == 0:
                self.population[i][random.randint(0, self.chromosome - 1)] = 1


    def check_bits(self):
        fit = 0
        for chromosone in self.population:
            for i in range(0, self.chromosome):
                fit += chromosone[i] * pow(2, (self.chromosome - 1) - i)
            if fit == 255:
                return True
            else:
                fit = 0
        return False


genetics = Genetic_Algorithim(8)
flag = False
gen = 1

while not flag:
    genetics.popultation_intial()
    genetics.fitness_calculate()
    genetics.selection()
    genetics.crossover()
    genetics.mutation()
    flag = genetics.check_bits()
    print("Generation: ", gen, " -> ", genetics.population)
    gen += 1
    if flag:
        print("Found 255 bit chromosone in ", gen-1)
        print("Population: ", genetics.population)
        
        
#Q2 Part B(Population size vs Generations)



x=[4,5,6,7,8,9,10 ]
y1=[11,7,43,31,29,6,17]
y2=[57,9,31,13,9,7,3]
y3=[56,6,75,4,21,9,46]
y4=[18,48,55,13,15,34,47]
plt.title('Population Size VS Num of Generations')
plt.xlabel('Population Size')
plt.ylabel('Num of generations')
plt.plot(x,y1,label="iteration 1")
plt.plot(x,y2,label="iteration 2")
plt.plot(x,y3,label="iteration 3")
plt.plot(x,y4,label="iteration 4")
plt.legend()
plt.show()
        

#Q2 part c (Chromosome length VS Generations)

x=[10,15,20,25,30]
y1=[97,4,28,17,27]
y2=[19,20,40,59,63]
y3=[13,24,36,3,27]
y4=[38,34,6,4,39]
plt.title('Chromosome Length VS Num of Generations')
plt.xlabel('Chromosome Length')
plt.ylabel('Num of generations')
plt.plot(x,y1,label="iteration 1")
plt.plot(x,y2,label="iteration 2")
plt.plot(x,y3,label="iteration 3")
plt.plot(x,y4,label="iteration 4")
plt.legend()
plt.show()


