# iHexin

unittest
```
self.driver.swipe(start_x=279, start_y=205, end_x=88, end_y=205, duration=500)
```

pytest_POM
```
driver.swipe(start_x=300, start_y=239, end_x=39, end_y=239, duration=500)
```
### 手势源码参考

放大
```
els = self.driver.find_elements_by_xpath("//UIAApplication[1]/UIAWindow[1]/UIAScrollView[1]/UIAStaticText[4]/UIAStaticText[1]")

		a1 = TouchAction()
		a1.press(els[0]).move_to(x=40, y=0).move_to(x=40, y=0).release()

		a2 = TouchAction()
		a2.press(els[0]).move_to(x=-40, y=0).move_to(x=-40, y=0).release()

		ma = MultiAction(self.driver, els[0])
		ma.add(a1, a2)
		ma.perform()
```
获取屏幕宽高
[ios simulator python 滑动怎么解决，求指导](https://testerhome.com/topics/3703)
```
		self.driver.get_window_size()
		print self.driver.get_window_size()
		print self.driver.get_window_size().get('width')
```
拖动股票
[appium Android 如何实现长按应用图标拖动到删除控件处执行删除操作](https://testerhome.com/topics/5346)
```
a1 = TouchAction(self.driver)
		a1.press(cell003_tuodong).wait(1000).move_to(cell001_tuodong).wait(100).release()
		a1.perform()
```
滑动手势封装
```
	def hx_left(self):
		el1 = self.w.get_window_size()
		width = el1.get('width')
		height = el1.get('height')
		start_x = width * (344 / 375.0)
		start_y = height * (134 / 667.0)
		end_x = width * (67 / 375.0)
		end_y = height * (134 / 667.0)
		self.w.swipe(start_x, start_y, end_x, end_y, duration=500)
```
长按手势封装
```
	def hx_longPress(self, element):
		
		location = element.location
		el_size = element.size

		x = el_size['width'] / 2.0 + location['x']
		y = el_size['height'] / 2.0 + location['y']

		return self.w.tap([(x, y)], duration=0.5)

```
滑动
```
def scroll(self, origin_el, destination_el):
        """Scrolls from one element to another

        :Args:
         - originalEl - the element from which to being scrolling
         - destinationEl - the element to scroll to

        :Usage:
            driver.scroll(el1, el2)
        """
        action = TouchAction(self)
        action.press(origin_el).move_to(destination_el).release().perform()
        return self
```
xpath查找元素的问题
```
self.driver.find_element_by_xpath("//UIAStaticText[@name='同花顺']").click()
```
计算cell数量
```
print len(self.driver.find_elements_by_xpath("//UIATableCell[@name]"))
```
拖动
```
    def drag_and_drop(self, origin_el, destination_el):
        """Drag the origin element to the destination element

        :Args:
         - originEl - the element to drag
         - destinationEl - the element to drag to
        """
        action = TouchAction(self)
        action.long_press(origin_el).move_to(destination_el).release().perform()
        return self
```
连续添加股票的(含添加和清除文本操作)
```
	stockCodes = [('600000', 'addPFYH_btn'), ('000001','addPAYH_btn')]
	#stockNames = ['','addPAYH_btn']
	for stockCode, stockName in stockCodes:
		searchStock_page.hx_send_keys(stockCode)
		try:
			eval('tianjiazixuan_page.{}.click()'.format(stockName))
		except:
			print '该股票已添加过'
		tianjiazixuan_page.qingchuwenben_button.click()
```
### 命名规则
1. 页面:对于有一个新page生成需创建一个新page,优先使用标题栏命名,若标题会改变则根据页面功能进行命名
2. 元素:数字开头的元素统一将数字放在末尾

### 三种等待时间的设置方法
- 第一种 sleep()： 设置固定休眠时间。 python 的 time 包提供了休眠方法 sleep() ， 导入 time包后就可以使用 sleep()进行脚本的执行过程进行休眠。
导入 time 包
```
import time
time.sleep()
```
- 第二种 implicitly_wait()：是 webdirver 提供的一个超时等待。隐的等待一个元素被发现，或一个命令完成。如果超出了设置时间的则抛出异常。
implicitly_wait():隐式等待
当使用了隐式等待执行测试的时候，如果 WebDriver没有在 DOM中找到元素，将继续等待，超出设定时间后则抛出找不到元素的异常
换句话说，当查找元素或元素并没有立即出现的时候，隐式等待将等待一段时间再查找 DOM，默认的时间是0
一旦设置了隐式等待，则它存在整个 WebDriver 对象实例的声明周期中，隐式的等到会让一个正常响应的应用的测试变慢，
它将会在寻找每个元素的时候都进行等待，这样会增加整个测试执行的时间。
implicitly_wait()方法比 sleep() 更加智能，后者只能选择一个固定的时间的等待，前者可以在一个时间
范围内智能的等待。
```
self.driver.implicitly_wait()
```
- 第三种  WebDriverWait()：同样也是 webdirver 提供的方法。在设置时间内，默认每隔一段时间检测一次当前。页面元素是否存在，如果超过设置时间检测不到则抛出异常。
```
详细格式如下：
WebDriverWait(driver, timeout, poll_frequency=0.5, ignored_exceptions=None)
driver - WebDriver 的驱动程序(Ie, Firefox, Chrome 或远程)
timeout - 最长超时时间，默认以秒为单位
poll_frequency - 休眠时间的间隔（步长）时间，默认为 0.5 秒
ignored_exceptions - 超时后的异常信息，默认情况下抛 NoSuchElementException 异常。
WebDriverWait()一般由 until()或 until_not()方法配合使用，下面是 until()和 until_not()方法的说明。
until(method, message=’’)
调用该方法提供的驱动程序作为一个参数，直到返回值不为 False。
until_not(method, message=’’)
调用该方法提供的驱动程序作为一个参数，直到返回值为 False。
lambda
lambda 提供了一个运行时动态创建函数的方法。
```