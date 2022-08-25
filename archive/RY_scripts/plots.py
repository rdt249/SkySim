import pickle

mypickle = open(f"DICEL/plots.pickle", "rb")
plots = pickle.load(mypickle)

#print(plots["ROOMT_1.2_0_NSTRIKE_I6-ND_PSTRIKE_I6-NC"])

x = plots["ROOMT_1.2_0_NSTRIKE_I6-ND_PSTRIKE_I6-NC"][0]
y = plots["ROOMT_1.2_0_NSTRIKE_I6-ND_PSTRIKE_I6-NC"][1]


print(x)

print(f"\n\n\n")

print(y)
