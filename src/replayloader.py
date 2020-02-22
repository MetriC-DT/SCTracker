import os
import sc2reader
import glob
from sc2reader.factories import SC2Factory
import PySimpleGUI as sg
from src.constants import *
from datetime import datetime


def get_player_info(source_path):
    if source_path and os.path.isdir(source_path):
        sc2 = SC2Factory(directory=source_path, depth=1, followlinks=True)
        replays = sc2.load_replays(source_path, load_level=2, load_maps=False)
        possible_players = []
        number_of_replay_files = len([name for name in os.listdir(source_path) if '.SC2Replay' in name])            
        number_of_replays_to_test = min(30, number_of_replay_files)

        for _ in range(number_of_replays_to_test):
            replay = next(replays)
            possible_players.extend([(player.name, player.toon_id) for player in replay.players if player.is_human])
        
        # generator to get the next highest player name
        def get_highest(lst):
            while lst:
                largest = max(lst, key=lambda x: lst.count(x)) if lst else ''
                lst = list(filter(lambda x: x != largest, lst)) if largest else []
                yield tuple(largest)

        highest = get_highest(possible_players)
        p = next(highest, None)

        if p:
            popup = sg.popup_yes_no(f'Are you {p[0]} (ID: {str(p[1])})?\n\n(Your ID does not change, even after a name change)', font='Arial 12')
            
            # checks if there are still names remaining
            while p and popup == 'No':
                p = next(highest, None)
                popup = sg.popup_yes_no(f'Are you {p[0]} (id={str(p[1])})?\n\n(Your ID does not change, even after a name change)', font='Arial 12') if p else 'No'
            
            if popup == 'Yes':
                return {
                    player_id_key: p[1],
                    player_name_key: p[0]
                }
            else:
                sg.popup_ok('Your ID has not been changed')
                return {}
        else:
            sg.popup_error(f'Cannot detect any SC2Replay files in:\n\n{source_path}')
            return {}
    else:
        sg.popup_error('Cannot resolve source path (Replay folder)!')
        return {}


def newest_replay_data(source_path, player_id, player_name):
    list_of_files = glob.glob(source_path + "/*.SC2Replay")
    latest_file = max(list_of_files, key=os.path.getctime)
    sc2 = SC2Factory(directory=source_path, depth=2, followlinks=True)
    replay = sc2.load_replay(latest_file)

    if replay.real_type != '1v1':
        sg.PopupError('Not designed for non-1v1 games!', title='Replay Type Error')
        return dict()
    
    values = list()
    values.append(get_datetime(replay))
    values.extend(get_players(replay, player_id, player_name))
    values.append(get_path(replay))
    values.append(get_map(replay))
    values.append(get_length(replay))
    return dict(values)

def replay_data(filepath, player_id, player_name):
    replay = sc2reader.load_replay(filepath)

    if replay.real_type != '1v1':
        sg.PopupError('Not designed for non-1v1 games!', title='Replay Type Error')
        return dict()
    
    values = list()
    values.append(get_datetime(replay))
    values.extend(get_players(replay, player_id, player_name))
    values.append(get_path(replay))
    values.append(get_map(replay))
    values.append(get_length(replay))
    return dict(values)

def get_datetime(replay):
    key = gamedatetime + 'input'
    value = datetime.fromtimestamp(replay.unix_timestamp).strftime("%Y-%m-%d %H:%M:%S")
    return (key, value)


def get_players(replay, player_id, player_name):
    if player_id and player_name and player_id in [player.toon_id for player in replay.players]:
        replay.players = sorted(replay.players, key=lambda player: player.toon_id != player_id)
    
    player_info = list()
    opponent_info = list()
    
    player = replay.players[0]
    opponent = replay.players[1]
    
    playername_key = playername + 'input'
    playername_value = player.name
    player_info.append((playername_key, playername_value))

    playermmr_key = playermmr + 'input'
    playermmr_value = player.init_data['scaled_rating']
    player_info.append((playermmr_key, playermmr_value))

    playerrace_key = playerrace + 'input'
    playerrace_value = player.play_race[0]
    player_info.append((playerrace_key, playerrace_value))

    playerclan_key = playerclan + 'input'
    playerclan_value = player.clan_tag
    player_info.append((playerclan_key, playerclan_value))

    opponentname_key = opponentname + 'input'
    opponentname_value = opponent.name
    opponent_info.append((opponentname_key, opponentname_value))

    opponentmmr_key = opponentmmr + 'input'
    opponentmmr_value = opponent.init_data['scaled_rating']
    opponent_info.append((opponentmmr_key, opponentmmr_value))

    opponentrace_key = opponentrace + 'input'
    opponentrace_value = opponent.play_race[0]
    opponent_info.append((opponentrace_key, opponentrace_value))

    opponentclan_key = opponentclan + 'input'
    opponentclan_value = opponent.clan_tag
    opponent_info.append((opponentclan_key, opponentclan_value))

    tag_key = tags + 'input'
    tag_value = '' if player.play_race[0] == player.pick_race[0] else 'RandomPlayer, '
    tag_value += '' if opponent.play_race[0] == opponent.pick_race[0] else 'RandomOpponent, '
    opponent_info.append((tag_key, tag_value))

    win_key = win + 'input'
    win_value = 0.5
    if player.result == 'Win':
        win_value = 1
    elif opponent.result == 'Win':
        win_value = 0

    player_info.append((win_key, win_value))

    return player_info + opponent_info


def get_map(replay):
    return (mapLabel + 'input', replay.map_name)


def get_path(replay):
    return (path + 'input', replay.filename.replace("\\", "/"))

def get_length(replay):
    return (length + 'input', replay.real_length.seconds)