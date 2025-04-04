# 開発者向けドキュメント

このドキュメントは、対話型商品レコメンド生成AIアプリの開発者向けの情報を提供します。

## システムアーキテクチャ

このアプリケーションは以下のコンポーネントで構成されています：

1. **フロントエンド**: Streamlitを使用したWebインターフェース
2. **バックエンド**: Python + LangChainによる商品推薦エンジン
3. **データストア**: CSVファイルベースの商品データベース
4. **RAG (Retrieval-Augmented Generation)**: OpenAI Embeddingsを使用した検索システム

### 処理フロー

1. ユーザーがチャット入力から商品の要望を入力
2. 入力テキストがRAGシステムに送信され、関連する商品情報を検索
3. 検索結果から最適な商品が選択され、ユーザーに表示
4. 会話履歴がセッションに保存され、連続した対話が可能

## ファイル構成

```
product_recommend/
├── .env                    # 環境変数（APIキーなど）
├── .gitignore              # Gitの除外ファイル設定
├── .streamlit/             # Streamlit設定ディレクトリ
│   └── config.toml         # Streamlit設定ファイル
├── components.py           # UI表示コンポーネント
├── constants.py            # 定数定義
├── data/                   # データディレクトリ
│   └── products.csv        # 商品データ
├── docs/                   # ドキュメントディレクトリ
│   ├── DEVELOPER.md        # 開発者向けドキュメント
│   └── AI_AGENT.md         # AIエージェント向けドキュメント
├── images/                 # 画像ディレクトリ
│   ├── ai_icon.jpg         # AIアイコン
│   ├── user_icon.jpg       # ユーザーアイコン
│   └── products/           # 商品画像ディレクトリ
├── initialize.py           # 初期化処理
├── logs/                   # ログディレクトリ
├── main.py                 # メインアプリケーション
├── README.md               # プロジェクト概要
├── requirements_mac.txt    # Mac用依存パッケージ
├── requirements_windows.txt # Windows用依存パッケージ
└── utils.py                # ユーティリティ関数
```

## 主要ファイルの役割

### main.py

メインアプリケーションファイルで、Streamlitアプリの構造と処理フローを定義しています。主な機能：
- アプリの初期化
- UIの表示
- ユーザー入力の処理
- 商品推薦結果の表示

### components.py

UI表示に関する関数を定義しています。主な機能：
- アプリタイトルの表示
- AIの初期メッセージ表示
- 会話ログの表示
- 商品情報の表示

### constants.py

アプリケーション全体で使用される定数を定義しています。主な定数：
- 画面表示関連の定数
- ログ出力関連の定数
- Retriever設定関連の定数
- エラーメッセージ

### initialize.py

アプリケーションの初期化処理を担当しています。主な機能：
- セッション状態の初期化
- ログ出力の設定
- RAG Retrieverの作成
- Windows環境での文字列調整

### utils.py

ユーティリティ関数を定義しています。主な機能：
- エラーメッセージの構築
- 形態素解析による日本語の単語分割

## RAGシステムの実装詳細

このアプリケーションでは、以下の2つのRetrieverを組み合わせたEnsembleRetrieverを使用しています：

1. **BM25Retriever**: キーワードベースの検索
2. **Chroma + OpenAI Embeddings**: 意味ベースの検索

これにより、キーワードマッチングと意味的な類似性の両方を考慮した高精度な検索が可能になっています。

```python
# initialize.py内のコード
embeddings = OpenAIEmbeddings()
db = Chroma.from_documents(docs, embedding=embeddings)
retriever = db.as_retriever(search_kwargs={"k": ct.TOP_K})

bm25_retriever = BM25Retriever.from_texts(
    docs_all,
    preprocess_func=utils.preprocess_func,
    k=ct.TOP_K
)
ensemble_retriever = EnsembleRetriever(
    retrievers=[bm25_retriever, retriever],
    weights=ct.RETRIEVER_WEIGHTS
)
```

## 開発環境のセットアップ

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

## 開発のヒント

### 新しい商品の追加

新しい商品を追加するには、`data/products.csv`ファイルに新しい行を追加します。以下の情報が必要です：

- id: 一意の商品ID
- name: 商品名
- category: 商品カテゴリ
- price: 価格
- maker: メーカー
- recommended_people: おすすめ対象ユーザー
- review_number: レビュー数
- score: 評価スコア
- file_name: 商品画像のファイル名（images/products/ディレクトリに配置）
- description: 商品説明

### ログの確認

アプリケーションのログは`logs/application.log`に出力されます。エラーが発生した場合や動作を確認したい場合は、このログファイルを確認してください。

### デバッグモード

Streamlitのデバッグモードを有効にするには、以下のコマンドを使用します：

```
streamlit run main.py --logger.level=debug
```

## パフォーマンスの最適化

- 商品データが大きくなる場合は、CSVファイルからデータベース（SQLiteなど）への移行を検討してください。
- OpenAI APIの呼び出し回数を減らすために、Embeddingsをキャッシュすることを検討してください。

## 将来の拡張案

1. **ユーザープロファイル**: ユーザーの好みを学習し、パーソナライズされた推薦を提供
2. **フィルタリング機能**: カテゴリ、価格帯などでフィルタリングする機能の追加
3. **商品比較**: 複数の商品を比較する機能の追加
4. **データベース連携**: 外部データベースとの連携
5. **APIの提供**: 他のアプリケーションから利用できるAPIの提供

## トラブルシューティング

### Windows環境での文字化け

Windows環境では、日本語の文字化けが発生する可能性があります。`initialize.py`の`adjust_string`関数で対応していますが、問題が発生する場合は以下を確認してください：

- Pythonのエンコーディング設定
- CSVファイルのエンコーディング
- Streamlitの設定

### OpenAI API関連のエラー

OpenAI APIに関連するエラーが発生した場合は、以下を確認してください：

- APIキーが正しく設定されているか
- APIの利用制限に達していないか
- ネットワーク接続が正常か

## コントリビューション

プロジェクトへの貢献を歓迎します。以下の手順で貢献できます：

1. リポジトリをフォーク
2. 新しいブランチを作成
3. 変更を加える
4. テストを実行
5. プルリクエストを送信

## 連絡先

開発に関する質問や問題がある場合は、リポジトリの管理者にお問い合わせください。