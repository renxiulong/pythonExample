
### selenium使用注意事项

------

#### 首次运行异常解决`selenium.common.exception.WebDriverException:Message:'chromedriver' executable needs to be in Path`

1. 打开chrome 输入 “chrome://version/”来查看chrome版本
2. 访问此网站http://chromedriver.storage.googleapis.com/index.html   然后选择合适版本的driver 
3. 如此后，运行程序应该就没问题了

```
# -*- coding: utf-8 -*-
__author__ = '任秀龙'

from selenium import webdriver
import time

chrome_driver = 'C:\chromeDriver\chromedriver.exe'
browser = webdriver.Chrome(executable_path=chrome_driver)
time.sleep(5)

url = "https://www.jianshu.com/p/111d5fd45487"
browser.get(url);
file = open('biaobai.json', 'w+', encoding="utf-8")
file.write(browser.page_source)

browser.quit();
```
