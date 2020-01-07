import PySimpleGUI as sg
import sc2reader
from SCTracker.database import database
from sc2reader.factories import SC2Factory

class GUI():
    appname = 'SCTracker'
    font = 'Arial 14'
    first_column_width = 15
    second_column_width = 40
    row_height = 1
    button_width = 19
    database = database()

    def __init__(self, active_folder):
        self.active_folder = active_folder
        self.set_layout()
    

    def set_layout(self):
        TextLabel = lambda key: sg.Text(text=key, key=key, size=(self.first_column_width, self.row_height), font=self.font, justification="right")
        SingleLineInput = lambda key: sg.InputText(default_text="", key=key, font=self.font, size=(self.second_column_width, self.row_height))
        EnterButton = lambda key: sg.Button(key, size=(self.button_width, self.row_height), key=key, font=self.font)

        self.layout = [
            [TextLabel("gamenumber"), SingleLineInput("gamenumberinput")],
            [TextLabel("datetime"), SingleLineInput("datetimeinput")],
            [TextLabel("playername"), SingleLineInput('playernameinput')],
            [TextLabel("playermmr"), SingleLineInput('playermmrinput')],
            [TextLabel("playerleague"), SingleLineInput('playerleagueinput')],
            [TextLabel("playerrace"), SingleLineInput('playerraceinput')],
            [TextLabel("playerclan"), SingleLineInput('playerclaninput')],
            [TextLabel("opponentname"), SingleLineInput('opponentnameinput')],
            [TextLabel("opponentmmr"), SingleLineInput('opponentmmrinput')],
            [TextLabel("opponentleague"), SingleLineInput('opponentleagueinput')],
            [TextLabel("opponentrace"), SingleLineInput('opponentraceinput')],
            [TextLabel("opponentclan"), SingleLineInput('opponentclaninput')],
            [TextLabel("map"), SingleLineInput('mapinput')],
            [TextLabel("win"), SingleLineInput('wininput')],
            [TextLabel("openersuccess"), SingleLineInput('openersuccessinput')],
            [TextLabel("gameplan"), SingleLineInput('gameplaninput')],
            [TextLabel("buildorder"), SingleLineInput('buildorderinput')],
            [TextLabel("reaction"), SingleLineInput('reactioninput')],
            [TextLabel("followup"), SingleLineInput('followupinput')],
            [TextLabel("tags"), SingleLineInput('tagsinput')],
            [TextLabel("length"), SingleLineInput('lengthinput')],
            [TextLabel("notes"), SingleLineInput('notesinput')],
            [TextLabel("path"), SingleLineInput('pathinput'), sg.FolderBrowse(target="pathinput", size=(self.button_width, self.row_height), font="Arial 12")],
            [TextLabel(""), EnterButton('commit'), EnterButton('load latest')]
        ]
    

    def run(self):
        window = sg.Window(self.appname, self.layout)
        while True:
            event, values = window.read()
            if event is None:
                break
            elif event == 'commit':
                print('commit')
            else:
                self.parse_event(event, values)        
        
        self.database.close()
        window.close()
    

    def parse_event(self, event, values):
        if event == "commit":
            self.commit(values)
        elif event == 'load latest':
            print('loading latest replay file')
        else:
            print(event, values)

    
    def commit(self, values):
        print("committing", values)