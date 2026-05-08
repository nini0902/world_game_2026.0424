---

description: "Task list for 新手首輪可玩迴圈"
---

# Tasks: 新手首輪可玩迴圈

**Input**: Design documents from `/specs/001-newbie-core-loop/`
**Prerequisites**: `plan.md`, `spec.md`

**Tests**: TDD required — 寫測試先（先失敗），再實作。

## 格式: `[ID] [P?] [Story] 說明`

- **[P]**: 可平行 (不同檔案、無依賴)
- **[Story]**: 對應 `spec.md` 的使用者故事 (US1, US2, US3)

## Phase 1: Setup (環境與專案結構)

- [ ] T001 Initialize project layout: create `src/`, `tests/unit/`, `tests/integration/`, `tests/contract/` (docs: README/developer-setup)
- [ ] T002 Configure formatter & linter (e.g., `prettier`/`eslint` or `black`/`flake8`), and add `Makefile` or `scripts/` helpers

---

## Phase 2: Foundational (阻塞性基礎)

Purpose: 實作首輪流程前的必要基礎（狀態機、資料模型、紀錄）

### Tests (先寫測試)

- [ ] T010 [P] Contract test: `tests/contract/test_core_flow.contract` — 定義首輪流程的高階契約（Start → StorySegment → Challenge → Outcome）
- [ ] T011 [P] Integration test: `tests/integration/test_state_transitions.py` — 驗證節點之間的狀態轉換（start → story → challenge → outcome）

### Implementation

- [ ] T012 [P] Create data models in `src/models/`:
  - `src/models/player_run.py` (class `PlayerRun`: id, start_time, current_node, status)
  - `src/models/story_segment.py` (sequence, content_id)
  - `src/models/challenge_state.py` (status: in_progress/success/fail, retry_count)
  - `src/models/run_outcome.py` (result_type, message)
- [ ] T013 [P] Implement state machine service `src/services/flow_engine.py` with clear transitions and idempotency for retry operations
- [ ] T014 [P] Add lightweight persistence adapter `src/services/storage.py` (initially in-memory with simple JSON dump for debug) and tests `tests/unit/test_storage.py`
- [ ] T015 [P] Implement basic observability hooks: structured logs for each transition (`src/services/observability.py`) and unit tests

Checkpoint: 基礎完成後可在端到端測試中驅動一個 `PlayerRun` 實例完成整輪流程

---

## Phase 3: User Story 1 - 完成第一輪流程 (P1) 🎯 MVP

Goal: 新手可從開始到結果完成首輪流程

### Tests (REQUIRED, 先寫且須失敗)

- [ ] T020 [P] E2E test: `tests/integration/test_full_flow_e2e.py` — 模擬玩家從開始按鈕到結果畫面的完整流程
- [ ] T021 [P] Unit test: `tests/unit/test_flow_engine_start_to_outcome.py` — 驗證給定 `PlayerRun` 可正確走完各節點

### Implementation

- [ ] T022 [P] Implement UI/CLI entrypoint `src/ui/start_screen.py` (or `cli/start.py`) that triggers `flow_engine.start_run()`
- [ ] T023 [P] Implement `src/ui/story_view.py` to render/load `StorySegment` content (stub content acceptable for v1)
- [ ] T024 [P] Implement `src/ui/challenge.py` to run a deterministic basic challenge (e.g., simple choice or timed input)
- [ ] T025 Integrate outcome screen `src/ui/outcome_view.py` showing `RunOutcome` and actions: `retry` or `back_to_start`
- [ ] T026 Add acceptance test wiring to ensure `tests/integration/test_full_flow_e2e.py` passes

Checkpoint: 完成 T020-T026 後，能以自動化測試驗證完整首輪流程

---

## Phase 4: User Story 2 - 失敗後可重試且不卡住 (P2)

### Tests

- [ ] T030 [P] Integration test: `tests/integration/test_retry_flow.py` — 模擬挑戰失敗後按下重試，確認回到正確節點且不產生重複實例
- [ ] T031 [P] Unit test: `tests/unit/test_challenge_retry_idempotency.py` — 驗證 `ChallengeState.retry()` 的行為

### Implementation

- [ ] T032 [P] Implement retry logic inside `flow_engine` ensuring idempotency and concurrency safety
- [ ] T033 Add guard to `storage` to prevent duplicate `PlayerRun` instances for same run id
- [ ] T034 Update UI to expose retry button and disable rapid double-clicks (debounce)

---

## Phase 5: User Story 3 - 進度提示與可理解回饋 (P3)

### Tests

- [ ] T040 [P] Unit test: `tests/unit/test_progress_indicators.py` — 驗證每節點能回傳 progress metadata
- [ ] T041 [P] Integration test: `tests/integration/test_outcome_readability.py` — 確認 outcome 文本可被驗證並顯示

### Implementation

- [ ] T042 [P] Implement progress metadata APIs in `flow_engine` and UI bindings to display current step and next step hint
- [ ] T043 Add human-readable outcome messages templates and tests

---

## Phase 6: Polish & Cross-Cutting

- [ ] T050 [P] Documentation: write `specs/001-newbie-core-loop/quickstart.md` with dev run steps and how to run tests
- [ ] T051 [P] Add logging + error context for debugging `PlayerRun` issues; ensure logs include run id and current_node
- [ ] T052 [P] Add CI job (simple) to run unit + integration tests
- [ ] T053 [ ] Accessibility & UX polish tasks (deferred)

## Dependencies & Order

- Foundation (Phase 2) blocks User Stories. Tests must be written before implementations for each story.
- Parallel opportunities: model + storage + observability tasks can run in parallel.

---

## Notes

- Keep tests deterministic and fast; prefer unit/integration split to keep E2E small.
- Per Constitution: 每個功能變更需伴隨測試與驗收證據才能合併。
