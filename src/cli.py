import sys
import argparse


class CustomArgumentParser(argparse.ArgumentParser):
    def format_help(self):
        formatter = self._get_formatter()
        formatter.add_text(self.description)
        positionals = [action for action in self._actions if action.option_strings == []]
        if positionals:
            formatter.start_section('positional arguments')
            formatter.add_arguments(positionals)
            formatter.end_section()
        formatter.add_text(self.epilog)

        return formatter.format_help()

    def print_help(self, file=None):
        print(self.format_help(), file=file)


parser = CustomArgumentParser()
unreal_mod_project_generator_parser = parser.add_subparsers(dest='unreal_mod_project_generator_parser')


ARGS = parser.parse_args()
CLI_ARGS = sys.argv[2:]


unreal_mod_project_generator_parser_dict = {
    'create_uproject': 'create_uproject',
    'delete_uproject': 'delete_uproject',
    'list_engine_info': "list_engine_info",
    'list_uproject_info': "list_uproject_info"
}


def cli_logic():
    for key in unreal_mod_project_generator_parser_dict.keys():
        if CLI_ARGS.unreal_mod_project_generator_parser == key:
            function_name = unreal_mod_project_generator_parser_dict[key]
            if function_name:
                function = globals().get(function_name)
                if function:
                    print(f'called function: {function_name}')
                    print('cli args:')
                    for arg in CLI_ARGS:
                        print(f'arg: {arg}')
                    function(*CLI_ARGS)
