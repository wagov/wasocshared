import os
from pathlib import Path
from itertools import groupby
from dateutil.parser import parse


def define_env(env):
    """
    This is the hook for defining variables, macros and filters

    - variables: the dictionary that contains the environment variables
    - macro: a decorator function, to declare a macro.
    """

    def get_title(path):
        line = ""
        with open(path) as f:
            while not line.startswith("#"):
                line = f.readline()
        return line[2:].strip()

    @env.macro
    def date_index(glob, prefix="", expand=3, include=None):
        """
        Insert an index to a glob pattern relative to top dir of documentation project.
        """
        files = Path(env.project_dir).glob(glob)
        mdtext = []
        # Reverse order, sorted by first 6 characters (year + month)
        months = groupby(reversed(sorted(files)), key=lambda f: f.name[0:6])
        month_count = 0
        for month, paths in months:
            month_text = parse(month + "01").strftime("%Y %B")
            if month_count < expand:
                indent = ""
                mdtext.append(f"#### {month_text}")
            else:
                indent = "    "
                mdtext.append(f'??? note "{month_text}"')
            mdtext.append("")
            for path in paths:
                title = get_title(path)
                mdtext.append(f"{indent}- [{title}]({prefix}{path.name})")
            month_count += 1
            if include is not None:
                if month_count > include:
                    break
        return "\n".join(mdtext)
