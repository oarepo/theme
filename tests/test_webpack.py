"""OARepo theme test suite for webpack integration.
"""
from oarepo_runtime.cli.assets import enumerate_assets


def test_webpack_themes(ui_app):
    with ui_app.app_context():
        aliases, asset_dirs, generated_paths = enumerate_assets()
        assert '../../theme.config$' in aliases
        assert '../../less/site' in aliases
        assert '../../less' in aliases
        assert '@less' in aliases
        assert 'themes/oarepo' in aliases
        assert generated_paths == []
