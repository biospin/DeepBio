
# 7. Using the Protein Data Bank

### In this chapter, we will cover the following recipes:
- [Finding a protein in multiple databases](01.Intro.ipynb)
- [Introducing Bio.PDB](02.PDB.ipynb)
- [Extracting more information from a PDB file](03.Stats.ipynb)
- [Computing molecular distances on a PDB file](04.Distance.ipynb)
- [Performing geometric operations](05.Mass.ipynb)
- [Implementing a basic PDB parser](06.Parser.ipynb)
- [intro PyMol](PyMol_Intro.py)
- [Animating with PyMol](PyMol_Movie.py)
- [Parsing mmCIF files with Biopython](07.mmCIF.ipynb)


## Introduction
Proteomics is the study of proteins that includes the protein function and structure. One
of the main objectives of this field is to characterize the 3D structure of proteins. One of
the most widely known computational resource in the Proteomics field is the Protein Data
Bank, a repository with structural data of large biomolecules. Of course, there are also many
databases that focus instead on protein primary structure; these are somewhat similar to
genomic databases that we have seen in Chapter 2, Next-generation Sequencing.



In this chapter, we will mostly focus on processing data from the PDB. We will see how to
parse PDB files, perform some geometric computations, and visualize molecules. We will
use the old PDB file format because conceptually, it allows you to perform most necessary
operations in a stable environment. Having said that, the newer mmCIF—slated to replace
the PDB format—will also be presented in a later recipe. We will use Biopython and introduce
PyMol for visualization. We will not discuss molecular docking here because this is probably
more suitable a chemoinformatics book.
Throughout this chapter, we will use a classic example of a protein: Tumor protein p53, a
protein involved in the regulation of the cell cycle (for example, apoptosis). This protein is
highly related to cancer. There is plenty of information available about this protein on the Web.
Let's start with something that you should be more familiar with right now: accessing
databases, especially for the protein primary structure (sequences of amino acids).