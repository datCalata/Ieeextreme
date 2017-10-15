def next_generation(last_gen,last_gen2):
    return last_gen+last_gen2
        

line = int(input())
generations = []
for i in range(line):
    generations.append(int(input()))



for catas in generations:
    #gen 1
    last_gen = 1
    last_gen2 = 1
    for i in range(1,catas):
        tmp = last_gen
        last_gen = next_generation(last_gen,last_gen2)
        last_gen2 = tmp
    print(last_gen%10)
