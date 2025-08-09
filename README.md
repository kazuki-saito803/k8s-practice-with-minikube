## 概要
このリポジトリは, Qiita記事と連携し, Minikube上でK8Sに関してハンズオン形式で学んでいくためのリポジトリです。Qiitaの記事から確認したい方はぜひ以下のQiitaもご確認いただけると幸いです。  
- [Kubernetesで最低限押さえておきたい基礎知識](https://qiita.com/kaz_saito803/items/f3d8b4a38b3c183381ad)  
- [Kubernetesクラスタの基礎的な操作について解説~PodとDeployment, Serviceの立ち上げ~](https://qiita.com/kaz_saito803/items/b0f0bd0e3cba427f0d5a)  
- [Kubernetesクラスタの基礎的な操作について解説~ConfigMapとSecretの使用~](https://qiita.com/kaz_saito803/items/60d0b737b5d47a522799)
## 利用方法
このリポジトリはQiita記事とセットで使用していただくことを想定しています。　　
gitをインストール後, 以下のcloneコマンドによりリポジトリをclone後は, 上記のリンクよりQiitaをご確認いただけますと幸いです。
## 各フォルダの説明
- **step1**: hello worldという文字列を返すFlaskアプリを単一のPodにコンテナ化してデプロイするマテリアルです。
- **step2**: step1のPodにServiceをつけて実際にリクエストを送るためのマテリアルです。
- **step3**: step1/2で作成したPodをDeploymentから作成して, Service経由でリクエストを送るためのマテリアルです。
- **step4**: configmapを利用してPod内で利用する変数を定義した例のマテリアルです。
- **step5**: secretを利用してリクエストを送る際に, 簡単な認証をする例のマテリアルです。