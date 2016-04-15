#Awesome-Blog


##特点
1. 使用aiohttp框架实现异步IO
2. 这个项目中自己写了一套ORM，并没有使用sqlalchemy.
3.


##项目结构：未完成

    awesome-python3-webapp/
    +-	www/
    |	+-	static/
    |	|	+-	css/
    |	|	|	+- addons/
    |	|	|	|	+- uikit.addons.min.css
    |	|	|	|	+- uikit.almost-flat.addons.min.css
    |	|	|	|	+- uikit.gradient.addons.min.css
    |	|	|	+- 	awesome.css
    |	|	|	+- 	uikit.almost-flat.addons.min.css
    |	|	|	+- 	uikit.gradient.addons.min.css
    |	|	|	+- 	uikit.min.css
    |	|	+-	fonts/
    |	|	|	+-	fontawesome-webfont.eot
    |	|	|	+- 	fontawesome-webfont.ttf
    |	|	|	+- 	fontawesome-webfont.woff
    |	|	|	+- 	FontAwesome.otf
    |	|	+-	img
    |	|	|	+-	user.png 
    |	|	+-	js/
    |	|	|	+- 	awesome.js
    |	|	|	+-	jqery.min.js
    |	|	|	+-	sha11.min.js
    |	|	|	+-	sticky.min.js
    |	|	| 	+- 	uikit.min.js
    |	|	|	+-	vue.min.js
    |	+-	templates/
    |	|	+-	__base__.html
    |	|	+-	blog.html
    |	|	+-	blogs.html
    |	|	+-	manage_blog_edit.html
    |	|	+-	manage_blogs.html
    |	|	+-	manage_comments.html
    |	|	+-	manage_users.html
    |	|	+-	register.html
    |	|	+-	signin.html
    |	|	+-	test.html
    |	+-	models.py
    |	+-	orm.py
    |	+-	handler.py
    |	+-	coroweb.py
    |	+-	apis.py
    |	+-	app.py
    |	+-	config.py
    |	+-	config_default.py
    |	+-	config_override
    |	+-	vavivon.ico
    |	+-	markdown2.py
    +-	.gitgore
    +-	LICENSE
    +-	README.md

routers:

/                   index                       blogs.html              
/show_all_users     show_all_users()            test.html               
/retister           register                    register.html
/signin             signin                      signin.html
/signout            signout                     
/manage/blogs/create
/manage/blogs
/manage/users




get /api/users      api_get_users
post /api/users     api_register_user
/api/authenticate   authenticate
/api/comments               api_comments
/api/blogs/{id}/comments            api_create_comment      
get  /api/blogs
post /api/blogs
/blog/{id}
/api/blogs/{id}