release = '1.11.1.RELEASE'
gfw_version = '5.10.1.RELEASE'
terasoluna_dependencies_version = '2.0.1'
terasoluna_dependencies_release_version = terasoluna_dependencies_version + '.RELEASE'
atrs_version='1.11.1.RELEASE'
framework_name = 'Macchinetta Server Framework (1.x)'

# Spring系
boot_version = '3.5.9'
boot_major_minor_version = ".".join(boot_version.split('.')[:2])
spring_version = '6.2.15'
spring_major_minor_version = ".".join(spring_version.split('.')[:2])
spring_data_version = '3.5.7'
spring_data_major_minor_version = ".".join(spring_data_version.split('.')[:2])
spring_security_version = '6.5.7'
spring_security_major_minor_version = ".".join(spring_security_version.split('.')[:2])


# Spring Boot Dependenciesで管理されているもの
jakarta_inject_version = '2.0.1'
aspectj_version = '1.9.25.1'
logback_version = '1.5.22'
slf4j_version = '2.0.17'
commons_lang3_version = '3.17.0'
jackson_databind_version = '2.19.4'
artemis_version = '2.40.0'
commons_dbcp_version = '2.13.0'
jakarta_mail_version = '2.0.5'
lombok_version = '1.18.42'
glassfish_jstl_version = '3.0.1'
reactor_core_version = '3.7.14'
reactor_netty_version = '1.2.13'
junit_version = '4.13.2'
hamcrest_version = '3.0'
mockito_version = '5.17.0'

## hibernate_orm_version = '6.6.39.Final'
hibernate_orm_major_version = '6'
hibernate_orm_minor_version = '6'
hibernate_orm_maintenance_version = '39'
hibernate_orm_version = hibernate_orm_major_version + '.' + hibernate_orm_minor_version + '.' + hibernate_orm_maintenance_version + '.Final'
hibernate_orm_major_minor_version = hibernate_orm_major_version + '.' + hibernate_orm_minor_version

# hibernate_validator_version = '8.0.3.Final'
hibernate_validator_major_version = '8'
hibernate_validator_minor_version = '0'
hibernate_validator_maintenance_version = '3'
hibernate_validator_version = hibernate_validator_major_version + '.' + hibernate_validator_minor_version + '.' + hibernate_validator_maintenance_version + '.Final'
hibernate_validator_major_minor_version = hibernate_validator_major_version + '.' + hibernate_validator_minor_version

# thymeleaf_version = '3.1.3.RELEASE'
thymeleaf_major_version = '3'
thymeleaf_minor_version = '1'
thymeleaf_maintenance_version = '3'
thymeleaf_version = thymeleaf_major_version + '.' + thymeleaf_minor_version + '.' + thymeleaf_maintenance_version + '.RELEASE'

## httpclient_version = '5.5.1'
httpclient_major_version = '5'
httpclient_minor_version = '5'
httpclient_maintenance_version = '1'
httpclient_version = httpclient_major_version + '.' + httpclient_minor_version + '.' + httpclient_maintenance_version

## httpcore_version = '5.3.6'
httpcore_major_version = '5'
httpcore_minor_version = '3'
httpcore_maintenance_version = '6'
# 過去のJavadocのリンクがなくなり、中途半端なURL形式でリダイレクトされるようになったため、currentで固定する。（Apache側で対応が入ったら再度戻す）
# httpcore_version = httpcore_major_version + '.' + httpcore_minor_version + '.' + httpcore_maintenance_version
httpcore_version = 'current'

# Spring Boot Dependenciesで管理されているもの
## 一部のバージョンのみが欲しいもの（フルバージョンも欲しい場合はmajor/minor/maintenanceに分けてください）
jstl_version = '3.0'
jakarta_persistence_version = '3.1'
jakarta_validation_version = '3.0'
jakarta_mail_api_version = '2.1'
jakarta_messaging_version = '3.1' # jakarta.jms
jakarta_servlet_version = '6.0'
jakarta_xml_ws_version = '4.0'
jetty_major_version = '12'

