import os
import glob
import json
import enums
import psutil
import settings
import pygetwindow


def get_engine_info() -> dict:
    return settings.settings['engine_info']


def get_unreal_engine_installs() -> list:
    return get_engine_info()['unreal_engine_installs']


def get_uproject_storage_directory() -> str:
    return get_engine_info()['uproject_storage_directory']


def get_override_default_uproject_storage_directory() -> bool:
    return get_engine_info()['override_default_uproject_storage_directory']


def get_process_name(exe_path: str) -> str:
    filename = os.path.basename(exe_path)
    return filename


def get_engine_window_title(uproject) -> str:
    return f'{get_process_name(uproject)[:-9]} - {'Unreal Editor'}'


def get_engine_process_name(unreal_editor_exe) -> str:
    return get_process_name(unreal_editor_exe)


def does_window_exist(window_title: str, use_substring_check: bool = False) -> bool:
    try:
        if use_substring_check:
            all_window_titles = pygetwindow.getAllTitles()
            matched_windows = [window for window in all_window_titles if window_title in window]
        else:
            try:
                matched_windows = pygetwindow.getWindowsWithTitle(window_title)
            except pygetwindow.PyGetWindowException as e:
                return False
        return len(matched_windows) > 0
    except pygetwindow.PyGetWindowException as e:
        print(f"An error occurred: {e}")
        return False
    

def is_process_running(process_name: str) -> bool:
    for proc in psutil.process_iter():
        try:
            if process_name.lower() in proc.name().lower():
                return True
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    return False


def is_game_ue4():
    if get_unreal_version_from_build_file().startswith('4'):
        return True
    else:
        return False


def is_game_ue5():
    return not is_game_ue4()


def get_unreal_editor_exe(engine_dir) -> str:
    if is_game_ue5():
        editor_exe = f'{engine_dir}/Engine/Binaries/Win64/UnrealEditor.exe'
    else:
        editor_exe = f'{engine_dir}/Engine/Binaries/Win64/UE4Editor.exe'
    return editor_exe


def get_win_dir_type() -> enums.PackagingDirType:
    if is_game_ue5():
        return enums.PackagingDirType.WINDOWS
    else:
        return enums.PackagingDirType.WINDOWS_NO_EDITOR


def get_win_dir_type_value() -> enums.PackagingDirType.value:
    return get_win_dir_type().value


def get_unreal_engine_build_file(engine_dir) -> str:
    return f'{engine_dir}/Engine/Build/Build.version'


def has_build_target_been_built(engine_dir) -> bool:
    return os.path.exists(get_unreal_engine_build_file(engine_dir))


def get_unreal_version_from_build_file() -> str:
    version_file_path = get_unreal_engine_build_file()        
    try:
        with open(version_file_path, 'r') as f:
            version_info = json.load(f)
            unreal_engine_major_version = version_info.get('MajorVersion', 0)
            unreal_engine_minor_version = version_info.get('MinorVersion', 0)
            return f'{unreal_engine_major_version}.{unreal_engine_minor_version}'
    except FileNotFoundError as error:
        raise error


def get_game_directory(game_exe) -> str:
    return os.path.dirname(get_game_project_directory(game_exe))


def get_game_project_name(game_exe) -> str:
    return os.path.basename(get_game_project_directory(game_exe))


def get_game_project_directory(game_exe) -> str:
    return os.path.dirname(os.path.dirname(os.path.dirname(game_exe)))


def get_games_paks_directory(game_exe):
    paks_dir = f'{get_game_project_directory(game_exe)}/Content/Paks'
    if os.path.isdir(paks_dir):
        return paks_dir
    else:
        return None
    

def get_files_in_tree(tree_path: str) -> list:
    return glob.glob(tree_path + '/**/*', recursive=True)


def get_file_extension(file_path: str) -> str:
    _, file_extension = os.path.splitext(file_path)
    return file_extension


def get_file_extensions(file_path: str) -> list:
    extensions = []
    files = get_files_in_tree(file_path)
    for file in files:
        extensions.append(get_file_extension(file))
    return extensions


def get_is_game_iostore() -> bool:
    is_game_iostore = False
    file_extensions = get_file_extensions(get_games_paks_directory())
    for file_extension in file_extensions:
        if file_extension == '.ucas':
            is_game_iostore = True
        elif file_extension == '.utoc':
            is_game_iostore = True
    return is_game_iostore


def does_game_use_sigs():
    game_uses = False
    file_extensions = get_file_extensions(get_games_paks_directory())
    for file_extension in file_extensions:
        if file_extension == '.sig':
            game_uses = True
    return game_uses


def does_game_have_pak_file():
    game_uses = False
    file_extensions = get_file_extensions(get_games_paks_directory())
    for file_extension in file_extensions:
        if file_extension == '.pak':
            game_uses = True
    return game_uses


def does_game_have_loose_files():
    return


def get_unreal_version_from_pak():
    return


def get_unreal_version_from_exe():
    return
