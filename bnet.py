# This is a sample Python script.
import sys
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

inputs=[]
for index in range(len(sys.argv)):
    if(index!=0):
        inputs.append(sys.argv[index])

def bnet():

    class BayesianNetwork:
        pass
    probabilities = BayesianNetwork()

    if "Bt" in inputs:
        if "Et" in inputs:
            alarm = 0.95
        else:
            alarm = 0.94

    else:
        if "Et" in inputs:
            alarm = 0.29
        else:
            alarm = 0.001

    if "At" in inputs:
        probabilities.Jt = 0.9
        probabilities.Mt = 0.7
    else:
        probabilities.Jt = 0.05
        probabilities.Mt = 0.01

    probabilities.Et=0.002
    probabilities.Ef=0.998
    probabilities.Bt=0.001
    probabilities.Bf=0.999

    def computeProbability():
        probability = float(1.0)
        for input in inputs:

            if input=="given":
                break

            if input=='At':
                probability = float(alarm) * probability
                continue
            if input=='Af':
                probability = float(1-alarm) * probability
                continue


            if input=='Jf':
                probability=probability * float(1-getattr(probabilities, 'Jt'))
                continue
            if input=='Mf':
                probability = probability * float(1 - getattr(probabilities, 'Mt'))
                continue


            probability=float(getattr(probabilities,input))*probability

        print("probability: "+'%.10f'%probability)
    computeProbability()
bnet()
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
