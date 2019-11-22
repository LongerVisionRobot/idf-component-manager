import sys

from component_manager.core import ComponentManager
from component_manager.utils.errors import FatalError


def action_extensions(base_actions, project_path):
    def callback(subcommand_name, ctx, args, components=None):
        try:
            manager = ComponentManager(args.project_dir)
            getattr(manager, subcommand_name)(components)
        except FatalError as e:
            print(e)
            sys.exit(2)

    components_option = {
        'names': ['-c', '--components'],
        'help': 'Add new components to manifest',
        'multiple': True,
    }

    return {
        'actions': {
            'install': {
                'callback': callback,
                'help': 'Install dependencies.',
                'options': [components_option]
            },
            'eject': {
                'callback': callback,
                'help': 'Add/move dependency to directory with unmanaged components.',
                'options': [components_option]
            }
        },
    }