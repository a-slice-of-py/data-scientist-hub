import os

def on_pre_build(*args, **kwargs) -> None:
    """Wrap actions to be executed on docs pre-build."""
    _index_resources(*args, **kwargs)

def _index_resources(*args, **kwargs) -> None:
    """Create index for eache resources section."""
    blacklist = ('.pages', 'index.md')
    resources = 'docs/resources'
    for section in os.listdir(resources):
        if section not in blacklist:
            index = [f"# {section.replace('-', ' ').title()}", '\n']
            path = f'{resources}/{section}'
            for file in os.listdir(path):
                if file not in blacklist:
                    with open(f"{path}/{file}", 'r') as f:
                        contents = f.readlines()
                        contents[0] = f'#{contents[0]}'
                        index.extend(contents)
                    index.append('\n')

            with open(f'{path}/index.md', 'w') as f:
                f.writelines(index)