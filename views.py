#若文字訊息中有https://，則自動將其URL建立LIFF
elif 'https://' in mtext:
    try:
        liff_id = liff_api.add(
            view_type="full",
            view_url=mtext)
        #1607718325-5QmeBQop=google首頁
        message.append(TextSendMessage(text='https://liff.line.me/'+liff_id))
        line_bot_api.reply_message(event.reply_token,message)
    except:
        print(err.message)
