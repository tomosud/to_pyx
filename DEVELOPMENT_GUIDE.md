# 開発ガイド

**更新条件**: 開発方針・アーキテクチャルール・コーディング規約の変更時

## 開発再開時のチェックリスト

1. **現在の状況確認**: [DEVELOPMENT_ENTRY.md](./DEVELOPMENT_ENTRY.md)
2. **環境セットアップ**: [CROSS_PLATFORM_PYTHON_SETUP.md](./CROSS_PLATFORM_PYTHON_SETUP.md)
3. **詳細仕様確認**: [CURRENT_SPECIFICATIONS.md](./CURRENT_SPECIFICATIONS.md)

## 開発の全体的な進行イメージ

### 基本方針
- **ゲームロジックとUIの完全分離**: 将来的なUI切り替えを容易にするため
- **最小限のインターフェースでゲームサイクル確立**: 演出は後から実装
- **機能の小分け・整理**: 段階的な開発で品質を保つ


## 開発方針

### コーディング規約
- **ファイル分割**: 1ファイル約400行以内で機能分割
- **クロスプラットフォーム対応**: Unixコマンド（`&&`等）使用禁止
- **パラメータ設定の一元化**: 全ゲーム設定値は`core/game_config.py`で管理
- **ドキュメント更新**: 仕様や計画変更時は[README.md](./README.md)、[developmentPlan.md](./developmentPlan.md)を更新

### パラメータ設定の一元化

**原則**: 全てのゲームパラメータは一元管理
