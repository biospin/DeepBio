
# 4. Population Genetics

### In this chapter, we will cover the following recipes:
- [Managing datasets with PLINK](biopython_04_population genetics1.ipynb)
- [Introducing the Genepop format](biopython_04_population genetics2.ipynb)
- [Exploring a dataset with Bio.PopGen](biopython_04_population genetics3.ipynb)
- [Computing F-statistics](biopython_04_population genetics4.ipynb)
- [Performing Principal Components Analysis](biopython_04_population genetics5.ipynb)
- [Investigating population structure with Admixture](biopython_04_population genetics6.ipynb)


## Introduction
Population genetics is the study of changes of frequency of alleles in a population on the
basis of selection, drift, mutation, and migration. The previous chapters focused mainly on
data processing and cleanup; this is the first chapter in which we will actually infer interesting
biological results.
There is a lot of interesting population genetics analysis based on sequence data, but as
we already have quite a few recipes to deal with sequence data, we will divert our attention
somewhere else. Also, we will not cover genomic structural variation such as Copy Number
Variation (CNVs) or inversions here. I will concentrate on analyzing SNP data, which is one
of the most common. We will perform many standard analyses, including population genetic
analyses with Python, such as FST (Fixation index), Principal Components Analysis (PCA),
and study of population structure.
