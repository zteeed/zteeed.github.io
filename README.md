# zteeed.github.io

Personal site and blog (Jekyll), deployed on GitHub Pages.

## Setup

Uses [mise](https://mise.jdx.dev/) for Ruby. Ruby and Jekyll/Sass versions are pinned to match [GitHub Pages](https://pages.github.com/versions/) (Ruby 3.3.4, Jekyll 3.10, Sass 3.7) so local build matches production.

```bash
mise install          # install Ruby 3.3.4
mise run install      # bundle install
mise run serve        # jekyll serve (default port 4000)
mise run build        # jekyll build
```

## Deploy

Push to `master`; GitHub Pages builds and serves the site.

## Theme

Based on the [Hacker theme](https://github.com/pages-themes/hacker) for GitHub Pages. Customization: `_config.yml`, `_sass/base.scss`, `_sass/custom.scss`, `_includes/` (header, footer, head).

## License

CC0 1.0 Universal
