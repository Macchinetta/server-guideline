更新履歴
================================================================================

.. tabularcolumns:: |p{0.15\linewidth}|p{0.25\linewidth}|p{0.60\linewidth}|
.. list-table::
    :header-rows: 1
    :widths: 15 25 60

    * - 更新日付
      - 更新箇所
      - 更新内容

    * - 2017-XX-XX
      - \-
      - 1.5.0 RELEASE版公開

    * -
      - 全般
      - ガイドラインの誤記(タイプミスや単純な記述ミスなど)の修正

        記載内容の改善

    * - 
      - :doc:`../Overview/FrameworkStack`
      - 利用するOSSのバージョンを更新

        * Spring IO PlatformのバージョンをBrussels-SR5に更新
        * MyBatisのバージョンを3.4.5に更新

        Spring IO Platformのバージョン更新に伴い利用するOSSのバージョンを更新

    * -
      - :doc:`../ImplementationAtEachLayer/DomainLayer`
      - 記載内容の追加

        * \ ``@Transactional`` \アノテーションの\ ``timeout`` \属性に関する記載を追加 

    * -
      - :doc:`../ArchitectureInDetail/WebApplicationDetail/Validation`
      - 記載内容の追加

        * \ ``@Compare`` \アノテーションの\ ``operator`` \属性に新たに追加された\ ``NOT_EQUAL`` \の説明を追加

        * \ ``@Email`` \アノテーションを使用する際の注意事項を追加

        ガイドラインのバグ修正

        * 共通ライブラリのチェックルールの拡張方法の実装例を修正

    * -
      - :doc:`../ArchitectureInDetail/WebApplicationDetail/ExceptionHandling`
      - 記載内容の修正

        * 共通ライブラリ(\ ``ExceptionLoggingFilter`` \)の変更に伴う修正、及び既存の誤記の修正

    * -
      - :doc:`../ArchitectureInDetail/WebApplicationDetail/TilesLayout`
      - 記載内容の修正

        * \ ``<definition>`` \タグ(Tiles定義ファイル)の\ ``name`` \属性のマッチングに関する説明、及び関連する箇所の誤解を招く表現を修正

    * -
      - :doc:`../ArchitectureInDetail/WebServiceDetail/RestClient`
      - Spring Framework 4.3対応に伴う修正

        * Basic認証用のリクエストヘッダの設定に関する記載を変更

    * -
      - :doc:`../ArchitectureInDetail/WebServiceDetail/SOAP`
      - 記載内容の修正

        * SOAP Web Serviceの実装に伴うインジェクションで使用するアノテーションを\ ``@Inject`` \から\ ``@Autowired`` \に変更
        * Spring FrameworkのJAX-WS連携機能についての誤記修正と、SOAPサーバがJava EEサーバのJAW-WS実装上で動作することに伴なう注意事項の追記

    * - 
      - :doc:`../ArchitectureInDetail/MessagingDetail/JMS`
      - 記載内容の修正

        * 非同期送信のトランザクション管理はChainedTransactionManagerではなくDefaultMessageListenerContainerで行うよう記述を修正

    * -
      - :doc:`../Security/Authentication`
      - 記載内容の修正

        * パスワードハッシュ化のためのクラス（\ ``Pbkdf2PasswordEncoder``\ ）の説明を追記し、それに伴い\ ``BCryptPasswordEncoder``\を推奨する記述を削除


    * -
      - :doc:`../Security/Authorization`
      - Spring Framework 4.3対応に伴う修正

        * ブランクプロジェクトから\ ``mvc:path-matching`` \の定義を削除しSpring MVCのデフォルト設定を使用するよう変更したことに伴う記載内容の修正

        記載内容の修正

        * Spring Securityでパス変数を使用するアクセスポリシーの定義に関する記載内容を修正

    * - 
      - :doc:`../Security/XSS`
      - 記載内容の修正、追加

        * JavaScript Escapingのサンプルソースを修正
        * \ ``document.write()`` \を使用する際の注意事項を追加

    * -
      - :doc:`../Security/OAuth`
      - 構成見直し

        * How to useをグラントタイプ毎に説明する章構成に変更

        記載内容の追加

        * Spring Security OAuthで発生する例外の一覧とハンドリング方法の追加

        * Spring Security OAuthの拡張ポイントについての説明を追加

        * リソースサーバに対するBasic認証設定方法の追加

        * インプリシットにおける後処理（アクセストークンクリア）の追加

        記載内容の改善

        * サンプルコードの修正

        * フロー図およびその説明の改善

    * -
      - :doc:`../UnitTest/index`
      - 新規追加

        * 単体テストを追加

    * - 2017-11-10
      - \-
      - 1.4.1 RELEASE版公開

    * -
      - 全般
      - ガイドラインの誤記(タイプミスや単純な記述ミスなど)の修正

    * - 2017-03-10
      - \-
      - 1.4.0 RELEASE版公開

.. raw:: latex

   \newpage
