#!/usr/bin/env python3
"""Check portfolio coverage, data integrity, derived numbers and Markdown links.

Uses only Python's standard library. Supports the full main-branch collection
or a single project branch. Does not assert real control effectiveness.
"""
from pathlib import Path
import json
import re
from collections import Counter
from statistics import median

ROOT = Path(__file__).resolve().parents[1]
P = ROOT / 'projects'

def check(condition, message):
    if not condition:
        raise SystemExit('FAIL: ' + message)

def load(path):
    return json.loads(path.read_text())

def rating(score):
    return 'Critical' if score >= 20 else 'High' if score >= 12 else 'Medium' if score >= 6 else 'Low'

expected_controls = {f'{group}.{n}' for group, count in [(5, 37), (6, 8), (7, 14), (8, 34)] for n in range(1, count + 1)}
path = P / 'ISO-27001-Gap-analysis' / 'controls.json'
if path.exists():
    controls = load(path)
    check(len(controls) == 93 and {r['id'] for r in controls} == expected_controls, 'Annex A coverage or duplicates')
    check(len({r['evidence'] for r in controls}) == 93, 'Duplicate evidence IDs')
    for r in controls:
        check(all(r.get(k) for k in ['current_state', 'remediation', 'closure_test', 'owner', 'due', 'rationale']), r['id'] + ' missing detail')
        check(r['status'] in {'Implemented', 'Partial', 'Missing'}, r['id'] + ' status')
        check(r['action_id'] == 'ACT-' + r['id'], r['id'] + ' action reference')
    check(Counter(r['status'] for r in controls) == {'Implemented': 5, 'Partial': 61, 'Missing': 27}, 'Control summary changed: update narrative')
    print('PASS: 93 unique controls; observations, actions and evidence references complete')

path = P / 'Conducting-a-Risk-Assessment-using-NIST' / 'risk-register.json'
if path.exists():
    risks = load(path)
    check(len(risks) == 16 and len({r['id'] for r in risks}) == 16, 'Risk count or IDs')
    asset_text = (path.parent / 'asset-inventory.md').read_text()
    asset_ids = set(re.findall(r'\| (A\d{2}) \|', asset_text))
    check(len(asset_ids) == 12, 'Asset count')
    for r in risks:
        check(set(r['asset_ids']) <= asset_ids, r['id'] + ' invalid asset')
        check(set(r['annex_a']) <= expected_controls, r['id'] + ' invalid control')
        for stage in ['inherent', 'current', 'target']:
            l, i = r[stage + '_likelihood'], r[stage + '_impact']
            check(1 <= l <= 5 and 1 <= i <= 5, r['id'] + ' scale')
            check(r[stage + '_score'] == l*i, r['id'] + ' arithmetic')
            check(r[stage + '_rating'] == rating(l*i), r['id'] + ' rating')
        check(r['target_score'] <= r['current_score'] <= r['inherent_score'], r['id'] + ' unexplained score direction')
        check(r['target_assumption'] and r['acceptance_evidence'] and r['due_scope'], r['id'] + ' treatment rationale or milestone scope missing')
        check(r['confidence'].startswith('Low'), r['id'] + ' evidence confidence')
        if r['id'] in {'R06', 'R08', 'R11'}:
            check(r['target_impact'] == r['current_impact'], r['id'] + ' unsupported impact reduction')
        if (P / 'ISO-27001-Gap-analysis' / 'controls.json').exists():
            by_id = {c['id']: c for c in controls}
            for ref in r['annex_a']:
                check(by_id[ref]['closure_test'] in r['acceptance_evidence'], r['id'] + ' stale action acceptance test')
    check(Counter(r['current_rating'] for r in risks) == {'Critical': 4, 'High': 10, 'Medium': 2}, 'Risk narrative totals')
    print('PASS: 12 assets, 16 risks; 48 scores and ratings; control cross-references')

path = P / 'Building-a-Third-Party-Vendor-Risk-Assessment' / 'assessment-data.json'
if path.exists():
    data = load(path)
    weights = {q['id']: q['weight'] for q in data['questions']}
    check(len(weights) == 24 and len(data['vendors']) == 3, 'Question/vendor count')
    gates = {'Q03', 'Q06', 'Q09', 'Q13', 'Q17'}
    for v in data['vendors']:
        rows = v['responses']
        check(len(rows) == 24 and {r['question_id'] for r in rows} == set(weights), v['name'] + ' response coverage')
        for r in rows:
            check(r['score'] in [0, 1, 2], v['name'] + ' response score')
            check(r['weighted_gap'] == weights[r['question_id']]*(2-r['score']), v['name'] + ' item arithmetic')
        points = sum(r['weighted_gap'] for r in rows)
        maximum = 2*sum(weights.values())
        pct = 100*points/maximum
        base = 'Low' if pct <= 15 else 'Moderate' if pct <= 35 else 'High' if pct <= 60 else 'Critical'
        unmet = [r['question_id'] for r in rows if r['question_id'] in gates and r['score'] < 2]
        final = 'Critical' if base == 'Critical' else 'High' if unmet else base
        check((v['gap_points'], v['max_points'], v['gap_percent']) == (points, maximum, round(pct, 2)), v['name'] + ' total arithmetic')
        check((v['base_rating'], v['unmet_gates'], v['final_rating']) == (base, unmet, final), v['name'] + ' gate/rating')
        if v['name'] == 'Cedar Insight Analytics':
            check(all(r['score'] == 0 for r in rows if r['question_id'] in {'Q05','Q11','Q24'}), 'Cedar unsupported claims credited')
    print('PASS: 72 vendor responses; weighted totals and mandatory gate overrides')

