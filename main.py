import os.path
import shutil

if __name__ == '__main__':
    dir_path = os.path.dirname(os.path.realpath(__file__))
    os.chdir(dir_path)
    # os.system("pytest -m cx") # 运行所有添加了 @pytest.mark.cx的case
    os.system("pytest")
    # 把一些Allure2配置文件放置在report folder
    shutil.copy2("report/environment.properties", "report/report_allure")
    shutil.copy2("report/categories.json", "report/report_allure")
    shutil.copy2("report/executor.json", "report/report_allure")
    shutil.copy2("report/launch.json", "report/report_allure")

    # 下面是为了在Allure2报表中能看到历史记录，需要手动的生成下
    if os.path.exists("report/report_allure/history"):
        shutil.rmtree("report/report_allure/history")

    if os.path.exists(r"httpserver/AllureReport/history"):
        shutil.copytree(r"httpserver/AllureReport/history", "report/report_allure/history")

    # 生成allure report
    print('generate allure report')
    os.system(r"D:\ProgramDev\allure-2.17.3\bin\allure generate ./report/report_allure -o "
              r"httpserver/AllureReport --clean")
