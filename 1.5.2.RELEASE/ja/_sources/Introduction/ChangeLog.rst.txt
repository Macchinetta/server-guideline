更新履歴
================================================================================

.. tabularcolumns:: |p{0.15\linewidth}|p{0.25\linewidth}|p{0.60\linewidth}|
.. list-table::
    :header-rows: 1
    :widths: 15 25 60
    :class: longtable

    * - 更新日付
      - 更新箇所
      - 更新内容

    * - 2019-04-22
      - \-
      - 1.5.2 RELEASE版公開

    * -
      - 全般
      - ガイドラインの誤記(タイプミスや単純な記述ミスなど)の修正

        記載内容の改善

        記載内容の修正・追加

        * ViewResolverの定義について、Spring 4.0以前からの\ ``<bean>``\要素を使用した定義方法を削除し、Spring 4.1以降の\ ``<mvc:view-resolvers>``\要素を使用した定義方法のみ解説するよう変更
        * 利用するミドルウェアのバージョンを更新

        Spring Framework 4.3.23より\ `XMLスキーマ処理が改善 <https://github.com/spring-projects/spring-framework/issues/22530>`_\されたため、ブランクプロジェクトにおけるBean定義ファイルのXMLスキーマファイル(.xsd)参照を\ ``http``\から\ ``https``\に変更

    * -
      - :doc:`../Introduction/CriteriaBasedMapping`
      - OWASP Top 10 を2013版から2017版へ変更

        * OWASP(Open Web Application Security Project)による観点の更新

    * - 
      - :doc:`../Overview/FrameworkStack`
      - 利用するOSSのバージョンを更新

        * Spring IO PlatformのバージョンをBrussels-SR17に更新

         * Spring Frameworkのバージョンを4.3.23に更新
         * Spring Securityのバージョンを4.2.12に更新
         * Spring Dataのバージョンを1.13.20に更新
         * Spring Security OAuthを2.0.17に更新
         * Hibernate Validatorのバージョンを5.3.6.Finalに更新
         * Jacksonのバージョンを2.8.11に更新

        * MyBatisのバージョンを3.4.6に更新
        * MyBatis-springのバージョンを1.3.2に更新

        利用するOSSのバージョンの更新による主な変更

         * Spring Security 4.2.5で変更となったセキュリティヘッダの付与タイミングによる、リクエストパスのマッチングにおける注意事項の追加
         * Spring Security OAuth 2.0.17よりリダイレクトURIのホワイトリストチェックの仕様が変更されたことへの対応
         * Lombok 1.16.22より\ ``@Data``\と\ ``@NoArgsConstructor``\を付与する順序によってコンパイルエラーが発生するようになったことへの対応

        TERASOLUNA Server Framework for Java (5.x)の共通ライブラリの新機能追加

        \ ``terasoluna-gfw-validator``\
         * バイト長チェック用Bean Validation制約アノテーション \ ``@ByteSize`` \

        共通ライブラリの機能改善

        \ ``terasoluna-gfw-common``\
         * \ ``SimpleReloadableI18nCodeList``\の追加
         * \ ``@ExistInCodeList`` \ で \ ``Number`` \ 型をサポートするよう改善
         * \ ``ReloadableCodeList`` \ のイミュータブル対応に伴う \ ``CodeListInterceptor``\ の仕様変更

    * -
      - :doc:`../ImplementationAtEachLayer/CreateWebApplicationProject`
      - 記載内容の追加

        * 大量にコードリストを定義する場合のBean定義方法に関する記載を追加

    * -
      - :doc:`../ImplementationAtEachLayer/ApplicationLayer`
      - 記載内容の追加

        * Spring Framework 4.3より追加された \ ``@RequestMapping``\ の合成アノテーションの説明を追加

    * -
      - :doc:`../ArchitectureInDetail/WebApplicationDetail/Validation`
      - 記載内容の追加

        * Hibernate Validatorで提供される\ ``TimeProvider``\を実装することで、基準日付の変更が可能である旨の説明を追加

    * -
      - :doc:`../ArchitectureInDetail/WebApplicationDetail/ExceptionHandling`
      - 記載内容の修正

        * \ ``DefaultHandlerExceptionResolver``\がハンドリングする例外一覧にSpring Framework 4.2より追加された\ ``org.springframework.web.bind.MissingPathVariableException``\を追加
        * \ ``SystemExceptionResolver#preventResponseCaching``\とSpring SecurityのCache-Controlヘッダの併用についての注意を追加

    * -
      - :doc:`../ArchitectureInDetail/WebApplicationDetail/Pagination`
      - 構成見直し

        * Overviewを取得データの表示、ページネーションリンクの表示、ページネーション情報の表示の3点について説明するように変更

    * -
      - :doc:`../ArchitectureInDetail/WebApplicationDetail/MessageManagement`
      - 記載内容の修正

        * \ ``SPRING_SECURITY_LAST_EXCEPTION`` \ が格納されるスコープの誤記を修正
        
    * -
      - :doc:`../ArchitectureInDetail/WebApplicationDetail/Internationalization`
      - 記載内容の追加

        * \ ``AcceptHeaderLocaleResolver``\と\ ``LocaleChangeInterceptor``\の指定可能な設定についての説明を追加

    * -
      - :doc:`../ArchitectureInDetail/WebApplicationDetail/Codelist`
      - 記載内容の修正

        * 独自カスタマイズしたコードリストのBean定義方法を、コンポーネントスキャンからBean定義ファイルによる定義に変更

        記載内容の追加

        * コードリストBeanをJSPから直接参照する方法を追加

    * -
      - :doc:`../ArchitectureInDetail/WebApplicationDetail/FileDownload`
      - 記載内容の追加

        * \ `CVE-2017-9096 <http://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2017-9096>`_\に関する説明及び注意点を追加

    * -
      - | :doc:`../ArchitectureInDetail/WebApplicationDetail/Ajax`
      - OWASP Top 10 2017対応に伴う修正

        * A8:2017に関連する、デシリアライズ時のWarningを追加
        * Macchinetta Server Framework (1.x)ではXXE対策済みのSpring MVCを使用しているため、
          XXE対策についてのWarningをNoteへ変更し、spring-oxmによる対策方法の記述を削除

    * -
      - | :doc:`../ArchitectureInDetail/WebServiceDetail/REST`
      - OWASP Top 10 2017対応に伴う修正

        * Macchinetta Server Framework (1.x)ではXXE対策済みのSpring MVCを使用しているため、
          XXE対策についてのWarningをNoteへ変更し、spring-oxmによる対策方法の記述を削除

        記載内容の追加

        * Spring Framework 4.3より追加された \ ``@RequestMapping``\ の合成アノテーションの説明を追加

        記述内容の修正

        * Dozerのカスタムコンバーターに関する記述を\ :doc:`../ArchitectureInDetail/GeneralFuncDetail/Dozer`\に統合

    * -
      - :doc:`../ArchitectureInDetail/DataAccessDetail/DataAccessMyBatis3`
      - 記載内容の追加

        * \ ``Pageable`` \ を利用した検索結果のソートについての説明を追加
        * JSR-310 Date and Time APIを使う場合の設定の記事を削除し、依存ライブラリとして別途\ ``mybatis-typehandlers-jsr310`` \を追加する必要はなくなった旨のNoteを追加

    * -
      - :doc:`../ArchitectureInDetail/GeneralFuncDetail/Logging`
      - 記載内容の修正

        * TERASOLUNA Server Framework for Java (5.x)の共通ライブラリが提供する\ ``TraceLoggingInterceptor``\のWARNログ出力に関する閾値の設定例を修正

    * -
      - :doc:`../ArchitectureInDetail/GeneralFuncDetail/Dozer`
      - 記載内容の削除

        * 現バージョン（Dozer5.5.0以降）ではCollection<T>を使用したBean間のマッピングも可能であるため、マッピングが失敗する旨を記述したTodoを削除

    * -
      - :doc:`../ArchitectureInDetail/MessagingDetail/JMS`
      - OWASP Top 10 2017対応に伴う修正

        * A8:2017に関連する、デシリアライズ時のWarningを追加

        記載内容の修正・追加

        * JMSを利用する際のBean定義の記載場所を再整理
        * JNDIを使用しない場合の\ ``DynamicDestinationResolver``\ のBean定義方法に関する記載を追加

    * -
      - :doc:`../Security/Authentication`
      - OWASP Top 10 2017対応に伴う修正

        * A10:2017に関連する、ログイン認証時のログについてのTipを追加

        記載内容の修正

        * \ ``PasswordEncoder``\インターフェースの実装クラス一覧を推奨するクラスのみ記載するように変更
        * 非推奨の\ ``PasswordEncoder``\について、\ ``ShaPasswordEncoder``\から\ ``MessageDigestPasswordEncoder``\を使用する方法に記載を変更
        
        記載内容の追加

        * \ ``SPRING_SECURITY_LAST_EXCEPTION`` \ が格納されるスコープの説明を追加

    * -
      - :doc:`../Security/CSRF`
      - OWASP Top 10 2017対応に伴う修正

        * OWASP Top 10 2013版へのリンクをOWASP Cheat Sheetへのリンクへ変更

    * -
      - :doc:`../Security/LinkageWithBrowser`
      - 記載内容の追加

        * Spring Securityが提供する\ ``HeaderWriterFilter``\の仕様変更と\ ``DelegatingRequestMatcherHeaderWriter``\でのリクエストパスのマッチングにおけるバグについての注意事項を追加
        * Spring Securityがサポートするセキュリティヘッダの一覧にReferrer-Policyヘッダを追加

    * -
      - :doc:`../Security/OAuth`
      - 記載内容の修正・追加

        * \ `CVE-2019-3778 <https://pivotal.io/security/cve-2019-3778>`_\ (オープンリダイレクト脆弱性)に関する注意喚起を追加
        * Spring Security OAuthのバージョン更新に伴いリダイレクトURI情報を保持するテーブルへの説明にWarningを追加
        * \ ``alias``\属性を用いた\ ``authentication-manager``\の定義に関する実装例、説明の修正

    * -
      - :doc:`../Tutorial/TutorialTodo`
      - 記載内容の修正・追加

        * 一覧表示機能作成時に、登録機能の一部を作成していた部分を変更し、一覧表示機能の動作確認できるように、コード例を追加
        * ガイドライン修正に伴う、サンプルコードの最新化

    * -
      - :doc:`../Tutorial/TutorialREST`
      - 記載内容の修正

        * spring-mvc-rest.xmlを作成する方法の説明を変更
        * ガイドライン修正に伴う、サンプルコードの最新化

    * -
      - :doc:`../Tutorial/TutorialSession`
      - 記載内容の修正

        * \ JSPのコードをTiles形式に修正
        * ガイドライン修正に伴う、サンプルコードの最新化

    * -
      - :doc:`../Tutorial/TutorialSecurity`
      - 記載内容の修正

        * \ ``SPRING_SECURITY_LAST_EXCEPTION`` \ が格納されるスコープの誤記を修正
        * ガイドライン修正に伴う、サンプルコードの最新化

    * -
      - :doc:`../Appendix/Lombok`
      - 記載内容の追加

        * Lombok 1.16.22における\ ``@Data``\と\ ``@NoArgsConstructor``\を付与する順序についてのWarningを追加

    * - 2018-03-09
      - \-
      - 1.5.1 RELEASE版公開

    * - 
      - :doc:`../Overview/FrameworkStack`
      - CVE-2018-1199への対応のため、利用するOSSのバージョンを更新

        * Spring Frameworkのバージョンを4.3.14に更新
        * Spring Securityのバージョンを4.2.4に更新

    * -
      - :doc:`../Security/OAuth`
      - 記載内容の修正

        * 認可サーバのチェックトークンエンドポイントのURL設定が反映されない不具合へのWarningを削除

    * - 2017-12-22
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

        * TERASOLUNA Server Framework for Java (5.x)の共通ライブラリのチェックルールの拡張方法の実装例を修正

    * -
      - :doc:`../ArchitectureInDetail/WebApplicationDetail/ExceptionHandling`
      - 記載内容の修正

        * TERASOLUNA Server Framework for Java (5.x)の共通ライブラリ(\ ``ExceptionLoggingFilter`` \)の変更に伴う修正、及び既存の誤記の修正

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
