#
# Copyright (c) 2025 CESNET z.s.p.o.
#
# This file is a part of oarepo-theme (see https://github.com/oarepo/oarepo-theme).
#
# oarepo-theme is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.
#
"""Pytest configuration.

See https://pytest-invenio.readthedocs.io/ for documentation on which test
fixtures are available.
"""

from __future__ import annotations

import pytest
from invenio_app.factory import create_ui as _create_ui


@pytest.fixture(scope="module")
def ui_app(request, app_config):
    """UI Application fixture."""
    app = _create_ui()
    app.config.update(app_config)
    return app
