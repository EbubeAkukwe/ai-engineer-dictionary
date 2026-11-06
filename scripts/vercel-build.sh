#!/usr/bin/env bash
set -euo pipefail

QUARTO_VERSION="1.10.20"
QUARTO_SHA256="c43fc13454337b7ca73ee78371228e1554679053b856a4ff07f068f2c36a5202"

if [[ "${VERCEL:-}" != "1" ]] && command -v quarto >/dev/null 2>&1 \
  && [[ "$(quarto --version)" == "$QUARTO_VERSION" ]]; then
  exec quarto render --output-dir _site
fi

if [[ "$(uname -s)" != "Linux" || "$(uname -m)" != "x86_64" ]]; then
  echo "This installer expects Vercel's Linux x86_64 build environment." >&2
  exit 1
fi

if ! command -v python3 >/dev/null 2>&1; then
  echo "Python 3 is required to render the project's Jupyter notebooks." >&2
  exit 1
fi

install_root=".vercel/quarto-cli"
python_env=".vercel/python"
mkdir -p "$install_root"

archive="$install_root/quarto-${QUARTO_VERSION}-linux-amd64.tar.gz"
release_url="https://github.com/quarto-dev/quarto-cli/releases/download/v${QUARTO_VERSION}"

curl --fail --location --silent --show-error \
  "$release_url/quarto-${QUARTO_VERSION}-linux-amd64.tar.gz" \
  --output "$archive"
printf '%s  %s\n' "$QUARTO_SHA256" "$archive" | sha256sum --check -

tar -xzf "$archive" -C "$install_root" --strip-components=1
quarto_bin="$install_root/bin/quarto"
if [[ "$("$quarto_bin" --version)" != "$QUARTO_VERSION" ]]; then
  echo "Installed Quarto version did not match $QUARTO_VERSION." >&2
  exit 1
fi

python3 -m venv "$python_env"
"$python_env/bin/python" -m pip install --disable-pip-version-check \
  -r requirements-build.txt
PATH="$python_env/bin:$PATH" "$quarto_bin" render --output-dir _site
