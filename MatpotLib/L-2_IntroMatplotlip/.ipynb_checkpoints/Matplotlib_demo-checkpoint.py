import matplotlib.pyplot as plt

years= [2000,2001,2002,2003,2005,2006,2007,2008,2009,2010]
runs=[500,700,1100,1500,1200,1800,2000,3000,1500,3000]
plt.plot(years,runs)
plt.xlabel("Years")
plt.ylabel("Run")
plt.title("Yearly run ")
plt.show()