# 対話型商品レコメンド生成AIアプリ

## 概要

このアプリケーションは、ユーザーの要望に基づいて最適な商品を推薦する対話型AIシステムです。自然言語での入力に対して、商品データベースから最も適した商品を検索し、詳細情報と共に表示します。

## 特徴

- **自然言語での対話**: 「こんな商品が欲しい」という自然な表現で商品を検索できます
- **詳細な商品情報**: 商品名、価格、カテゴリ、メーカー、評価、商品画像、説明文などの詳細情報を表示
- **RAG技術の活用**: Retrieval-Augmented Generation技術により、高精度な商品推薦を実現
- **直感的なUI**: Streamlitを使用した使いやすいインターフェース

## 使い方

1. アプリを起動する
   ```
   streamlit run main.py
   ```

2. ブラウザが自動的に開き、アプリケーションが表示されます

3. 画面下部のチャット入力欄に、探している商品の特徴や要望を入力します
   - 例: 「長時間使える、高音質なワイヤレスイヤホン」
   - 例: 「机のライト」
   - 例: 「USBで充電できる加湿器」

4. AIが最適な商品を推薦し、詳細情報を表示します

## 必要環境

- Python 3.8以上
- 必要パッケージ:
  - Windows環境: `pip install -r requirements_windows.txt`
  - Mac環境: `pip install -r requirements_mac.txt`
- OpenAI APIキー（.envファイルに設定）

## インストール方法

1. リポジトリをクローン
   ```
   git clone https://github.com/ShuFukayama/product_recommend.git
   ```

2. 仮想環境を作成し有効化
   ```
   # Windows
   python -m venv venv
   .\venv\Scripts\activate

   # Mac
   python -m venv venv
   source venv/bin/activate
   ```

3. 必要なパッケージをインストール
   ```
   # Windows
   pip install -r requirements_windows.txt

   # Mac
   pip install -r requirements_mac.txt
   ```

4. `.env`ファイルを作成し、OpenAI APIキーを設定
   ```
   OPENAI_API_KEY=your_api_key_here
   ```

5. アプリケーションを起動
   ```
   streamlit run main.py
   ```

## 開発者向け情報

開発者向けの詳細情報は[開発者ドキュメント](docs/DEVELOPER.md)を参照してください。

## AIエージェント向け情報

AIエージェント（Roocode）向けの詳細情報は[AIエージェントドキュメント](docs/AI_AGENT.md)を参照してください。

## ライセンス

このプロジェクトは独自のライセンスの下で提供されています。詳細については管理者にお問い合わせください。