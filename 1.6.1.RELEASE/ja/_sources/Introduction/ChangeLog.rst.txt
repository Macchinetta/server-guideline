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

    * - 2019-03-26
      - \-
      - 1.6.1 RELEASE版公開

    * -
      - 全般
      - Java SE 8および11のサポートに伴う修正

        * サポート対象外となるJava SE 7を利用する際の記述を削除
        * サポート対象となるJava SE 11を利用する際の記述を追加

        ガイドラインの誤記(タイプミスや単純な記述ミスなど)の修正

        記載内容の改善

        記載内容の修正・追加

        * ViewResolverの定義について、Spring 4.0以前からの\ ``<bean>``\要素を使用した定義方法を削除し、Spring 4.1以降の\ ``<mvc:view-resolvers>``\要素を使用した定義方法のみ解説するよう変更
        * 利用するミドルウェアのバージョンを更新

    * -
      - :doc:`../Introduction/CriteriaBasedMapping`
      - OWASP Top 10 を2013版から2017版へ変更

        * OWASP(Open Web Application Security Project)による観点の更新

    * -
      - :doc:`../Overview/FrameworkStack`
      - 利用するOSSの管理方法の変更

        * 利用するライブラリの管理にSpring Bootを利用するよう変更

        利用するOSSのバージョンを更新

        * Spring Boot 2.1.2の適用

         * Spring Frameworkのバージョンを5.1.4に更新
         * Spring Securityのバージョンを5.1.3に更新
         * Spring Dataのバージョンを2.1.4に更新
         * Hibernate Validatorのバージョンを6.0.14(Bean Validation 2.0)に更新
         * Joda Timeのバージョンを2.10.1に更新
         * Jacksonのバージョンを2.9.8に更新
         * Apache HttpClientを4.5.6に更新
         * Lombokを1.18.4に更新

        * Spring Security OAuthを2.2.4に更新
        * MyBatisのバージョンを3.5.0に更新
        * MyBatis Springのバージョンを2.0.0に更新
        * Dozerのバージョンを6.4.1に更新
        * Apache POIを3.17に更新
        * iTextが非サポートになったため、OpenPDF 1.0.5を追加

        利用するOSSのバージョンの更新による主な変更

        * Spring Framework 5.0.0よりJasperReportsが非サポートとなったことへの対応
        * Spring Framework 5.0.3よりiTextが非サポートとなり、代わりにOpenPDFがサポートされたことへの対応
        * Spring Framework 4.2から非推奨ととなっていた\ ``AbstractExcelView``\がSpring Framework 5.0で削除されたことに伴う対応
        * Spring Framework 5.0.0よりクエリ文字列に対するURLエンコーディングの仕様が変更されたことへの対応
        * Spring Framework 5.0.0より指定サイズを超えるファイルのアップロードやマルチパートのリクエストが行われた際に発生する例外の仕様が変更されたことに伴う対応
        * Spring Framework 5.0.0よりSpEL評価時におけるnull-safety機能が追加されたことへの対応
        * Spring Security 5より非推奨の\ ``PasswordEncoder``\のパッケージが廃止になったことへの対応
        * Spring Security 5.0.2および5.1.2で変更となったセキュリティヘッダの付与タイミングによる、リクエストパスのマッチングにおける注意事項の追加
        * Spring Security OAuth 2.2.2よりリダイレクトURIのホワイトリストチェックの仕様が変更されたことへの対応

        TERASOLUNA Server Framework for Java (5.x)の共通ライブラリの新機能追加

        \ ``terasoluna-gfw-validator``\
         * バイト長チェック用Bean Validation制約アノテーション \ ``@ByteSize`` \ 

        TERASOLUNA Server Framework for Java (5.x)の共通ライブラリの機能改善

        \ ``terasoluna-gfw-common``\
         * \ ``SimpleI18nCodeList``\のロケール解決方法の改善
         * \ ``SimpleReloadableI18nCodeList``\の追加
         * \ ``@ExistInCodeList`` \ で \ ``Number`` \ 型をサポートするよう改善
         * \ ``ReloadableCodeList`` \ のイミュータブル対応に伴う \ ``CodeListInterceptor``\ の仕様変更
         * \ ``@ExistInCodeList`` \ をBean Validation 2.0に準拠するよう仕様変更
        \ ``terasoluna-gfw-codepoints``\
         * \ ``@ConsistOf`` \ をBean Validation 2.0に準拠するよう仕様変更
        \ ``terasoluna-gfw-validator``\
         * \ ``@ByteMax`` \ 及び\ ``@ByteMin`` \ をBean Validation 2.0に準拠するよう仕様変更

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
      - Bean Validation 2.0(Hibernate Validator 6.0)対応に伴う修正

        * Bean Validation 2.0及びHibernate Validator 6.0では、コレクション内の各値に対して入力チェックできるようになった旨の説明を追加
        * Bean Validation 2.0では、一つのフィールドに同じアノテーションを複数指定できる旨の説明を追加
        * Bean Validation 2.0及びHibernate Validator 6.0で追加されたアノテーションに対する説明を追加
        * Hibernate Validator 6.0で非推奨となったアノテーションに対する説明を追加
        * Bean Validation 2.0で提供される\ ``ClockProvider``\を実装することで、基準日付の変更が可能である旨の説明を追加

    * -
      - :doc:`../ArchitectureInDetail/WebApplicationDetail/ExceptionHandling`
      - Spring Framework 5.1.4対応に伴う修正

        * \ ``DefaultHandlerExceptionResolver``\がハンドリングする例外一覧からSpring Framework 5.0より廃止された\ ``org.springframework.web.servlet.mvc.multiaction.NoSuchRequestHandlingMethodException``\を削除

        記載内容の修正

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
      - :doc:`../ArchitectureInDetail/WebApplicationDetail/FileUpload`
      - Spring Framework 5.1.4対応に伴う修正

        * 指定サイズを超えるファイルのアップロードやマルチパートのリクエストが行われた際に発生する例外の仕様が変更されたことに伴い、Noteを追加

    * -
      - :doc:`../ArchitectureInDetail/WebApplicationDetail/FileDownload`
      - Spring Framework 5.1.4対応に伴う修正

        * JasperReportsが非サポートとなったため、JasperReportsに言及している記載を修正
        * iTextの代わりにOpenPDFがサポートされるようになった旨の説明を追加し、実装例を修正
        * Spring Framework 4.2から非推奨ととなっていた\ ``AbstractExcelView``\がSpring Framework 5.0で削除されたことに伴う対応

    * -
      - :doc:`../ArchitectureInDetail/WebApplicationDetail/TagLibAndELFunctions`
      - Spring Framework 5.1.4対応に伴う修正

        * Spring Frameworkのクエリ文字列に対するURLエンコーディングの仕様変更に伴うTERASOLUNA Server Framework for Java (5.x)の共通ライブラリ(\ ``f:query()``\, \ ``f:u()``\)の変更についてWarningを追加

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
      - :doc:`../ArchitectureInDetail/WebServiceDetail/RestClient`
      - Spring Framework 5.1.4対応に伴う修正

        * \ ``AsyncRestTemplate``\がSpring Framework 5より非推奨となった旨と、代替となるクラスが非サポートであることの説明を追加

    * -
      - :doc:`../ArchitectureInDetail/DataAccessDetail/DataAccessMyBatis3`
      - 記載内容の追加

        * \ ``Pageable`` \ を利用した検索結果のソートについての説明を追加

    * -
      - :doc:`../ArchitectureInDetail/GeneralFuncDetail/Logging`
      - 記載内容の修正

        * TERASOLUNA Server Framework for Java (5.x)の共通ライブラリが提供する\ ``TraceLoggingInterceptor``\のWARNログ出力に関する閾値の設定例を修正

    * -
      - :doc:`../ArchitectureInDetail/GeneralFuncDetail/Dozer`
      - Dozer 6.4.1対応に伴う修正

        * Dozer のバージョンアップ対応に伴い、ガイドラインに記載されているコード例を修正
        * Dozer 6.2.0において、単方向マッピングの挙動が仕様と異なっていたバグが修正されたことの説明を追加
        * Dozer 6.3.0よりJAXBがデフォルト利用されるようになったため、挙動の変更の注意点をWARNINGに追加
        * Dozer 6.4.0より一部のJSR-310 Date and Time APIがサポートされた旨の説明を追加

        記載内容の削除

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

        * Spring Security 5より非推奨の\ ``PasswordEncoder``\のパッケージが廃止されたことに伴い、\ ``MessageDigestPasswordEncoder``\を使用する方法に記載を修正

        記載内容の改善

        * ブランクプロジェクトで定義する\ ``PasswordEncoder``\を\ ``BCryptPasswordEncoder``\から\ ``DelegatingPasswordEncoder``\に変更したことに伴う記載内容の変更

        記載内容の追加

        * \ ``SPRING_SECURITY_LAST_EXCEPTION`` \ が格納されるスコープの説明を追加

    * -
      - :doc:`../Security/Authorization`
      - Spring Framework 5.1.4対応に伴う修正

        * SpEL評価時におけるnull-safetyの影響についての注意事項を追加

        記載内容の追加

        * Spring Securityが提供する\ ``AccessDeniedHandler``\の実装クラスの一覧に\ ``RequestMatcherDelegatingAccessDeniedHandler``\を追加

    * -
      - :doc:`../Security/CSRF`
      - OWASP Top 10 2017対応に伴う修正

        * OWASP Top 10 2013版へのリンクをOWASP Cheat Sheetへのリンクへ変更

    * -
      - :doc:`../Security/LinkageWithBrowser`
      - Spring Security 5.1.3対応に伴う修正

        * Spring Securityが提供する\ ``HeaderWriterFilter``\の仕様変更と\ ``DelegatingRequestMatcherHeaderWriter``\でのリクエストパスのマッチングにおけるバグについての注意事項を追加

        記載内容の追加

        * Spring Securityがサポートするセキュリティヘッダの一覧にReferrer-Policyヘッダを追加
        * Spring Securityがサポートするセキュリティヘッダの一覧にFeature-Policyヘッダを追加

    * -
      - :doc:`../Security/OAuth`
      - Spring Security OAuth 2.2.2対応に伴う修正

        * Spring Security OAuthのバージョン更新に伴いリダイレクトURI情報を保持するテーブルへの説明にWarningを追加

        記載内容の修正

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
      - :doc:`../Appendix/Java11Changes`
      - 新規追加

        * Java SE 8からJava SE 11までの主要な変更点を追加

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
