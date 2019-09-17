#start

vaken = "n"

print("Du sover djupt som en björn i idé...")

while vaken == "n":
    vaken = input("har du vaknat [y/n]: ").lower()



print("Du går och duschar för att du stinker")
print("Någon vill döda dig och har lämnat en brödrost i duschen")

duscha = input("vill du duscha med brödrosten? [y/n]: ").lower()

if duscha == "y":
    print("Du dog")
elif duscha == "n":
    print("Duschen var kall men du stod kvar för att livet kunde inte bli värre nu.")
else:
    print("Din dag är över för att flera timmar hade räknats förbi för att du inte kunde välja en simpel sak.")



season = False
while season == False:
    season = input("vilken årstid är det? [vår, vinter, sommar, höst] ").lower()
    if season == "vår" or season == "vinter" or season == "höst":
        print("Det blåser kallt ute")
        print("Du klär på dig varma kläder")
    elif season == "sommar":
        print("Summertime, summertime, sum sum summertime. En t-shirt är tillräckligt")
    else:
        season = False
    