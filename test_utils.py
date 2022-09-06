from utils import load_candidates_from_json, get_candidate_id, get_candidates_by_name, get_candidates_by_skill


DATA_JSON = 'candidates.json'

data_cand = load_candidates_from_json(DATA_JSON)

cand_id = get_candidate_id(1, data_cand)


cand_name = get_candidates_by_name('AdEla', data_cand)
print(cand_name)

cand_skill = get_candidates_by_skill('pythoN', data_cand)

print(len(cand_skill))