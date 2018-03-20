import matplotlib.pyplot as pl
import pandas as pd
import json

with open("../data/network1/callback.json", "r") as file:
    data = json.load(file)

print(data["loss"])

df = pd.DataFrame(data)
print (df)

df.plot()
pl.show()
#pl.savefig("epoch.png")
