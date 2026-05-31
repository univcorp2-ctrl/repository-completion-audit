import json
from pathlib import Path


def load_status() -> dict:
    return json.loads(Path('repository-status.json').read_text(encoding='utf-8'))


def test_repository_count_matches_entries() -> None:
    data = load_status()
    assert data['total_repositories'] == len(data['repositories']) == 33


def test_required_fields_exist() -> None:
    required = {'name', 'program', 'status', 'ci', 'action'}
    data = load_status()
    for repo in data['repositories']:
        assert required <= repo.keys(), repo
        assert repo['name']
        assert repo['status'] in {'complete', 'needs_attention', 'scaffold', 'not_fully_checked'}


def test_attention_items_are_visible() -> None:
    data = load_status()
    attention = [repo for repo in data['repositories'] if repo['status'] == 'needs_attention']
    names = {repo['name'] for repo in attention}
    assert {'real-estate-sender-automation', 'gmail-sheets-property-mailer', 'github-full-automation'} <= names


def test_global_job_aggregator_is_verified() -> None:
    data = load_status()
    repo = next(item for item in data['repositories'] if item['name'] == 'global-job-aggregator-mvp')
    assert repo['status'] == 'complete'
    assert 'collect_success' in repo['ci']
