from selenium import webdriver

voteFull = int(input(" Qtd de comentarios: "))
counter = 2
browser = webdriver.Firefox()
browser.get('https://m.facebook.com/story.php?story_fbid=1166085417090247&id=100010663997335&fs=0&focus_composer=0')
btn = browser.find_element_by_xpath('/html/body/div/div/div[2]/div/div[1]/div[2]/a[2]')
btn.click()
login = browser.find_element_by_xpath('//*[@id="m_login_email"]')
login.send_keys("alaf.ns4@gmail.com")
pwd = browser.find_element_by_xpath('/html/body/div/div/div[2]/div/table/tbody/tr/td/div[3]/div[2]/form/ul/li[2]/section/input')
pwd.send_keys("bixezudita")
btn = browser.find_element_by_xpath('/html/body/div/div/div[2]/div/table/tbody/tr/td/div[3]/div[2]/form/ul/li[3]/input')
btn.click()

while counter <= voteFull:
    browser.get('https://m.facebook.com/story.php?story_fbid=1166085417090247&id=100010663997335&fs=0&focus_composer=0')    
    caixa_de_mensagem = browser.find_element_by_xpath('//*[@id="composerInput"]')
    msg = str(counter) + " comentarios"
    caixa_de_mensagem.send_keys(msg)
    btn = browser.find_element_by_xpath('/html/body/div/div/div[2]/div/div[1]/div[2]/div/div[6]/form[1]/table/tbody/tr/td[2]/div/input')
    btn.click()
    counter = counter + 1

browser.quit() #//*[@id="comment_form_100027033491001_603839813860463"]/div[1]/div[3]/button
