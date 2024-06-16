import psutil
import settings
import pygetwindow


def get_unreal_engine_installs() -> list:
    return settings.settings['engine_info']['unreal_engine_installs']


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


def is_game_ue5():
    return


def is_game_ue5():
    return


def game_project_name():
    return


def is_game_iostore():
    return


def does_game_use_sigs():
    return


def does_game_use_loose_file_loading():
    return