# Spring Boot Dependenciesで管理されているもの以外
mybatis_version = '3.5.19'
mybatis_major_minor_version = ".".join(mybatis_version.split('.')[:2])
mybatis_spring_version = '3.0.5'
commons_beanutils_version = '1.11.0'
java_time_jsptags_version = '2.0.2'
openpdf_version = '2.0.5'
poi_version = '5.4.1'
guava_version = '33.5.0-jre'
commons_collections_version = '4.5.0'
commons_io_version = '2.20.0'
dbunit_version = '2.8.0'
spring_test_dbunit_version = '1.3.0'
sts_version = '5.0.0.RELEASE'
maven_version = '3.9.9'
chrome_version = '145'
talend_api_tester_version = '25.16.0'

## tomcat_version = '10.1.50'
tomcat_major_version = '10'
tomcat_minor_version = '1'
tomcat_maintenance_version = '50'
tomcat_version = tomcat_major_version + '.' + tomcat_minor_version + '.' + tomcat_maintenance_version

## mapstruct_version = '1.6.3'
mapstruct_major_version = '1'
mapstruct_minor_version = '6'
mapstruct_maintenance_version = '3'
mapstruct_version = mapstruct_major_version + '.' + mapstruct_minor_version + '.' + mapstruct_maintenance_version

## postgresql_version = '18.1'
postgresql_major_version = '18'
postgresql_minor_version = '1'
postgresql_version = postgresql_major_version + '.' + postgresql_minor_version

# Spring Boot Dependenciesで管理されているもの以外
## 一部のバージョンのみが欲しいもの（フルバージョンも欲しい場合はmajor/minor/maintenanceに分けてください）
jakarta_pages_version = '3.1' # jakarta.servlet.jsp
jakarta_platform_version = '10' # Jakarta EE Version
jboss_version = '7.4'
redhat_fuse_version = '6.0'
log4j_adaptor_version = '2.3'


# rstファイル内のバージョン表記を置換する。
rst_epilog = f"""
.. |release| replace:: {release}
.. |gfw_version| replace:: {gfw_version}
.. |spring_version| replace:: {spring_version}
.. |spring_major_minor_version| replace:: {spring_major_minor_version}
.. |spring_data_version| replace:: {spring_data_version}
.. |boot_version| replace:: {boot_version}
.. |spring_security_version| replace:: {spring_security_version}
.. |spring_security_major_minor_version| replace:: {spring_security_major_minor_version}
.. |mybatis_version| replace:: {mybatis_version}
.. |mybatis_major_minor_version| replace:: {mybatis_major_minor_version}
.. |mybatis_spring_version| replace:: {mybatis_spring_version}
.. |jakarta_inject_version| replace:: {jakarta_inject_version}
.. |aspectj_version| replace:: {aspectj_version}
.. |logback_version| replace:: {logback_version}
.. |slf4j_version| replace:: {slf4j_version}
.. |jackson_databind_version| replace:: {jackson_databind_version}
.. |thymeleaf_version| replace:: {thymeleaf_version}
.. |hibernate_validator_version| replace:: {hibernate_validator_version}
.. |httpclient_version| replace:: {httpclient_version}
.. |hibernate_orm_version| replace:: {hibernate_orm_version}
.. |commons_beanutils_version| replace:: {commons_beanutils_version}
.. |commons_lang3_version| replace:: {commons_lang3_version}
.. |mapstruct_version| replace:: {mapstruct_version}
.. |java_time_jsptags_version| replace:: {java_time_jsptags_version}
.. |commons_dbcp_version| replace:: {commons_dbcp_version}
.. |openpdf_version| replace:: {openpdf_version}
.. |poi_version| replace:: {poi_version}
.. |jakarta_mail_version| replace:: {jakarta_mail_version}
.. |guava_version| replace:: {guava_version}
.. |commons_collections_version| replace:: {commons_collections_version}
.. |commons_io_version| replace:: {commons_io_version}
.. |glassfish_jstl_version| replace:: {glassfish_jstl_version}
.. |lombok_version| replace:: {lombok_version}
.. |junit_version| replace:: {junit_version}
.. |hamcrest_version| replace:: {hamcrest_version}
.. |mockito_version| replace:: {mockito_version}
.. |dbunit_version| replace:: {dbunit_version}
.. |spring_test_dbunit_version| replace:: {spring_test_dbunit_version}
.. |sts_version| replace:: {sts_version}
.. |maven_version| replace:: {maven_version}
.. |chrome_version| replace:: {chrome_version}
.. |tomcat_version| replace:: {tomcat_version}
.. |tomcat_major_version| replace:: {tomcat_major_version}
.. |tomcat_minor_version| replace:: {tomcat_minor_version}
.. |postgresql_version| replace:: {postgresql_version}
.. |talend_api_tester_version| replace:: {talend_api_tester_version}
.. |jetty_major_version| replace:: {jetty_major_version}
.. |framework_name| replace:: {framework_name}
.. |jakarta_persistence_version| replace:: {jakarta_persistence_version}
.. |hibernate_orm_major_minor_version| replace:: {hibernate_orm_major_minor_version}
.. |hibernate_validator_major_minor_version| replace:: {hibernate_validator_major_minor_version}
.. |jakarta_validation_version| replace:: {jakarta_validation_version}
"""

