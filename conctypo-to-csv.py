# conctypo-to-csv.py

from __future__ import unicode_literals, print_function

import plac, csv, json, os
import pandas as pd

# define the arguments that can be called when running the program from terminal
@plac.annotations(
    sample=("Language sample. Options are WALS-174, Hasp-100, WALS-100. Defaults to all.", "option", "s", str),
    fname=("Filename. Defaults to conctypo-data.csv", "option","n",str))

def main(sample=None, fname="conctypo-data.csv"):

    dir_path = "conctypo-data/"

    features = [('Gender','g'),('Number','n'),('Case','c'),('Def','d',),('Person','p'),('Clf','f')]
    categories = ['Dem','Num','Adj']

    data = dict()

    # scans dir_path and loads all the data
    for entry in os.scandir(dir_path):
        if entry.path.endswith(".json"):
            with open(entry.path) as lg_data:
                entry = json.load(lg_data)
                if sample is None or sample in entry['Samples']:
                    data[entry['code']] = entry

    print("Loaded {} lgs".format(len(data)))

    # if we find a category containing "x" then we can set all booleans to 0
    def set_no_concord(lg,cat):
        for (feature,f) in features:
            label = feature+"_"+cat
            lg[label] = 0

    # a function to set whether the lexical category exists
    def set_exist(lg,cat,boolean):
        label = "Exist_"+cat
        lg[label] = boolean

    # a function that defines a key FEATURE_CAT and then sets it to 0 or 1
    # depending on whether its abbreviated form shows up in the CAT value 
    # from the dictionary
    def set_feature(lg,cat,feature,f):
        label = feature+"_"+cat
        if f in lg[cat]:
            lg[label] = 1
        else:
            lg[label] = 0

    # checks the free-form value in the corresponding CAT dictionary entry 
    # and then sets booleans accordingly
    def set_concord(lg,cat):
        if 'z' in lg[cat].lower():
            set_exist(lg,cat,0)
            set_no_concord(lg,cat)
        if 'x' in lg[cat].lower():
            set_no_concord(lg,cat)
        else:
            for (feature,f) in features:
                set_feature(lg,cat,feature,f)

    print("Setting boolean values...")

    for lg in data:
        for cat in categories:
            set_exist(data[lg],cat,1)
            set_concord(data[lg],cat)

    pd_data = pd.DataFrame.from_dict(data, orient='index')
    cols = ['Language','code','Glottocode','Genus','Subfamily','Family','Area']
    for cat in categories:
        for t in ['Exist','Gender','Number','Case']:
            label = t+"_"+cat
            cols.append(label)
    
    with open(fname,"w") as file:
        file.write(pd_data.filter(items=cols).to_csv(index=False))

if __name__ == '__main__':
    plac.call(main)