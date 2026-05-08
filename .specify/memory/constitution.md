<!--
Sync Impact Report
- Version change: N/A (template) -> 1.0.0
- Modified principles:
	- [PRINCIPLE_1_NAME] -> I. 規格驅動與可追溯需求
	- [PRINCIPLE_2_NAME] -> II. 小步交付與向後相容預設
	- [PRINCIPLE_3_NAME] -> III. TDD 優先（不可妥協）
	- [PRINCIPLE_4_NAME] -> IV. 分層測試與契約保障
	- [PRINCIPLE_5_NAME] -> V. 可觀測性與可維運性
- Added sections:
	- 技術與品質約束
	- 開發流程與品質門檻
- Removed sections:
	- 無
- Templates requiring updates:
	- ✅ updated: .specify/templates/plan-template.md
	- ✅ updated: .specify/templates/spec-template.md
	- ✅ updated: .specify/templates/tasks-template.md
- Follow-up TODOs:
	- 無
-->

# world_game_2026.0424 Constitution

## Core Principles

### I. 規格驅動與可追溯需求
所有功能開發 MUST 以核准後之規格文件為起點，且每項功能需求、驗收情境、
實作任務之間 MUST 可追溯。任何未記錄於規格的需求變更 MUST 先回寫規格，
再進入實作。
理由：降低需求漂移與溝通落差，確保交付內容可審核、可重現。

### II. 小步交付與向後相容預設
所有變更 SHOULD 以小批次、可獨立驗證方式交付；除非規格明確宣告破壞性變更，
否則 MUST 維持既有對外契約之向後相容。若需破壞相容性，MUST 在規格與計畫中
明確記載風險、遷移策略與回滾方案。
理由：降低整合風險，提升發佈可控性與使用者信任。

### III. TDD 優先（不可妥協）
所有需求實作 MUST 遵循 TDD（Red-Green-Refactor）：先撰寫測試、確認測試失敗、
再進行最小實作使測試通過，最後重構。未有對應測試之功能程式碼 MUST NOT 合併。
測試涵蓋範圍 MUST 對應規格中的驗收情境與邊界條件。
理由：以可執行規格保護行為正確性，並降低回歸缺陷成本。

### IV. 分層測試與契約保障
專案 MUST 依風險採用分層測試策略（單元、整合、契約/端對端）。跨模組介面、
資料結構、外部整合點之變更 MUST 補齊契約或整合測試，以驗證相容性與錯誤處理。
理由：避免僅靠單元測試造成的整體行為盲區。

### V. 可觀測性與可維運性
關鍵流程 MUST 具備足夠可觀測訊號（結構化日誌、錯誤脈絡、必要指標）以支援
問題定位。任何新增流程 MUST 定義失敗行為與回報方式，避免靜默失敗。
理由：提升除錯效率與運維穩定性。

## 技術與品質約束

- 需求文件、計畫文件與任務文件 SHOULD 以繁體中文撰寫，除非外部整合或法規要求
	使用其他語言。
- 每一項使用者故事 MUST 可獨立驗證，且具備至少一條可執行驗收情境。
- 新增相依套件或工具 MUST 於文件中記錄目的、替代方案評估與移除成本。
- PR MUST 附上測試證據（例如測試命令與結果摘要）與風險說明。

## 開發流程與品質門檻

1. 規格：先定義使用者故事、驗收情境、邊界條件與成功指標。
2. 計畫：在實作前完成技術背景、風險、架構決策與 Constitution Check。
3. 任務：依使用者故事拆分，先測試任務後實作任務，標示依賴關係。
4. 實作：嚴格遵循 Red-Green-Refactor，維持小步提交。
5. 審查：Code Review MUST 驗證本憲章原則符合性，未符合者不得合併。

## Governance

本憲章優先於專案內其他慣例或臨時流程。修訂憲章 MUST 透過文件化提案，
並同步更新受影響模板與指令文件。

版本政策採語意化版本：
- MAJOR：原則移除、重新定義或治理方式產生不相容改變。
- MINOR：新增原則/章節或實質擴充既有規範。
- PATCH：僅文字澄清、錯字修正或不改變治理語意之調整。

合規審查要求：
- 每次 PR 審查 MUST 檢查是否符合本憲章。
- 每次 /speckit.plan 與 /speckit.tasks 產出 MUST 反映 TDD 優先與測試追溯。
- 發現不符合時 MUST 先補文件與測試，再進行功能合併。

**Version**: 1.0.0 | **Ratified**: 2026-04-24 | **Last Amended**: 2026-04-24

<!-- Knowie: Project Knowledge -->
## Project Knowledge

This project maintains structured knowledge in `knowledge/`:

- **Principles** (`knowledge/principles.md`): Core axioms and derived development principles — the project's non-negotiable rules.
- **Vision** (`knowledge/vision.md`): Goals, current state, architecture decisions, and roadmap.
- **Experience** (`knowledge/experience.md`): Distilled lessons from past development — patterns, pitfalls, and takeaways.

Read these files at the start of any task to understand the project's *why* and constraints.
Additional context may be found in `knowledge/research/`, `knowledge/design/`, and `knowledge/history/`.
<!-- /Knowie -->
