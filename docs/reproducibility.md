# Reproducibility

## Environment

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Core checks

```bash
make test
make reproduce-small
make reproduce-cpp
```

`make test` runs the repository's independent unit and certificate checks. `make reproduce-small` reruns the exact Python experiments. `make reproduce-cpp` compiles and runs the Flower-snark normalizer and the selected Barnette reverse-reachability batch.

The public repository contains software, data, and certificates. Manuscript compilation is intentionally handled in the separate private author bundle.

Historical logs whose original random-generation pipelines were not fully recoverable are labelled as historical rather than reproducible results in [`mathematical_status.md`](mathematical_status.md).
