def total(gallenons, sickles, knuts):
    return(gallenons * 17 + sickles) * 29 + kunts

#coins = [100,50,25]
coins = {"gallenons" : 100, "sickles" : 50, "knuts":25}
print(total(**coins), "Knuts") # dictionary use double **

#print(total(*coins), "Knuts")

