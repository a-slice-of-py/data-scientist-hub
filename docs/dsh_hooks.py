import os

def on_pre_build(*args, **kwargs) -> None:
    """Wrap actions to be executed on docs pre-build."""
    _index_resources(*args, **kwargs)

def _index_resources(*args, **kwargs) -> None:
    """Create index for eache resources section."""
    blacklist = ('.pages', 'index.md')
    resources = 'docs/resources'
    newline = '\n'

    for section in sorted(os.listdir(resources)):
        if section not in blacklist:
            index = [f"# {section.replace('-', ' ').title()}", newline, newline]
            path = f'{resources}/{section}'
            for file in sorted(os.listdir(path)):
                if file not in blacklist:
                    with open(f"{path}/{file}", 'r') as f:
                        lines = f.readlines()
                        for i, line in enumerate(lines):
                            if line.startswith('#'):
                                lines[i] = f'#{line}'
                        index.extend(lines)
                    if index[-1] == newline or index[-1].endswith(newline):
                        index.append(newline)
                    else:
                        index.extend([newline, newline])

            with open(f'{path}/index.md', 'w') as f:
                f.writelines(index)