import flet as ft
import random
import time

def main(page: ft.Page):
    page.title = "Family Feud Game"
    page.bgcolor = "#96B0D7"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    quizzes = {"Entertainment 🎬":
        {"questions":["Name an artist people avoid singing at karaoke.", "Name a movie genre better in theaters.", "Name a famous animated dog.", "Name something people buy at a concert."],
        "correct":[["mariah carey", "adele", "beyonce", "taylor swift", "ariana grande"],["action", "horror", "comedy", "fantasy", "romance"],["scooby doo", "snoopy", "pluto", "blue", "brian"],["merch", "food", "drinks", "tickets", "glow sticks"]]},
        "Everyday Life 🏠":
        {"questions":["Name something you find in a classroom.", "Name something people forget at home.", "Name something found in a refrigerator.", "Name something people do before school."],
        "correct":[["pencil", "teacher", "desk", "computer", "books", "students", "board"],["phone", "wallet", "keys", "homework", "lunch"],["milk", "eggs", "juice", "water", "cheese", "yogurt"],["brush teeth", "eat breakfast", "pack backpack", "get ready"]]},
        "Funny & Random 👻":
        {"questions":["What do people do after seeing a ghost?", "Name something people are scared of.", "Name something people yell during traffic."],
        "correct":[["run", "scream", "pray", "cry", "hide"],["spiders", "heights", "snakes", "darkness", "clowns"],["move", "watch out", "go", "idiot", "hurry"]]},
        "Food & Drinks 🍕":
        {"questions":["Name a popular pizza topping.", "Name something people drink in the morning.", "Name a fast food restaurant.", "Name something eaten at the movies."],
        "correct":[["pepperoni", "cheese", "mushrooms", "ham", "sausage"],["coffee", "juice", "milk", "tea", "water"],["McDonalds", "Burger King", "Wendys", "KFC", "Subway", "Taco Bell"],["popcorn", "candy", "nachos", "chips"]]},
        "Sports & Games ⚽":
        {"questions":["Name a sport played with a ball.", "Name something athletes wear.", "Name a popular video game.", "Name something people do at the gym."],
        "correct":[["basketball", "soccer", "baseball", "football", "volleyball", "tennis"],["shoes", "jersey", "shorts", "helmet", "suit"],["Minecraft", "Fortnite", "Roblox", "FIFA", "GTA", "Sims 4", "League of Legends"],["run", "lift weights", "stretch", "exercise", "cardio", "lose weight"]]}}

    team1 = []
    team2 = []
    current_category = [""]
    current_question = [0]
    team1_score = [0]
    team2_score = [0]
    current_player1 = [""]
    current_player2 = [""]
    current_answers = []
    guessed_answers = []
    buzzed_team = [""]
    current_turn = [""]
    first_wrong = [True]
    steal_mode = [False]

    logo = ft.Image(src="logo.png", width=500, height=250)
    question_text = ft.Text("", size=28, text_align=ft.TextAlign.CENTER)
    result_text = ft.Text("", size=22, color="#901414", text_align=ft.TextAlign.CENTER)
    player_text = ft.Text("", size=24, weight=ft.FontWeight.BOLD)
    buzz_text = ft.Text("PRESS A OR L TO ANSWER!", size=28, weight=ft.FontWeight.BOLD, color="#081D3A")
    score_text = ft.Text("TEAM 1: 0 | TEAM 2: 0", size=24, weight=ft.FontWeight.BOLD)

    answers_left_text = ft.Text("", size=22)
    answer_input = ft.TextField(label="Type your answer...", width=400, visible=False)

    input_team1 = ft.TextField(label="1: Add a team member")
    input_team2 = ft.TextField(label="2: Add a team member")
    team1_text = ft.Text("")
    team2_text = ft.Text("")
    wheel_team1 = ft.Text("🔄",size=80)
    wheel_team2 = ft.Text("🔄",size=80)
    team1_player_text = ft.Text("Team 1 Player: ???", size=22)
    team2_player_text = ft.Text("Team 2 Player: ???", size=22)

    def make_team_text(team):
        text = ""
        for person in team:
            if text == "":
                text = person
            else:
                text = text + ", " + person
        return text

    def add_team1(e):
        try:
            if len(input_team1.value) < 3:
                raise ValueError("Name must have at least 3 letters")
            if input_team1.value != "":
                team1.append(input_team1.value)
                team1_text.value = "Team 1: " + make_team_text(team1)
                input_team1.value = ""
        except ValueError as error:
            team1_text.value = "❌ Error: " + str(error)

    def add_team2(e):
        try:
            if len(input_team2.value) < 3:
                raise ValueError("Name must have at least 3 letters")
            if input_team2.value != "":
                team2.append(input_team2.value)
                team2_text.value = "Team 2: " + make_team_text(team2)
                input_team2.value = ""
        except ValueError as error:
            team2_text.value = "❌ Error: " + str(error)

    def choose_entertainment(e):
        current_category[0] = "Entertainment 🎬"
        topic_view.visible = False
        wheel_view.visible = True

    def choose_everyday(e):
        current_category[0] = "Everyday Life 🏠"
        topic_view.visible = False
        wheel_view.visible = True

    def choose_funny(e):
        current_category[0] = "Funny & Random 👻"
        topic_view.visible = False
        wheel_view.visible = True

    def choose_food(e):
        current_category[0] = "Food & Drinks 🍕"
        topic_view.visible = False
        wheel_view.visible = True

    def choose_sports(e):
        current_category[0] = "Sports & Games ⚽"
        topic_view.visible = False
        wheel_view.visible = True

    def spin_team1_player(e):
        if len(team1) > 0:
            spin_list = ["🔄", "🔃"]
            for i in range(12):
                wheel_team1.value = spin_list[0]
                time.sleep(0.04)
                wheel_team1.value = spin_list[1]
                time.sleep(0.04)
            wheel_team1.value = "✅"
            random_number = random.randint(0,len(team1)-1)
            current_player1[0] = team1[random_number]
            team1_player_text.value = "Selected Player: " + current_player1[0]

    def spin_team2_player(e):
        if len(team2) > 0:
            spin_list = ["🔄", "🔃"]
            for i in range(12):
                wheel_team2.value = spin_list[0]
                time.sleep(0.04)
                wheel_team2.value = spin_list[1]
                time.sleep(0.04)
            wheel_team2.value = "✅"
            random_number = random.randint(0,len(team2)-1)
            current_player2[0] = team2[random_number]
            team2_player_text.value = "Selected Player: " + current_player2[0]

    def start_game(e):
        wheel_view.visible = False
        player_view.visible = True

        current_question[0] = 0
        team1_score[0] = 0
        team2_score[0] = 0
        score_text.value = "TEAM 1: 0 | TEAM 2: 0"

    def begin_questions(e):
        player_view.visible = False
        game_view.visible = True
        show_question()

    def make_answers_text(answer_list):
        final_text = ""
        for answer in answer_list:
            if final_text == "":
                final_text = answer
            else:
                final_text = final_text + ", " + answer
        return final_text

    def show_question():
        current_answers.clear()
        guessed_answers.clear()

        buzzed_team[0] = ""
        first_wrong[0] = True
        steal_mode[0] = False
        total_questions = len(quizzes[current_category[0]]["questions"])

        if current_question[0] >= total_questions:
            question_text.value = "🎉 GAME OVER"
            if team1_score[0] > team2_score[0]:
                result_text.value = "🏆 TEAM 1 WINS!"
            elif team2_score[0] > team1_score[0]:
                result_text.value = "🏆 TEAM 2 WINS!"
            else:
                result_text.value = "🤝 IT'S A TIE!"

            submit_button.visible = False
            next_button.visible = False
            answer_input.visible = False
            answers_left_text.visible = False
            buzz_text.visible = False
            restart_button.visible = True
            return

        question_text.value = quizzes[current_category[0]]["questions"][current_question[0]]
        answers = quizzes[current_category[0]]["correct"][current_question[0]]
        for answer in answers:
            current_answers.append(answer)

        player_text.value = current_player1[0] + " VS " + current_player2[0]

        buzz_text.value = "PRESS A OR L TO BUZZ!"
        buzz_text.visible = True

        answer_input.visible = False
        answer_input.value = ""
        submit_button.visible = False
        next_button.visible = False
        result_text.value = ""
        answers_left_text.value = "Answers Left: " + str(len(current_answers))

    def key_pressed(e):
        if buzzed_team[0] != "":
            return
        if e.key.lower() == "a":
            buzzed_team[0] = "TEAM 1"
            current_turn[0] = "TEAM 1"
            buzz_text.value = "🚨 TEAM 1 BUZZED FIRST!"

            answer_input.visible = True
            submit_button.visible = True

        elif e.key.lower() == "l":
            buzzed_team[0] = "TEAM 2"
            current_turn[0] = "TEAM 2"
            buzz_text.value = "🚨 TEAM 2 BUZZED FIRST!"

            answer_input.visible = True
            submit_button.visible = True
    page.on_keyboard_event = key_pressed

    def submit_answer(e):
        try:
            user_answer = answer_input.value.lower()
            if answer_input.value == "":
                raise ValueError("You cannot leave the answer empty")
            if user_answer in current_answers and user_answer not in guessed_answers:
                guessed_answers.append(user_answer)
                if current_turn[0] == "TEAM 1":
                    team1_score[0] += 1
                else:
                    team2_score[0] += 1
                score_text.value = "TEAM 1: " + str(team1_score[0]) + " | TEAM 2: " + str(team2_score[0])
                answers_left = len(current_answers) - len(guessed_answers)
                answers_left_text.value = "Answers Left: " + str(answers_left)
                result_text.value = "✅ Correct! " + user_answer
                answer_input.value = ""

                if answers_left == 0:
                    all_answers = make_answers_text(current_answers)
                    result_text.value = "🎉 ALL ANSWERS FOUND!" + all_answers
                    submit_button.visible = False
                    next_button.visible = True
                else:
                    buzz_text.value = current_turn[0] + " KEEP GOING!"

            elif user_answer in guessed_answers:
                result_text.value = "⚠️ That answer was already used! ⚠️"

            else:
                result_text.value = "❌ Wrong Answer!"
                if first_wrong[0] == True:
                    first_wrong[0] = False
                    steal_mode[0] = True
                    if current_turn[0] == "TEAM 1":
                        current_turn[0] = "TEAM 2"
                    else:
                        current_turn[0] = "TEAM 1"
                    buzz_text.value = "🔥" + current_turn[0] + " CAN STEAL!"

                elif steal_mode[0] == True:
                    all_answers = make_answers_text(current_answers)
                    result_text.value = "❌ STEAL FAILED!\n" + "Possible answers:\n" + all_answers
                    submit_button.visible = False
                    next_button.visible = True
        except ValueError as error:
            result_text.value = "❌ Error: " + str(error)

    def next_question(e):
        current_question[0] += 1
        if len(team1) > 0:
            random_number = random.randint(0, len(team1)-1)
            current_player1[0] = team1[random_number]
            team1_player_text.value = "Team 1 Player: " + current_player1[0]
        if len(team2) > 0:
            random_number = random.randint(0,len(team2)-1)
            current_player2[0] = team2[random_number]
            team2_player_text.value = "Team 2 Player: " + current_player2[0]
        show_question()

    def restart(e):
        game_view.visible = False
        intro_view.visible = True
        restart_button.visible = False
        question_text.value = ""
        result_text.value = ""

    def start_intro(e):
        intro_view.visible = False
        instructions_view.visible = True

    def go_teams(e):
        instructions_view.visible = False
        teams_view.visible = True

    def go_topics(e):
        teams_view.visible = False
        topic_view.visible = True

    start_button = ft.Button("START GAME ▶️", on_click=start_intro, width=300)
    intro_view = ft.Column([logo, start_button], horizontal_alignment=ft.CrossAxisAlignment.CENTER)
    confirm_button = ft.Button("START THE QUIZ", on_click=start_game)

    instructions_button = ft.Button("CONTINUE ➡️", on_click=go_teams)
    instructions_view = ft.Column([ft.Text("📜 HOW TO PLAY", size=30, weight=ft.FontWeight.BOLD), ft.Text("1. Add players to both teams.\n" + "2. Choose a category.\n" + "3. Spin to choose one player from each team.\n" + "4. TEAM 1 presses A to buzz.\n" + "5. TEAM 2 presses L to buzz.\n" + "6. Keep answering until getting one wrong.\n" + "7. Other team gets one steal chance.\n" + "8. Team with most points wins! 🏆\n", size=20, text_align=ft.TextAlign.CENTER), instructions_button], horizontal_alignment=ft.CrossAxisAlignment.CENTER, visible=False)

    entertainment_button = ft.Button("Entertainment 🎬", on_click=choose_entertainment, width=300)
    everyday_button = ft.Button("Everyday Life 🏠", on_click=choose_everyday, width=300)
    funny_button = ft.Button("Funny & Random 👻", on_click=choose_funny, width=300)
    food_button = ft.Button("Food & Drinks 🍕", on_click=choose_food, width=300)
    sports_button = ft.Button("Sports & Games ⚽", on_click=choose_sports, width=300)

    topic_view = ft.Column([ft.Text("📚 CHOOSE A CATEGORY",size=25), entertainment_button, everyday_button, funny_button, food_button, sports_button], horizontal_alignment=ft.CrossAxisAlignment.CENTER, visible=False)
    add_team1_button = ft.Button("Add Team 1", on_click=add_team1)
    add_team2_button = ft.Button("Add Team 2", on_click=add_team2)
    spin_team1_button = ft.Button("SPIN TEAM 1 🔄", on_click=spin_team1_player)
    spin_team2_button = ft.Button("SPIN TEAM 2 🔄", on_click=spin_team2_player)

    begin_button = ft.Button("BEGIN FACE OFF 🔥", on_click=begin_questions)
    restart_button = ft.Button("PLAY AGAIN 🔄", on_click=restart, visible=False)
    next_page_button = ft.Button("NEXT ➡️", on_click=go_topics)
    submit_button = ft.Button("SUBMIT ANSWER ✅", on_click=submit_answer, visible=False)
    next_button = ft.Button("NEXT QUESTION ➡️", on_click=next_question, visible=False)

    teams_view = ft.Column([ft.Text("👥 ADD TEAM MEMBERS", size=25), input_team1, add_team1_button, team1_text, input_team2, add_team2_button, team2_text, next_page_button], visible=False)
    wheel_view = ft.Column([ft.Text("🎡 READY TO START?", size=25), confirm_button], horizontal_alignment=ft.CrossAxisAlignment.CENTER, visible=False)
    player_view = ft.Column([ft.Text("🔥 FAMILY FEUD FACE OFF", size=28), ft.Row([ft.Column([wheel_team1, spin_team1_button, team1_player_text], horizontal_alignment=ft.CrossAxisAlignment.CENTER), ft.Column([wheel_team2, spin_team2_button, team2_player_text], horizontal_alignment=ft.CrossAxisAlignment.CENTER)], alignment=ft.MainAxisAlignment.CENTER), begin_button], horizontal_alignment=ft.CrossAxisAlignment.CENTER, visible=False)
    game_view = ft.Column([player_text, score_text, answers_left_text, question_text, buzz_text, answer_input, submit_button, next_button, result_text, restart_button], spacing=20, horizontal_alignment=ft.CrossAxisAlignment.CENTER, visible=False)
    page.add(intro_view, instructions_view, teams_view, topic_view, wheel_view, player_view, game_view)
ft.run(main=main,assets_dir="assets")
