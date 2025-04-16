from math import trunc

def calculate_required_run_rate(target_score, current_score, total_overs, current_over):
    balls_played = trunc(current_over) * 6 + ((current_over - trunc(current_over)) * 10)
    balls_remaining = (total_overs * 6) - balls_played
    balls_remaining_in_overs = trunc(balls_remaining / 6) + ((balls_remaining - (trunc(balls_remaining / 6) * 6)) / 10)
    required_run_rate = (target_score - current_score) / balls_remaining_in_overs
    return required_run_rate, balls_played, balls_remaining_in_overs

def calculate_current_run_rate(current_score, balls_played):
    balls_played_in_overs = trunc(balls_played / 6) + ((balls_played - (trunc(balls_played / 6) * 6)) / 10)
    return current_score / balls_played_in_overs

def predict_final_score(current_score, current_run_rate, balls_remaining_overs):
    return current_score + (balls_remaining_overs * current_run_rate)

def predict_score_at_over(current_score, current_run_rate, balls_played, over):
    balls_remaining_at_overs_in_balls = (over * 6) - balls_played
    balls_remaining_at_overs_in_overs = (trunc(balls_remaining_at_overs_in_balls / 6) +
                                                   ((balls_remaining_at_overs_in_balls - (trunc(balls_remaining_at_overs_in_balls / 6) * 6)) / 10))

    return current_score + (balls_remaining_at_overs_in_overs * current_run_rate)

def over_by_over_score_tracker(batting_team, total_overs):
    print("\n📊 Over-by-Over Score Tracker\n")
    over_count = 1
    while over_count <= total_overs:
        score = int(input(f"Enter score at end of over {over_count}: "))
        avg_run_rate = score / over_count
        print(f"➡️  {batting_team} is scoring {avg_run_rate:.2f} runs per over after {over_count} overs\n")
        over_count += 1

def analyzing_winning_team(batting_team_score, bowling_team_score, batting_team, bowling_team, batting_team_wickets):
    print("\n📊 Match Summary\n" + "-"*30)
    print(f"🏏 {batting_team}: {batting_team_score}/{batting_team_wickets}")
    print(f"🎯 {bowling_team}: {bowling_team_score} (Target)\n")

    if batting_team_score > bowling_team_score:
        wickets_remaining = 10 - batting_team_wickets
        print(f"🎉 Congratulations! {batting_team} won by {wickets_remaining} wicket(s)! 🏆")
    elif batting_team_score < bowling_team_score:
        runs_short = bowling_team_score - batting_team_score
        print(f"🎉 Congratulations! {bowling_team} won by {runs_short} run(s)! 🏆")
    else:
        print("🤝 It's a tie! What a thrilling match! ⚖️")

    print("-" * 30)


def main():
    print("🏏 Welcome to the Cricket Match Analyzer!\n")

    batting_team = input("Enter batting team: ")
    target_score = int(input("Enter target score: "))
    current_score = int(input("Enter current score: "))
    total_overs = float(input("Enter total number of overs: "))
    current_over = float(input("Enter current over (e.g., 10.4): "))

    # Required Run Rate
    required_run_rate, balls_played, balls_remaining_overs = calculate_required_run_rate(
        target_score, current_score, total_overs, current_over
    )

    if required_run_rate < 0:
        print(f"🏆 {batting_team} has already crossed the target and won the match!")
    else:
        print(f"\n📌 {batting_team} needs {required_run_rate:.2f} runs/over to reach the target of {target_score}")

    # Current Run Rate
    current_run_rate = calculate_current_run_rate(current_score, balls_played)
    print(f"⚡ Current Run Rate: {current_run_rate:.2f} runs/over")

    # Final Score Prediction
    predicted_score = predict_final_score(current_score, current_run_rate, balls_remaining_overs)
    print(f"📈 At this rate, {batting_team} will score around {predicted_score:.2f} by the end of the innings")

    # Prediction at a Specific Over
    print("\n🔮 Score Prediction at a Specific Over")
    input_over = float(input("Enter the over to predict score at (e.g., 16.0): "))
    predicted_score_at_specified_over = predict_score_at_over(current_score, current_run_rate, balls_played, input_over)
    print(f"📊 Predicted score at over {input_over}: {predicted_score_at_specified_over:.2f}")

# Over-by-over tracker (optional)
    track = input("\n📝 Would you like to enter over-by-over scores? (yes/no): ").lower()
    if track == "yes":
        over_by_over_score_tracker(batting_team, int(total_overs))

# 🏆 Analyzing the winner of the match
    print("\n📢 Analyzing the winner of the match...")
    bowling_team = input("Enter the team that was bowling in the 2nd innings: ")
    batting_team = input("Enter the team that was batting in the 2nd innings: ")
    bowling_team_score = int(input(f"Enter {bowling_team}'s final score (target): "))
    batting_team_score = int(input(f"Enter {batting_team}'s final score: "))
    batting_team_wickets = int(input(f"Enter number of wickets lost by {batting_team}: "))

    analyzing_winning_team(
        batting_team_score,
        bowling_team_score,
        batting_team,
        bowling_team,
        batting_team_wickets
    )

    print("\n✅ Done! Thank you for using Cricket Match Analyzer.")

if __name__ == "__main__":
    main()




