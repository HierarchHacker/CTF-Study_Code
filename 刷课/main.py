import http.cookiejar
import json
import os
import re
import time
import urllib.parse
import urllib.request
import requests
from colorama import init
init(autoreset=True)

from webbrowser import open as openPage

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36',
    'UA-AUTHORIZATION': '6C9AB1F740287E6A489678843D42A27D',
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh',
    'Connection': 'keep-alive',
}
Token = {}
userName = None


def login():
    global Token
    global headers
    username = input("请输入用户名：")
    password = input("请输入密码：")
    cookie = http.cookiejar.CookieJar()
    handler = urllib.request.HTTPCookieProcessor(cookie)
    opener = urllib.request.build_opener(handler)
    login_url = "https://www.ulearning.cn/umooc/user/login.do"
    values = {
        "name": username,
        "passwd": password,
        "yancode": "",
        "redirectURL": "",
        "isFrom": "",
        "newLocale": ""
    }
    postdata = urllib.parse.urlencode(values).encode("UTF-8")
    response = opener.open(login_url, data=postdata)
    for item in cookie:
        Token[item.name] = urllib.parse.unquote(item.value)
    if 'AUTHORIZATION' in Token and 'token' in Token and 'UMOOC_SESSION' in Token:
        with open('./cookies.txt', 'wb', True) as f:
            f.write(json.dumps(Token).encode('UTF-8'))
        headers['UA-AUTHORIZATION'] = Token['AUTHORIZATION']
        headers['AUTHORIZATION'] = Token['AUTHORIZATION']
        return "登陆成功..."
    else:
        print("用户名或密码错误，登陆失败")
        return login()


def get_course_list():
    """
    获取课程列表
    :return: 所有课程列表
    """
    rsp = requests.get(
        url="https://courseapi.ulearning.cn/courses/students?keyword=&publishStatus=1&type=1&pn=1&ps=1000&lang=zh",
        headers=headers)
    jsonData = rsp.json()
    rsp.close()
    return jsonData['courseList']  # 所有课程列表


def choose_course(course_list):
    """
    选择课程ID
    :param course_list: 课程列表
    :return: 所选课程
    """
    total = len(course_list)  # 课程总数
    print("您共有%d门课程：" % total)
    i = 0
    while i < total:
        print("课程编号：\033[1;33m%d\033[0m 课程名称：\033[1;33m%s\033[0m" % (i + 1, course_list[i]['name']))
        i += 1
    coursesId = int(input("请选择课程编号："))
    if coursesId <= 0 or coursesId > total:
        print("\033[1;31m没有此课程！请重新选择\033[0m")
        return choose_course(course_list)
    else:
        print("当前课程编号为：\033[1;32m%d\033[0m 课程名称：\033[1;32m%s\033[0m" % (coursesId, course_list[coursesId - 1]['name']))
        return course_list[coursesId - 1]


def get_course_class(course_id):
    """
    获取课程对应的班级
    :param course_id:
    :return: 班级
    """
    get_course_class_api = "https://courseapi.ulearning.cn/classes/information/student/%d?lang=zh" % course_id
    rsp = requests.get(url=get_course_class_api, headers=headers)
    classData = rsp.json()
    rsp.close()
    return classData


def get_textbook_list(course):
    """
    获取课程下所有教材列表
    :param course: 课程
    :return: 所有教材列表
    """
    print("开始获取 \033[1;33m%s\033[0m 课程下所有章节内容：" % course['name'])
    get_textbookId_api = "https://courseapi.ulearning.cn/textbook/student/%d/list" % course[
        'id']  # 获取该课程下所有书籍(一门课可能有多本书)
    rsp = requests.get(url=get_textbookId_api, headers=headers)
    textbookJsonData = rsp.json()
    rsp.close()
    return textbookJsonData


def choose_textbook(textbook_list):
    """
    选择某课程下需要学习的教材
    :param textbook_list: 课程下所有教材列表
    :return: 所选择的教材
    """
    textbookTotal = len(textbook_list)
    if textbookTotal == 1:
        print("该课程下有一门教材：《%s》，您无法选择其他" % textbook_list[0]['name'])
        return textbook_list[0]
    elif textbookTotal == 0:
        exit("\033[1;31m没有要学的，你学个得儿\033[0m")
    else:
        i = 0
        print("该课程下有%d本教材需要学习：" % textbookTotal)
        while i < textbookTotal:
            print("教材ID：\033[1;33m%d\033[0m，教材名称：《\033[1;33m%s\033[0m》" % (i + 1, textbook_list[i]['name']))
            i += 1

        textbookID = int(input("请选择要学习的书籍："))
        if textbookID <= 0 or textbookID > textbookTotal:
            print("\033[1;31m没有此书籍，请重新选择！\033[0m")
            return choose_textbook(textbook_list)
        else:
            print("当前选择学习书籍名称：《\033[1;32m%s\033[0m》", textbook_list[textbookID - 1]['name'])
            return textbook_list[textbookID - 1]


