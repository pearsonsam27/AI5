1.) Samuel Pearson 10711339
2.) Python
3.) Windows 10
4.) I first create the Bayesian Network by checking the inputs and setting components probabilities respective to their inputs.
For example: if Bt and Et are in inputs, alarm is set to .95

Then the computeProbability() is run, where it cycles through the inputs multiplying probabilities.
It breaks at given as those probabilities are established when the network is initialized.

5.) 
This can be run from cmd prompt assuming python.exe is setup as the default for .py files
From the project folder I run an input like:
	python bnet.py Jt Af given Bt Ef