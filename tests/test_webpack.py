#
# Copyright (c) 2025 CESNET z.s.p.o.
#
# This file is a part of oarepo-theme (see https://github.com/oarepo/theme).
#
# oarepo-theme is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.
#
"""OARepo theme test suite for webpack integration."""

from __future__ import annotations

from importlib.metadata import entry_points

from flask import current_app
from flask_webpackext import current_webpack


def enumerate_assets():
    asset_dirs = []
    generated_paths = []
    aliases = {}
    themes = current_app.config["APP_THEME"] or ["semantic-ui"]
    project = current_webpack.project
    if hasattr(project, "generated_paths"):
        generated_paths += project.generated_paths

    for ep in entry_points(group="invenio_assets.webpack"):
        webpack = ep.load()
        for wp_theme_name, wp_theme in webpack.themes.items():
            if wp_theme_name in themes:
                asset_dirs.append(wp_theme.path)
                if hasattr(wp_theme, "generated_paths"):
                    generated_paths += list(set(wp_theme.generated_paths) - set(generated_paths))
                aliases.update(wp_theme.aliases)
    return aliases, asset_dirs, generated_paths


def test_webpack_themes(ui_app):
    with ui_app.app_context():
        aliases, _asset_dirs, generated_paths = enumerate_assets()
        assert "../../theme.config$" in aliases
        assert "../../less/site" in aliases
        assert "../../less" in aliases
        assert "@less" in aliases
        assert "themes/oarepo" in aliases
        assert generated_paths == []
