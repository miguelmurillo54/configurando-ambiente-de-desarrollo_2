echo -- Running environment tests
pip install pipenv
pipenv install pytest
pipenv run pytest -rA envcheck.py > test_results.txt
git add *
git commit -m "Submitting results"
git push
