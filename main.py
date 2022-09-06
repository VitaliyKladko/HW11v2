from flask import Flask, render_template
from utils import load_candidates_from_json, get_candidate_id, get_candidates_by_name, get_candidates_by_skill

app = Flask(__name__)
app.debug = True

DATA_JSON = 'candidates.json'

# Это список объектов(экз. Candidate) всех кандидатов
candidate_list_obj = load_candidates_from_json(DATA_JSON)

@app.route('/')
def main_page():
    return render_template('list.html', data=candidate_list_obj)

@app.route('/candidate/<int:id>/')
def get_candidate_by_id(id):
    cand_by_id = get_candidate_id(id, candidate_list_obj)
    img = 'https://cdn.oboi7.com/static/images/m/eb/d4/ebd49b562c85011b4b86a98b2a1f2dc5758f1138.jpg'
    if cand_by_id:
        return render_template('card.html', name=cand_by_id.name, pos=cand_by_id.position, picture=img, skills=cand_by_id.skills)
    return "Not Found"

@app.route('/search/<candidate_name>/')
def get_candidate_by_name(candidate_name):
    cand_by_name = get_candidates_by_name(candidate_name, candidate_list_obj)
    if cand_by_name:
        return render_template('candidate_name.html', cand_by_name=cand_by_name)
    return "Not Found"


@app.route('/skill/<skill_name>/')
def candidate_by_skill(skill_name):
    cand_by_ckill = get_candidates_by_skill(skill_name, candidate_list_obj)
    return render_template('search.html', data=cand_by_ckill, skill=skill_name)

if __name__ == '__main__':
    app.run()
