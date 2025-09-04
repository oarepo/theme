#
# Copyright (c) 2025 CESNET z.s.p.o.
#
# This file is a part of oarepo-theme (see https://github.com/oarepo/theme).
#
# oarepo-theme is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.
#
"""OARepo theme test suite for webpack integration."""

from oarepo_runtime.cli.assets import enumerate_assets


def test_webpack_themes(ui_app):
    with ui_app.app_context():
        aliases, asset_dirs, generated_paths = enumerate_assets()
        assert "../../theme.config$" in aliases
        assert "../../less/site" in aliases
        assert "../../less" in aliases
        assert "@less" in aliases
        assert "themes/oarepo" in aliases
        assert generated_paths == []