extlinks = {
    # Macchinetta
    'url_single_blank': (f'https://github.com/Macchinetta/macchinetta-web-blank/tree/{release}' + f'%s', None),
    'url_multi_blank': (f'https://github.com/Macchinetta/macchinetta-web-multi-blank/tree/{release}' + f'%s', None),
    'url_tutorial': (f'https://github.com/Macchinetta/tutorial-apps/tree/{release}' + f'%s', None),
    'url_macchinetta_guideline_issues': (f'https://github.com/Macchinetta/server-guideline/issues' + f'%s', None),
    'url_atrs': (f'https://github.com/Macchinetta/atrs-thymeleaf/tree/{atrs_version}' + f'%s', None),
    'url_tested_environment': (f'https://github.com/Macchinetta/spring-functionaltest/wiki/Tested-Environment' + f'%s', None),
    # terasoluna
    'url_terasolunaorg': (f'https://github.com/terasolunaorg' + f'%s', None),
    'url_gfw': (f'https://github.com/terasolunaorg/terasoluna-gfw/tree/{gfw_version}' + f'%s', None),
    'url_gfw_issues': (f'https://github.com/terasolunaorg/terasoluna-gfw/issues' + f'%s', None),
    'url_gfw_func': (f'https://github.com/terasolunaorg/terasoluna-gfw-functionaltest/tree/{gfw_version}' + f'%s', None),
    'url_terasoluna_dependencies': (f'https://github.com/terasolunaorg/terasoluna-dependencies/tree/{terasoluna_dependencies_release_version}' + f'%s', None),
    'url_migrationguide': (f'https://github.com/terasolunaorg/terasoluna-gfw/wiki/Migration-Guide-%s_ja#step-1-update-dependency-libraries', None),
    'url_terasoluna_dependencies_wiki': (f'https://github.com/terasolunaorg/terasoluna-dependencies/wiki/{terasoluna_dependencies_version}' + f'%s', None),
    'url_terasoluna_guideline': (f'http://terasolunaorg.github.io/guideline' + f'%s', None),
    # tutorial
    'url_session_tutorial': (f'http://localhost:8080/%s/loginForm', None),
    'url_todo_api': (f'http://localhost:8080/todo/api/v1' + f'%s', None),
    'url_localhost': (f'http://localhost:8080' + f'%s', None),
    # spring
    'url_spring_io': (f'https://spring.io' + f'%s', None),
    'url_spring_reference': (f'https://docs.spring.io/spring-framework/reference/{spring_major_minor_version}' + f'%s', None),
    'url_spring_javadoc': (f'https://docs.spring.io/spring-framework/docs/{spring_version}/javadoc-api' + f'%s', None),
    'url_spring_github': (f'https://github.com/spring-projects/spring-framework/blob/v{spring_version}' + f'%s', None),
    'url_spring_framework_issues': (f'https://github.com/spring-projects/spring-framework/issues' + f'%s', None),
    'url_spring_data_reference': (f'https://docs.spring.io/spring-data/commons/reference/{spring_data_major_minor_version}/repositories' + f'%s', None),
    'url_spring_data_jpa': (f'https://docs.spring.io/spring-data/jpa/reference/{spring_data_major_minor_version}/repositories' + f'%s', None),
    'url_spring_boot_reference': (f'https://docs.spring.io/spring-boot/{boot_major_minor_version}' + f'%s', None),
    'url_spring_security_site': (f'https://docs.spring.io/spring-security/site/docs/{spring_security_version}/api/org/springframework/security' + f'%s', None),
    'url_spring_security_reference': (f'https://docs.spring.io/spring-security/reference' + f'%s', None),
    'url_spring_security_issues': (f'https://github.com/spring-projects/spring-security/issues' + f'%s', None),
    'url_sts_github': (f'https://github.com/spring-projects/spring-tools/wiki/Previous-Versions' + f'%s', None),
    'url_spring_projects': (f'https://github.com/spring-projects' + f'%s', None),
    # 参考書籍
    'url_gihyo_spring3': (f'https://gihyo.jp/book/2012/978-4-7741-5380-3' + f'%s', None),
    'url_shoeisha': (f'https://www.shoeisha.co.jp/book/detail' + f'%s', None),
    'url_apress': (f'https://link.springer.com/book/10.1007' + f'%s', None),
    'url_manning': (f'https://www.manning.com/books' + f'%s', None),
    'url_oreilly_spring_data': (f'https://www.oreilly.com/library/view/spring-data/9781449331863' + f'%s', None),
    # apache
    'url_tomcat': (f'https://tomcat.apache.org/tomcat-{tomcat_major_version}.{tomcat_minor_version}-doc' + f'%s', None),
    'url_maven': (f'https://maven.apache.org' + f'%s', None),
    'url_maven_central': (f'https://search.maven.org' + f'%s', None),
    'url_tomee_javadoc': (f'https://tomee.apache.org/jakartaee-10.0/javadoc/jakarta' + f'%s', None),
    'url_commons_dbcp': (f'https://commons.apache.org/proper/commons-dbcp' + f'%s', None),
    'url_artemis': (f'https://activemq.apache.org/components/artemis/documentation/{artemis_version}' + f'%s', None),
    'url_sonatype': (f'https://www.sonatype.com/products' + f'%s', None),
    'url_freemarker': (f'https://freemarker.apache.org' + f'%s', None),
    'url_http_client_home': (f'https://hc.apache.org/httpcomponents-client-{httpclient_major_version}.{httpclient_minor_version}.x' + f'%s', None),
    # 5.5.1のAPIドキュメントが削除されてしまっているので、5.5.2を設定
    'url_http_client': (f'https://hc.apache.org/components/httpcomponents-client-{httpclient_major_version}.{httpclient_minor_version}.x/5.5.2/httpclient5/apidocs' + f'%s', None),
    'url_http_client_javadoc': (f'https://javadoc.io/static/org.apache.httpcomponents.client5/httpclient5/{httpclient_version}/org/apache/hc/client5/http' + f'%s', None),
    'url_http_core': (f'https://hc.apache.org/httpcomponents-core-{httpcore_major_version}.{httpcore_minor_version}.x/{httpcore_version}/httpcore5/apidocs/org/apache/hc/core5' + f'%s', None),
    'url_sonatype_maven': (f'https://help.sonatype.com/en/maven-repositories.html#configuring-apache-maven' + f'%s', None),
    'url_apache_poi': (f'https://poi.apache.org' + f'%s', None),
    'url_apache_cxf': (f'https://cxf.apache.org' + f'%s', None),
    'url_cxf_jaxws': (f'https://cwiki.apache.org/confluence/display/CXF20DOC/JAX-WS+Configuration' + f'%s', None),
    'url_tiles': (f'https://tiles.apache.org/framework/index.html' + f'%s', None),
    'url_log4j': (f'https://logging.apache.org/log4j/2.x' + f'%s', None),
    'url_log4j_adaptor': (f'https://logging.apache.org/log4j/{log4j_adaptor_version}.x/log4j-to-slf4j/index.html' + f'%s', None),
    # other
    'url_javase17': (f'https://docs.oracle.com/en/java/javase/17' + f'%s', None),
    'url_serviceloader': (f'https://docs.oracle.com/javase/8/docs/api/java/util/ServiceLoader.html' + f'%s', None),
    'url_java8_security': (f'https://docs.oracle.com/javase/jp/8/docs/technotes/guides/security/enhancements-8.html' + f'%s', None),
    'url_mybatis3': (f'https://mybatis.org/mybatis-3' + f'%s', None),
    'url_mybatis_spring': (f'https://mybatis.org/spring/index.html' + f'%s', None),
    'url_thymeleaf': (f'https://www.thymeleaf.org' + f'%s', None),
    'url_abstractattributetagprocessor': (f'https://www.thymeleaf.org/apidocs/thymeleaf/{thymeleaf_version}/org/thymeleaf/processor/element/AbstractAttributeTagProcessor.html' + f'%s', None),
    'url_thymeleaf_tutorial': (f'https://www.thymeleaf.org/doc/tutorials/{thymeleaf_major_version}.{thymeleaf_minor_version}' + f'%s', None),
    'url_thymeleaf_articles': (f'https://www.thymeleaf.org/doc/articles/' + f'%s', None),
    'url_jakarta_tag': (f'https://jakarta.ee/specifications/tags/{jstl_version}/jakarta-tags-spec-{jstl_version}.html' + f'%s', None),
    'url_jakarta_persistence': (f'https://jakarta.ee/specifications/persistence/{jakarta_persistence_version}/jakarta-persistence-spec-{jakarta_persistence_version}.html' + f'%s', None),
    'url_jakarta_validation': (f'https://jakarta.ee/specifications/bean-validation/{jakarta_validation_version}/jakarta-bean-validation-spec-{jakarta_validation_version}.html' + f'%s', None),
    'url_jakarta_mail_apidocs': (f'https://jakarta.ee/specifications/mail/{jakarta_mail_api_version}/apidocs/jakarta.mail/jakarta/mail' + f'%s', None),
    'url_jakarta_mail_spec': (f'https://jakarta.ee/specifications/mail/{jakarta_mail_api_version}/jakarta-mail-spec-{jakarta_mail_api_version}.html' + f'%s', None),
    'url_jakarta_messaging_apidocs': (f'https://jakarta.ee/specifications/messaging/{jakarta_messaging_version}/apidocs/jakarta.messaging/jakarta/jms' + f'%s', None),
    'url_jakarta_messaging_spec': (f'https://jakarta.ee/specifications/messaging/{jakarta_messaging_version}/jakarta-messaging-spec-{jakarta_messaging_version}.html' + f'%s', None),
    'url_jakarta_pages': (f'https://jakarta.ee/specifications/pages/{jakarta_pages_version}/jakarta-server-pages-spec-{jakarta_pages_version}.html' + f'%s', None),
    'url_jakarta_validation_apidocs': (f'https://jakarta.ee/specifications/platform/{jakarta_platform_version}/apidocs/jakarta' + f'%s', None),
    'url_jakarta_xml_ws': (f'https://jakarta.ee/specifications/xml-web-services/{jakarta_xml_ws_version}/jakarta-xml-ws-spec-{jakarta_xml_ws_version}' + f'%s', None),
    'url_jakarta_servlet': (f'https://jakarta.ee/specifications/servlet/{jakarta_servlet_version}/jakarta-servlet-spec-{jakarta_servlet_version}.html' + f'%s', None),
    'url_hibernate_orm': (f'https://docs.hibernate.org/orm/{hibernate_orm_major_version}.{hibernate_orm_minor_version}' + f'%s', None),
    'url_hibernate_validator': (f'https://docs.hibernate.org/validator/{hibernate_validator_major_version}.{hibernate_validator_minor_version}' + f'%s', None),
    'url_hibernate_validator_github': (f'https://github.com/hibernate/hibernate-validator/tree/{hibernate_validator_version}/engine/src/main/resources/org/hibernate/validator' + f'%s', None),
    'url_hibernate_validator_bug': (f'https://hibernate.atlassian.net/browse/HV-881' + f'%s', None),
    'url_postgresql': (f'https://www.postgresql.org/docs/{postgresql_major_version}' + f'%s', None),
    'url_mapstruct': (f'https://mapstruct.org' + f'%s', None),
    'url_mapstruct_document': (f'https://mapstruct.org/documentation/{mapstruct_major_version}.{mapstruct_minor_version}' + f'%s', None),
    'url_lombok': (f'https://projectlombok.org' + f'%s', None),
    'url_owasp': (f'https://owasp.org' + f'%s', None),
    'url_owasp_project_top10': (f'https://owasp.org/www-project-top-ten' + f'%s', None),
    'url_owasp_community': (f'https://owasp.org/www-community' + f'%s', None),
    'url_owasp_top10': (f'https://owasp.org/Top10' + f'%s', None),
    'url_owasp_header': (f'https://owasp.org/www-project-secure-headers' + f'%s', None),
    'url_owasp_cheatsheets': (f'https://cheatsheetseries.owasp.org/cheatsheets' + f'%s', None),
    'url_cve': (f'https://cve.mitre.org/cgi-bin/cvename.cgi' + f'%s', None),
    'url_jackson_javadoc': (f'https://javadoc.io/doc/com.fasterxml.jackson.core/jackson-databind/{jackson_databind_version}/com/fasterxml/jackson/databind' + f'%s', None),
    'url_jackson_github': (f'https://github.com/FasterXML/jackson' + f'%s', None),
    'url_jacksonviews': (f'https://www.baeldung.com/jackson-json-view-annotation' + f'%s', None),
    'url_reactor_javadoc': (f'https://javadoc.io/static/io.projectreactor/reactor-core/{reactor_core_version}/reactor/core/publisher' + f'%s', None),
    'url_reactor_reference': (f'https://projectreactor.io/docs/netty/{reactor_netty_version}/reference' + f'%s', None),
    'url_rfc': (f'https://datatracker.ietf.org/doc/html' + f'%s', None),
    'url_selenium': (f'https://www.selenium.dev' + f'%s', None),
    'url_slf4j': (f'https://www.slf4j.org' + f'%s', None),
    'url_redhat_hibernate': (f'https://access.redhat.com/documentation/en-us/red_hat_jboss_enterprise_application_platform/{jboss_version}/html/developing_hibernate_applications/reference_material' + f'%s', None),
    'url_javatime_jsptags': (f'https://github.com/sargue/java-time-jsptags#java-8-javatime-jsp-tags' + f'%s', None),
    'url_thymeleaf_github': (f'https://github.com/thymeleaf' + f'%s', None),
    'url_WebEngineContext': (f'https://github.com/thymeleaf/thymeleaf/blob/thymeleaf-{thymeleaf_version}/lib/thymeleaf/src/main/java/org/thymeleaf/context/WebEngineContext.java#L525-L532' + f'%s', None),
    'url_angus_mail': (f'https://eclipse-ee4j.github.io/angus-mail' + f'%s', None),
    'url_passay': (f'https://www.passay.org' + f'%s', None),
    'url_chrome': (f'https://www.google.co.jp/chrome' + f'%s', None),
    'url_martinfowler': (f'https://martinfowler.com' + f'%s', None),
    'url_mojohaus': (f'https://www.mojohaus.org' + f'%s', None),
    'url_w3c': (f'https://www.w3.org/TR' + f'%s', None),
    'url_ietf_rfc': (f'https://www.ietf.org/rfc' + f'%s', None),
    'url_redhat_openjdk': (f'https://developers.redhat.com/products/openjdk/download' + f'%s', None),
    'url_mockito': (f'https://site.mockito.org' + f'%s', None),
    'url_mockito_javadoc': (f'https://javadoc.io/doc/org.mockito/mockito-core/{mockito_version}/org.mockito/org/mockito' + f'%s', None),
    'url_junit4': (f'https://junit.org/junit4' + f'%s', None),
    'url_hamcrest': (f'https://hamcrest.org/JavaHamcrest' + f'%s', None),
    'url_dbunit': (f'https://dbunit.sourceforge.net' + f'%s', None),
    'url_spring_test': (f'https://springtestdbunit.github.io/spring-test-dbunit' + f'%s', None),
    'url_talend_api_tester': (f'https://chrome.google.com/webstore/detail/talend-api-tester-free-ed/aejoelaoggembcahagimdiliamlcdmfm' + f'%s', None),
    'url_db2_insert': (f'https://www.ibm.com/docs/en/db2/latest?topic=statements-insert' + f'%s', None),
    'url_mysql_insert': (f'https://dev.mysql.com/doc/refman/en/insert.html' + f'%s', None),
    'url_xml_namespace_mapping': (f'https://access.redhat.com/documentation/en-us/red_hat_jboss_fuse/{redhat_fuse_version}/html/developing_applications_using_jax-ws/jaxwsdatanamespacemapping' + f'%s', None),
    'url_mockito_github': (f'https://github.com/mockito/mockito' + f'%s', None),
    'url_jdk11_note': (f'https://www.oracle.com/java/technologies/javase/11-relnote-issues.html#JDK-8145252' + f'%s', None),
    'url_oracle_grants': (f'https://docs.oracle.com/en/database/oracle/oracle-database/23/sqlrf/GRANT.html#GUID-20B4E2C0-A7F8-4BC8-A5E8-BE61BDC41AC3' + f'%s', None),
    'url_jep252': (f'https://openjdk.org/jeps/252' + f'%s', None),
    'url_jodatime_interval': (f'https://www.joda.org/joda-time/apidocs/org/joda/time/Interval.html' + f'%s', None),
    'url_openpdf': (f'https://github.com/LibrePDF/OpenPDF' + f'%s', None),
    'url_threeten_extra': (f'https://www.threeten.org/threeten-extra' + f'%s', None),
    'url_greenmail': (f'https://greenmail-mail-test.github.io/greenmail' + f'%s', None),
    'url_distributed_transaction': (f'https://www.infoworld.com/article/2077963/distributed-transactions-in-spring-with-and-without-xa.html' + f'%s', None),
    'url_best_effort_1_phase_commit': (f'https://gharshangupta.blogspot.com/2015/03/spring-distributed-transactions-using_2.html' + f'%s', None),
    'url_ie_error': (f'https://docs.microsoft.com/ja-jp/archive/blogs/ieinternals/friendly-http-error-pages' + f'%s', None),
    'url_bootstrap': (f'https://getbootstrap.com' + f'%s', None),
    'url_bluetrip': (f'https://github.com/crittermike/bluetrip' + f'%s', None),
    'url_square_okhttp': (f'https://square.github.io/okhttp' + f'%s', None),
    'url_jaxws_timeoutkey': (f'https://github.com/javaee/metro-jax-ws/issues/1166' + f'%s', None),
    'url_rich_domain_model': (f'https://www.dddcommunity.org' + f'%s', None),
    'url_bean_validation': (f'https://jcp.org/en/jsr/detail?id=349' + f'%s', None),
    'url_fips': (f'https://www.nist.gov/federal-information-standards-fips' + f'%s', None),
    'url_linux_openssl': (f'https://www.openssl.org/source' + f'%s', None),
    'url_windows_openssl': (f'https://slproweb.com/products/Win32OpenSSL.html' + f'%s', None),
    'url_caniuse': (f'https://caniuse.com/stricttransportsecurity' + f'%s', None),
    'url_hstspreload': (f'https://hstspreload.org' + f'%s', None),
    'url_soumu_password': (f'https://www.soumu.go.jp/main_sosiki/cybersecurity/kokumin/security/business/staff/06' + f'%s', None),
    'url_nist_password': (f'https://pages.nist.gov/800-63-3/sp800-63b.html' + f'%s', None),
    'url_logback': (f'https://logback.qos.ch' + f'%s', None),
    'url_spring_security_rsa': (f'https://github.com/dsyer/spring-security-rsa' + f'%s', None),
    'url_ltsv': (f'http://ltsv.org' + f'%s', None),
    'url_horizontal_bar': (f'https://www.unicode.org/Public/MAPPINGS/OBSOLETE/EASTASIA/JIS/JIS0208.TXT' + f'%s', None),
    'url_jetty': (f'https://jetty.org/docs/jetty/{jetty_major_version}' + f'%s', None),
    }