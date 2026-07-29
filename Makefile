PYTHON ?= python3

.PHONY: validate validate-strict test secrets

validate:
	$(PYTHON) aurora-canon-reconciler/scripts/validate_repository.py
	PYTHONPATH=aurora-canon-reconciler/scripts $(PYTHON) -m unittest discover \
		-s aurora-canon-reconciler/tests -p 'test_*.py'

validate-strict:
	$(PYTHON) aurora-canon-reconciler/scripts/validate_repository.py --strict

test:
	PYTHONPATH=aurora-canon-reconciler/scripts $(PYTHON) -m unittest discover \
		-s aurora-canon-reconciler/tests -p 'test_*.py'

secrets:
	gitleaks git . --redact=100
