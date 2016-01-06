
# 3. Working with Genomes

### In this chapter, we will cover the following recipes:
- [Working with high-quality reference genomes](01.Reference_Genome.ipynb)
- [Dealing with low-quality reference genomes](02.Low_Quality.ipynb)
- [Traversing genome annotations](03.Annotations.ipynb)
- [Extracting genes from a reference using annotations](04.Getting_Gene.ipynb)
- [Finding orthologues using the Ensembl REST API](05.Orthology.ipynb)
- [Retrieving gene ontology information from Ensembl](06.Gene_Ontology.ipynb)
- [생물정보학 PPT](bioinfo-6-141007062607-conversion-gate01.pptx)

## Introduction
Many tasks in computational biology are dependent on the existence of reference genomes. If
you are performing a sequence alignment, finding genes, or studying genetics of populations
at several points of your work, you will be directly or indirectly using a genome reference. In
this chapter, we will develop some recipes to work with reference genomes and deal with
varying quality of references (which can vary for high-quality, like with the human genome, to
problematic with non-model species). We will also see how to deal with genome annotations
(working with text databases that will point us to interesting features in the genome) and
extract sequence data using the annotation information. Also, we will try to find some gene
orthologues across species. Finally, we will access a gene ontology (GO) database.
