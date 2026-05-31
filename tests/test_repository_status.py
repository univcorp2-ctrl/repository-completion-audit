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
        assert repo['status'] in {'complete', 'fixed_verifying', 'needs_attention', 'scaffold', 'not_fully_checked'}


def test_attention_items_are_visible() -> None:
    data = load_status()
    attention = [repo for repo in data['repositories'] if repo['status'] == 'needs_attention']
    names = {repo['name'] for repo in attention}
    assert {'real-estate-sender-automation', 'gmail-sheets-property-mailer', 'github-full-automation'} <= names