def get_textbook_directory_item(textbook_id, class_id):
    """
    获取教材的目录
    :param textbook_id: 教材id
    :param class_id: 班级id
    :return:
    """
    get_textbook_directory_api = "https://api.ulearning.cn/course/stu/%d/directory?classId=%d" % (textbook_id, class_id)
    rsp = requests.get(url=get_textbook_directory_api, headers=headers)
    directoryData = rsp.json()
    rsp.close()
    return directoryData['chapters']


def choose_textbook_chapter(chapter_list):
    """
    选择教材下的某章节
    :param chapter_list: 章节列表
    :return: 所选章节列表（可以多选）
    """
    chapterTotal = len(chapter_list)
    print("本教材共有：%d章（\033[1;31m注：理论上已关闭学习的章节也是可以刷的\033[0m）：" % chapterTotal)
    i = 0
    while i < chapterTotal:
        print("章节编号：\033[1;33m%d\033[0m，章节标题：\033[1;33m%s\033[0m，章节状态：%s" % (
            i + 1, chapter_list[i]['nodetitle'],
            "\033[1;31m关闭学习\033[0m" if chapter_list[i]['hide'] == 1 else "\033[1;32m开放学习\033[0m"))
        i += 1
    print("请选择要学习的章节（\033[1;31m注：可以选择多个章节，请用逗号或空格隔开\033[0m）：", end="")
    chapterIds = input()
    chapterIds = re.split(",|，|\s+", chapterIds)
    chooseChapter = []
    for e in chapterIds:
        if 1 <= int(e) <= chapterTotal:
            chooseChapter.append(chapter_list[int(e) - 1])
        else:
            continue
    return chooseChapter


def get_chapter_whole_page(chapter_id):
    """
    获取一章下所有小节的完整页面
    :param chapter_id:
    :return:
    """
    get_chapter_whole_page_api = "https://api.ulearning.cn/wholepage/chapter/stu/%d" % chapter_id
    rsp = requests.get(url=get_chapter_whole_page_api, headers=headers)
    wholePage = rsp.json()['wholepageItemDTOList']
    rsp.close()
    return wholePage


def submit(data):
    """
    提交数据，老规矩：为了防止程序不可控，不公开加密函数，由我提供服务调用
    :param data:
    :return:
    """
    postJsonStr = json.dumps(data)
    rsp = requests.post(url="https://pay.ufec.cn/getSign.php", headers=headers, data=postJsonStr)
    payload = rsp.text
    rsp.close()
    rsp = requests.post(url="https://api.ulearning.cn/yws/api/personal/sync?courseType=4&platform=PC",
                        headers=headers, data=payload)
    returnMsg = rsp.text
    rsp.close()
    return returnMsg


def pass_section(whole_page):
    """
    完成小节
    :param whole_page:
    :return:
    """
    studyStartTime = int(time.time())
    page = {
        "itemid": whole_page['itemid'],
        "autoSave": 1,
        "withoutOld": None,
        "complete": 1,
        "studyStartTime": studyStartTime,
        "userName": userName,
        "score": 100,
        'pageStudyRecordDTOList': list()
    }
    wholepageDTOList = whole_page['wholepageDTOList']  # 一节下面有多个小节
    for pages in wholepageDTOList:
        page['pageStudyRecordDTOList'].append(pass_page(pages, studyStartTime))
    msg = submit(page)
    if msg == '1':
        print("\033[1;32m成功！\033[0m")
    else:
        print("\033[1;31m失败！\033[0m")


