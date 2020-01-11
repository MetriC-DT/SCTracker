import PySimpleGUI as sg
import sc2reader
import json
import os

from tabulate import tabulate

from SCTracker.database import database
from SCTracker.replayloader import *
from SCTracker.constants import *


class GUI():
    font = 'Arial 12'
    first_column_width = 15
    second_column_width = 40
    row_height = 1
    button_width = 19
    database = database()

    def __init__(self, active_folder):
        self.active_folder = active_folder
        self.set_layout()
        self.run()
    

    def set_layout(self):
        TextLabel = lambda key: sg.Text(text=key, key=key, size=(self.first_column_width, self.row_height), font=self.font, justification='right')
        EmptySpace = lambda length: sg.Text(text='', size=(length, self.row_height), font=self.font)
        SingleLineInput = lambda key: sg.InputText(default_text='', key=key, font=self.font, size=(self.second_column_width, self.row_height))
        EnterButton = lambda key: sg.Button(key, size=(self.button_width, self.row_height), key=key, font=self.font, bind_return_key=True)
        MultiLineInput = lambda key: sg.Multiline(key=key, size=(self.second_column_width - 2, 3), font=self.font, autoscroll=True)

        self.layout = [
            [TextLabel(gamenumber), SingleLineInput(gamenumber + 'input')],
            [TextLabel(gamedatetime), SingleLineInput(gamedatetime + 'input')],
            [TextLabel(playername), SingleLineInput(playername + 'input')],
            [TextLabel(playermmr), SingleLineInput(playermmr + 'input')],
            [TextLabel(playerleague), SingleLineInput(playerleague + 'input')],
            [TextLabel(playerrace), SingleLineInput(playerrace + 'input')],
            [TextLabel(playerclan), SingleLineInput(playerclan + 'input')],
            [TextLabel(opponentname), SingleLineInput(opponentname + 'input')],
            [TextLabel(opponentmmr), SingleLineInput(opponentmmr + 'input')],
            [TextLabel(opponentleague), SingleLineInput(opponentleague + 'input')],
            [TextLabel(opponentrace), SingleLineInput(opponentrace + 'input')],
            [TextLabel(opponentclan), SingleLineInput(opponentclan + 'input')],
            [TextLabel(mapLabel), SingleLineInput(mapLabel + 'input')],
            [TextLabel(win), SingleLineInput(win + 'input')],
            [TextLabel(gameplan), SingleLineInput(gameplan + 'input')],
            [TextLabel(openersuccess), SingleLineInput(openersuccess + 'input')],
            [TextLabel(buildorder), SingleLineInput(buildorder + 'input')],
            [TextLabel(reaction), SingleLineInput(reaction + 'input')],
            [TextLabel(followup), SingleLineInput(followup + 'input')],
            [TextLabel(tags), SingleLineInput(tags + 'input')],
            [TextLabel(length), SingleLineInput(length + 'input')],
            [TextLabel(notes), MultiLineInput(notes + 'input')],
            [TextLabel(path), SingleLineInput(path + 'input'), sg.FileBrowse(target='pathinput', size=(self.button_width, self.row_height), font=self.font, file_types=(('SC2Replay files', '*.SC2Replay'),))],
            [EmptySpace(self.first_column_width), EnterButton('commit replay'), EnterButton('load latest replay')],
            [EmptySpace(self.first_column_width), EnterButton('add build'), EnterButton('view builds')],
            [EmptySpace(self.first_column_width), EnterButton('set replay folder'),  EnterButton('view replay folder'), EnterButton('set player id')]
        ]
    

    def run(self):
        self.window = sg.Window(appname, self.layout)
        while True:
            event, values = self.window.read()
            if event is None:
                break
            else:
                self.parse_event(event, values)
        
        self.database.close()
        self.window.close()
    

    def parse_event(self, event, values):
        if event == 'commit replay':
            self.commit_replay(values)
        elif event == 'load latest replay':
            self.load_latest_replay(values)
        elif event == 'add build':
            self.add_build()
        elif event == 'view builds':
            self.view_builds()
        elif event == 'set replay folder':
            self.set_replay_folder()
        elif event == 'view replay folder':
            self.view_replay_folder()
        elif event == 'set player id':
            self.set_player_id()
        else:
            print(event, values)


    def commit_replay(self, values):
        self.database.add_replay_entry(values)

    
    def load_latest_replay(self, values):
        print('load latest replay')
        self.clear(values)
        
        try:
            with open(config_file, 'r') as f:
                config = json.load(f)
                directory = config[replay_folder_key]
                player_id = config[player_id_key]
                player_name = config[player_name_key]
                
                game_count = self.database.get_data('SELECT COUNT(gamenumber) FROM ' + database.replays_table)[0][0] + 1
                values = {gamenumber + 'input': game_count}
                values.update(newest_replay_data(directory, player_id, player_name))

                self.window.fill(values)
        
        except Exception as e:
            sg.PopupError('Make sure you have both your replay folder and your player id set\nError:', e)

    
    def clear(self, values):
        for value in [v for v in values if 'input' in v]:
            self.window[value]('')

    
    def add_build(self):
        print('adding build')
        build = sg.PopupGetText('Number | Opponent Race | Description', title='add build')
        
        if build is None:
            return None
        elif self.validate_build([item.strip() for item in build.split('|')]):
            self.database.add_build_entry([item.strip() for item in build.split('|')])
        else:
            sg.PopupError('Follow the correct format!', title='Format Error')
            self.add_build()


    def validate_build(self, build):
        initial_check = build is not None and isinstance(build, list) and len(build) == 3
        try:
            int(build[0])
            return initial_check and all([(item != '') for item in build])
        except Exception:
            return False

    
    def view_builds(self):
        print('showing build list')
        execute_string = """
            SELECT number, opponent, description, 100*SUM(win)/COUNT(number) AS winrate
            FROM builds, replays
            WHERE number=gameplan AND (win=1 OR win=0)
            GROUP BY number
            ORDER BY opponent, number, winrate;
        """
        data = self.database.get_data(execute_string)
        headers = [description[0] for description in self.database.cursor.description]
        sg.PopupScrolled(tabulate(data, headers=headers), title='build list', font='Courier 12', size=(110, None))


    def set_replay_folder(self):
        folder = sg.PopupGetFolder('Select your replay folder', title='Replay Folder')
        
        if bool(folder) == True:
            with open(config_file, 'w') as f:
                json.dump({replay_folder_key: folder}, f, indent=4)
            sg.Popup('Replay folder set')
    
    
    def view_replay_folder(self):
        try:
            with open(config_file, 'r') as f:
                config = json.load(f)
                directory = config[replay_folder_key]
                if directory:
                    os.startfile(directory)
                else:
                    sg.PopupError('Replay folder not set!')
        except Exception:
            sg.PopupError('Replay folder not set!')
    
    
    def set_player_id(self):
        try:
            player_info = dict()
            config = dict()
            with open(config_file, 'r') as f:
                config = json.load(f)
                player_info = get_player_info(config[replay_folder_key])
                print(player_info)
            
            if player_info:
                with open(config_file, 'w') as f:
                    config.update(player_info)
                    json.dump(config, f, indent=4)

        except Exception as e:
            sg.PopupError('set the replay folder first!\nError:', e)