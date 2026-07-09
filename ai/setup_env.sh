#!/bin/bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$SCRIPT_DIR"

# Load Miniconda (adjust module name for your HPC if needed)
if command -v module >/dev/null 2>&1; then
  module load miniconda3/24.1.2-py310 2>/dev/null || true
fi

# Create Conda environment from this directory's environment.yml
conda env create -f environment.yml

# Activate the environment
conda activate 7030_class_1

# Install optional pip packages
pip install -r requirements.txt

# Register Python kernel
python -m ipykernel install --user --name 7030_class_1 --display-name "Python (7030_class_1)"

# Register R kernel
Rscript -e 'IRkernel::installspec(name="ir_7030_class_1", displayname="R (7030_class_1)")'

echo "Environment setup complete. Start JupyterLab with:"
echo "  conda activate 7030_class_1"
echo "  jupyter lab --no-browser --port=2000"
