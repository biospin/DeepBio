
# 5. Population Genetics Simulation

### In this chapter, we will cover the following recipes:
- [Introducing forward-time simulations](Basic_SimuPOP.ipynb)
- [Simulating selection](Selection.ipynb)
- [Simulating population structure using island and stepping-stone models](Pop_Structure.ipynb)
- [Modeling complex demographic scenarios](Complex.ipynb)
- [Simulating the coalescent with Biopython and fastsimcoal](Coalescent.ipynb)


## Introduction
In the previous chapter, we used Python to analyze population genetics datasets based on
real data. In this chapter, we will see how to use Python to simulate population genetics data.
From teaching to developing new statistical methods or to analyze the performance of existing
methods, simulated datasets have plenty of applications.

There are two kinds of simulation. One is coalescent simulation that goes backwards in time.
Second is forward time. As the name implies, it simulates going forward. The coalescent
simulation is computationally less expensive because only the most recent generation of
individuals need to be completely rendered; previous generations only need parents of
the previous generation to be maintained. On the other hand, this severely limits what can
be simulated because we need to complete populations to make decisions on e.g. which
individuals mate. Forward time simulations are computationally more demanding and
normally more complex to code, but they allow you to have much more flexibility.