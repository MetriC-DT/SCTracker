@echo off
pip install -r requirements.txt
pip install -U git+https://github.com/ggtracker/sc2reader.git
pip install pyinstaller

python "build_utils/get_sc2reader_path.py" > sc2reader
SET /p sc2readerpath=<sc2reader
DEL sc2reader

pyinstaller --clean --windowed --noconfirm --name="SCTracker" --add-data="%sc2readerpath%;sc2reader" --add-data="SCTracker;SCTracker" --add-data="Scripts;Scripts" run.py