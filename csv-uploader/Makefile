PROJ_NAME := $(shell basename $(PWD))
VENVS_DIR := $(HOME)/.venvs
VENV := $(VENVS_DIR)/$(PROJ_NAME)


.PHONY: test
test:
	@echo $(VENV)
	@echo $(SHELL)


.PHONY: help
help:
	@grep "^# help\:" Makefile | grep -v grep | sed 's/\# help\: //' | sed 's/\# help\://'

# help: MAINTAIN
# help: venv            - create a clean virtual environment for development
.PHONY: venv
venv:
	@echo Creating fresh virtual environment $(VENV)...
	@test -d "$(VENVS_DIR)" || mkdir -p "$(VENVS_DIR)"
	@rm -rf "$(VENV)"
	@python3 -m venv "$(VENV)"
	@$(SHELL) -c "source $(VENV)/bin/activate && pip install --upgrade pip setuptools wheel && pip install -r requirements.txt"
	@echo "\nEnter virtual environment using:\n. $(VENV)/bin/activate\n"


# help: venv-update     - update a virtual environment for development
.PHONY: venv-update
venv-update:
	@$(SHELL) -c "source $(VENV)/bin/activate && pip install --upgrade pip setuptools wheel && pip install --upgrade -r requirements.txt"
	@echo "\nEnter virtual environment using:\n. $(VENV)/bin/activate\n"


# help: activate        - enter existing venv
.PHONY: activate
activate:
	@echo "\nEnter virtual environment using:\n. $(VENV)/bin/activate\n"


## help: clean          - clean all files
#.PHONY: clean
#clean:
#	@rm -rf ./site


## help: git-clean      - clean all files using .gitignore rules
#.PHONY: git-clean
#git-clean:
#	@git clean -X -f -d


## help: git-scrub      - clean all files, even untracked files
#.PHONY: git-scrub
#git-scrub:
#	@git clean -x -f -d

# help: git-push       - push files to Github
.PHONY: git-push
git-push:
	@git push origin main

# help:
# help: APPLICATION
# help: run             - launch application 
.PHONY: run
run:
	@$(SHELL) -c "source $(VENV)/bin/activate && export FLASK_ENV=development && python app.py"



# Keep these lines at the end of the file to retain output formatting.
# help:

