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


    @env.macro
    def include_file(filename, start_line=0, end_line=None, until=None):
        """
        Include a file, optionally indicating start_line and end_line
        (start counting from 0)
        The path is relative to the top directory of the documentation
        project.
        """
        full_filename = os.path.join(env.project_dir, filename)
        with open(full_filename, 'r') as f:
            lines = f.readlines()
        line_range_full = lines[start_line:end_line]
        line_range = []
        if until is not None:
            for line in line_range_full:
                if line.strip() != until.strip():
                    line_range.append(line)
        else:
            line_range = line_range_full
        return ''.join(line_range)
    
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
        return("\n".join(mdtext))