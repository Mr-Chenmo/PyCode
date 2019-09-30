# ��˿
���ķ�����[The Flask Mega-Tutorial Part VIII: Followers](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-viii-followers)

����Flask Mega-Tutorialϵ�еĵڰ˲��֣��ҽ����������ʵ��������Twitter�������罻����ġ���˿�����ܡ�

�ڱ����У��ҽ������ʹ��Ӧ�õ����ݿ⡣ ��ϣ��Ӧ�õ��û��ܹ����ɱ�ݵع�ע�����û��� ������Ҫ��չ���ݿ⣬�Ա����˭��ע��˭������������Ҫ�ѵöࡣ

*���µ�GitHub����Ϊ��[Browse](https://github.com/miguelgrinberg/microblog/tree/v0.8),?[Zip](https://github.com/miguelgrinberg/microblog/archive/v0.8.zip),?[Diff](https://github.com/miguelgrinberg/microblog/compare/v0.7...v0.8).*

## ����������ݿ��ϵ

������˵��������Ϊÿ���û�ά��һ������˿���û��б�͡���ע���û��б� ���ҵ��ǣ���ϵ�����ݿ�û���б����͵��ֶ����������ǣ���ôֻ��ͨ����������ֶκ�����֮��Ĺ�ϵ��ʵ�֡�

���ݿ�����һ�������û��ı�����ʣ�µľ��������ȷ����֯����֮��Ĺ�ע�뱻��ע�Ĺ�ϵ�� �����ǻع˻������ݿ��ϵ���͵ĺ�ʱ����

### һ�Զ�

���Ѿ���[������](https://github.com/luhuisicnu/The-Flask-Mega-Tutorial-zh/blob/master/docs/%e7%ac%ac%e5%9b%9b%e7%ab%a0%ef%bc%9a%e6%95%b0%e6%8d%ae%e5%ba%93.md)���ù���һ�Զ��ϵ�����Ǹù�ϵ��ʾ��ͼ������ע��ʵ�ʱ����ֱ�Ϊuser��post����

![һ�Զ��ϵ](https://camo.githubusercontent.com/24953a3d07267864e9437dbbb499e310d0a57d1a/687474703a2f2f75706c6f61642d696d616765732e6a69616e7368752e696f2f75706c6f61645f696d616765732f343936313532382d373839623732656339353232383331352e706e673f696d6167654d6f6772322f6175746f2d6f7269656e742f7374726970253743696d61676556696577322f322f772f31323430)

�û����û���̬ͨ�������ϵ�����������У�һ���û�ӵ��*��*���û���̬����һ���û���̬����*һ*���û������ߣ������ݿ���*��*���ⷽʹ����һ��*���*�Ա�ʾһ�Զ��ϵ���������һ�Զ��ϵ�У������`post`���`user_id`�ֶΣ�����ֶν��û���ÿ����̬���������߹�����������

�����ԣ�`user_id`�ֶ��ṩ��ֱ�ӷ��ʸ����û���̬�����ߣ����Ƿ����أ� ͸������ϵ�������ͨ���������û���������û���̬���б�`post`���е�`user_id`�ֶ�Ҳ���Իش�������⣬���ݿ�������������Խ��и�Ч�Ĳ�ѯ����������user_id�ֶε���X���û���̬����

### ��Զ�

��Զ��ϵ����Ӹ��ӣ��ٸ����ӣ����ݿ�����`students`���`teachers`��һ��ѧ��ѧϰ*��*λ��ʦ�Ŀγ̣�һλ��ʦ����*��*��ѧ��������������ص���һ�Զ��ϵ��

�����������͵Ĺ�ϵ������Ҫ�ܹ���ѯ���ݿ�����ȡ���ڸ���ѧ���Ľ�ʦ���б��Լ�ĳ����ʦ�γ��е�ѧ�����б� ��Ҫ�ڹ�ϵ�����ݿ������������Ĺ�ϵ�������׶��٣���Ϊ�޷�ͨ�������б�����������ɴ˲�����

չ�ֶ�Զ��ϵ��Ҫʹ�ö����*������*�����������ݿ���β���ѧ���ͽ�ʦ��ʾ����

![��Զ�](https://camo.githubusercontent.com/2dfb55edbdeafd45b017b60469dc32652a3b6033/687474703a2f2f75706c6f61642d696d616765732e6a69616e7368752e696f2f75706c6f61645f696d616765732f343936313532382d616337653665613634313331626331362e706e673f696d6167654d6f6772322f6175746f2d6f7269656e742f7374726970253743696d61676556696577322f322f772f31323430)

��Ȼ����������������ԣ���������������Ĺ������ȷ�ܹ���Ч�ػش����ж�Զ��ϵ�Ĳ�ѯ��

### ���һ��һ��һ

���һ��ϵ������һ�Զ��ϵ�� ��ͬ���ǣ����ֹ�ϵ�Ǵӡ��ࡱ�ĽǶ������ġ�

һ��һ�Ĺ�ϵ��һ�Զ�������� ʵ�������Ƶģ�����һ��Լ������ӵ����ݿ⣬�Է�ֹ���ࡱһ���ж�����ӡ� ��Ȼ���������͵Ĺ�ϵ�����õģ�������������������ô�ձ顣

>����ע�������������Ȥ��Ҳ���Կ�����д��һƪ���Ƶ����ݿ��ϵ���¡���[Web�����г��õ����ݹ�ϵ](https://www.jianshu.com/p/07c1d309f037)

## ʵ�ַ�˿����

�鿴���й�ϵ���͵ĸ�Ҫ��������ȷ��ά����˿��ϵ����ȷ����ģ���Ƕ�Զ��ϵ����Ϊ�û����Թ�ע*��*�������û��������û�����ӵ��*��*����˿�� ��������ѧ������ʦ�������У���Զ��ϵ����������ʵ�塣 ���ڷ�˿��ϵ�У��û���ע�����û���ֻ��һ���û�ʵ�塣 ��ô����Զ��ϵ�ĵڶ���ʵ����ʲô�أ�

�ù�ϵ�ĵڶ���ʵ��Ҳ���û��� һ�����ʵ����������ͬһ���������ʵ���Ĺ�ϵ����Ϊ*�����ù�ϵ*�������������������õ��ġ�

ʹ�������ö�Զ��ϵ��ʵ�ַ�˿���Ƶı�ṹʾ��ͼ��

![��Զ�](https://camo.githubusercontent.com/42f706333b5e7f3a082409b6f5aa07cace67d294/687474703a2f2f75706c6f61642d696d616765732e6a69616e7368752e696f2f75706c6f61645f696d616765732f343936313532382d303032383264306465633030643131632e706e673f696d6167654d6f6772322f6175746f2d6f7269656e742f7374726970253743696d61676556696577322f322f772f31323430)

`followers`���ǹ�ϵ�Ĺ����� �˱��е������ָ���û����е������У���Ϊ�����û��������û��� �ñ��е�ÿ����¼�����ע�ߺͱ���ע�ߵ�һ����ϵ�� ��ѧ������ʦ������һ����������������������ݿ�ش����й��ڹ�ע�ͱ���ע�����⣬�����㹻�ɾ����䡣

## ���ݿ�ģ�͵�ʵ��

���ȣ������������ݿ�����ӷ�˿���ưɡ�����`followers`������
```
followers = db.Table('followers',
    db.Column('follower_id', db.Integer, db.ForeignKey('user.id')),
    db.Column('followed_id', db.Integer, db.ForeignKey('user.id'))
)
```

������ͼ�й������ֱ�ӷ��롣 ��ע�⣬��û������Ϊ�û����û���̬��������������������Ϊģ�͡� ��Ϊ����һ���������û���������ݵĸ����������Ҵ�������ʱ��û�й�����ģ���ࡣ

�����ҿ������û�����������Զ�Ĺ�ϵ�ˣ�
```
class User(UserMixin, db.Model):
    # ...
    followed = db.relationship(
        'User', secondary=followers,
        primaryjoin=(followers.c.follower_id == id),
        secondaryjoin=(followers.c.followed_id == id),
        backref=db.backref('followers', lazy='dynamic'), lazy='dynamic')
```

������ϵ�Ĺ���ʵ�����ס� ������Ϊ`post`һ�Զ��ϵ��������������ʹ��`db.relationship`����������ģ�����еĹ�ϵ�� ���ֹ�ϵ��`User`ʵ������������`User`ʵ�������԰��չ���������ͨ�����ֹ�ϵ������һ���û���˵������û���ע�Ҳ��û��� ���������û��ж�����`followed`�Ĺ�ϵ����Ϊ���Ҵ�����ѯ�����ϵʱ���ҽ��õ��ѹ�ע���û��б����Ҳ���б��� ���������������`db.relationship()`���еĲ�����

*   `'User'`�ǹ�ϵ���е��Ҳ�ʵ�壨�����ʵ�忴�����ϼ��ࣩ���������������ù�ϵ�������Ҳ��ò������඼ʹ��ͬһ��ʵ�塣
*   `secondary`?ָ�������ڸù�ϵ�Ĺ���������ʹ���������涨���`followers`��
*   `primaryjoin`?ָ����ͨ����ϵ����������ʵ�壨��ע�ߣ������� ����ϵ�е�����join�����ǹ�ϵ���е�`follower_id`�ֶ��������ע�ߵ��û�IDƥ�䡣`followers.c.follower_id`���ʽ�����˸ù�ϵ���е�`follower_id`�С�
*   `secondaryjoin`?ָ����ͨ����ϵ��������Ҳ�ʵ�壨����ע�ߣ������� �� ���������`primaryjoin`���ƣ�Ψһ���������ڣ�������ʹ�ù�ϵ����ֶε���`followed_id`�ˡ�
*   `backref`�������Ҳ�ʵ����η��ʸù�ϵ������࣬��ϵ������Ϊ`followed`���������Ҳ��ҽ�ʹ��`followers`����ʾ��������û����б�����˿�б����ӵ�`lazy`������ʾ�����ѯ��ִ��ģʽ������Ϊ��̬ģʽ�Ĳ�ѯ��������ִ�У�ֱ�������ã���Ҳ���������û���̬һ�Զ�Ĺ�ϵ�ķ�ʽ��
*   `lazy`��`backref`�е�`lazy`���ƣ�ֻ������ǰ�������Ӧ�������ʵ�壬`backref`�е���Ӧ�����Ҳ�ʵ�塣

�����������Ƚ����ѣ���Ҳ���ع��ڵ��ġ��Ҵ�����ͻ�����չʾ���������Щ��ϵ��ִ�в�ѯ��һ�оͻ����������ˡ�

���ݿ�ı������Ҫ��¼��һ���µ����ݿ�Ǩ���У�
```
(venv) $ flask db migrate -m "followers"
INFO  [alembic.runtime.migration] Context impl SQLiteImpl.
INFO  [alembic.runtime.migration] Will assume non-transactional DDL.
INFO  [alembic.autogenerate.compare] Detected added table 'followers'
  Generating /home/miguel/microblog/migrations/versions/ae346256b650_followers.py ... done

(venv) $ flask db upgrade
INFO  [alembic.runtime.migration] Context impl SQLiteImpl.
INFO  [alembic.runtime.migration] Will assume non-transactional DDL.
INFO  [alembic.runtime.migration] Running upgrade 37f06a334dbf -> ae346256b650, followers
```

## ��ע��ȡ����ע

��лSQLAlchemy ORM��һ���û���ע��һ���û�����Ϊ����ͨ��`followed`��ϵ�����һ���б������ʹ�á� ���磬������������û��洢��`user1`��`user2`�����У��ҿ�������������򵥵������ʵ�֣�
```
user1.followed.append(user2)
```

Ҫȡ����ע���û����ҿ�����ô����
```
user1.followed.remove(user2)
```

�����ע��ȡ����ע�Ĳ����൱���ף�����Ȼ�������δ���Ŀ������ԣ������Ҳ���ֱ���ڴ�����ʹ�á�appends���͡�removes����ȡ����֮���ҽ���`User`ģ����ʵ�֡�follow���͡�unfollow�������� ��ý�Ӧ���߼�����ͼ����ת�Ƶ�ģ�ͻ��������������ģ���У���Ϊ����ڱ���֮�󽫻ῴ������ʹ�õ�Ԫ���Ը������ס�

�������û�ģ������Ӻ�ɾ����ע��ϵ�Ĵ�������
```
class User(UserMixin, db.Model):
    #...

    def follow(self, user):
        if not self.is_following(user):
            self.followed.append(user)

    def unfollow(self, user):
        if self.is_following(user):
            self.followed.remove(user)

    def is_following(self, user):
        return self.followed.filter(
            followers.c.followed_id == user.id).count() > 0
```

`follow()`��`unfollow()`����ʹ�ù�ϵ�����`append()`��`remove()`�������б�Ҫ�ڴ����ϵ֮ǰ��ʹ��һ��`is_following()`������ȷ�ϲ�����ǰ�������Ƿ���ϣ����磬�����Ҫ��`user1`��ע`user2`������ʵ֤�������ϵ�����ݿ����Ѿ����ڣ��Ҿ�û��Ҫ�ظ������ˡ� ��ͬ���߼�����Ӧ����ȡ����ע��

`is_following()`��������һ������`followed`��ϵ�Ĳ�ѯ����������û�֮��Ĺ�ϵ�Ƿ��Ѿ����ڡ� ���Ѿ���������ʹ��SQLAlchemy��ѯ�����`filter_by()`���������磬���Ҹ����û������û��� ��������ʹ�õ�`filter()`���������ƣ����Ǹ���ƫ��ײ㣬��Ϊ�����԰�������Ĺ���������������`filter_by()`����ֻ�ܼ���Ƿ����һ������ֵ�� ����`is_following()`��ʹ�õĹ��������ǣ����ҹ�����������������Ϊ`self`�û����Ҳ�����Ϊ`user`�����������С� ��ѯ��`count()`�������������ؽ���������� �����ѯ�Ľ����`0`��`1`����˼�������1���Ǵ���0ʵ��������ȵġ� ���������Ĳ�ѯ������`all()`��`first()`�����Ѿ�������ʹ�ù��ˡ�

## �鿴�ѹ�ע�û��Ķ�̬

�����ݿ���֧�ַ�˿���ƵĹ�������β����������ȴ��©��һ����Ҫ�Ĺ��ܡ�Ӧ����ҳ����Ҫչʾ�ѵ�¼�û���ע�����������û��Ķ�̬������Ҫ�����ݿ��ѯ��������Щ�û���̬��

���Զ��׼��ķ�������ִ��һ����ѯ�Է����ѹ�ע�û����б�������֪������ʹ��`user.followed.all()`��䡣Ȼ���ÿ���ѹ�ע���û�ִ��һ����ѯ���������ǵ��û���̬����������û��Ķ�̬��������ʱ�䵹��ϲ���һ���б��С�������������ʵ��Ȼ��

���ַ����м������⡣ ���һ���û���ע��һǧ�ˣ��ᷢ��ʲô�� ����Ҫִ��һǧ�����ݿ��ѯ���ռ����е��û���̬�� Ȼ������Ҫ�ϲ��������ڴ��е�һǧ���б� ��Ϊ�ڶ������⣬���ǵ�Ӧ����ҳ���ս�ʵ��*��ҳ*��������������ʾ���п��õ��û���̬��ֻ����ǰ����������ʾһ���������ṩ����Ȥ���û��鿴���ද̬�� �����Ҫ�����ǵ�������������ʾ��̬������ô��֪����Щ�û���̬���������û������µ��أ����������ȵõ������е��û���̬������������� ��ʵ������һ�����Ľ�����������ܺܺõ�Ӧ�Թ�ģ����

�û���̬�ĺϲ�������������޷�����ģ�������Ӧ����ִ�лᵼ��Ч��ʮ�ֵ��£� �����ֹ����ǹ�ϵ���ݿ��ó��ġ� �ҿ���ʹ�����ݿ���������������Ը���Ч�ķ�ʽִ�в�ѯ������ ������������Ҫ�ṩ�ķ����ǣ���������Ҫ�õ�����Ϣ��ִ��һ�����ݿ��ѯ��Ȼ�������ݿ��ҳ����������Ч�ķ�ʽ����ȡ��Щ��Ϣ��

��������������ѯ��
```
class User(db.Model):
    #...
    def followed_posts(self):
        return Post.query.join(
            followers, (followers.c.followed_id == Post.user_id)).filter(
                followers.c.follower_id == self.id).order_by(
                    Post.timestamp.desc())
```

��������Ϊֹ�������Ӧ����ʹ�õ���ӵĲ�ѯ�� �ҽ�����һ��һ���ؽ�������ѯ�� ����㿴һ�������ѯ�Ľṹ�����ע�⵽��������Ҫ���֣��ֱ���`join()`��`filter()`��`order_by()`�����Ƕ���SQLAlchemy��ѯ����ķ�����
```
Post.query.join(...).filter(...).order_by(...)
```

### ���ϲ�ѯ

Ҫ���join�����Ĺ��ܣ���������һ�����ӡ� ��������һ�������������ݵ�`User`��

| id | username |
| --- | --- |
| 1 | john |
| 2 | susan |
| 3 | mary |
| 4 | david |

Ϊ�˼��������ֻ�ᱣ���û�ģ�͵�`id`��`username`�ֶ��Ա���в�ѯ�������Ķ���ȥ��

����`followers`��ϵ�������ݱ������û�`john`��ע�û�`susan`��?`david`���û�`susan`��ע�û�`mary`���û�`mary`��ע�û�`david`����Щ���������±���ʾ��

| follower_id | followed_id |
| --- | --- |
| 1 | 2 |
| 1 | 4 |
| 2 | 3 |
| 3 | 4 |

����û���̬���а�����ÿ���û���һ����̬��

| id | text | user_id |
| --- | --- | --- |
| 1 | post from susan | 2 |
| 2 | post from mary | 3 |
| 3 | post from david | 4 |
| 4 | post from john | 1 |

���ű�Ҳʡ����һЩ������������۷�Χ���ֶΡ�

������Ϊ�ò�ѯ�ٴ���Ƶ�`join()`���ã�
```
Post.query.join(followers, (followers.c.followed_id == Post.user_id))
```

�����û���̬���ϵ���join������ ��һ��������followers�������ڶ���������join*����*�� �ҵ�������ñ��ĺ�������ϣ�����ݿⴴ��һ����ʱ�������û���̬��͹�ע�߱��е����ݽ����һ�� ���ݽ����ݲ������ݵ��������кϲ���

��ʹ�õ�������ʾ��followers��ϵ���`followed_id`�ֶα�������û���̬���`user_id`�ֶΡ� Ҫִ�д˺ϲ������ݿ⽫���û���̬��join����ࣩ��ȡÿ����¼����׷��`followers`��ϵ��join���Ҳࣩ�е�ƥ�����������м�¼�� ���`followers`��ϵ�����ж����¼������������ô�û���̬�����н��ظ����֡� �������һ���������û���̬��followers��ϵ����ȴû��ƥ�䣬��ô���û���̬�ļ�¼���������join�����Ľ���С�

���������涨���ʾ�����ݣ�ִ��join�����Ľ�����£�

| id | text | user_id | follower_id | followed_id |
| --- | --- | --- | --- | --- |
| 1 | post from susan | 2 | 1 | 2 |
| 2 | post from mary | 3 | 2 | 3 |
| 3 | post from david | 4 | 1 | 4 |
| 3 | post from david | 4 | 3 | 4 |

ע��`user_id`��`followed_id`���������������ж�����ȵģ���Ϊ����join������ �����û�`john`���û���̬�����������ʱ���У���Ϊ����ע�б���û�а���`john`�û������仰˵��û���κ��˹�עjohn�� ������`david`���û���̬���������Σ���Ϊ���û���������˿��

��Ȼ���������join��������ȴû�еõ���Ҫ�Ľ�������������ȥ����Ϊ��ֻ�Ǹ���Ĳ�ѯ��һ���֡�

### ����

Join����������һ�����б���ע�û����û���̬���б�Զ��������Ҫ���ǲ������ݡ� ��ֻ������б��һ���Ӽ�����Ȥ����ĳ���û���ע���û��ǵĶ�̬����������Ҫ��`filter()`���޳������Ҳ���Ҫ�����ݡ�

���ǹ��˲��ֵĲ�ѯ��䣺
```
filter(followers.c.follower_id == self.id)
```

�ò�ѯ��`User`���һ��������`self.id`���ʽ��ָ�Ҹ���Ȥ���û���ID��`filter()`��ѡ��ʱ����`follower_id`�е������ID���У����仰˵����ֻ����follower(��˿)�Ǹ��û������ݡ�

���������ڶ�`id`Ϊ�����û�`john`�ܿ������û���̬����Ȥ�����Ǵ���ʱ����˺�Ľ����

| id | text | user_id | follower_id | followed_id |
| --- | --- | --- | --- | --- |
| 1 | post from susan | 2 | 1 | 2 |
| 3 | post from david | 4 | 1 | 4 |

����������Ҫ�Ľ����

���ס����ѯ�Ǵ�`Post`���з����ģ����Ծ����������õ��������ݿⴴ����һ����ʱ������Ϊ��ѯ��һ���֣���������ǰ����ڴ���ʱ���е��û���̬�� �������������ִ��join������ӵ������С�

### ����

��ѯ���̵����һ���ǶԽ�����������ⲿ�ֵĲ�ѯ������£�
```
order_by(Post.timestamp.desc())
```

�������Ҫ˵���ǣ���ϣ��ʹ���û���̬������ʱ������������н���б�����֮�󣬵�һ������������µ��û���̬��

## �������̬�͹�ע���û���̬

����`followed_posts()`������ʹ�õĲ�ѯ�Ƿǳ����õģ�����һ�����ƣ������������������Լ��Ķ�̬���������ǵĹ�ע���û���̬��ʱ�����У����ò�ѯȴ����δ����

�����ֿ��ܵķ�ʽ����չ�˲�ѯ�԰����û��Լ��Ķ�̬�� ��ֱ���˵��ķ����ǽ���ѯ����ԭ������Ҫȷ�������û�����ע�������Լ��� ����������Լ��ķ�˿����ô����Ĳ�ѯ�ͻ��ҵ����Լ��Ķ�̬�Լ����ע�������˵Ķ�̬�� ���ַ�����ȱ���ǻ�Ӱ���˿��ͳ�����ݡ� �����˵ķ�˿����������һ���������Ǳ�������ʾ֮ǰ���е����� �ڶ��ַ�����ͨ�������ڶ�����ѯ�����û��Լ��Ķ�̬��Ȼ��ʹ�á�union��������������ѯ�ϲ�Ϊһ����ѯ��

��˼����֮����ѡ���˵ڶ��������� ��������Կ���`followed_posts()`�����ѱ���չ��ͨ�����ϲ�ѯ�������û��Լ��Ķ�̬��
```
    def followed_posts(self):
        followed = Post.query.join(
            followers, (followers.c.followed_id == Post.user_id)).filter(
                followers.c.follower_id == self.id)
        own = Post.query.filter_by(user_id=self.id)
        return followed.union(own).order_by(Post.timestamp.desc())
```

��ע�⣬`followed`��`own`��ѯ�������������֮ǰ���еĺϲ���

## ���û�ģ��ִ�е�Ԫ����

��Ȼ�Ҳ�����������ԡ����ӡ��ķ�˿���Ƶ������Ƿ����� �����ұ�д�������صĴ���ʱ���ҵ��ĵ�������Ӧ�õĲ�ͬ�����޸��˴���֮�����ȷ���������뽫������������� ȷ���Ѿ���д�Ĵ����ڽ���������Ч����ѷ����Ǵ���һ���Զ������ԣ��������ÿ�θ��´����ִ�в��ԡ�

Python����һ���ǳ����õ�`unittest`�����������ɱ�д��ִ�е�Ԫ���ԡ� ��������Ϊ`User`���е����з�����дһЩ��Ԫ���Բ��洢��*tests.py*ģ�飺
```
from datetime import datetime, timedelta
import unittest
from app import app, db
from app.models import User, Post

class UserModelCase(unittest.TestCase):
    def setUp(self):
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite://'
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_password_hashing(self):
        u = User(username='susan')
        u.set_password('cat')
        self.assertFalse(u.check_password('dog'))
        self.assertTrue(u.check_password('cat'))

    def test_avatar(self):
        u = User(username='john', email='john@example.com')
        self.assertEqual(u.avatar(128), ('https://www.gravatar.com/avatar/'
                                         'd4c74594d841139328695756648b6bd6'
                                         '?d=identicon&s=128'))

    def test_follow(self):
        u1 = User(username='john', email='john@example.com')
        u2 = User(username='susan', email='susan@example.com')
        db.session.add(u1)
        db.session.add(u2)
        db.session.commit()
        self.assertEqual(u1.followed.all(), [])
        self.assertEqual(u1.followers.all(), [])

        u1.follow(u2)
        db.session.commit()
        self.assertTrue(u1.is_following(u2))
        self.assertEqual(u1.followed.count(), 1)
        self.assertEqual(u1.followed.first().username, 'susan')
        self.assertEqual(u2.followers.count(), 1)
        self.assertEqual(u2.followers.first().username, 'john')

        u1.unfollow(u2)
        db.session.commit()
        self.assertFalse(u1.is_following(u2))
        self.assertEqual(u1.followed.count(), 0)
        self.assertEqual(u2.followers.count(), 0)

    def test_follow_posts(self):
        # create four users
        u1 = User(username='john', email='john@example.com')
        u2 = User(username='susan', email='susan@example.com')
        u3 = User(username='mary', email='mary@example.com')
        u4 = User(username='david', email='david@example.com')
        db.session.add_all([u1, u2, u3, u4])

        # create four posts
        now = datetime.utcnow()
        p1 = Post(body="post from john", author=u1,
                  timestamp=now + timedelta(seconds=1))
        p2 = Post(body="post from susan", author=u2,
                  timestamp=now + timedelta(seconds=4))
        p3 = Post(body="post from mary", author=u3,
                  timestamp=now + timedelta(seconds=3))
        p4 = Post(body="post from david", author=u4,
                  timestamp=now + timedelta(seconds=2))
        db.session.add_all([p1, p2, p3, p4])
        db.session.commit()

        # setup the followers
        u1.follow(u2)  # john follows susan
        u1.follow(u4)  # john follows david
        u2.follow(u3)  # susan follows mary
        u3.follow(u4)  # mary follows david
        db.session.commit()

        # check the followed posts of each user
        f1 = u1.followed_posts().all()
        f2 = u2.followed_posts().all()
        f3 = u3.followed_posts().all()
        f4 = u4.followed_posts().all()
        self.assertEqual(f1, [p2, p4, p1])
        self.assertEqual(f2, [p2, p3])
        self.assertEqual(f3, [p3, p4])
        self.assertEqual(f4, [p4])

if __name__ == '__main__':
    unittest.main(verbosity=2)
```

��������ĸ��û�ģ�͵Ĳ��ԣ����������ϣ���û�ͷ��ͷ�˿���ܡ� `setUp()`��`tearDown()`�����ǵ�Ԫ���Կ�ֱܷ���ÿ������֮ǰ��֮��ִ�е����ⷽ���� ����`setUp()`��ʵ����һЩС���ɣ��Է�ֹ��Ԫ����ʹ�������ڿ����ĳ������ݿ⡣ ͨ����Ӧ�����ø���Ϊ`sqlite://`�����ڲ��Թ�����ͨ��SQLAlchemy��ʹ��SQLite�ڴ����ݿ⡣ `db.create_all()`�������е����ݿ�� ���Ǵ�ͷ��ʼ�������ݿ�Ŀ��ٷ������ڲ������൱���á� �����ڿ����������������������ݿ�ṹ�������Ѿ�ͨ�����ݿ�Ǩ�Ƶ��ֶ�����չʾ���ˡ�

�����ʹ���������������������������
```
(venv) $ python tests.py
test_avatar (__main__.UserModelCase) ... ok
test_follow (__main__.UserModelCase) ... ok
test_follow_posts (__main__.UserModelCase) ... ok
test_password_hashing (__main__.UserModelCase) ... ok

----------------------------------------------------------------------
Ran 4 tests in 0.494s

OK
```

��������ÿ�ζ�Ӧ�ý��и���ʱ���������������в��ԣ���ȷ�����ڲ��ԵĹ���û���ܵ�Ӱ�졣 ���⣬ÿ�ν���һ��������ӵ�Ӧ��ʱ����Ӧ��Ϊ���дһ����Ԫ���ԡ�

## ��Ӧ���м��ɷ�˿����

���ݿ��ģ���з�˿���Ƶ�ʵ�������Ѿ���ɣ�������û�н������ɵ�Ӧ���У�����������Ҫ���������ܡ� ֵ�ø��˵��ǣ�ʵ����û��ʲô�����ս�������������Ѿ�ѧ���ĸ��

����������������µ�·�ɺ���ͼ�����������ṩ���û���ע��ȡ����ע��URL���߼�ʵ�֣�
```
@app.route('/follow/<username>')
@login_required
def follow(username):
    user = User.query.filter_by(username=username).first()
    if user is None:
        flash('User {} not found.'.format(username))
        return redirect(url_for('index'))
    if user == current_user:
        flash('You cannot follow yourself!')
        return redirect(url_for('user', username=username))
    current_user.follow(user)
    db.session.commit()
    flash('You are following {}!'.format(username))
    return redirect(url_for('user', username=username))

@app.route('/unfollow/<username>')
@login_required
def unfollow(username):
    user = User.query.filter_by(username=username).first()
    if user is None:
        flash('User {} not found.'.format(username))
        return redirect(url_for('index'))
    if user == current_user:
        flash('You cannot unfollow yourself!')
        return redirect(url_for('user', username=username))
    current_user.unfollow(user)
    db.session.commit()
    flash('You are not following {}.'.format(username))
    return redirect(url_for('user', username=username))
```

��ͼ�������߼����Զ�������Ҫע�����еĴ����飬�Է�ֹ������������⣬�������ڳ�������ʱ���û��ṩ���õ���Ϣ��

�ҽ������������ͼ������·�ɵ�ÿ���û��ĸ�����ҳ�У��Ա������û�ִ�й�ע��ȡ����ע�Ĳ�����
```
        ...
        <h1>User: {{ user.username }}</h1>
        {% if user.about_me %}<p>{{ user.about_me }}</p>{% endif %}
        {% if user.last_seen %}<p>Last seen on: {{ user.last_seen }}</p>{% endif %}
        <p>{{ user.followers.count() }} followers, {{ user.followed.count() }} following.</p>
        {% if user == current_user %}
        <p><a href="{{ url_for('edit_profile') }}">Edit your profile</a></p>
        {% elif not current_user.is_following(user) %}
        <p><a href="{{ url_for('follow', username=user.username) }}">Follow</a></p>
        {% else %}
        <p><a href="{{ url_for('unfollow', username=user.username) }}">Unfollow</a></p>
        {% endif %}
        ...
```

�û�������ҳ�ı����һ����������ʵ�ʱ���֮�����һ�У�����ʾ���û�ӵ�ж��ٸ���˿�͹�ע�û������ǵ���鿴�Լ��ĸ�����ҳʱ���ֵġ�Edit�����ӵ��У����ܻ���������������֮һ��
*   ����û��鿴��(��)�Լ��ĸ�����ҳ����Ȼ�ǡ�Edit�����Ӳ��䡣
*   ����û��鿴������δ��ע���û��ĸ�����ҳ����ʾ��Follow�����ӡ�
*   ����û��鿴�����Ѿ���ע���û��ĸ�����ҳ����ʾ��Unfollow�����ӡ�


��ʱ����������и�Ӧ�ã�����һЩ�û�������һ�¹�ע��ȡ����ע�û��Ĺ��ܡ� Ψһ��Ҫ��ס���ǣ���Ҫ�ֶ�������Ҫ��ע��ȡ����ע���û��ĸ�����ҳURL����ΪĿǰû�а취�鿴�û��б� ���磬��������ע`susan`������Ҫ��������ĵ�ַ��������*http://localhost:5000/user/susan*�Է��ʸ��û��ĸ�����ҳ�� ��ȷ�����ڲ��Թ�ע��ȡ����ע��ʱ�����⵽�����˿�͹�ע�������仯��

��Ӧ����Ӧ�õ���ҳ����ʾ�û���̬���б������һ�û��������������Ĺ�������Ϊ�û����ܷ���̬�� �����һ��ݻ����ҳ������ƹ�����ֱ�������û���̬���ܵ���ɡ�
