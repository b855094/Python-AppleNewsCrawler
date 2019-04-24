#!/bin/sh

nohup sh get_news_url.sh > getUrl.log 2>&1 &
nohup sh get_news_content.sh > getContent.log 2>&1 &
nohup sh get_news_view.sh > getView.log 2>&1 &
