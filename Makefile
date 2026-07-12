PYTHON ?= python
CXX ?= g++
CXXFLAGS ?= -O3 -std=c++17 -Wall -Wextra

.PHONY: test reproduce-small reproduce-cpp manifest clean

test:
	PYTHONPATH=. $(PYTHON) -m pytest -q

reproduce-small:
	PYTHONPATH=. $(PYTHON) repro_runs/scripts/bf_quadratic_checks.py | tee repro_runs/scripts/bf_quadratic_checks.stdout
	PYTHONPATH=. $(PYTHON) repro_runs/scripts/blossom_certificate.py | tee repro_runs/scripts/blossom_certificate.stdout
	PYTHONPATH=. $(PYTHON) repro_runs/scripts/three_decomposition_exhaustive.py | tee repro_runs/scripts/three_decomposition_exhaustive.stdout
	PYTHONPATH=. $(PYTHON) repro_runs/scripts/combined_checks.py | tee repro_runs/scripts/combined_checks.stdout
	PYTHONPATH=. $(PYTHON) repro_runs/scripts/other_conjectures_checks.py | tee repro_runs/scripts/other_conjectures_checks.stdout

reproduce-cpp:
	mkdir -p build
	$(CXX) $(CXXFLAGS) berge_fulkerson/cpp/j5_rewrite.cpp -o build/j5_rewrite
	build/j5_rewrite < berge_fulkerson/instances/j5/j5_input.txt | tee berge_fulkerson/logs/j5res_reproduced.txt
	$(CXX) $(CXXFLAGS) barnette/cpp/test_barnette_k.cpp -o build/test_barnette_k
	build/test_barnette_k < barnette/instances/steps8.txt | tee barnette/logs/steps8res_reproduced.txt

manifest:
	find . -type f -not -path './.git/*' -not -name 'SHA256SUMS.txt' -print0 | sort -z | xargs -0 sha256sum > SHA256SUMS.txt

clean:
	find . -name '__pycache__' -type d -prune -exec rm -rf {} +
	find . -name '*.pyc' -delete
	rm -rf build .pytest_cache
