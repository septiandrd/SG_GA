import random
import math

def genPopulias(nPop, nKrom):
    krom = [0]
    pop = []
    numbers = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]

    for i in range(nPop) :
        for j in range(nKrom-1):
            add = int(round(random.choice(numbers)))
            if (j != nKrom - 2):
                numbers.remove(add)
            krom.append(add)
        numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
        krom.append(0)
        pop.append(krom)
        krom = [0]
    return pop

def swap(krom,a,b,exc) :
    for i in range(len(krom)) :
        if (krom[i]==a and i!=exc) :
            krom[i] = b

def randomParent(nPop) :
    a = int(round(random.uniform(0,nPop)))
    return a

def hitungFitness(krom,koor) :
    jarakTotal = 0
    for i in range(len(krom)-1) :
        a = koor[krom[i]]
        b = koor[krom[i+1]]
        jarak = round(math.sqrt(((a[0]-b[0])**2)+((a[1]-b[1])**2)))
        jarakTotal +=jarak

    return jarakTotal


if __name__ == '__main__':

    node = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
    koor = [[82,76],[96,44],[50,5],[49,8],[13,7],[29,89],[58,30],[84,39],[14,24],[2,39],[3,82],[5,10],[98,52],[84,25],[61,59],[1,65]]

    pCross = 0.8
    pMutasi = 0.1

    nPop = 500
    nGen = 100
    nKrom = len(node)

    pop = genPopulias(nPop,nKrom)

    for i in range (nGen):

        anak = []
        fitness = []

        for j in range (nPop/2):

            #SELEKSI ORANG TUA

            parent1 = randomParent(nPop-1)
            parent2 = randomParent(nPop-1)

            anak1 = pop[parent1][:]
            anak2 = pop[parent2][:]
            #CROSSOVER

            rand = random.random()
            titik = int(round(random.uniform(0,nKrom-1)))

            if rand<=pCross :
                for k in range (1,titik) :
                    a = anak1[k]
                    b = anak2[k]
                    anak1[k] = b
                    anak2[k] = a
                    swap(anak1,b,a,k)
                    swap(anak2,a,b,k)

            #MUTASI

            rand = random.random()
            titik1 = int(round(random.choice(list({1,2,3,4,5,6,7,8,9,10,11,12,13,14,15}))))
            titik2 = int(round(random.choice(list({1,2,3,4,5,6,7,8,9,10,11,12,13,14,15}-{titik1}))))

            if rand <= pMutasi :
                tmp = anak1[titik1]
                anak1[titik1] = anak1[titik2]
                anak1[titik2] = tmp

            rand = random.random()
            titik1 = int(round(random.choice(list({1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15}))))
            titik2 = int(round(random.choice(list({1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15}-{titik1}))))

            if rand <= pMutasi:
                tmp = anak2[titik1]
                anak2[titik1] = anak2[titik2]
                anak2[titik2] = tmp

            anak.append(anak1)
            anak.append(anak2)

        # PRINT ANAK
        print anak
        gab = pop + anak
        for j in range (len(gab)) :
            fitness.append(hitungFitness(gab[j],koor))

        # PRNT FITNESS
        print fitness

        # PRINT STEADYSTATE
        steadyState = sorted(range(len(fitness)),key=lambda k:fitness[k], reverse = False)
        pop = []
        for j in range(nPop) :
            pop.append(gab[steadyState[j]])
        print pop

    print "\nGenerasi Ke-",nGen
    print "Rute Terbaik : ",pop[0]
    print "Cost (Jarak) : " ,fitness[steadyState[0]]
