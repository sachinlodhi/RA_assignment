# import os
# # # import re
# # # l = ['YeartoGrad','TermDesc','Class','PersonName','Grade','Cwid','UnitsEarned','MajoratEntry','Major(Latest)','AcademicStanding','UnitsAttempting','Email','EnrollmentStatusCode','Graduated','NotGraduatedNotEnrolled','ExpectedGradTerm','FirstGeneration','UnitsNeeded','CohortType','underrepresented','EOP','Parentleveledu','GPA','EnrolledNotGraduated','AdmitType','ProgramStatus','ProgramAction','AcademicCareer']\
# # #
# # #
# # # words_to_filter = ["email", "name", "cwid"]
# # #
# # # # Create a regex pattern that matches any of the words in a case-insensitive manner
# # # pattern = re.compile(r"|".join(re.escape(word) for word in words_to_filter), re.IGNORECASE)
# # #
# # # # Filter the list to get elements that match the pattern
# # # filtered_list = [word for word in l if pattern.search(word)]
# # #
# # # # Print the filtered list
# # # print(filtered_list)
# #
# #
# # l1 = ["a", "b","c", "d"]
# # l2 = ["b"]
# # final = [i for i in l1 if i not in l2]
# # print(final)
#
#
# # import random
# # unique_digits = set()
# # main_df_len = 100
# #
# # while True:
# #         unique_digits.add(random.randint(0,100))
# #         if len(unique_digits)==main_df_len:
# #                 break
# #
# # print(unique_digits)
# #
# #
# # print(len(unique_digits))
#
# # filename = "./static/uploads/data.csv"
# # _, file_extension = os.path.splitext(filename)
# # print(_)
#
# #
#
# # import math
# #
# # print(math.ceil(16/5))
#
#
#
# # import glob, shutil
# #
# # print(glob.glob("templates/*.html"))
#
#
#
#
#
#
# from flask import Flask, render_template, Response
# import time
#
# app = Flask(__name__)
#
# def generate_logs():
#     while True:
#         # Simulate server-side logs
#         log_message = "Log message from server: " + str(time.time())
#         # yield "hello there\n\n"
#         yield f"data: hello there\n\n"
#         time.sleep(1)  # Simulate logs every 1 second
#
# @app.route('/')
# def index():
#     return render_template('index.html')
#
# @app.route('/logs')
# def logs():
#     return Response(generate_logs(), content_type='text/event-stream')
#
# if __name__ == '__main__':
#     app.run(debug=True)


def check_status():
    # print("Checking statusssss")
    with open('status.txt', 'r+') as file:
        status = file.read()
        print("Status is", status)
        if status:
            file.truncate(0)

