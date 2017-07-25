# Shodan
This is a script to get data from Shodan(https://www.shodan.io/), the same with ZoomEye(https://github.com/starnightcyber/ZoomEye)</br>
这个脚本用来从Shodan获取相关查询的数据，跟从ZoomEye获取数据的脚本类似。

You may first refer to :</br>
The official Python library for Shodan https://developer.shodan.io</br>
And this is its github page: https://github.com/achillean/shodan-python</br>
首先，请参考以上资料，确保Shodan的环境运行。

And this script does more than the given example, to make this script work, plean first registered to Shodan, so that you have an
API Key, replace that with your own key.

SHODAN_API_KEY = "YOUR_API_KEY"</br>

上面的参考资料仅仅是给出了一个简单的示例，这个脚本能获取和保存更多的数据，当然从Shodan获取的json格式的数据是一样的，脚本中做了更多的解析。在运行这个脚本
之前请用自己的API KEY替换代码中的"YOUR_API_KEY"


This script works on python2.7, if your python version is python3.x, you may need to do few changes to make it work.
Running this script is very ease, the following is the example.</br>
这个脚本是在python2.7的环境下运行的，如果你的python的环境是python3.x, 可能需要简单的修改即可。使用这个脚本很简单，下面是使用示例。

### Sample
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++</br>
please input search query : weblogic            
please input file name to save data : weblogic </br>
Total results 1203 , pages : 13 </br>
page 1 ... left: 12 time: 30s </br>
page 2 ... left: 11 time: 53s </br>
page 3 ... left: 10 time: 1m:15s </br>
page 4 ... left: 9 time: 1m:58s </br>
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++</br>
This script will try to get all data(query:weblogic) that Shodan returns and saves reult to file(weblogic), surely consumes more query credits. If you just want to test it, please check variable num.</br>
这个脚本会尝试从Shodan获取所有的数据(根据你的查询)，当然也就会消耗更多的query credits. 可以自己改变一下脚本中的num变量即可。
