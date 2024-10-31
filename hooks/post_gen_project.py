import os

REMOVE_PATHS = [
    '{% if not cookiecutter.same_dir %}{{ cookiecutter.__project_name }}.cpp{% endif %}',
    '{% if not cookiecutter.same_dir %}{{ cookiecutter.__project_name }}.h{% endif %}',
    '{% if cookiecutter.same_dir %}{{ cookiecutter.__project_name }}\\{{ cookiecutter.__project_name }}.cpp{% endif %}',
    '{% if cookiecutter.same_dir %}{{ cookiecutter.__project_name }}\\{{ cookiecutter.__project_name }}.h{% endif %}',
    '{% if cookiecutter.same_dir %}{{ cookiecutter.__project_name }}\\CMakeLists.txt{% endif %}',
    '{% if cookiecutter.same_dir %}{{ cookiecutter.__project_name }}\\{% endif %}',
]

for path in REMOVE_PATHS:
    path = path.strip()
    if path and os.path.exists(path):
        os.unlink(path) if os.path.isfile(path) else os.rmdir(path)