# Implementation Plan: 新手首輪可玩迴圈

**Branch**: `001-newbie-core-loop` | **Date**: 2026-05-08 | **Spec**: specs/001-newbie-core-loop/spec.md
**Input**: Feature specification from `specs/001-newbie-core-loop/spec.md`

## Summary

實作「新手首輪可玩迴圈」的最小可行版本 (MVP)：從開始畫面啟動、播放劇情片段、執行基礎挑戰、顯示結果與重試機制。採 TDD 流程：先寫測試、再最小實作、持續擴充。

## Technical Context (決策)

- **Language / Runtime**: Python 3.11+（目前 repo 已以 Python 測試為準）
- **Project Type**: 單一 Python 套件（CLI / prototype UI）
- **Testing**: `unittest`（現有）、長期建議使用 `pytest` 作為主要 runner；保留 contract/integration/unit 分層。
- **Storage**: 開發階段使用 in-memory adapter (`InMemoryStorage`)；生產或長期儲存採 SQLite 或 PostgreSQL（透過抽象 adapter）。
- **Observability**: 結構化日誌（JSON metadata 包含 `run_id`、`current_node`、`status`），錯誤需帶上下文以利除錯。
- **CI**: GitHub Actions（簡單 workflow：checkout → setup-python → install deps → run lint → run tests）
- **Target Platform / Constraints**: Linux CI runner、測試需快速且確定性高；初版無高併發需求。

## Constitution Check

- [x] TDD gate defined: 每個 user story 都在 `tasks.md` 定義測試目標（unit/integration/contract）
- [x] Test traceability: `spec.md` → `tasks.md` → `tests/` 已建立初版關聯
- [ ] Backward compatibility: 無對外 API，N/A（後續變更需文件）
- [x] Observability: 已在 `tasks.md` 列入日誌與 run id

## Project Structure (concrete)

```text
specs/001-newbie-core-loop/
├── spec.md
├── plan.md
├── tasks.md
├── quickstart.md (TBD)
└── checklists/

src/
├── models/
│   └── player_run.py
├── services/
│   ├── flow_engine.py
│   └── storage.py
tests/
├── unit/
├── integration/
│   └── test_full_flow_e2e.py
└── contract/
```

## Implementation Steps (short)

1. 確認 `spec.md` 與 `tasks.md`（已完成）
2. 建立最小 domain model 與 storage adapter（`PlayerRun`, `InMemoryStorage`）——已完成
3. 實作 `flow_engine.start_run()` 驅動整輪流程（最小實作，已完成）
4. 寫整合測試（`tests/integration/test_full_flow_e2e.py`）並通過（已完成）
5. 擴充單元測試與邊界條件（next）
6. 提供 CI workflow 與 quickstart 文件

## CI / Dev setup (proposal)

- Add `.github/workflows/ci.yml` with steps:
  - `actions/checkout`
  - `actions/setup-python@v4` (python-version: '3.11')
  - `pip install -r requirements.txt`（或無需求時跳過）
  - run `python -m unittest discover -v`

## Next action items (short)

- Implement unit tests for `storage` and `flow_engine` (`tests/unit/`) — 優先
- Add `quickstart.md`：如何在本地跑測試與 demo
- Add CI workflow

