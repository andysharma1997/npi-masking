from presidio_analyzer import Pattern,PatternRecognizer
import os.path as path
import pandas as pd

def load_names():
    file_path_male = path.abspath(path.join(__file__,"../../../resources/"+"Indian-Male-Names.csv"))
    file_path_female = path.abspath(path.join(__file__,"../../../resources/"+"Indian-Female-Names.csv"))
    df_male = pd.read_csv(file_path_male)
    df_male.dropna(inplace=True)
    df_male["name"] = df_male.name.apply(lambda x: x.lower())
    df_female = pd.read_csv(file_path_female)
    df_female.dropna(inplace=True)
    df_female["name"] = df_female.name.apply(lambda x: x.lower())
    male_names = df_male.name.to_list()
    female_names = df_female.name.to_list()
    return  male_names + female_names
    
    
class NameRecoganizer:
    expected_confidence_level = 0.7 # expected confidence level for this recognizer
    
    def __init__(self,supported_entity) -> None:
        self.names = load_names()
        self.name_recogizer = PatternRecognizer(supported_entity=supported_entity, deny_list=self.names)
    
    def load(self):
        return self.name_recogizer