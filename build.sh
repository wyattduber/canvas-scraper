#!/bin/bash

#export PATH=$PATH://my.files.iastate.edu/Profiles/$(whoami)/AppData/Roaming/Python/Python38/Scripts

python -m PyQt6.uic.pyuic --from-imports qtdesigner/BasicOperationWidget.ui -o generated/BasicOperationWidgetUI.py
python -m PyQt6.uic.pyuic --from-imports qtdesigner/BalanceBeamWidget.ui -o generated/BalanceBeamWidgetUI.py
python -m PyQt6.uic.pyuic --from-imports qtdesigner/LiveStreamWidget.ui -o generated/LiveStreamWidgetUI.py
python -m PyQt6.uic.pyuic --from-imports qtdesigner/DebugWidget.ui -o generated/DebugWidgetUI.py
python -m PyQt6.uic.pyuic --from-imports qtdesigner/MainWindow.ui -o generated/MainWindowUI.py
python -m PyQt6.uic.pyuic --from-imports qtdesigner/DacModeWidget.ui -o generated/DacModeWidgetUI.py
python -m PyQt6.uic.pyuic --from-imports qtdesigner/SamplingGenerationStart.ui -o generated/SamplingGenerationStartUI.py
python -m PyQt6.uic.pyuic --from-imports qtdesigner/ModeSelectorWidget.ui -o generated/ModeSelectorWidgetUI.py
python -m PyQt6.uic.pyuic --from-imports qtdesigner/ConnectionWidget.ui -o generated/ConnectionWidgetUI.py

python -m PyQt6.pyrcc_main  qtdesigner/main_window.qrc -o generated/main_window_rc.py
python -m PyQt6.pyrcc_main  qtdesigner/basic_operation.qrc -o generated/basic_operation_rc.py
python -m PyQt6.pyrcc_main  qtdesigner/balance_beam.qrc -o generated/balance_beam_rc.py
