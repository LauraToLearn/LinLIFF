urlpatterns = [
    path('admin/', admin.site.urls),
    url('^callback',views.callback),
    url('^notify',views.notify),
    url('^ig_command',views.ig_command),
    url('^comm',views.comm),
    url('^index/(?P<day>\d+)/(?P<post_title>.+)$',views.index),
    url('^Weather_Predict',views.Weather_Predict),
    
    #新增liff這個url，這個是用來建例LIFF轉跳頁面用的
    url('^liff',views.liff),
    #新增sayhi這一個url，並設定(?P<name>.+)，用來獲得user的名字參數並顯示在畫面上
    url('^sayhi/(?P<name>.+)',views.sayhi),

]
