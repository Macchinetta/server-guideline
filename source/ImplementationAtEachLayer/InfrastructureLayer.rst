インフラストラクチャ層の実装
================================================================================

.. only:: html

 .. contents:: 目次
    :depth: 3
    :local:

インフラストラクチャ層では、\ :ref:`repository-class-label`\ を行う。

RepositoryImplは、Repositoryインタフェースで定義したメソッドの実装を行う。


.. _repository-class-label:

RepositoryImplの実装
--------------------------------------------------------------------------------

以下に、MyBatis3を使って、リレーショナルデータベース用のRepositoryを作成する方法を紹介する。

* :ref:`repository-mybatis3-label`


.. _repository-mybatis3-label:

MyBatis3を使ってRepositoryを実装
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

リレーショナルデータベースとの永続APIとしてMyBatis3を使う場合、
MyBatis3から提供されている「:ref:`DataAccessMyBatis3AppendixAboutMapperMechanism`」を利用してRepositoryインタフェースを作成すると、
基本的にはRepositoryImplを実装する必要はない。

これは、MyBatis3が、Mapperインタフェースのメソッドと呼び出すステートメント(SQL)のマッピングを自動で行う仕組みになっているためである。

MyBatis3を使用する場合、アプリケーション開発者は、

* Repositoryインタフェース(メソッドの定義)
* マッピングファイル(SQLとO/Rマッピングの定義)

の作成を行う。

| 以下に、Repositoryインタフェースとマッピングファイルの作成例を示す。
| MyBatis3の使用方法の詳細は、\ :doc:`../ArchitectureInDetail/DataAccessDetail/DataAccessMyBatis3`\ を参照されたい。

- Repositoryインタフェース(Mapperインタフェース)の作成例

 .. code-block:: java

    package com.example.domain.repository.todo;

    import com.example.domain.model.Todo;

    // (1)
    public interface TodoRepository {
        // (2)
        Todo findByTodoId(String todoId);
    }

 .. tabularcolumns:: |p{0.10\linewidth}|p{0.90\linewidth}|
 .. list-table::
    :header-rows: 1
    :widths: 10 90

    * - 項番
      - 説明
    * - | (1)
      - POJOのインタフェースとして作成する。

        MyBatis3のインタフェースやアノテーションなどを指定する必要はない。
    * - | (2)
      - Repositoryのメソッドを定義する。

        基本的には、MyBatis3のアノテーションを付与する必要はないが、
        一部のケースでアノテーションを指定する事もある。


- マッピングファイルの作成例

 .. code-block:: xml

    <?xml version="1.0" encoding="UTF-8"?>
    <!DOCTYPE mapper PUBLIC "-//mybatis.org/DTD Mapper 3.0//EN"
        "http://mybatis.org/dtd/mybatis-3-mapper.dtd">
    <!-- (3) -->
    <mapper namespace="com.example.domain.repository.todo.TodoRepository">

        <!-- (4) -->
        <select id="findByTodoId" parameterType="string" resultMap="todoResultMap">
          SELECT
              todo_id,
              title,
              finished
          FROM
              t_todo
          WHERE
              todo_id = #{todoId}
        </select>

        <!-- (5) -->
        <resultMap id="todoResultMap" type="Todo">
            <result column="todo_id" property="todoId" />
            <result column="title" property="title" />
            <result column="finished" property="finished" />
        </resultMap>

    </mapper>


 .. tabularcolumns:: |p{0.10\linewidth}|p{0.90\linewidth}|
 .. list-table::
    :header-rows: 1
    :widths: 10 90

    * - 項番
      - 説明
    * - | (3)
      - Repositoryインタフェース毎にマッピングファイルを作成する。

        マッピングファイルのネームスペース(\ ``mapper``\ 要素の\ ``namespace``\ 属性)には、
        RepositoryインタフェースのFQCN(Fully Qualified Class Name)を指定する。
    * - | (4)
      - Repositoryインタフェースに定義したメソッド毎に実行するステートメント(SQL)の定義を行う。

        ステートメントID(各ステートメント要素(\ ``select``\/\ ``insert``\/\ ``update``\/\ ``delete``\ 要素の\ ``id``\ 属性)には、
        Repositoryインタフェースのメソッド名を指定する。
    * - | (5)
      - クエリを発行する場合は、必要に応じてO/Rマッピングの定義を行う。

        シンプルなO/Rマッピングであれば自動マッピングを利用する事ができるが、複雑なO/Rマッピングを行う場合は、
        個別にマッピングの定義が必要となる。

        上記例のマッピング定義は、シンプルなO/Rマッピングなので自動マッピングを利用する事もできる。



.. raw:: latex

   \newpage

