# Experience

## Lessons

### 先對齊需求再除錯

- **Theory said**: 只要先改程式讓畫面能跑，bug 會跟著消失。
- **Actually happened**: 在需求定義不清時直接修 bug，會反覆卡在同一類問題，因為每次修正都可能偏離真正預期行為。
- **Resolved by**: 先回到規格確認應有行為，補最小重現步驟，再用對應測試驗證修正結果。
- **Lesson**: 卡 bug 時先釐清預期行為與重現條件，比直接改碼更快脫離反覆除錯循環。
- **Source**: knowledge/history/001-card-bug-pattern.md
