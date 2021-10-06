Starting Code for lga-coding-sis Programming Questions
=======================================================

For using C++, run make(1) or gmake(1) at the command line, make changes to 
codingsis.cxx.

For Java, run make(1) or gmake(1) at the command line, make changes to 
codingsis.java.

For Python3, simply edit sis-python.


All the programs simulate the flow-balanced simple inventory system
discussed in the text.  Demands are read from a text file (provided as
the first command line argument). The output statistics are the average
demand, order (quantity), order frequency (setup), holding, and shortage
(quantities).

Additionally, all the programs are reasonable representations of
Algorithm 1.3.1 of the text, although some less-subscript-laden variable
names have been used.  The only substantial change is the reporting of
summary statistics instead of the n inventory and order sizes for the
simulation.

