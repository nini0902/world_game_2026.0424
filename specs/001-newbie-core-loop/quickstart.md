快速上手 (Quickstart)

本檔說明如何在本地環境執行測試與示範 flow。

先決條件
- 已安裝 Python 3.11
- 建議使用虛擬環境 (venv)

建立與啟用虛擬環境

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -U pip
```

安裝相依套件（目前無額外套件）

```bash
pip install -r requirements.txt || true
```

執行所有單元與整合測試

```bash
python -m unittest discover -v tests/unit
python -m unittest discover -v tests/integration
```

在互動模式下執行最小範例

```bash
python -c "from src.services.flow_engine import start_run; print(start_run())"
```

日誌與除錯
- 預設程式會使用 Python logging。要看到 debug/info 訊息，可在環境中啟用簡單 logging：

```bash
python -c "import logging; logging.basicConfig(level=logging.DEBUG); from src.services.flow_engine import start_run; start_run()"
```

下一步建議
- 若要長期開發，請建立 `requirements.txt` 並加入測試/linters（例如 `pytest`, `flake8`）
- 若要永久觀察，建議串接 structured logger 或 APM
