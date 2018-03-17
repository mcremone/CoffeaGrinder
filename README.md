# CoffeeMaker

## Update:

Ciao, I have pushed the version of our nanoaod Analyzer reading on multiple nanoaod files hosted in eospublic. The notebook (Zpeak_nano_multipledataset_v2.ipynb) equipped with:

      a.) The Hadoop-Xrootd connector, declared in spark context (EOS.jar) to enable reading nanoaods files hosts in eospublic.
      b.) The code structure is almost identical to Melo's z-mumu-cr.ipynb. By aggregating the derived quantities such as the kinematics of the reconstructed Z boson in a column and save the state variable (pass/fail muon selection). 
      c.) It is a work in progress, we have not figure how to implement the plotting end due to the known issues we have discussed.

## To-do:

      a.) The weights of each processes does not save at first evaluation, looking for a better implementation.
      b.) Plot a histogram with weight from a collection which facilitated with histogrammar features.
      c.) If the plotting issue resolved, we will scale up the operation by topping up more nanoaod MC and datasetsa.
      d.) Re-optimize the code and conduct an assessment on how much we gain from spark in term of time and efficiencies.

If the Zpeak exercise is a success, we can move forward to port other analysis into spark based analytical framework.