def pass_page(page, study_start_time):
    """
    完成每节的每个页面
    :param page:
    :param study_start_time:
    :return:
    """
    pageType = None
    if page['contentType'] == 5:
        pageType = "图文型"
    elif page['contentType'] == 6:
        pageType = "视频型"
    elif page['contentType'] == 7:
        pageType = "练习题"

    if pageType is not None:
        print("\033[1;31m注：请根据页面类型选择时间，建议时间选择权重：视频型 > 练习题 > 图文型\033[0m")
    print("\t\t请输入 \033[1;34m%s\033[0m 的学习时间（类型：\033[1;32m%s\033[0m）：" % (page['content'], pageType if pageType is not None else "未知"), end="")
    studyTime = int(input())
    pageStudyRecord = {
        "pageid": page['relationid'],
        "complete": 1,
        "studyTime": studyTime,
        "score": 100,
        "answerTime": 1,
        "submitTimes": study_start_time + studyTime,  # 开始学习时间 + 自定时间
        "questions": list(),
        "videos": list(),
        "speaks": list()
    }

    if page['contentType'] == 5:
        # 图文形直接返回
        return pageStudyRecord
    elif page['contentType'] == 6:
        # 视频形式
        coursepageDTOList = page['coursepageDTOList']
        startTime = study_start_time  # 视频学习时间，首次等于初始时间
        for coursepageDTO in coursepageDTOList:
            pageStudyRecord['videos'].append({
                "videoid": coursepageDTO['resourceid'],
                "current": studyTime,
                "status": 1,
                "recordTime": studyTime,
                "time": studyTime,
                "startEndTimeList": [
                    {
                        "startTime": startTime,
                        "endTime": startTime + studyTime
                    }
                ]
            })
            startTime = startTime + studyTime  # 处理完后衔接上次提交时间
        return pageStudyRecord

    elif page['contentType'] == 7:
        # 练习题
        questions = page['coursepageDTOList']
        for question in questions:
            pageStudyRecord['coursepageId'] = question['coursepageDTOid']
            pageStudyRecord['questions'] = pass_question(question)
        return pageStudyRecord


def pass_question(question):
    """
    自动做题
    :param question:
    :return: 答案
    """
    parentId = question['parentid']
    questionsRes = []
    for q in question['questionDTOList']:
        rsp = requests.get(url="https://api.ulearning.cn/questionAnswer/%d?parentId=%d" % (q['questionid'], parentId),
                           headers=headers)
        answerData = rsp.json()
        rsp.close()
        questionsRes.append({
            "questionid": q['questionid'],
            "answerList": answerData['correctAnswerList'],
            "score": int(q['score'])
        })
    return questionsRes


def pass_chapter(chapter):
    """
    完整一章内容
    :param chapter:
    :return:
    """
    wholePages = get_chapter_whole_page(chapter['nodeid'])
    for section in chapter['items']:
        print("开始学习 \033[1;34m%s\033[0m 小节内容" % section['title'])
        for whole_page in wholePages:
            if whole_page['itemid'] == section['itemid']:
                pass_section(whole_page)


def run():
    global Token
    global userName
    global headers
    print("\033[1;33m欢迎使用优学院刷课脚本， 工具只是辅助作用切勿用来盈利，一切后果与作者无关\033[0m")
    try:
        f = open('./cookies.txt')
        f.close()
    except FileNotFoundError:
        # 创建空白文件
        open('./cookies.txt', 'w')
    except PermissionError:
        exit("You don't have permission to access this file")
    size = os.path.getsize('./cookies.txt')
    if size == 0:
        print("开始登陆....")
        login()
    else:
        with open('./cookies.txt', 'r') as f:
            s = f.read()
        Token = dict(json.loads(s))
    with open('./cookies.txt', 'r', encoding="UTF-8") as f:
        s = f.read()
    Token = dict(json.loads(s))
    headers['UA-AUTHORIZATION'] = Token['AUTHORIZATION']
    headers['AUTHORIZATION'] = Token['AUTHORIZATION']
    USER_INFO = json.loads(Token['USER_INFO'])
    userName = str(USER_INFO['name']).replace('%', '\\').encode("utf8").decode('unicode_escape')
    courseList = get_course_list()  # 课程列表
    course = choose_course(courseList)  # 选择的单个课程
    classInfo = get_course_class(course['id'])  # 该课程的班级信息
    textbookList = get_textbook_list(course)  # 课程下的教材列表
    textbook = choose_textbook(textbookList)  # 选择学习的教材
    directoryList = get_textbook_directory_item(textbook['courseId'], classInfo['classId'])  # 教材目录
    chapters = choose_textbook_chapter(directoryList)  # 从目录中选择章节
    if len(chapters) == 0:
        exit("啥都不选？？？")
    else:
        for chapter in chapters:
            pass_chapter(chapter)


if __name__ == '__main__':
    print("是否打开使用说明页面(y or n)：", end="")
    isOpenPage = input()
    if isOpenPage == 'y' or isOpenPage == 'yes':
        openPage("https://www.ufec.cn/archives/fuck-ulearning.html#tmpshNSC") # 使用说明
    run()
