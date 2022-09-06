import json
from classCand import Candidate

def load_candidates_from_json(path):
    """
    Возвращает список объектов класса Candidate
    """
    with open(path, 'r', encoding='utf-8') as file:
        data_candidate = json.load(file)
        candidate_list_obj = []
        for item in data_candidate:
            id = item['id']
            name = item['name']
            picture = item['picture']
            position = item['position']
            gender = item['gender']
            age = item['age']
            skills = item['skills']
            candidate = Candidate(id, name, picture, position, gender, age, skills)
            candidate_list_obj.append(candidate)
    return candidate_list_obj

def get_candidate_id(candidate_id, candidate_list_obj):
    """
    Возвращает одного кандидата по его ID
    Функция возвращает объект класса Candidate
    """
    for candidate in candidate_list_obj:
        if candidate.id == candidate_id:
            return candidate

def get_candidates_by_name(candidate_name, candidate_list_obj):
    """
    Возвращает кандидатов по имени(именно по имени)
    """
    candidate_classes = []
    for candidate in candidate_list_obj:
        if candidate_name.lower() in candidate.name.lower():
            candidate_classes.append(candidate)
    return candidate_classes


def get_candidates_by_skill(skill_name, candidate_list_obj):
    """
    Возвращает кандидатов по skills
    """
    candidate__by_skill = []
    for candidate in candidate_list_obj:
        if skill_name.lower() in candidate.skills.lower():
            candidate__by_skill.append(candidate)
    return candidate__by_skill

