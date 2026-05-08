# PR Draft: 新手首輪可玩迴圈 (MVP) — `001-newbie-core-loop`

## 標題
Feat: 新手首輪可玩迴圈 — MVP + 測試與 CI

## 摘要
本分支實作最小可行版本的「新手首輪可玩迴圈」，並採 TDD 流程建立測試與 CI。變更包含 domain model、簡易 flow engine、in-memory storage、單元與整合測試，以及 GitHub Actions CI。此 PR 目的是提供可驗證的基線，讓後續功能能在有測試保護下逐步擴充。

## 主要變更檔案
- `specs/001-newbie-core-loop/spec.md` (現有)
- `specs/001-newbie-core-loop/plan.md` (已補技術決策)
- `specs/001-newbie-core-loop/tasks.md` (任務拆解)
- `src/models/player_run.py` (新增)
- `src/services/storage.py` (新增 `InMemoryStorage`)
- `src/services/flow_engine.py` (新增最小實作 `start_run`)
- `tests/integration/test_full_flow_e2e.py` (新增 E2E 測試)
- `tests/unit/test_storage.py` (新增)
- `tests/unit/test_flow_engine.py` (新增)
- `.github/workflows/ci.yml` (新增 CI workflow)

## 本地測試結果 (已執行)
- Unit tests: 2 passed
- Integration tests: 1 passed

執行指令：
```bash
python3 -m unittest discover -v tests/unit
python3 -m unittest discover -v tests/integration
```

## 影響面與相依
- 暫用 in-memory storage，生產環境應提供 adapter（SQLite/Postgres）。
- API/介面皆為內部模組，尚無公開對外契約。

## Reviewer Checklist
- [ ] 檢查 `spec.md` 與 `tasks.md` 是否符合預期需求
- [ ] 程式碼風格與簡單安全檢查
- [ ] 執行本地測試：`python -m unittest discover -v tests`
- [ ] 同意合併後的 next-steps（observability / quickstart / PR 說明）

## 下一步建議
1. 新增觀測/結構化日誌（`flow_engine` 中引入 log metadata）
2. 撰寫 `quickstart.md`（如何在本地跑測試與 demo）
3. 若合併，建立 adapter 以接上 SQLite/Postgres 作為長期儲存

---
_備註：若要我代為在 GitHub 建立 PR（草稿或正式 PR），我可以用 `gh` 指令幫你開啟。_
