# OARepo Theme

SemanticUI theme overlay for [Invenio](https://inveniosoftware.org/) framework based repositories.

## Overview

This package provides a customized Semantic UI theme configuration for Invenio applications, specifically designed to integrate with OARepo repositories. It extends the default Invenio-App-RDM theme with custom styling capabilities and supports integration with multiple OARepo UI packages.

## Installation

```bash
pip install oarepo-theme
```

### Requirements

- Python 3.13+
- Invenio 14.x
- OARepo 14.x

## Key Features

### 1. Webpack Theme Bundle Integration

**Source:** [`oarepo_theme/webpack.py`](oarepo_theme/webpack.py)

The package provides a `WebpackThemeBundle` that integrates with Invenio's asset management system:

```python
from oarepo_theme.webpack import theme

# The theme bundle is automatically loaded via entry points
# It provides Semantic UI theme configuration with custom aliases
```

**Key capabilities:**

- Webpack bundle configuration for Semantic UI assets
- Path aliases for Less/CSS customization
- Integration with Invenio's asset compilation pipeline
- Support for custom theme overrides

### 2. Theme Configuration System

**Source:** [`oarepo_theme/assets/semantic-ui/less/theme.config`](oarepo_theme/assets/semantic-ui/less/theme.config)

Centralized theme configuration that sets Semantic UI component themes:

```less
/* Global */
@site        : 'rdm';
@reset       : 'default';

/* Elements */
@button      : 'rdm';
@container   : 'rdm';
@header      : 'rdm';
@input       : 'rdm';
@label       : 'rdm';
/* ... and more */
```

The configuration specifies which theme variant to use for each Semantic UI component, defaulting to the 'rdm' theme from Invenio-App-RDM.

### 3. Custom Theme Override System

**Source:** [`oarepo_theme/assets/semantic-ui/less/oarepo/theme.less`](oarepo_theme/assets/semantic-ui/less/oarepo/theme.less)

Hierarchical theme loading system that supports multiple customization layers:

```less
/* Loading order (from lowest to highest priority): */
1. Default Semantic UI theme
2. Packaged SUI theme
3. Invenio-theme
4. Invenio-App-RDM theme
5. OARepo package themes (oarepo_ui, oarepo_vocabularies_ui, etc.)
6. Custom component variables
7. Site-specific overrides
```

**Supported OARepo packages:**

- `oarepo_ui` - Core UI components
- `oarepo_vocabularies_ui` - Vocabulary management UI
- `oarepo_dashboard` - Dashboard components
- `oarepo_communities` - Community features
- `oarepo_requests_ui` - Request workflow UI

Each package can provide:

- Component variables (`.variables` files)
- Style overrides (`.overrides` files)

### 4. Webpack Aliases

The theme bundle configures the following Webpack aliases for easy asset referencing:

| Alias | Target | Purpose |
|-------|--------|---------|
| `../../theme.config$` | `less/theme.config` | Theme configuration file |
| `../../less/site` | `less/site` | Site-specific styles |
| `../../less` | `less` | Less source directory |
| `@less` | `less` | Less imports shorthand |
| `themes/oarepo` | `less/oarepo` | OARepo theme directory |

Usage in Less files:

```less
@import "@less/oarepo/custom-component.less";
@import "themes/oarepo/theme.less";
```

### 5. Custom Template Support

**Source:** [`oarepo_theme/assets/semantic-ui/templates/`](oarepo_theme/assets/semantic-ui/templates/)

The package provides template directories for customizing UI components:

- `custom_fields/` - Templates for custom field rendering

Templates can be overridden in your application by placing files in the same structure.

## Development

### Setup

```bash
# Clone repository
git clone https://github.com/oarepo/oarepo-theme.git
cd oarepo-theme

./run.sh venv
```

### Running Tests

```bash
./run.sh test
```

Or run specific test file:

```bash
pytest tests/test_webpack.py -s
```

### Testing Theme Integration

The package includes tests that verify:

- Webpack alias configuration
- Theme bundle registration
- Asset directory paths
- Entry point loading

See [`tests/test_webpack.py`](tests/test_webpack.py) for examples.

## Integration with OARepo Applications

### Using the Theme in Your Application

The theme is automatically registered via Invenio entry points when installed:

```python
[project.entry-points."invenio_assets.webpack"]
oarepo_theme = "oarepo_theme.webpack:theme"
```

No additional configuration is needed - the theme will be available after installation.

### Customizing the Theme

To customize the theme in your application:

1. **Override variables:** Create files in your app's `assets/less/` directory:

   ```less
   /* assets/less/globals/site.variables */
   @primaryColor: #2185d0;
   @linkColor: #4183c4;
   ```

2. **Add custom styles:** Create override files:

   ```less
   /* assets/less/elements/button.overrides */
   .ui.button {
     border-radius: 4px;
   }
   ```

3. **Extend component themes:** Add package-specific overrides following the pattern in `theme.less`.

### Building Assets

After making theme changes:

```bash
# In your Invenio application
invenio webpack buildall
```

## Entry Points

The package registers the following Invenio entry point:

```python
[project.entry-points."invenio_assets.webpack"]
oarepo_theme = "oarepo_theme.webpack:theme"
```

This entry point is automatically discovered by Invenio and makes the theme available to the asset compilation system.

## Architecture

### Theme Loading Hierarchy

The theme system follows a cascading architecture where each layer can override the previous ones:

```text
Semantic UI Default
    ↓
Packaged Theme (e.g., 'default', 'rdm')
    ↓
Invenio Theme (invenio-theme)
    ↓
Invenio-App-RDM Theme
    ↓
OARepo Package Themes (oarepo_ui, oarepo_vocabularies_ui, etc.)
    ↓
Site Custom Components
    ↓
Application-Specific Overrides
```

This allows for maximum flexibility while maintaining consistency across OARepo applications.

### Asset Organization

```text
oarepo_theme/
├── assets/
│   └── semantic-ui/
│       ├── less/
│       │   ├── theme.config          # Theme component configuration
│       │   └── oarepo/
│       │       └── theme.less         # Custom theme loader
│       └── templates/
│           └── custom_fields/         # Custom field templates
└── webpack.py                         # Webpack bundle definition
```

## License

Copyright (c) 2025 CESNET z.s.p.o.

OARepo Theme is free software; you can redistribute it and/or modify it under the terms of the MIT License. See [LICENSE](LICENSE) file for more details.

## Links

- Documentation: <https://github.com/oarepo/oarepo-theme>
- PyPI: <https://pypi.org/project/oarepo-theme/>
- Issues: <https://github.com/oarepo/oarepo-theme/issues>
- OARepo Project: <https://github.com/oarepo>

## Acknowledgments

This project builds upon [Invenio Framework](https://inveniosoftware.org/) and [Semantic UI](https://semantic-ui.com/), and is developed as part of the OARepo ecosystem.
