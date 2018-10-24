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
## How to run

### Prerequisites

* Python 2.7
* numpy version 1.13.1 
* jupyter 4.3+   
* ipython version 5.7+  
* histbook     
* vega version 1.1 
* uproot 

```
pip install numpy==1.13
pip install jupyter --user
pip install ipython
pip install histbook --user
pip install vega==1.1 --user
pip install uproot --user
```
Note: you might need to upgrade pip to version 18 to get Jupyter 4.3 or above  (`pip install --upgrade pip`)

### Setup
Once you have installed the prerequisites, set up the striped client
```
  git clone http://cdcvs.fnal.gov/projects/nosql-ldrd striped     
  cd striped
  python setup.py install --user 
```

Now on a different directory, clone Coffea repository
```
  git clone git@github.com:LPC-DM/CoffeaMaker.git
  
 ```
### Run
Launch Jypyter Notebook
```
   cd CoffeaMaker/
   jupyter notebook
```
It should open a new page in your default browser. If not , you can follow the link displayed in the terminal.  At the page you will find the directories and files from the location you ran jupyter notebook. select one of the samples to run it.

