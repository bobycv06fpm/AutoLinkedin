def getSkills():
    import pandas as pd

    data = pd.read_excel('../../data/skills/Skillset.xlsx', engine='openpyxl')
    skills_dict = {}

    skills_dict['Maths'] = [x.lower() for x in data['Maths'].values.tolist() if str(x) != 'nan']
    skills_dict['Autres'] = [x.lower() for x in data['Autres'].values.tolist() if str(x) != 'nan']
    skills_dict['Soft_Skills'] = [x.lower() for x in data['Soft_Skills'].values.tolist() if str(x) != 'nan']
    skills_dict['ML/AI'] = [x.lower() for x in data['ML/AI'].values.tolist() if str(x) != 'nan']
    skills_dict['Visualisation'] = [x.lower() for x in data['Visualisation'].values.tolist() if str(x) != 'nan']
    skills_dict['MLOps'] = [x.lower() for x in data['MLOps'].values.tolist() if str(x) != 'nan']
    skills_dict['Langages'] = [x.lower() for x in data['Langages'].values.tolist() if str(x) != 'nan']
    skills_dict['Web'] = [x.lower() for x in data['Web'].values.tolist() if str(x) != 'nan']

    return skills_dict

def findSkillType(skill, skills_dict):
    for skills_cat in skills_dict.keys():
        if skill in skills_dict[skills_cat]:
            return skills_cat
    return 'Autres'

def clusterSkills(skills_list, skills_dict):
    skills_type = {}
    for skill in skills_list:
        skills_type[skill] = findSkillType(skill, skills_dict)
    inv_map = {}
    for k, v in skills_type.items():
        inv_map[v] = inv_map.get(v, []) + [k]
    return inv_map

def merge_skills(dict1, dict2):
     dict3 = {}
     for key in set().union(dict1, dict2):
         if key in dict1: dict3.setdefault(key, []).extend(dict1[key])
         if key in dict2: dict3.setdefault(key, []).extend(dict2[key])
     return dict3