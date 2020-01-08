# FFA Classic v0.54 for mac

FFA Classic v0.54 をmacOS Catalina(10.15.1)で動かせます。

## 手順

### 1. apacheでperl CGIを有効化

`sudo subl /etc/apache2/httpd.conf`

1. 次の行を有効にする
    * `LoadModule cgi_module libexec/apache2/mod_cgi.so`
    * `LoadModule perl_module libexec/apache2/mod_perl.so`
    * `AddHandler cgi-script .cgi`
1. OptionsにExecCGIを追加
    * `Options FollowSymLinks Multiviews ExecCGI`
1. `<Directory "/Library/WebServer/CGI-Executables">`内でhtml, gifを有効にする設定を追加
    * `AddHandler text/html .html`
    * `AddHandler image/gif .gif`

### 2. ffaの設置

1. /Library/WebServer/Documents/CGI-Executables に本リポジトリの ffa以下のファイルを設置する
1. ロック機構を動かすために、CGI-Executables の他者書き込み権限を追加
    * `sudo chmod 777 /Library/WebServer/Documents/CGI-Executables`
1. 書き込みファイルに書き込み権限を設定
    * `chmod 666 recode.cgi`
    * `chmod 666 message.cgi`
    * `chmod 666 winner.cgi`
    * `chmod 666 chara.cgi`

### 3. apatcheの起動

1. `sudo apachectl start`

### 4. アクセス

http://localhost/cgi-bin/ffadventure.cgi
