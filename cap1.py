# pema tshering yangchen
# section A
# 02230295
# REFERENCES
# Links that you referred while solving 
# https://www.phind.com/
# https://chat.openai.com/

# SOLUTION
# Your Solution Score:49995
# 77671685

def calculate_score(opponent_choice, result):
    #scoring system define
    scores = {'A': 1, 'B': 2, 'C': 3, 'X': 0, 'Y': 3, 'Z': 6}

    #calculate score
    return scores[opponent_choice] + scores[result]

#read input
def main():
    file_path = "input_5_cap1.txt"  
    with open(file_path, 'r') as file:
        lines = file.readlines()

    #initialize
    total_score = 0

    #process
    for line in lines:
        #extract opponent's choice and result for each round
        opponent_choice, result = line.split()
        
        #calculate the score for the round and update the total score
        round_score = calculate_score(opponent_choice, result)
        total_score += round_score

    print("Total Score:", total_score)

if __name__ == "__main__":
    main()