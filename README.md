# 🚧GM-BOT:基于群专属头衔进行管理的BOT



## 原有命令列表

menu,#menu,菜单,#菜单,help 均可呼出此菜单

###所有命令的#都是英文字母的#，键盘上是shift+3(#)

——命令	（命令示例）说明



### 通用命令

——#导出群成员	(#导出群成员)导出本群成员名单

——#exportmembers	(#exportmembers)快速导出本群成员名单，数据可能不是实时，注意核对

——#roll	(#roll)随机一个0-100的数字

——#wordcloud	(#wordcloud)根据群聊天记录记录生成词云

——#selfwordcloud	(#selfwordcloud)根据自己的发言记录生成词云，通过临时会话发送结果

——#analysegroup	(#analysegroup)根据群聊天记录生成时段记录分析

——#selfanalysegroup	(#selfanalysegroup)根据群自己的发言记录生成时段记录分析，通过临时会话发送结果

——#messagerank	(#messagerank)根据记录生成当前发言排名

——#sptitlecount	(#sptitlecount)统计当前群聊各头衔人数

——任意文字包含两个emoji，仅限前两个emoji

——关键词触发的相关命令，关键词: []



### 以下为我画你猜相关命令
——我画你猜 猜的词	(我画你猜 苹果)开启群的我画你猜，可通过私聊bot发送此命令

——#whncstop uuid	(#whncstop uuid)提前结束uuid对应的我画你猜

——#whncstatus	(#whncstatus)查询当前群的我画你猜剩余任务



### 仅管理员/群主有效的命令
——#kick	(#kick)将当前群聊当前时间入群一天但未获取头衔的踢出群聊

——#kickdetect	(#kickdetect)将detect命令检测到的当前群聊入群一天但未获取头衔的踢出群聊

——#kickforce	(#kickforce)将当前群聊未获取头衔的踢出群聊

——#kicklowlevel	(#kicklowlevel 99)踢出当前群聊低于某一等级的群员

——#kicknegative	(#kicknegative 未发言天数x)踢出当前群聊x天未发言的

——#kicklastdetect	(#kicklastdetect)踢出当前群聊前一次被检测到的人，包括以下命令所有以#detect开头的命令

——#detect	(#detect)查询当前群聊入群一天但未获取头衔的

——#detectr	(#detectr)查询当前群聊入群一天但未获取头衔的,上限20

——#detectforce	(#detectforce)查询当前群聊未获取头衔的

——#detectforcer	(#detectforcer)查询当前群聊未获取头衔的,上限20

——#detectnegative	(#detectnegative 未发言天数x)查询当前群聊x天未发言的

——#detectlowlevel	(#detectlowlevel 99)检测当前群聊低于某一等级的群员

——#detectspecialtitle	(#detectspecialtitle 头衔关键字 头衔关键字)检测当前群聊具有特定头衔的群员, 关键字使用模糊匹配

——#permissionblock	(#permissionblock qq号 qq号...)用于屏蔽特定成员的所有命令，也可用@来代替qq号

——#permissionallow	(#permissionallow qq号 qq号...)用于恢复特定成员的所有命令，也可用@来代替qq号

——#temppermissionblock	(#temppermissionblock qq号 qq号...)用于屏蔽特定成员临时对话的所有命令，也可用@来代替qq号

——#temppermissionallow	(#temppermissionallow qq号 qq号...)用于恢复特定成员临时对话的所有命令，也可用@来代替qq号

——#进群通知	(#进群通知 通知内容...)修改进群通知内容，不输入内容将取消进群通知信息



### 以下为chatGpt/new bing相关命令
### 如果希望gpt渲染LaTeX，请在原有命令后加上math，例如#gptmath”
### 触发At或者引用可以替代#gpt这四个字，如需渲染请以math开头
### #gpt，at或者回复触发的是各自qq号对应的上下文
——#gpt	(#gpt 任意文本)发起对话请求，请耐心等待图片返回

——#reset	(#reset prompt)重置发起者qq号对应的上下文对话请求,如果带了文本，会作为prompt

——.+\.pdf\s+.+	(任意pdf.pdf 查询语句)检索pdf返回所需要的信息，不具备上下文，pdf的token不能超出16k



### 以下为直播订阅相关命令，当前可指定平台关键字:[BILIBILI, 哔哩哔哩, douyu, DOUYU, b站, B站, 斗鱼, bili, bilibili]
### 任意房间当无人订阅时将不会发送开播通知
——#subadd	(#subadd 平台关键字 房间号)订阅直播通知

——#subrm	(#subrm 平台关键字 房间号)取消订阅

——#sublist	(#sublist)查看当前所有订阅情况



### meme合成相关命令
——memes列表：查看支持的memes列表

——{表情名称}+可能的参数：memes列表中的表情名称，根据提供的文字或图片制作表情包

——meme搜索+关键词：搜索表情包关键词

——{表情名称}+详情：查看该表情所支持的参数