path = P / 'Designing-a-security-awareness-training-program' / 'synthetic-campaign-data.json'
if path.exists():
    data = load(path)
    events = data['events']
    check(data['simulated'] is True and len(events) == 240, 'Synthetic data identification/count')
    cohorts = []
    for campaign in ['baseline', 'follow-up']:
        rows = [r for r in events if r['campaign'] == campaign]
        ids = {r['participant_id'] for r in rows}
        cohorts.append(ids)
        check(len(ids) == len(rows) == 120, 'Campaign unique population')
        check(Counter(r['department'] for r in rows) == {'Engineering':35,'Customer Operations':30,'Sales':25,'Corporate Services':20,'Leadership':10}, 'Department totals')
        for r in rows:
            check(not r['dummy_submit'] or r['unique_human_click'], 'Submission without click')
            check(not r['unique_human_click'] or r['delivered'], 'Click without delivery')
            check((r['report_minutes'] is not None) == r['reported'], 'Report time missing or unexpected')
        den = sum(r['delivered'] for r in rows)
        m = data['expected_metrics'][campaign]
        check(m['delivered'] == den, 'Delivery denominator')
        report_text = (path.parent / 'campaign-results-report.md').read_text()
        minutes = median(r['report_minutes'] for r in rows if r['reported'])
        check(f'{minutes:.1f} min' in report_text, 'Median reporting time mismatch')
        for department in {r['department'] for r in rows}:
            group = [r for r in rows if r['department'] == department]
            group_den = sum(r['delivered'] for r in group)
            report_row = next(line for line in report_text.splitlines() if line.startswith('| '+department+' |'))
            cells = [cell.strip() for cell in report_row.split('|')[1:-1]]
            offset = 2 if campaign == 'baseline' else 3
            for index, field in [(offset, 'unique_human_click'), (offset+2, 'reported')]:
                count = sum(r[field] for r in group)
                check(cells[index] == f'{count}/{group_den} ({100*count/group_den:.2f}%)', 'Department metric mismatch: '+department)
        for label, field in [('clicks','unique_human_click'),('submissions','dummy_submit'),('reports','reported')]:
            count = sum(r[field] for r in rows)
            check(m[label] == count and m[label+'_rate'] == round(100*count/den, 2), 'Campaign derived metric')
    check(cohorts[0] == cohorts[1], 'Cohort mismatch')
    check([data['expected_metrics'][c]['clicks'] for c in ['baseline','follow-up']] == [24,10], 'Click narrative')
    check([data['expected_metrics'][c]['reports'] for c in ['baseline','follow-up']] == [30,60], 'Report narrative')
    print('PASS: 240 participant-round records; cohorts, department totals and reported rates')

markdown_files = list(P.rglob('*.md')) + [ROOT/'README.md']
for path in list(P.rglob('*')) + list((ROOT/'tools').glob('*.py')) + [ROOT/'README.md']:
    if path.is_file():
        text = path.read_text()
        check(chr(0x2014) not in text and ('\\u' + '2014') not in text.lower(), str(path) + ' em dash found')
contexts = [path.read_text() for path in P.glob('*/company-context.md')]
check(len(set(contexts)) <= 1, 'Company context differs between projects')
for path in markdown_files:
    text = path.read_text()
    check(text.count('```') % 2 == 0, str(path) + ' unclosed code fence')
    for target in re.findall(r'\[[^\]]*\]\(([^)]+)\)', text):
        if target.startswith(('https://', 'http://', 'mailto:', '#')):
            continue
        local = target.split('#', 1)[0]
        check((path.parent/local).exists(), f'{path.relative_to(ROOT)} -> missing {target}')
    for line in text.splitlines():
        if line.startswith('|'):
            check(line.endswith('|'), str(path) + ' malformed table row')
print(f'PASS: local links and Markdown structure in {len(markdown_files)} documents')
print('Validation complete. These checks do not establish real-world assurance or legal compliance.')
