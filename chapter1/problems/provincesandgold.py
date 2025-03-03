nums = list(map(int,input().split()))
treasure = ""
vic = ""
purchasepower = (nums[0] * 3) + (nums[1] * 2) + (nums[2] * 1) 
if purchasepower >= 8:
    vic = "Province"
elif purchasepower >= 5:
    vic = "Duchy"
elif purchasepower >= 2:
    vic = "Estate"
if purchasepower >= 6:
    treasure = "Gold"
elif purchasepower >= 3:
    treasure = "Silver"
elif purchasepower < 3:
    treasure = 'Copper'
if vic != "":
    print(vic,"or",treasure)
else:
    print(treasure)
