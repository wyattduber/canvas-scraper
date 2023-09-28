#!/bin/bash

pyuic6 --from-imports qtdesigner/BasicOperationWidget.ui -o generated/BasicOperationWidgetUI.py
pyuic6 --from-imports qtdesigner/BalanceBeamWidget.ui -o generated/BalanceBeamWidgetUI.py
pyuic6 --from-imports qtdesigner/LiveStreamWidget.ui -o generated/LiveStreamWidgetUI.py
pyuic6 --from-imports qtdesigner/DebugWidget.ui -o generated/DebugWidgetUI.py
pyuic6 --from-imports qtdesigner/MainWindow.ui -o generated/MainWindowUI.py
pyuic6 --from-imports qtdesigner/DacModeWidget.ui -o generated/DacModeWidgetUI.py
pyuic6 --from-imports qtdesigner/SamplingGenerationStart.ui -o generated/SamplingGenerationStartUI.py
pyuic6 --from-imports qtdesigner/ModeSelectorWidget.ui -o generated/ModeSelectorWidgetUI.py

pyrcc6 qtdesigner/main_window.qrc -o generated/main_window_rc.py
pyrcc6 qtdesigner/basic_operation.qrc -o generated/basic_operation_rc.py
pyrcc6 qtdesigner/balance_beam.qrc -o generated/balance_beam_rc.py
