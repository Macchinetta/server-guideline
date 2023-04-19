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

  * - 2023-04-28
    - \-
    - 1.9.1 RELEASE版公開

  * -
    - 全般
    - ガイドラインの誤記(タイプミスや単純な記述ミスなど)の修正

      記載内容の改善

      記載内容の修正・追加

      * ログインジェクション対策としてlogbackのフォーマットパターンを修正
      * Jakarta EE 8 ベースからJakarta EE 10 ベースへ切り替えることに伴う記述修正
      * Java 1.8 ベースから Java 17 ベースへ切り替えることに伴う記述修正
      * Tilesに関する記述を削除
      * Dozerに関する記述を削除
      * リクエストのハンドラメソッドに@RequestMapping合成アノテーションを使用するように修正
      * Spring Securityのパス解析で使用されるMatcherがAntPathRequestMatcherとなるように修正

  * -
    - \ :doc:`../Introduction/Introduction`\
    - 記載内容の修正

      * 動作検証環境に関するNoteを修正

  * -
    - \ :doc:`../Overview/FrameworkStack`\
    - 記載内容の修正

      利用するOSSのバージョンを更新

      * Spring Bootを3.0.1に更新
      * MyBatisを3.5.11に更新
      * MyBatis Springを3.0.1に更新
      * Jakarta Dependency Injectionを2.0.1に更新
      * OpenPDFを1.3.30に更新
      * Apache POIを5.2.3に更新
      * Guavaを31.1-jreに更新
      * commons-collectionsをcommons-collections4の4.4に更新
      
      Spring Bootのバージョン更新に伴い利用するOSSのバージョンを更新

      * Spring Frameworkを6.0.3に更新
      * Spring Dataを3.0.0に更新
      * Spring Securityを6.0.1に更新
      * AspectJを1.9.19に更新
      * Logbackを1.4.5に更新
      * SLF4Jを2.0.6に更新
      * Jacksonを2.14.1に更新
      * Hibernate Validatorを8.0.0.Final(Bean Validation 3.0)に更新
      * Apache Commons Langを3.12.0に更新
      * Apache Commons DBCPを2.9.0に更新
      * Lombokを1.18.24に更新
      
      Spring Bootのバージョン更新に伴い利用するOSSを変更

      * Java MailをAngus Mailの1.0.0(Jakarta Mail 2.1)へ変更
      * HttpClientをHttpClient5の5.1.4へ変更
      * Apache Standard TaglibをJakarta Standard Tag Libraryの3.0.1へ変更
      
      利用するOSSを追加

      * MapStruct 1.5.3.Finalを追加
      * Java Time Jsptags 2.0.0を追加
      
      利用するOSSのサポートを終了

      * Apache Tilesをサポート対象外として削除
      * Joda Timeをサポート対象外として削除
      * Dozerをサポート対象外として削除
      
      単体テストで利用するOSSのバージョンを更新

      * DB Unitを2.7.3.に更新
      * Mockitoを4.8.1に更新
      * Spring Testを6.0.3に更新
      
      記載内容の修正

      * Apache Tilesのサポートが終了したことに伴い、画面レイアウトに関するページがなくなったことに対するTipを追加
      * Logback1.2.8以降モジュール構成が変わったことに関するTipを追加
      * 共通ライブラリが提供するJoda-Timeに関する機能を非推奨化

  * -
    - \ :doc:`../Overview/SpringMVCOverview`\
    - 記載内容の修正

      * Spring MVCに関する説明を修正
      * クラス階層の図を最新化

  * -
    - \ :doc:`../ArchitectureInDetail/WebApplicationDetail/ExceptionHandling`\
    - 記載内容の修正
  
      * NestedServletExceptionが削除されたことに伴い例外ハンドリングのパターンを修正

  * -
    - \ :doc:`../ArchitectureInDetail/WebApplicationDetail/FileUpload`\
    - 記載内容の修正
  
      * Commons FileUploadに関する記述を削除

  * -
    - \ :doc:`../ArchitectureInDetail/WebApplicationDetail/FileDownload`\
    - 記載内容の修正
  
      * AbstractPdfViewを継承したクラスの実装例で使用しているParagraphに渡す型を修正

  * -
    - Tilesによる画面レイアウト
    - 削除
  
      * Jakarta EE 10 への移行に伴い該当のページを削除

  * -
    - \ :doc:`../ArchitectureInDetail/WebServiceDetail/RestClient`\
    - 記載内容の修正
    
      * AsyncRestTemplateの代替としてWebClientへ修正
      * HttpClient5への移行に伴いSSL自己署名証明書の処理を修正

  * -
    - \ :doc:`../ArchitectureInDetail/GeneralFuncDetail/Logging`\
    - 記載内容の修正
    
      * Logbackの設定の読み込みについてのNoteを修正

  * -
    - \ :doc:`../ArchitectureInDetail/GeneralFuncDetail/DateAndTime`\
    - 記載内容の修正
    
      * Clockについての記述を追加
      * JSR-310のJSP Tag Libraryについて記述を追加

  * -
    - \ :doc:`../ArchitectureInDetail/GeneralFuncDetail/SystemDate`\
    - 記載内容の修正
    
      * Joda Timeを削除しJSR-310ベースへ修正

  * -
    - \ :doc:`../ArchitectureInDetail/MessagingDetail/Email`\
    - 記載内容の削除

      * GreenMailを利用したテストを削除

  * -
    - \ :doc:`../ArchitectureInDetail/MessagingDetail/JMS`\
    - 記載内容の修正

      * Apache ActiveMQ からApache ActiveMQ Artemisへ変更
       
  * -
    - \ :doc:`../ArchitectureInDetail/GeneralFuncDetail/BeanMapping`\
    - 新規追加

      * Beanマッピングに使用するライブラリをDozerからMapStructに変更

  * -
    - \ :doc:`../Security/SpringSecurity`\
    - 記載内容の修正・追加

      * Spring Security 5.7.0よりSecurityContextPersistenceFilterが非推奨となり、SecurityContextHolderFilterが推奨となったことへの対応
      * 認可処理のフィルターがFilterSecurityInterceptorからAuthorizationFilterへ変更になったことに伴う修正
      * AuthorizationFilterに関するWarningを追加
      * Spring Securityのパスパターン解析がデフォルトでMVC形式となったことに対するTipを追加

  * -
    - \ :doc:`../Security/Authentication`\
    - 記載内容の修正

      * Spring Security 5.7.0よりSecurityContextPersistenceFilterが非推奨となり、SecurityContextHolderFilterが推奨となったことへの対応
      * PasswordEncoderのデフォルトコンストラクタ削除に伴う修正

  * -
    - \ :doc:`../Security/Authorization`\
    - 記載内容の修正・追加

      * 認可処理のデフォルト値がdenyAllになったことに伴う修正
      * 認可処理のフィルターがFilterSecurityInterceptorからAuthorizationFilterへ変更になったことに伴う修正

  * -
    - \ :doc:`../Security/OAuth2`\
    - 記載内容の修正・追加

      * OAuth(org.springframework.security.oauth)へのリンクを削除
      * Spring SecurityのOAuth2のアーキテクチャのフローを修正
      * クライアント認可処理のフローを修正
      * How to Useの修正
      * Proxy Serverを経由している場合についてのNoteを追加

  * -
    - \ :doc:`../Tutorial/TutorialTodo`\
    - 記載内容の追加

      * JSPの警告についてNoteを追加

  * -
    - \ :doc:`../Tutorial/TutorialREST`\
    - 記載内容の修正

      * DHC REST ClientのキャプチャをTalend API Testerのものに修正

  * -
    - \ :doc:`../Tutorial/TutorialSecurity`\
    - 記載内容の修正

      * systemExceptionResolverの除外設定からNestedServletExceptionを削除

  * -
    - \ :doc:`../Appendix/Lombok`\
    - 記載内容の追加

      * MapStructと併用するための記述を追加

  * -
    - \ :doc:`../Appendix/Java17Settings`\
    - 記載内容の修正

      * ページタイトルを「Java SE 8からJava SE 11までの主要な変更点」から「Java SE 17を使用するための設定」へ修正

  * -
    - \ :doc:`../Appendix/SpringToolSuite4`\
    - 記載内容の追加

      * プラグインが入れられない問題についてNoteを追加
      * JSPの警告についてNoteを追加

  * -
    - OAuth(org.springframework.security.oauth)
    - 削除

      * org.springframework.security.oauthがEOLしたことに伴い該当ページを削除

  * -
    - \ :doc:`../Appendix/JodaTime`\
    - 移動

      * Joda Timeをスタック対象外としたことに伴い該当ページをAppendixへ移動

  * -
    - \ :doc:`../Appendix/SOAP`\
    - 移動

      * Spring Frameworkが提供していたJAX-WSの連携機能が削除されたことに伴い該当ページをAppendixへ移動

  * - 2022-03-30
    - \-
    - 1.8.1 RELEASE版公開

  * -
    - 全般
    - ガイドラインの誤記(タイプミスや単純な記述ミスなど)の修正

      記載内容の改善

      記載内容の修正・追加

      * ログインジェクション対策としてlogbackのフォーマットパターンを修正

  * -
    - \ :doc:`../Introduction/CriteriaBasedMapping`\
    - OWASP Top 10 を2017版から2021版へ変更

      * OWASP(Open Web Application Security Project)による観点の更新

  * -
    - \ :doc:`../Overview/FrameworkStack`\
    - 利用するOSSのバージョンを更新

      * Spring Bootを2.6.1に更新
      * MyBatisを3.5.7に更新
      * Dozerを6.5.2に更新
      * Apache POIを4.1.2に更新

      Spring Boot のバージョン更新に伴い利用するOSSのバージョンを更新

      * Spring Frameworkを5.3.13に更新
      * Spring Dataを2.6.0に更新
      * Spring Securityを5.6.0に更新
      * Hibernateを5.6.1(JPA 2.2)に更新
      * AspectJを1.9.7に更新
      * SLF4Jを1.7.32に更新
      * Jacksonを2.13.0に更新
      * Hibernate Validatorを6.2.0(Bean Validation 2.0)に更新
      * Apache Commons Langを3.12.0に更新
      * Apache Commons DBCPを2.9.0に更新
      * Lombokを1.18.22に更新
      * Logbackを1.2.7に更新

      単体テストで利用するOSSのバージョンを更新

      * DB Unitを2.7.2に更新
      * Mockitoを4.0.0に更新
      * Spring Testを5.3.13に更新

      利用するOSSのサポートを終了

      * Spring Security標準OAuthのサポートに伴い、非推奨となっているSpring Security OAuthをサポート対象外として削除

      記載内容の追加

      * \ `CVE-2021-42550 <https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-42550>`_\ に関する説明及び注意点を追加

  * -
    - \ :doc:`../ImplementationAtEachLayer/CreateProject`\
    - 記載内容の修正

      * warファイルのコピーに使用するmaven-dependency-pluginのバージョンを更新し、使用するゴールをcopyに変更

  * -
    - \ :doc:`../ArchitectureInDetail/WebServiceDetail/RestClient`\
    - 記載内容の修正

      * \ ``RequestFactoryBean``\ 内の\ ``HttpClient``\ がクローズされるように修正

  * -
    - \ :doc:`../Security/OAuth2`\
    - 記載内容の修正

      * Spring Security標準OAuthのサポートに伴い、説明内容を修正

  * -
    - \ :doc:`../Security/SecureLoginDemo`\
    - 記載内容の修正

      * Passayを1.6.1に更新したことに伴い、説明内容を修正

  * -
    - \ :doc:`../Tutorial/TutorialREST`\
    - 記載内容の追加

      * REST ClientがDHC REST ClientからTalend API Testerに置き換わっていることについてのNoteを追加

  * -
    - \ :doc:`../Tutorial/TutorialSession`\
    - 記載内容の追加

      * JDK11の場合のビルド手順についてのNoteを追加

  * -
    - \ :doc:`../UnitTest/ImplementsOfUnitTest/ImplementsOfTestByLayer`\
    - 記載内容の削除

      * DB Unitの更新に伴い、Apache POIのダウングレードに関するWarningを削除

  * -
    - \ :doc:`../Appendix/SpringToolSuite4`\
    - 新規追加

      * STS4の設定手順を追加

  * -
    - OAuth(org.springframework.security.oauth)
    - 新規追加

      * Spring Security標準OAuthのサポートに伴い、Spring Security OAuthの説明をAppendixへ移動

  * - 2021-03-26
    - \-
    - 1.8.0 RELEASE版公開

  * -
    - 全般
    - Java EEからJakarta EEへ切り替えことに伴う記述修正

      記載内容の修正・追加

      * 利用するミドルウェアのバージョンを更新

  * -
    - \ :doc:`../Overview/FrameworkStack`\
    - 利用するOSSのバージョンを更新

      * Spring Bootを2.4.1に更新
      * Spring Security OAuthを2.5.0に更新
      * MyBatisを3.5.6に更新
      * MyBatis Springを2.0.6に更新
      * Joda Timeを2.10.9に更新

      Spring Boot のバージョン更新に伴い利用するOSSのバージョンを更新

      * Spring Frameworkを5.3.2に更新
      * Spring Dataを2.4.2に更新
      * Spring Securityを5.4.2に更新
      * Hibernateを5.4.25(JPA 2.2)に更新
      * AspectJを1.9.6に更新
      * SLF4Jを1.7.30に更新
      * Jacksonを2.11.3に更新
      * Hibernate Validatorを6.1.6(Bean Validation 2.0)に更新
      * Apache Commons Langを3.11に更新
      * Apache Commons DBCPを2.8.0に更新
      * Apache HttpClientを4.5.13に更新
      * Lombokを1.18.16に更新

      単体テストで利用するOSSのバージョンを更新

      * Hamcrestを2.2に更新
      * Mockitoを3.6.28に更新
      * Spring Testを5.3.2に更新

      利用するOSSのバージョンの更新による主な変更

      * Spring Boot 2.3よりjoda-timeをバージョン管理しなくなったため、terasoluna-gfw-parentで管理するよう変更
      * Spring Framework 5.3.0より\ ``@PathVariable``\ でバインドされる値に拡張子が含まれるように変更されたことへの対応
      * Spring Framework 5.3.0より\ ``HandlerInterceptor``\ のパス指定におけるワイルドカードの使用方法が変更されたことへの対応
      * Spring Framework 5.3.0より\ ``HandlerInterceptorAdapter``\ が非推奨となったことへの対応
      * Spring Framework 5.3.0より\ ``JdbcTemplate``\ のメソッドのうち一部が非推奨となったことへの対応
      * Spring Security OAuth 2.5.0より\ ``DefaultUserAuthenticationConverter#getAuthorities``\ の可視性が変更されたことへの対応
      * Hibernate Validator 6.1.0より日本語メッセージが提供されたことへの対応
      * JUnit 4.13より\ ``org.junit.Assert#assertThat``\ が非推奨となったことへの対応

      TERASOLUNA Server Framework for Java (5.x)の共通ライブラリの機能改善

      * 共通ライブラリが用意する入力チェックルールの日本語メッセージを提供
      * \ ``@Compare``\ がBean Validation 2.0に準拠
      * Bootstrap v4以降に対応するため、以下の変更

        - \ ``ResultMessages``\ の標準メッセージタイプに、\ ``primary``\ 、\ ``secondary``\ 、\ ``light``\ 、\ ``dark``\ を追加
        - \ ``<t:pagination>``\ タグに、\ ``anchorClass``\ 属性を追加

      * 共通ライブラリの非推奨APIを削除

  * -
    - \ :doc:`../ImplementationAtEachLayer/CreateWebApplicationProject`\
    - 記載内容の修正

      * Mavenセントラルリポジトリで公開されるOracle JDBC DriverのgroupIdが変更されたことへの対応
      * オフライン環境でプロジェクト開発を続けるための事前作業について、一部手順に誤りがあったため修正

  * -
    - \ :doc:`../ImplementationAtEachLayer/ApplicationLayer`\
    - Spring Framework 5.3.0対応に伴う修正

      * Spring Framework 5.3.0より\ ``@PathVariable``\ でバインドされる値に拡張子が含まれるように変更されたことへの対応
      * Spring Framework 5.3.0より\ ``HandlerInterceptor``\ のパス指定におけるワイルドカードの使用方法が変更されたことへの対応
      * Spring Framework 5.3.0より\ ``HandlerInterceptorAdapter``\ が非推奨となったことへの対応

      記載内容の追加

      * \ ``addAttribute``\ 、\ ``addFlashAttribute``\ で第一引数を省略した際、\ ``Conventions#getVariableName``\ の仕様に基づき属性名が決まる説明を追加

  * -
    - \ :doc:`../ImplementationAtEachLayer/CreateProject`\
    - 記載内容の修正

      * Tomcatへデプロイする際にコンテキストXMLファイルを配置するファイルパスを修正

  * -
    - \ :doc:`../ArchitectureInDetail/WebApplicationDetail/Validation`\
    - 記載内容の修正

      * Hibernate Validator 6.1.0より日本語メッセージが提供されたことへの対応
      * 共通ライブラリが用意する入力チェックルールの日本語メッセージを提供
      * \ ``@Compare``\ がBean Validation 2.0に準拠
      * 相関項目チェックルールのコード例において、エラーメッセージを確認用フィールドに表示するように変更
      * Bean Validationを利用した相関項目チェックルールのコード例をBean Validation 2.0に準拠するよう変更

  * -
    - \ :doc:`../ArchitectureInDetail/WebApplicationDetail/Pagination`\
    - 記載内容の修正

      * \ ``<t:pagination>``\ タグに、\ ``anchorClass``\ 属性を追加

  * -
    - \ :doc:`../ArchitectureInDetail/WebApplicationDetail/MessageManagement`\
    - 記載内容の修正

      * \ ``ResultMessages``\ の標準メッセージタイプに、\ ``primary``\ 、\ ``secondary``\ 、\ ``light``\ 、\ ``dark``\ を追加
      * \ ``ResultMessages``\ の標準メッセージタイプから、非推奨の\ ``warn``\ を削除
      * CSSライブラリBootstrapリンク先を最新化

  * -
    - \ :doc:`../ArchitectureInDetail/DataAccessDetail/ExclusionControl`\
    - 記載内容の修正

      * \ ``ObjectOptimisticLockingFailureException``\ のFQCNの誤りを修正

  * -
    - \ :doc:`../ArchitectureInDetail/GeneralFuncDetail/SystemDate`\
    - 記載内容の修正

      * JUnit 4.13より\ ``org.junit.Assert#assertThat``\ が非推奨となったことへの対応

  * -
    - \ :doc:`../Security/Authentication`\
    - 記載内容の修正・追加

      * \ ``UserDetails``\ 実装クラスの\ ``equals``\ メソッドについての説明を追加
      * ブランクプロジェクトにおいてSpring Securityのフォーム認証を使用しない場合の注意事項を追加

  * -
    - OAuth(org.springframework.security.oauth)
    - 記載内容の修正・追加

      * Spring Security OAuth 2.5.0より\ ``DefaultUserAuthenticationConverter#getAuthorities``\ の可視性が変更されたことへの対応
      * Spring Security OAuthが非推奨となったことへの対応

  * -
    - \ :doc:`../UnitTest/UnitTestOverview`\
    - Spring Boot のバージョン更新に伴い利用するOSSのバージョンを更新

      * Hamcrestを2.2に更新
      * Mockitoを3.6.28に更新
      * Spring Testを5.3.2に更新

  * -
    - \ :doc:`../UnitTest/ImplementsOfUnitTest/ImplementsOfTestByLayer`\
    - 記載内容の修正

      * Spring Framework 5.3.0より\ ``JdbcTemplate``\ のメソッドのうち一部が非推奨となったことへの対応
      * JUnit 4.13より\ ``org.junit.Assert#assertThat``\ が非推奨となったことへの対応

  * -
    - \ :doc:`../UnitTest/ImplementsOfUnitTest/UsageOfLibraryForTest`\
    - 記載内容の修正・追加

      * Mockito 2より\ ``org.mockito.Matchers``\ が非推奨となったことへの対応
      * \ ``MockMultipartHttpServletRequestBuilder``\ の主なメソッドの説明に\ ``part``\ メソッドを追加
      * \ ``MockMultipartHttpServletRequestBuilder``\ において、リクエストを送信する際に"/"から始まらないパスを指定した場合のエラーの説明を追加

  * -
    - \ :doc:`../Tutorial/TutorialREST`\
    - 記載内容の修正

      * \ ``MessageConverter``\ および\ ``ObjectMapper``\ の定義方法を\ \ :doc:`../ArchitectureInDetail/WebServiceDetail/REST`\ に合わせるよう変更

  * - 2021-01-07
    - \-
    - 1.7.1 RELEASE版公開

  * -
    - \ :doc:`../ArchitectureInDetail/WebApplicationDetail/SessionManagement`\
    - 記載内容の追加

      * 「同一セッション内のリクエストの同期化」の適用範囲についての注意事項を追加

  * - 2020-06-29
    - \-
    - 1.7.0 RELEASE版公開

  * -
    - 全般
    - ガイドラインの誤記(タイプミスや単純な記述ミスなど)の修正

      記載内容の改善

      記載内容の修正・追加

      * 利用するミドルウェアのバージョンを更新

      * Spring Framework 5.1.16より\ `XMLスキーマ処理が改善 <https://github.com/spring-projects/spring-framework/issues/22504>`_\ されたため、ブランクプロジェクトにおけるBean定義ファイルのXMLスキーマファイル(.xsd)参照を\ ``http``\ から\ ``https``\ に変更
      * Spring Framework 5.1より\ `ログ出力の見直し <https://github.com/spring-projects/spring-framework/issues/21437>`_\ が行われたため、ブランクプロジェクトにおいてマッピングされたハンドラメソッドのログを出力するよう変更

  * -
    - \ :doc:`../Introduction/CriteriaBasedMapping`\
    - 記載内容の追加

      * CVE-2020-5408を追加

  * -
    - \ :doc:`../Overview/FrameworkStack`\
    - 利用するOSSのバージョンを更新

      * Spring Bootを2.2.4に更新
      * Spring Security OAuthを2.4.0に更新
      * MyBatisを3.5.3に更新
      * MyBatis Springを2.0.3に更新
      * Apache Commons BeanUtilsを1.9.4に更新
      * Dozerを6.5.0に更新
      * Apache POIを4.1.1に更新

      Spring Boot のバージョン更新に伴い利用するOSSのバージョンを更新

      * Spring Frameworkを5.2.3に更新
      * Spring Dataを2.2.4に更新
      * Spring Securityを5.2.1に更新
      * AspectJを1.9.5に更新
      * SLF4Jを1.7.30に更新
      * Jacksonを2.10.2に更新
      * Hibernate Validatorを6.0.18(Bean Validation 2.0)に更新
      * Apache Commons Langを3.9に更新
      * Joda Timeを2.10.5に更新
      * Apache Commons DBCPを2.7.0に更新
      * Apache HttpClientを4.5.10に更新
      * Lombokを1.18.10に更新

      単体テストで利用するOSSのバージョンを更新

      * Hamcrestを2.1に更新
      * Mockitoを3.1.0に更新
      * Spring Testを5.2.3に更新

      利用するOSSのバージョンの更新による主な変更

      * Spring Security 5.2で追加された\ ``Argon2PasswordEncoder``\ の記述を追加
      * Spring Security 5.2で追加された\ ``LogoutSuccessEvent``\ および\ ``LogoutSuccessEventPublishingLogoutHandler``\ の記述を追加
      * Spring Security 5.2で追加された\ ``ClearSiteDataHeaderWriter``\ および\ ``HeaderWriterLogoutHandler``\ の記述を追加
      * Spring Security 5.2.1において、既存のセキュリティヘッダがある場合の挙動が変更されたこと（\ `spring-projects/spring-security#6454 <https://github.com/spring-projects/spring-security/issues/6454>`_\ ）への対応
      * Spring Data 2.2において、廃止予定であった非推奨APIが削除されたことへの対応
      * Spring Boot 2.2.0からJavaMailがJakarta Mailにバージョンアップしたことへの対応
      * Hamcrest 2.1からHamcrestのモジュールが統合されたため、記載するOSSライブラリを変更

      利用するOSSのサポートを終了

      * JDBC 4.2に対応していないLog4JDBCをサポート対象外として削除

      TERASOLUNA Server Framework for Java (5.x)の共通ライブラリの機能改善

      * 共通ライブラリが用意する入力チェックルールのデフォルトエラーメッセージを共通ライブラリで提供
      * \ ``<t:pagination>``\ タグに、\ ``innerElementClass``\ 属性を追加
      * \ ``Argon2PasswordEncoder``\ のサポートに伴い、\ ``bcprov-jdk15on``\ への依存関係を共通ライブラリで管理

      記載内容の追加

      * 共通ライブラリの構成要素に、TERASOLUNA Server Framework のバージョンについてのNoteを追加

  * -
    - \ :doc:`../ImplementationAtEachLayer/ApplicationLayer`\
    - 記載内容の追加

      * \ ``@RequestMapping``\ の値（value属性）を省略した場合の動作についてのNoteを追加
      * パス設計時の注意点についてのWarningを追加

  * -
    - \ :doc:`../ArchitectureInDetail/WebApplicationDetail/Validation`\
    - 記載内容の追加

      * 日付時刻の検証（\ ``@Past``\ 、\ ``@Future``\ 、\ ``@PastOrPresent``\ 、\ ``@FutureOrPresent``\ ）に適切な型を使用する必要があることについてのWarningを追加

      記載内容の修正

      * 共通ライブラリが用意する入力チェックルールのデフォルトエラーメッセージを共通ライブラリで提供するように変更したことに伴う記載内容の変更

  * -
    - \ :doc:`../ArchitectureInDetail/WebApplicationDetail/Pagination`\
    - Spring Data 2.2対応に伴う修正

      * Spring Data 2.2において、廃止予定であった非推奨APIが削除されたことに伴う実装例の修正

      TERASOLUNA Server Framework for Java (5.x)の共通ライブラリの機能改善

      * \ ``<t:pagination>``\ タグに、\ ``innerElementClass``\ 属性を追加

  * -
    - \ :doc:`../ArchitectureInDetail/WebApplicationDetail/Internationalization`\
    - 記載内容の修正

      * \ ``LocaleChangeInterceptor``\ の仕様についてのNoteを修正

  * -
    - \ :doc:`../ArchitectureInDetail/WebApplicationDetail/Codelist`\
    - 記載内容の修正

      * \ ``@ExistInCodeList``\ の入力チェックエラーメッセージについての記述を\ \ :doc:`../ArchitectureInDetail/WebApplicationDetail/Validation`\ に統合

  * -
    - \ :doc:`../ArchitectureInDetail/WebApplicationDetail/TagLibAndELFunctions`\
    - TERASOLUNA Server Framework for Java (5.x)の共通ライブラリのバグ改修に伴う修正

      * 共通ライブラリのバグ改修(\ `terasoluna-gfw#846 <https://github.com/terasolunaorg/terasoluna-gfw/issues/846>`_\)に伴い、\ ``f:query``\ の仕様に関する説明を修正

  * -
    - \ :doc:`../ArchitectureInDetail/WebServiceDetail/RestClient`\
    - 記載内容の修正

      * \ ``AsyncRestTemplate``\ のスレッドプールをカスタマイズする方法の誤った説明を修正

  * -
    - \ :doc:`../ArchitectureInDetail/DataAccessDetail/DataAccessCommon`\
    - 記載内容の削除

      *  共通ライブラリの変更に伴うlog4jdbcの記載の削除

  * -
    - Beanマッピング(Dozer)
    - 記載内容の削除

      * Dozer 6.5.0よりJSR-310 Date and Time APIで使用できるはずのパターン文字が使用できない不具合が解消されたため、不具合を記述したWarningを削除

      記載内容の追加

      * javax.el標準APIの実装ライブラリが存在しないことにより発生する警告についての説明を追加

      記載内容の修正

      * Dozer 6.5.0より、Mavenを利用してJava SE 9以降でビルドする場合JAXBを利用するための設定が不要になったため、WarningをNoteに変更し説明を修正

  * -
    - \ :doc:`../ArchitectureInDetail/MessagingDetail/Email`\
    - Spring Boot 2.2.4対応に伴う修正

      * JavaMailからJakarta Mailにバージョンアップしたことに伴い、説明内容を修正

      記載内容の修正

      * JavaMail 1.4.4よりマルチバイト文字を使用する際にメール本文終端に余計な文字が付与される不具合が修正された旨を追記

  * -
    - \ :doc:`../ArchitectureInDetail/MessagingDetail/JMS`\
    - 記載内容の修正・追加

      * Spring Framework 5.0.0より、Spring JMSの動作にJMS 2.0のAPIが必要になったことによる記載の修正
      * ActiveMQ Clientにおいて、JMS API 2.0で動作するために必要なライブラリ一覧を追加
      * リスナークラスを格納するパッケージ配下をcomponent-scan対象とする必要がある旨の説明を追加

  * -
    - \ :doc:`../Security/SpringSecurity`\
    - 記載内容の修正

      * Spring Security 5.0.1, 4.2.4, 4.1.5より、デフォルトで利用される\ ``HttpFirewall``\ インタフェースの実装クラスが変更されたことに対する記述の修正

  * -
    - \ :doc:`../Security/Authentication`\
    - Spring Security 5.2.x対応に伴う修正

      * Spring Security 5.2で追加された\ ``Argon2PasswordEncoder``\ の記述を追加
      * Spring Security 5.2で追加された\ ``LogoutSuccessEvent``\ および\ ``LogoutSuccessEventPublishingLogoutHandler``\ の記述を追加
      * Spring Security 5.2で追加された\ ``ClearSiteDataHeaderWriter``\ および\ ``HeaderWriterLogoutHandler``\ の記述を追加

      TERASOLUNA Server Framework for Java (5.x)の共通ライブラリの機能改善

      * \ ``Argon2PasswordEncoder``\ のサポートに伴い、\ ``bcprov-jdk15on``\ への依存関係を共通ライブラリで管理

      記載内容の追加

      * PasswordEncoderに定義されているメソッドの一覧にSpring Security 5.1で追加された\ ``upgradeEncoding``\ を追加

      記載内容の修正

      * \ ``@EventListener``\ が処理する認証イベントの指定方法を改善
      * \ ``@EventListener``\ クラスを格納するパッケージの明示および注意点の記載
      * Spring Securityが提供するクラスをまとめた表の見直し

  * -
    - \ :doc:`../Security/Authorization`\
    - 記載内容の修正

      * Spring Securityが提供するクラスをまとめた表の見直し

  * -
    - \ :doc:`../Security/SessionManagement`\
    - 記載内容の修正

      * Spring Security 5.0.1, 4.2.4, 4.1.5以降では、デフォルトの設定でURL RewritingによるセッションIDの連携を行えず、設定を変更した場合、脆弱性が発生する可能性がある旨の記述を追加

  * -
    - \ :doc:`../Security/LinkageWithBrowser`\
    - Spring Security 5.2.x対応に伴う修正

      * Spring Security 5.2で追加された\ ``ClearSiteDataHeaderWriter``\ の記述を追加
      * Spring Security 5.2で追加されたStrict-Transport-SecurityヘッダのpreloadディレクティブについてのNoteを追加
      * \ `spring-projects/spring-security#6454 <https://github.com/spring-projects/spring-security/issues/6454>`_\ により解消されたWarning「個別に付与したセキュリティヘッダがSpring Securityにより上書き（追加）される問題」を削除

      記載内容の追加

      * Content Security Policyヘッダに関するIEがサポートしていないことについてのWarningを追加
      * Content Security Policyヘッダで混在コンテンツをブロックする方法についてのNoteを追加

  * -
    - \ :doc:`../Security/Encryption`\
    - 記載内容の修正

      * CVE-2020-5408により\ ``Encryptors#queryableText``\ メソッドを非推奨とする旨のNoteを追加し、コード例を削除

  * -
    - \ :doc:`../Security/SecureLoginDemo`\
    - 記載内容の修正

      * \ ``@EventListener``\ が処理する認証イベントの指定方法を改善
      * \ ``@EventListener``\ クラスを格納するパッケージの変更

  * -
    - \ :doc:`../UnitTest/UnitTestOverview`\
    - Spring Boot のバージョン更新に伴い利用するOSSのバージョンを更新

      * Hamcrestを2.1に更新
      * Mockitoを3.1.0に更新
      * Spring Testを5.2.3に更新

      記載内容の修正

      * Hamcrest 2.1から\ ``hamcrest-core``\, \ ``hamcrest-library``\ が\ ``hamcrest``\ に統合されたため、記載するOSSライブラリを変更

  * -
    - \ :doc:`../UnitTest/ImplementsOfUnitTest/ImplementsOfTestByLayer`\
    - 記載内容の追加

      * データ定義ファイルにExcel形式（.xlsx）のファイルを使用する場合のApache POIについてWarningを追加

  * -
    - \ :doc:`../Appendix/Java17Settings`\
    - 記載内容の追加

      * 「推移的に解決されるJava EE関連モジュールの競合」節の追加

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

      * ViewResolverの定義について、Spring 4.0以前からの\ ``<bean>``\ 要素を使用した定義方法を削除し、Spring 4.1以降の\ ``<mvc:view-resolvers>``\ 要素を使用した定義方法のみ解説するよう変更
      * 利用するミドルウェアのバージョンを更新

  * -
    - \ :doc:`../Introduction/CriteriaBasedMapping`\
    - OWASP Top 10 を2013版から2017版へ変更

      * OWASP(Open Web Application Security Project)による観点の更新

  * -
    - \ :doc:`../Overview/FrameworkStack`\
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
      * Spring Framework 4.2から非推奨ととなっていた\ ``AbstractExcelView``\ がSpring Framework 5.0で削除されたことに伴う対応
      * Spring Framework 5.0.0よりクエリ文字列に対するURLエンコーディングの仕様が変更されたことへの対応
      * Spring Framework 5.0.0より指定サイズを超えるファイルのアップロードやマルチパートのリクエストが行われた際に発生する例外の仕様が変更されたことに伴う対応
      * Spring Framework 5.0.0よりSpEL評価時におけるnull-safety機能が追加されたことへの対応
      * Spring Security 5より非推奨の\ ``PasswordEncoder``\ のパッケージが廃止になったことへの対応
      * Spring Security 5.0.2および5.1.2で変更となったセキュリティヘッダの付与タイミングによる、リクエストパスのマッチングにおける注意事項の追加
      * Spring Security OAuth 2.2.2よりリダイレクトURIのホワイトリストチェックの仕様が変更されたことへの対応

  * -
    - \ :doc:`../Overview/FrameworkStack`\
    - TERASOLUNA Server Framework for Java (5.x)の共通ライブラリの新機能追加

      \ ``terasoluna-gfw-validator``\
       * バイト長チェック用Bean Validation制約アノテーション \ ``@ByteSize`` \

      TERASOLUNA Server Framework for Java (5.x)の共通ライブラリの機能改善

      \ ``terasoluna-gfw-common``\
       * \ ``SimpleI18nCodeList``\ のロケール解決方法の改善
       * \ ``SimpleReloadableI18nCodeList``\ の追加
       * \ ``@ExistInCodeList`` \ で \ ``Number`` \ 型をサポートするよう改善
       * \ ``ReloadableCodeList`` \ のイミュータブル対応に伴う \ ``CodeListInterceptor``\ の仕様変更
       * \ ``@ExistInCodeList`` \ をBean Validation 2.0に準拠するよう仕様変更
      \ ``terasoluna-gfw-codepoints``\
       * \ ``@ConsistOf`` \ をBean Validation 2.0に準拠するよう仕様変更
      \ ``terasoluna-gfw-validator``\
       * \ ``@ByteMax`` \ 及び\ ``@ByteMin`` \ をBean Validation 2.0に準拠するよう仕様変更

  * -
    - \ :doc:`../ImplementationAtEachLayer/CreateWebApplicationProject`\
    - 記載内容の追加

      * 大量にコードリストを定義する場合のBean定義方法に関する記載を追加

  * -
    - \ :doc:`../ImplementationAtEachLayer/ApplicationLayer`\
    - 記載内容の追加

      * Spring Framework 4.3より追加された \ ``@RequestMapping``\ の合成アノテーションの説明を追加

  * -
    - \ :doc:`../ArchitectureInDetail/WebApplicationDetail/Validation`\
    - Bean Validation 2.0(Hibernate Validator 6.0)対応に伴う修正

      * Bean Validation 2.0及びHibernate Validator 6.0では、コレクション内の各値に対して入力チェックできるようになった旨の説明を追加
      * Bean Validation 2.0では、一つのフィールドに同じアノテーションを複数指定できる旨の説明を追加
      * Bean Validation 2.0及びHibernate Validator 6.0で追加されたアノテーションに対する説明を追加
      * Hibernate Validator 6.0で非推奨となったアノテーションに対する説明を追加
      * Bean Validation 2.0で提供される\ ``ClockProvider``\ を実装することで、基準日付の変更が可能である旨の説明を追加

  * -
    - \ :doc:`../ArchitectureInDetail/WebApplicationDetail/ExceptionHandling`\
    - Spring Framework 5.1.4対応に伴う修正

      * \ ``DefaultHandlerExceptionResolver``\ がハンドリングする例外一覧からSpring Framework 5.0より廃止された\ ``org.springframework.web.servlet.mvc.multiaction.NoSuchRequestHandlingMethodException``\ を削除

      記載内容の修正

      * \ ``DefaultHandlerExceptionResolver``\ がハンドリングする例外一覧にSpring Framework 4.2より追加された\ ``org.springframework.web.bind.MissingPathVariableException``\ を追加
      * \ ``SystemExceptionResolver#preventResponseCaching``\ とSpring SecurityのCache-Controlヘッダの併用についての注意を追加

  * -
    - \ :doc:`../ArchitectureInDetail/WebApplicationDetail/Pagination`\
    - 構成見直し

      * Overviewを取得データの表示、ページネーションリンクの表示、ページネーション情報の表示の3点について説明するように変更

  * -
    - \ :doc:`../ArchitectureInDetail/WebApplicationDetail/MessageManagement`\
    - 記載内容の修正

      * \ ``SPRING_SECURITY_LAST_EXCEPTION`` \ が格納されるスコープの誤記を修正

  * -
    - \ :doc:`../ArchitectureInDetail/WebApplicationDetail/Internationalization`\
    - 記載内容の追加

      * \ ``AcceptHeaderLocaleResolver``\ と\ ``LocaleChangeInterceptor``\ の指定可能な設定についての説明を追加

  * -
    - \ :doc:`../ArchitectureInDetail/WebApplicationDetail/Codelist`\
    - 記載内容の修正

      * 独自カスタマイズしたコードリストのBean定義方法を、コンポーネントスキャンからBean定義ファイルによる定義に変更

      記載内容の追加

      * コードリストBeanをJSPから直接参照する方法を追加

  * -
    - \ :doc:`../ArchitectureInDetail/WebApplicationDetail/FileUpload`\
    - Spring Framework 5.1.4対応に伴う修正

      * 指定サイズを超えるファイルのアップロードやマルチパートのリクエストが行われた際に発生する例外の仕様が変更されたことに伴い、Noteを追加

  * -
    - \ :doc:`../ArchitectureInDetail/WebApplicationDetail/FileDownload`\
    - Spring Framework 5.1.4対応に伴う修正

      * JasperReportsが非サポートとなったため、JasperReportsに言及している記載を修正
      * iTextの代わりにOpenPDFがサポートされるようになった旨の説明を追加し、実装例を修正
      * Spring Framework 4.2から非推奨ととなっていた\ ``AbstractExcelView``\ がSpring Framework 5.0で削除されたことに伴う対応

  * -
    - \ :doc:`../ArchitectureInDetail/WebApplicationDetail/TagLibAndELFunctions`\
    - Spring Framework 5.1.4対応に伴う修正

      * Spring Frameworkのクエリ文字列に対するURLエンコーディングの仕様変更に伴うTERASOLUNA Server Framework for Java (5.x)の共通ライブラリ(\ ``f:query()``\, \ ``f:u()``\)の変更についてWarningを追加

  * -
    - | \ :doc:`../ArchitectureInDetail/WebApplicationDetail/Ajax`\
    - OWASP Top 10 2017対応に伴う修正

      * A8:2017に関連する、デシリアライズ時のWarningを追加
      * Macchinetta Server Framework (1.x)ではXXE対策済みのSpring MVCを使用しているため、
        XXE対策についてのWarningをNoteへ変更し、spring-oxmによる対策方法の記述を削除

  * -
    - | \ :doc:`../ArchitectureInDetail/WebServiceDetail/REST`\
    - OWASP Top 10 2017対応に伴う修正

      * Macchinetta Server Framework (1.x)ではXXE対策済みのSpring MVCを使用しているため、
        XXE対策についてのWarningをNoteへ変更し、spring-oxmによる対策方法の記述を削除

      記載内容の追加

      * Spring Framework 4.3より追加された \ ``@RequestMapping``\ の合成アノテーションの説明を追加

      記述内容の修正

      * Dozerのカスタムコンバーターに関する記述を Beanマッピング(Dozer) に統合

  * -
    - \ :doc:`../ArchitectureInDetail/WebServiceDetail/RestClient`\
    - Spring Framework 5.1.4対応に伴う修正

      * \ ``AsyncRestTemplate``\ がSpring Framework 5より非推奨となった旨と、代替となるクラスが非サポートであることの説明を追加

  * -
    - \ :doc:`../ArchitectureInDetail/DataAccessDetail/DataAccessMyBatis3`\
    - 記載内容の追加

      * \ ``Pageable`` \ を利用した検索結果のソートについての説明を追加
      * JSR-310 Date and Time APIを使う場合の設定の記事を削除し、依存ライブラリとして別途\ ``mybatis-typehandlers-jsr310`` \ を追加する必要はなくなった旨のNoteを追加

  * -
    - \ :doc:`../ArchitectureInDetail/GeneralFuncDetail/Logging`\
    - 記載内容の修正

      * TERASOLUNA Server Framework for Java (5.x)の共通ライブラリが提供する\ ``TraceLoggingInterceptor``\ のWARNログ出力に関する閾値の設定例を修正

  * -
    - Beanマッピング(Dozer)
    - Dozer 6.4.1対応に伴う修正

      * Dozer のバージョンアップ対応に伴い、ガイドラインに記載されているコード例を修正
      * Dozer 6.2.0において、単方向マッピングの挙動が仕様と異なっていたバグが修正されたことの説明を追加
      * Dozer 6.3.0よりJAXBがデフォルト利用されるようになったため、挙動の変更の注意点をWARNINGに追加
      * Dozer 6.4.0より一部のJSR-310 Date and Time APIがサポートされた旨の説明を追加

      記載内容の削除

      * 現バージョン（Dozer5.5.0以降）ではCollection<T>を使用したBean間のマッピングも可能であるため、マッピングが失敗する旨を記述したTodoを削除

  * -
    - \ :doc:`../ArchitectureInDetail/MessagingDetail/JMS`\
    - OWASP Top 10 2017対応に伴う修正

      * A8:2017に関連する、デシリアライズ時のWarningを追加

      記載内容の修正・追加

      * JMSを利用する際のBean定義の記載場所を再整理
      * JNDIを使用しない場合の\ ``DynamicDestinationResolver``\ のBean定義方法に関する記載を追加

  * -
    - \ :doc:`../Security/Authentication`\
    - OWASP Top 10 2017対応に伴う修正

      * A10:2017に関連する、ログイン認証時のログについてのTipを追加

      記載内容の修正

      * Spring Security 5より非推奨の\ ``PasswordEncoder``\ のパッケージが廃止されたことに伴い、\ ``MessageDigestPasswordEncoder``\ を使用する方法に記載を修正

      記載内容の改善

      * ブランクプロジェクトで定義する\ ``PasswordEncoder``\ を\ ``BCryptPasswordEncoder``\ から\ ``DelegatingPasswordEncoder``\ に変更したことに伴う記載内容の変更

      記載内容の追加

      * \ ``SPRING_SECURITY_LAST_EXCEPTION`` \ が格納されるスコープの説明を追加

  * -
    - \ :doc:`../Security/Authorization`\
    - Spring Framework 5.1.4対応に伴う修正

      * SpEL評価時におけるnull-safetyの影響についての注意事項を追加

      記載内容の追加

      * Spring Securityが提供する\ ``AccessDeniedHandler``\ の実装クラスの一覧に\ ``RequestMatcherDelegatingAccessDeniedHandler``\ を追加

  * -
    - \ :doc:`../Security/CSRF`\
    - OWASP Top 10 2017対応に伴う修正

      * OWASP Top 10 2013版へのリンクをOWASP Cheat Sheetへのリンクへ変更

  * -
    - \ :doc:`../Security/LinkageWithBrowser`\
    - Spring Security 5.1.3対応に伴う修正

      * Spring Securityが提供する\ ``HeaderWriterFilter``\ の仕様変更と\ ``DelegatingRequestMatcherHeaderWriter``\ でのリクエストパスのマッチングにおけるバグについての注意事項を追加

      記載内容の追加

      * Spring Securityがサポートするセキュリティヘッダの一覧にReferrer-Policyヘッダを追加
      * Spring Securityがサポートするセキュリティヘッダの一覧にFeature-Policyヘッダを追加

  * -
    - OAuth(org.springframework.security.oauth)
    - Spring Security OAuth 2.2.2対応に伴う修正

      * Spring Security OAuthのバージョン更新に伴いリダイレクトURI情報を保持するテーブルへの説明にWarningを追加

      記載内容の修正

      * \ ``alias``\ 属性を用いた\ ``authentication-manager``\ の定義に関する実装例、説明の修正

      記載内容の追加

      * \ `CVE-2019-3778 <https://tanzu.vmware.com/security/cve-2019-3778>`_\ (オープンリダイレクト脆弱性)に関する注意喚起を追加

  * -
    - \ :doc:`../Tutorial/TutorialTodo`\
    - 記載内容の修正・追加

      * 一覧表示機能作成時に、登録機能の一部を作成していた部分を変更し、一覧表示機能の動作確認できるように、コード例を追加
      * ガイドライン修正に伴う、サンプルコードの最新化

  * -
    - \ :doc:`../Tutorial/TutorialREST`\
    - 記載内容の修正

      * spring-mvc-rest.xmlを作成する方法の説明を変更
      * ガイドライン修正に伴う、サンプルコードの最新化

  * -
    - \ :doc:`../Tutorial/TutorialSession`\
    - 記載内容の修正

      * \ JSPのコードをTiles形式に修正
      * ガイドライン修正に伴う、サンプルコードの最新化

  * -
    - \ :doc:`../Tutorial/TutorialSecurity`\
    - 記載内容の修正

      * \ ``SPRING_SECURITY_LAST_EXCEPTION`` \ が格納されるスコープの誤記を修正
      * ガイドライン修正に伴う、サンプルコードの最新化

  * -
    - \ :doc:`../Appendix/Java17Settings`\
    - 新規追加

      * Java SE 8からJava SE 11までの主要な変更点を追加

  * - 2018-03-09
    - \-
    - 1.5.1 RELEASE版公開

  * -
    - \ :doc:`../Overview/FrameworkStack`\
    - CVE-2018-1199への対応のため、利用するOSSのバージョンを更新

      * Spring Frameworkのバージョンを4.3.14に更新
      * Spring Securityのバージョンを4.2.4に更新

  * -
    - OAuth(org.springframework.security.oauth)
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
    - \ :doc:`../Overview/FrameworkStack`\
    - 利用するOSSのバージョンを更新

      * Spring IO PlatformのバージョンをBrussels-SR5に更新
      * MyBatisのバージョンを3.4.5に更新

      Spring IO Platformのバージョン更新に伴い利用するOSSのバージョンを更新

  * -
    - \ :doc:`../ImplementationAtEachLayer/DomainLayer`\
    - 記載内容の追加

      * \ ``@Transactional`` \ アノテーションの\ ``timeout`` \ 属性に関する記載を追加

  * -
    - \ :doc:`../ArchitectureInDetail/WebApplicationDetail/Validation`\
    - 記載内容の追加

      * \ ``@Compare`` \ アノテーションの\ ``operator`` \ 属性に新たに追加された\ ``NOT_EQUAL`` \ の説明を追加

      * \ ``@Email`` \ アノテーションを使用する際の注意事項を追加

      ガイドラインのバグ修正

      * TERASOLUNA Server Framework for Java (5.x)の共通ライブラリのチェックルールの拡張方法の実装例を修正

  * -
    - \ :doc:`../ArchitectureInDetail/WebApplicationDetail/ExceptionHandling`\
    - 記載内容の修正

      * TERASOLUNA Server Framework for Java (5.x)の共通ライブラリ(\ ``ExceptionLoggingFilter`` \)の変更に伴う修正、及び既存の誤記の修正

  * -
    - Tilesによる画面レイアウト
    - 記載内容の修正

      * \ ``<definition>`` \ タグ(Tiles定義ファイル)の\ ``name`` \ 属性のマッチングに関する説明、及び関連する箇所の誤解を招く表現を修正

  * -
    - \ :doc:`../ArchitectureInDetail/WebServiceDetail/RestClient`\
    - Spring Framework 4.3対応に伴う修正

      * Basic認証用のリクエストヘッダの設定に関する記載を変更

  * -
    - \ :doc:`../Appendix/SOAP`\
    - 記載内容の修正

      * SOAP Web Serviceの実装に伴うインジェクションで使用するアノテーションを\ ``@Inject`` \ から\ ``@Autowired`` \ に変更
      * Spring FrameworkのJAX-WS連携機能についての誤記修正と、SOAPサーバがJava EEサーバのJAW-WS実装上で動作することに伴なう注意事項の追記

  * -
    - \ :doc:`../ArchitectureInDetail/MessagingDetail/JMS`\
    - 記載内容の修正

      * 非同期送信のトランザクション管理はChainedTransactionManagerではなくDefaultMessageListenerContainerで行うよう記述を修正

  * -
    - \ :doc:`../Security/Authentication`\
    - 記載内容の修正

      * パスワードハッシュ化のためのクラス（\ ``Pbkdf2PasswordEncoder``\ ）の説明を追記し、それに伴い\ ``BCryptPasswordEncoder``\ を推奨する記述を削除


  * -
    - \ :doc:`../Security/Authorization`\
    - Spring Framework 4.3対応に伴う修正

      * ブランクプロジェクトから\ ``mvc:path-matching`` \ の定義を削除しSpring MVCのデフォルト設定を使用するよう変更したことに伴う記載内容の修正

      記載内容の修正

      * Spring Securityでパス変数を使用するアクセスポリシーの定義に関する記載内容を修正

  * -
    - \ :doc:`../Security/XSS`\
    - 記載内容の修正、追加

      * JavaScript Escapingのサンプルソースを修正
      * \ ``document.write()`` \ を使用する際の注意事項を追加

  * -
    - OAuth(org.springframework.security.oauth)
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
    - \ :doc:`../UnitTest/index`\
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
