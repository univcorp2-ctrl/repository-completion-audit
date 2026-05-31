# リポジトリ完成状況一覧

調査日時: 2026-05-31 JST

## 判定ルール

- **完了 / 運用可能**: CI成功、またはREADME・workflow・実行手順・主要コードが揃っている。
- **修正済み / 再確認中**: 今回コードやworkflowを補完し、CIまたは本番実行workflowを確認中。
- **要対応**: workflow未実行、CI失敗、または本番導線不足が確認された。
- **検証 / 雛形**: smoke test、hello world、scaffold、学習・確認用。
- **未確認**: 公開一覧では存在確認済みだが、今回は中身やCIまで確定できていない。

## 全体サマリー

| No | Repository | 種別 | 状態 | CI / 実行確認 | 今回の扱い |
|---:|---|---|---|---|---|
| 1 | repository-completion-audit | 監査ダッシュボード | 完了 / 運用可能 | 新規CI追加 | 今回この台帳を作成 |
| 2 | crypto-auto-trade-sim | 暗号資産売買シミュレーション | 完了 / 運用可能 | success: 26710381733 | open PR 3件は別途整理 |
| 3 | scenario-master-db-auto | シナリオDB自動生成 | 完了 / 運用可能 | success: 26709652218 | 監視継続 |
| 4 | stock-investment-simulator | 株式投資シミュレーター | 完了 / 運用可能 | success: 26708211525 | 監視継続 |
| 5 | enoking-monitor-starter | 監視スターター | 完了 / 運用可能 | success: 26703862410 | 監視継続 |
| 6 | real-estate-investor-needs-form | 不動産投資家ニーズフォーム | 完了 / 運用可能 | success: 26673947493 | 監視継続 |
| 7 | telegram-ai-company-hub | Telegram AI社内Hub | 完了 / 運用可能 | success: 26630491230 | 監視継続 |
| 8 | gmail-property-attachment-saver | Gmail物件添付保存 | 完了 / 運用可能 | success: 26628848052 | 監視継続 |
| 9 | public-drive-property-ocr-cloud | Drive物件OCRクラウド | 完了 / 運用可能 | success: 26696068963 | 以前の保留仕様は解消済み |
| 10 | real-estate-sender-automation | 不動産送信自動化 | 要対応 | no workflow run | CI/実行手順の補完候補 |
| 11 | global-job-aggregator-mvp | グローバル求人収集MVP | 修正済み / 再確認中 | CI success: 26711375511、collect再確認中 | collector/CLI/workflow修正済み |
| 12 | hello-world-python-worker-scaffold-test | Worker雛形テスト | 検証 / 雛形 | 未確認 | 本番プログラムではなく検証用 |
| 13 | hello-world-python-0522-test | Python hello world | 検証 / 雛形 | 未確認 | 本番プログラムではなく検証用 |
| 14 | x-realestate-autopost | X不動産自動投稿 | 完了 / 運用可能 | success: 25795306855 | 監視継続 |
| 15 | gmail-sheets-property-mailer | Gmail/Sheets物件メール | 要対応 | no workflow run | CI/実行手順の補完候補 |
| 16 | github-full-automation | GitHub全自動化 | 要対応 | failure: 26204365931 | workflow再設計候補 |
| 17 | facebook-auto-post | Facebook自動投稿 | 未確認 | 未確認 | 次回詳細確認対象 |
| 18 | autonomous-cloud-business-automation | クラウド業務自動化 | 未確認 | 未確認 | 次回詳細確認対象 |
| 19 | line-sheet-digest | LINE/Sheetsダイジェスト | 未確認 | 未確認 | 次回詳細確認対象 |
| 20 | real-estate-investment-analyzer | 不動産投資分析 | 未確認 | 未確認 | 次回詳細確認対象 |
| 21 | eight-card-cleaner | Eight名刺整理 | 未確認 | 未確認 | 次回詳細確認対象 |
| 22 | obsidian-calendar-agent | Obsidianカレンダーagent | 未確認 | 未確認 | 次回詳細確認対象 |
| 23 | linkedin-ai-crowdworks-bot | LinkedIn/CrowdWorks bot | 未確認 | 未確認 | 次回詳細確認対象。利用規約・安全性確認が必要 |
| 24 | openmythos-gpt-claude-api | GPT/Claude API | 未確認 | 未確認 | 次回詳細確認対象 |
| 25 | crypto-arbitrage-scanner-jp | 暗号資産アービトラージ | 未確認 | 未確認 | 次回詳細確認対象 |
| 26 | ai-ci-auto-fixer | AI CI自動修正 | 未確認 | 未確認 | 次回詳細確認対象 |
| 27 | rock-paper-scissors-python | じゃんけんPython | 検証 / 雛形 | 未確認 | 小規模デモ |
| 28 | chatgpt-worker-smoketest | Worker smoke test | 検証 / 雛形 | 未確認 | 本番プログラムではなく検証用 |
| 29 | testgpt | GPTテスト | 検証 / 雛形 | 未確認 | 本番プログラムではなく検証用 |
| 30 | Github-pull-and-push-automation- | GitHub push/pull自動化 | 未確認 | 未確認 | 次回詳細確認対象 |
| 31 | Add-repository | repo追加テスト | 検証 / 雛形 | 未確認 | 本番プログラムではなく検証用 |
| 32 | SuperNote | ノート系 | 未確認 | 未確認 | 次回詳細確認対象 |
| 33 | Gmail-auto-reply_gemini | Gemini Gmail自動返信 | 未確認 | 未確認 | 次回詳細確認対象 |

## 今回完了まで進めたもの

### repository-completion-audit

- 台帳READMEを作成
- `docs/repository-status.md` を作成
- `repository-status.json` を作成
- CIでJSON妥当性・件数・必須フィールドを検証
- devcontainerとarchitecture docsを追加

### global-job-aggregator-mvp

- `Collect jobs` workflow の失敗を確認
- collector本体を外部APIの一部失敗に耐える実装へ修正
- FastAPIダッシュボードとAPIを整理
- CLI直接実行時のimport経路を修正
- CI smoke testを追加
- collect workflowをpush/schedule/workflow_dispatchで実行できるよう更新

## 残っている未完了・仕掛かり

| Repository | 理由 | 次にやること |
|---|---|---|
| real-estate-sender-automation | workflow run が見つからない | README/CI/実行コマンド/Secrets一覧を確認して補完 |
| gmail-sheets-property-mailer | workflow run が見つからない | Gmail/Sheets連携のSecretsとCIを補完 |
| github-full-automation | 最新workflow failure、ログ詳細なし | workflowを分解し、診断ログを出すよう修正 |
| linkedin-ai-crowdworks-bot | 自動操作系の可能性 | 各サービス規約・API利用可否を確認し、安全なAPI連携に限定 |
