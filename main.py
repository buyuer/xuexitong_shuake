import os
import cv2
import time

# adb路径
adb_path = "F:\\Development\\SDK\\Android\\android-sdk\\platform-tools\\adb.exe"
# 截图缓存路径
cache_path = "D:\\test\\"


def match_template(image, template, md=cv2.TM_CCOEFF_NORMED):
    # cv2.imshow("image", image)
    # cv2.imshow("template", template)
    result = cv2.matchTemplate(image, template, md)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
    if max_val > 0.8:
        return True, max_loc[0] + template.shape[1] / 2, max_loc[1] + template.shape[0] / 2
    else:
        return False, -1, -1


def get_screencap_to_path(path):
    os.system(
        adb_path + " shell /system/bin/screencap -p /sdcard/screenshot.png")
    os.system(
        adb_path + " pull /sdcard/screenshot.png " + path)
    return path


def get_screencap():
    get_screencap_to_path(cache_path + "screenshot.png")
    return cv2.imread(cache_path + "screenshot.png", 1)


def simulate_tap(x, y):
    os.system(adb_path + " shell input tap " + str(x) + " " + str(y))


def simulate_swipe(x1, y1, x2, y2):
    os.system(adb_path + " shell input swipe " + str(x1) + " " + str(y1) + " " + str(x2) + " " + str(y2))


def find_submit_loc(image):
    image_submit = cv2.imread("./Resource/submit.jpg", 1)
    return match_template(image, image_submit)


def find_option_loc(image):
    image_a = cv2.imread("./Resource/A.jpg", 1)
    return match_template(image, image_a)


def find_yes_loc(image):
    image_yes = cv2.imread("./Resource/yes.jpg", 1)
    return match_template(image, image_yes)


def find_retry_loc(image):
    image_play = cv2.imread("./Resource/retry.jpg", 1)
    return match_template(image, image_play)


def find_video_loc(image):
    image_video = cv2.imread("./Resource/video.jpg", 1)
    return match_template(image, image_video)


if __name__ == '__main__':

    is_just_play = False

    while True:
        screen = get_screencap()

        # 判断横屏还是竖屏
        print(screen.shape)
        if screen.shape[0] < screen.shape[1]:
            submit_is_find, submit_x, submit_y = find_submit_loc(screen)
            is_just_play = True
            # 如果找到提交按钮，说明需要做题
            print("播放视频中")
            if submit_is_find:
                print("单选题")
                option_is_find, option_x, option_y = find_option_loc(screen)
                simulate_tap(option_x, option_y)
                print("选中了A选项位置", option_x, option_y)
                time.sleep(0.05)
                simulate_tap(submit_x, submit_y)
                print("点击提交")
                time.sleep(0.05)
                yes_is_find, yes_x, yes_y = find_yes_loc(get_screencap())
                if yes_is_find:
                    simulate_tap(submit_x, submit_y)
                    print("提交成功")
                else:
                    print("答案错误，尝试B选项")
                    simulate_tap(option_x, option_y + 50)
                    print("选中了B选项位置", option_x, option_y)
                    time.sleep(0.05)
                    simulate_tap(submit_x, submit_y)
                    print("点击提交")
                    time.sleep(0.05)
                    yes_is_find, yes_x, yes_y = find_yes_loc(get_screencap())
                    if yes_is_find:
                        simulate_tap(submit_x, submit_y)
                        print("提交成功")
                    else:
                        print("答案错误，尝试C选项")
                        simulate_tap(option_x, option_y + 100)
                        print("选中了C选项位置", option_x, option_y + 100)
                        time.sleep(0.05)
                        simulate_tap(submit_x, submit_y)
                        print("点击提交")
                        time.sleep(0.05)
                        yes_is_find, yes_x, yes_y = find_yes_loc(get_screencap())
                        if yes_is_find:
                            simulate_tap(submit_x, submit_y)
                            print("提交成功")

            else:
                print("不需要做选择题")
            is_retry_find, retry_x, retry_y = find_retry_loc(screen)
            if is_retry_find:
                print("点击重试")
                simulate_tap(retry_x + 150, retry_y + 150)
            else:
                print("未发现重试")
        else:
            print("需要翻页")
            while True:
                is_video_find, video_x, video_y = find_video_loc(get_screencap())
                if is_video_find:
                    if is_just_play:
                        time.sleep(2)
                        simulate_swipe(screen.shape[1] - 100, screen.shape[0] / 2, 200, screen.shape[0] / 2)
                        print("向右滑动")
                        is_just_play = False
                    else:
                        print("找到了视频标签")
                        simulate_tap(screen.shape[1] / 2, video_y - 200)
                        break
                else:
                    simulate_swipe(screen.shape[1] - 100, screen.shape[0] / 2, 200, screen.shape[0] / 2)
                    print("向右滑动")
                    time.sleep(2)

        if cv2.waitKey(1000) == 27:
            break
    cv2.destroyAllWindows()
