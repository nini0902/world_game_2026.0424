# Feature Specification: 新手首輪可玩迴圈

**Feature Branch**: `001-newbie-core-loop`  
**Created**: 2026-04-24  
**Status**: Draft  
**Input**: User description: "建立新手首輪可玩迴圈（開始、劇情片段、基礎挑戰、結果回饋與可重試）"

## User Scenarios & Testing *(mandatory)*

> Constitution Rule: TDD is non-negotiable. Define acceptance tests first,
> confirm they fail, then implement.

### User Story 1 - 完成第一輪流程 (Priority: P1)

新手玩家可以從開始畫面進入遊戲，體驗一段劇情、完成一次基礎挑戰，並看到清楚的結果回饋。

**Why this priority**: 這是產品最小可玩價值，若無法跑完首輪流程，其他功能皆無法驗證。

**Independent Test**: 以新玩家身份自起始畫面進入，完整執行到結果畫面並確認流程結束。

**Acceptance Scenarios**:

1. **Given** 玩家在開始畫面, **When** 點擊開始遊戲, **Then** 進入第一段劇情片段。
2. **Given** 玩家完成基礎挑戰, **When** 系統結算, **Then** 顯示結果回饋並允許回到開始或重試。

**Pre-Implementation Test Plan**: 先撰寫端到端流程測試與關鍵狀態轉換測試；初始必須失敗，因為流程頁面與狀態轉換尚未實作。

---

### User Story 2 - 失敗後可重試且不卡住 (Priority: P2)

新手玩家在挑戰失敗後可快速重試，不會停在無法前進的狀態。

**Why this priority**: 體驗早期最常流失點是失敗後無明確下一步，必須先解決。

**Independent Test**: 模擬挑戰失敗並驗證玩家可在兩步內重新開始本輪流程。

**Acceptance Scenarios**:

1. **Given** 玩家在基礎挑戰中失敗, **When** 系統顯示結果, **Then** 提供可用的重試操作並成功回到該輪起點。

**Pre-Implementation Test Plan**: 先撰寫失敗狀態到重試狀態的流程測試與邊界測試；初始必須失敗，因為錯誤流程與重試入口尚未建立。

---

### User Story 3 - 提供可理解的進度與回饋 (Priority: P3)

玩家在首輪流程中能知道自己目前在哪個步驟，並在完成後得到可理解的結果說明。

**Why this priority**: 進度與回饋明確可降低新手困惑，提升完成率。

**Independent Test**: 在每個流程節點確認有對應進度提示，結束時有結果說明可讀。

**Acceptance Scenarios**:

1. **Given** 玩家位於任一流程節點, **When** 觀察畫面, **Then** 能看到當前步驟與下一步提示。

**Pre-Implementation Test Plan**: 先撰寫節點提示存在性與結果說明可見性測試；初始必須失敗，因為提示文案與狀態映射尚未建立。

---

### Edge Cases

- 玩家在劇情片段中中斷並返回時，重新進入應回到明確可用狀態，不得出現空白畫面。
- 玩家連續快速點擊重試時，系統應避免建立重複流程實例。
- 玩家在結果畫面刷新後，仍應能回到可預期的開始狀態。

## Requirements *(mandatory)*

### Functional Requirements

- **FR-001**: System MUST 提供開始畫面，允許玩家啟動首輪流程。
- **FR-002**: System MUST 依序呈現劇情片段、基礎挑戰、結果回饋三個核心節點。
- **FR-003**: 玩家 MUST 能在挑戰失敗後執行重試並回到可運行狀態。
- **FR-004**: System MUST 在每個節點提供當前進度與下一步提示。
- **FR-005**: System MUST 在流程完成或失敗時提供可理解的結果說明與下一步操作。
- **FR-006**: System MUST 記錄每次流程執行的結果狀態，以支援除錯與行為驗證。
- **FR-007**: System MUST 確保重試行為不會產生重複或衝突的流程狀態。

### Key Entities *(include if feature involves data)*

- **PlayerRun**: 代表玩家一次首輪流程執行，包含起始時間、目前節點、完成狀態。
- **StorySegment**: 代表首輪中展示的劇情片段，包含順序、內容、顯示條件。
- **ChallengeState**: 代表基礎挑戰執行狀態，包含進行中、成功、失敗與重試次數。
- **RunOutcome**: 代表流程結算結果，包含結果類型、說明文字、可用操作。

## Success Criteria *(mandatory)*

### Measurable Outcomes

- **SC-001**: 至少 90% 的新玩家可在一次嘗試內完成首輪流程。
- **SC-002**: 玩家在失敗後可於 10 秒內找到並執行重試操作。
- **SC-003**: 每個核心節點皆有明確進度提示，且在走查中可 100% 被辨識。
- **SC-004**: 針對首輪流程的關鍵驗收情境，測試通過率達 100%。

## Assumptions

- 目標使用者為第一次接觸此類遊戲的新手玩家與短時段遊玩者。
- 首版僅處理單一路徑流程，不含分支劇情與進階角色系統。
- 目前不納入完整存檔系統，流程中斷後採回到可預期起點的策略。
- 視覺與音效細節優化屬後續階段，首版以流程可玩與可驗證為優先。
